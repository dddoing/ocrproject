"""
LLM Service - Translation and analysis using Claude/GPT
"""
from typing import Dict, List, Optional
import anthropic
from app.core.config import settings


class LLMService:
    """LLM-based translation and analysis service"""

    def __init__(self):
        """Initialize Claude API client"""
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    async def analyze(
        self,
        text: str,
        target_language: str,
        document_type: str,
        segments: List[Dict]
    ) -> Dict:
        """
        Analyze document with LLM

        Args:
            text: Extracted text from OCR
            target_language: Target language for translation
            document_type: Type of document
            segments: OCR segments with bounding boxes

        Returns:
            Dict with translation, summary, key_info, advice
        """
        try:
            prompt = self._build_prompt(text, target_language, document_type)

            # Call Claude API
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # Parse response
            response_text = message.content[0].text

            # TODO: Parse structured JSON response
            analysis = {
                "document_type": document_type,
                "translation": response_text,  # Simplified
                "summary": "Summary pending",
                "key_info": {
                    "items": [],
                    "prices": [],
                    "dates": [],
                    "contacts": []
                },
                "advice": "Advice pending"
            }

            return analysis

        except Exception as e:
            raise Exception(f"LLM analysis failed: {str(e)}")

    def _build_prompt(self, text: str, target_language: str, document_type: str) -> str:
        """Build prompt for LLM based on document type"""

        base_prompt = f"""You are analyzing a {document_type} document. The extracted text is:

{text}

Please provide a comprehensive analysis in {target_language}:

1. **Translation**: Translate the entire document into {target_language}
2. **Summary**: Provide a concise summary of the key points
3. **Key Information**: Extract structured information (dates, amounts, names, etc.)
4. **Contextual Advice**: Provide practical advice based on the document type

Document Type: {document_type}
"""

        # Add type-specific instructions
        type_specific = self._get_type_specific_instructions(document_type)
        if type_specific:
            base_prompt += f"\n{type_specific}"

        return base_prompt

    def _get_type_specific_instructions(self, document_type: str) -> str:
        """Get type-specific analysis instructions"""
        instructions = {
            "menu": "- Identify dishes, ingredients, prices\n- Note any allergen information\n- Suggest popular items",
            "contract": "- Highlight key terms and conditions\n- Identify important dates and obligations\n- Flag potential risks",
            "receipt": "- Extract all items and prices\n- Verify calculations\n- Categorize expenses",
            "medical": "- Translate medication names\n- Note dosage and frequency\n- Highlight warnings",
        }
        return instructions.get(document_type, "")
