/**
 * TypeScript type definitions
 */

export interface OCRSegment {
  text: string
  bbox: number[]
  confidence: number
}

export interface OCRResult {
  full_text: string
  segments: OCRSegment[]
  detected_languages: string[]
  confidence: number
}

export interface KeyInfo {
  items: string[]
  prices: string[]
  dates: string[]
  contacts: string[]
}

export interface Analysis {
  document_type: string
  translation: string
  summary: string
  key_info: KeyInfo
  advice: string
}

export interface AnalysisResult {
  ocr_result: OCRResult
  analysis: Analysis
  metadata: {
    processing_time: number
    confidence_score: number
  }
}

export interface AnalysisRequest {
  file: File
  target_language: string
  document_type?: string
}
