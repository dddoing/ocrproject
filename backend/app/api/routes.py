"""
API route definitions
"""
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from app.models.schemas import AnalysisRequest, AnalysisResponse
from app.services.ocr_service import OCRService
from app.services.llm_service import LLMService
from app.services.image_service import ImageService
from app.services.document_service import DocumentService

router = APIRouter()

# Initialize services
ocr_service = OCRService()
llm_service = LLMService()
image_service = ImageService()
document_service = DocumentService()


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_document(
    file: UploadFile = File(...),
    target_language: str = Form("en"),
    document_type: Optional[str] = Form(None)
):
    """
    Analyze a document image with OCR and LLM

    Args:
        file: Image file (JPG, PNG, PDF)
        target_language: Target language code (e.g., 'en', 'ko', 'ja')
        document_type: Optional document type hint

    Returns:
        AnalysisResponse with OCR results, translation, and insights
    """
    try:
        # Validate file
        if file.content_type not in ["image/jpeg", "image/png", "image/jpg", "application/pdf"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Only JPG, PNG, PDF allowed.")

        # Read and preprocess image
        image_data = await file.read()
        processed_image = await image_service.preprocess(image_data)

        # Perform OCR
        ocr_result = await ocr_service.extract_text(processed_image)

        # Classify document type
        if not document_type:
            document_type = await document_service.classify(
                ocr_result["full_text"],
                ocr_result.get("segments", [])
            )

        # LLM analysis
        analysis = await llm_service.analyze(
            text=ocr_result["full_text"],
            target_language=target_language,
            document_type=document_type,
            segments=ocr_result.get("segments", [])
        )

        # Combine results
        response = AnalysisResponse(
            ocr_result=ocr_result,
            analysis=analysis,
            metadata={
                "processing_time": 0.0,  # TODO: Add timing
                "confidence_score": ocr_result.get("confidence", 0.0)
            }
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@router.get("/history")
async def get_history():
    """Get user's analysis history"""
    # TODO: Implement history retrieval
    return {"message": "History endpoint - coming soon"}


@router.post("/feedback")
async def submit_feedback():
    """Submit feedback on translation quality"""
    # TODO: Implement feedback submission
    return {"message": "Feedback endpoint - coming soon"}
