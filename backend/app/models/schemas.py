"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class OCRSegment(BaseModel):
    """Single OCR text segment"""
    text: str
    bbox: List[float]
    confidence: float


class OCRResult(BaseModel):
    """OCR extraction result"""
    full_text: str
    segments: List[OCRSegment]
    detected_languages: List[str]
    confidence: float


class KeyInfo(BaseModel):
    """Extracted key information"""
    items: List[str] = []
    prices: List[str] = []
    dates: List[str] = []
    contacts: List[str] = []


class Analysis(BaseModel):
    """LLM analysis result"""
    document_type: str
    translation: str
    summary: str
    key_info: KeyInfo
    advice: str


class AnalysisRequest(BaseModel):
    """Request for document analysis"""
    target_language: str = Field(default="en", description="Target language code")
    document_type: Optional[str] = Field(None, description="Optional document type hint")


class AnalysisResponse(BaseModel):
    """Complete analysis response"""
    ocr_result: Dict
    analysis: Dict
    metadata: Dict


class HistoryItem(BaseModel):
    """Single history entry"""
    id: str
    timestamp: str
    document_type: str
    source_language: str
    target_language: str
    summary: str


class FeedbackRequest(BaseModel):
    """User feedback submission"""
    analysis_id: str
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
