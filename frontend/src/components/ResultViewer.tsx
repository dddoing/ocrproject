'use client'

import { AnalysisResult } from '@/types'

interface ResultViewerProps {
  result: AnalysisResult
}

export default function ResultViewer({ result }: ResultViewerProps) {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6 space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">OCR Results</h2>

      {/* Detected Languages */}
      <div>
        <h3 className="text-sm font-medium text-gray-700 mb-2">Detected Languages</h3>
        <div className="flex gap-2">
          {result.ocr_result.detected_languages.map((lang) => (
            <span
              key={lang}
              className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-medium"
            >
              {lang.toUpperCase()}
            </span>
          ))}
        </div>
      </div>

      {/* Original Text */}
      <div>
        <h3 className="text-sm font-medium text-gray-700 mb-2">Extracted Text</h3>
        <div className="bg-gray-50 rounded-md p-4 max-h-64 overflow-y-auto">
          <p className="text-gray-900 whitespace-pre-wrap">{result.ocr_result.full_text}</p>
        </div>
      </div>

      {/* Confidence Score */}
      <div>
        <h3 className="text-sm font-medium text-gray-700 mb-2">Confidence Score</h3>
        <div className="flex items-center gap-3">
          <div className="flex-1 bg-gray-200 rounded-full h-2">
            <div
              className="bg-green-500 h-2 rounded-full transition-all"
              style={{ width: `${result.ocr_result.confidence * 100}%` }}
            />
          </div>
          <span className="text-sm font-medium text-gray-900">
            {(result.ocr_result.confidence * 100).toFixed(1)}%
          </span>
        </div>
      </div>

      {/* Text Segments */}
      {result.ocr_result.segments.length > 0 && (
        <div>
          <h3 className="text-sm font-medium text-gray-700 mb-2">
            Text Segments ({result.ocr_result.segments.length})
          </h3>
          <div className="space-y-2 max-h-48 overflow-y-auto">
            {result.ocr_result.segments.map((segment, index) => (
              <div key={index} className="flex justify-between items-center bg-gray-50 p-2 rounded">
                <span className="text-sm text-gray-900">{segment.text}</span>
                <span className="text-xs text-gray-500">
                  {(segment.confidence * 100).toFixed(0)}%
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
