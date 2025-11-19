'use client'

import { useState } from 'react'
import ImageUploader from '@/components/ImageUploader'
import ResultViewer from '@/components/ResultViewer'
import DocumentAnalysis from '@/components/DocumentAnalysis'
import { AnalysisResult } from '@/types'

export default function Home() {
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null)
  const [isAnalyzing, setIsAnalyzing] = useState(false)

  const handleAnalysisComplete = (result: AnalysisResult) => {
    setAnalysisResult(result)
    setIsAnalyzing(false)
  }

  const handleAnalysisStart = () => {
    setIsAnalyzing(true)
    setAnalysisResult(null)
  }

  return (
    <div className="space-y-8">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">
          Upload Your Document
        </h2>
        <p className="text-gray-600">
          Upload any document image for instant OCR, translation, and analysis
        </p>
      </div>

      <ImageUploader
        onAnalysisComplete={handleAnalysisComplete}
        onAnalysisStart={handleAnalysisStart}
      />

      {isAnalyzing && (
        <div className="flex justify-center items-center py-12">
          <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-primary-600"></div>
        </div>
      )}

      {analysisResult && !isAnalyzing && (
        <div className="space-y-6">
          <ResultViewer result={analysisResult} />
          <DocumentAnalysis analysis={analysisResult.analysis} />
        </div>
      )}
    </div>
  )
}
