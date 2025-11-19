"""
OCR Service - Text extraction from images
Uses EasyOCR for multi-language support
"""
import easyocr
from typing import Dict, List
import numpy as np
from app.core.config import settings


class OCRService:
    """OCR text extraction service"""

    def __init__(self):
        """Initialize EasyOCR reader"""
        self.reader = easyocr.Reader(settings.OCR_LANGUAGES, gpu=False)

    async def extract_text(self, image: np.ndarray) -> Dict:
        """
        Extract text from image using OCR

        Args:
            image: Preprocessed image as numpy array

        Returns:
            Dict with full_text, segments, detected_languages, confidence
        """
        try:
            # Perform OCR
            results = self.reader.readtext(image)

            # Parse results
            segments = []
            full_text_parts = []

            for bbox, text, confidence in results:
                segments.append({
                    "text": text,
                    "bbox": bbox,
                    "confidence": float(confidence)
                })
                full_text_parts.append(text)

            full_text = " ".join(full_text_parts)

            # Detect languages (simplified)
            detected_languages = self._detect_languages(full_text)

            return {
                "full_text": full_text,
                "segments": segments,
                "detected_languages": detected_languages,
                "confidence": sum(s["confidence"] for s in segments) / len(segments) if segments else 0.0
            }

        except Exception as e:
            raise Exception(f"OCR extraction failed: {str(e)}")

    def _detect_languages(self, text: str) -> List[str]:
        """
        Detect languages in text (simplified version)
        TODO: Implement proper language detection
        """
        # Simple heuristic - check for character ranges
        languages = []

        # Korean
        if any('\uac00' <= char <= '\ud7a3' for char in text):
            languages.append("ko")

        # Japanese
        if any('\u3040' <= char <= '\u309f' or '\u30a0' <= char <= '\u30ff' for char in text):
            languages.append("ja")

        # Chinese
        if any('\u4e00' <= char <= '\u9fff' for char in text):
            languages.append("zh")

        # Default to English if ASCII
        if not languages and text.isascii():
            languages.append("en")

        return languages or ["unknown"]
