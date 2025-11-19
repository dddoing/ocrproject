'use client'

import { useState, useCallback } from 'react'
import { analyzeDocument } from '@/lib/api'
import { AnalysisResult } from '@/types'

interface ImageUploaderProps {
  onAnalysisComplete: (result: AnalysisResult) => void
  onAnalysisStart: () => void
}

export default function ImageUploader({
  onAnalysisComplete,
  onAnalysisStart,
}: ImageUploaderProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [targetLanguage, setTargetLanguage] = useState('en')
  const [error, setError] = useState<string | null>(null)

  const handleFileSelect = useCallback((file: File) => {
    setSelectedFile(file)
    setError(null)

    // Create preview
    const reader = new FileReader()
    reader.onloadend = () => {
      setPreview(reader.result as string)
    }
    reader.readAsDataURL(file)
  }, [])

  const handleDrop = useCallback(
    (e: React.DragEvent<HTMLDivElement>) => {
      e.preventDefault()
      const file = e.dataTransfer.files[0]
      if (file && file.type.startsWith('image/')) {
        handleFileSelect(file)
      }
    },
    [handleFileSelect]
  )

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      handleFileSelect(file)
    }
  }

  const handleAnalyze = async () => {
    if (!selectedFile) return

    try {
      setError(null)
      onAnalysisStart()

      const result = await analyzeDocument({
        file: selectedFile,
        target_language: targetLanguage,
      })

      onAnalysisComplete(result)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Analysis failed. Please try again.')
      onAnalysisComplete(null as any) // Reset loading state
    }
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 space-y-4">
      {/* Language Selector */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Target Language
        </label>
        <select
          value={targetLanguage}
          onChange={(e) => setTargetLanguage(e.target.value)}
          className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-500 focus:border-transparent"
        >
          <option value="en">English</option>
          <option value="ko">Korean (한국어)</option>
          <option value="ja">Japanese (日本語)</option>
          <option value="zh">Chinese (中文)</option>
          <option value="es">Spanish (Español)</option>
          <option value="fr">French (Français)</option>
          <option value="de">German (Deutsch)</option>
        </select>
      </div>

      {/* Drop Zone */}
      <div
        onDrop={handleDrop}
        onDragOver={(e) => e.preventDefault()}
        className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-primary-500 transition-colors cursor-pointer"
      >
        {preview ? (
          <div className="space-y-4">
            <img
              src={preview}
              alt="Preview"
              className="max-h-64 mx-auto rounded-lg"
            />
            <p className="text-sm text-gray-600">{selectedFile?.name}</p>
          </div>
        ) : (
          <div className="space-y-2">
            <svg
              className="mx-auto h-12 w-12 text-gray-400"
              stroke="currentColor"
              fill="none"
              viewBox="0 0 48 48"
            >
              <path
                d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                strokeWidth={2}
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            <div className="text-sm text-gray-600">
              <label htmlFor="file-upload" className="relative cursor-pointer rounded-md font-medium text-primary-600 hover:text-primary-500">
                <span>Upload a file</span>
                <input
                  id="file-upload"
                  name="file-upload"
                  type="file"
                  accept="image/*,.pdf"
                  className="sr-only"
                  onChange={handleFileInput}
                />
              </label>
              <p className="pl-1">or drag and drop</p>
            </div>
            <p className="text-xs text-gray-500">PNG, JPG, PDF up to 10MB</p>
          </div>
        )}
      </div>

      {/* Error Message */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-md p-4">
          <p className="text-sm text-red-600">{error}</p>
        </div>
      )}

      {/* Analyze Button */}
      <button
        onClick={handleAnalyze}
        disabled={!selectedFile}
        className="w-full bg-primary-600 text-white py-3 px-6 rounded-md font-medium hover:bg-primary-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
      >
        Analyze Document
      </button>
    </div>
  )
}
