"""
Document Service - Document type classification
"""
from typing import Dict, List


class DocumentService:
    """Document type classification service"""

    async def classify(self, text: str, segments: List[Dict]) -> str:
        """
        Classify document type based on content

        Args:
            text: Full extracted text
            segments: OCR segments

        Returns:
            Document type string
        """
        text_lower = text.lower()

        # Menu keywords
        menu_keywords = ['menu', 'dish', 'cuisine', 'appetizer', 'entree', 'dessert', 'beverage', 'price', '$', '₩', '¥', '€']
        if any(keyword in text_lower for keyword in menu_keywords):
            return "menu"

        # Contract keywords
        contract_keywords = ['agreement', 'contract', 'party', 'terms', 'conditions', 'hereby', 'whereas']
        if any(keyword in text_lower for keyword in contract_keywords):
            return "contract"

        # Receipt keywords
        receipt_keywords = ['receipt', 'total', 'subtotal', 'tax', 'payment', 'transaction', 'item']
        if any(keyword in text_lower for keyword in receipt_keywords):
            return "receipt"

        # Medical keywords
        medical_keywords = ['prescription', 'medication', 'dosage', 'mg', 'tablet', 'capsule', 'patient', 'doctor']
        if any(keyword in text_lower for keyword in medical_keywords):
            return "medical"

        # Sign/Notice keywords
        sign_keywords = ['warning', 'caution', 'notice', 'attention', 'prohibited', 'exit', 'entrance']
        if any(keyword in text_lower for keyword in sign_keywords):
            return "sign"

        # Default
        return "general"
