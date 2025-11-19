"""
Image Service - Image preprocessing for OCR
"""
import cv2
import numpy as np
from PIL import Image
import io


class ImageService:
    """Image preprocessing service"""

    async def preprocess(self, image_data: bytes) -> np.ndarray:
        """
        Preprocess image for better OCR results

        Args:
            image_data: Raw image bytes

        Returns:
            Preprocessed image as numpy array
        """
        try:
            # Convert bytes to PIL Image
            image = Image.open(io.BytesIO(image_data))

            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Convert to numpy array
            img_array = np.array(image)

            # Convert RGB to BGR for OpenCV
            img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

            # Apply preprocessing steps
            processed = self._enhance_image(img_bgr)

            return processed

        except Exception as e:
            raise Exception(f"Image preprocessing failed: {str(e)}")

    def _enhance_image(self, image: np.ndarray) -> np.ndarray:
        """
        Enhance image quality for OCR

        Steps:
        1. Denoise
        2. Convert to grayscale
        3. Apply adaptive thresholding
        4. Deskew (rotation correction)
        """
        # Denoise
        denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

        # Convert to grayscale
        gray = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)

        # Adaptive thresholding for better contrast
        thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )

        # Deskew (simple version)
        deskewed = self._deskew(thresh)

        return deskewed

    def _deskew(self, image: np.ndarray) -> np.ndarray:
        """
        Correct image rotation
        """
        # Detect edges
        edges = cv2.Canny(image, 50, 150, apertureSize=3)

        # Detect lines using Hough transform
        lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

        if lines is not None:
            # Calculate average angle
            angles = []
            for line in lines:
                rho, theta = line[0]
                angle = (theta * 180 / np.pi) - 90
                angles.append(angle)

            median_angle = np.median(angles)

            # Rotate if angle is significant
            if abs(median_angle) > 0.5:
                (h, w) = image.shape[:2]
                center = (w // 2, h // 2)
                M = cv2.getRotationMatrix2D(center, median_angle, 1.0)
                rotated = cv2.warpAffine(
                    image, M, (w, h),
                    flags=cv2.INTER_CUBIC,
                    borderMode=cv2.BORDER_REPLICATE
                )
                return rotated

        return image
