'use client'

import { Analysis } from '@/types'

interface DocumentAnalysisProps {
  analysis: Analysis
}

export default function DocumentAnalysis({ analysis }: DocumentAnalysisProps) {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6 space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-900">Analysis & Translation</h2>
        <span className="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-sm font-medium">
          {analysis.document_type}
        </span>
      </div>

      {/* Translation */}
      <div>
        <h3 className="text-lg font-semibold text-gray-900 mb-2">Translation</h3>
        <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-md p-4">
          <p className="text-gray-900 whitespace-pre-wrap">{analysis.translation}</p>
        </div>
      </div>

      {/* Summary */}
      {analysis.summary && (
        <div>
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Summary</h3>
          <div className="bg-gray-50 rounded-md p-4">
            <p className="text-gray-900">{analysis.summary}</p>
          </div>
        </div>
      )}

      {/* Key Information */}
      {(analysis.key_info.items.length > 0 ||
        analysis.key_info.prices.length > 0 ||
        analysis.key_info.dates.length > 0 ||
        analysis.key_info.contacts.length > 0) && (
        <div>
          <h3 className="text-lg font-semibold text-gray-900 mb-3">Key Information</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {analysis.key_info.items.length > 0 && (
              <InfoCard title="Items" items={analysis.key_info.items} color="green" />
            )}
            {analysis.key_info.prices.length > 0 && (
              <InfoCard title="Prices" items={analysis.key_info.prices} color="blue" />
            )}
            {analysis.key_info.dates.length > 0 && (
              <InfoCard title="Dates" items={analysis.key_info.dates} color="purple" />
            )}
            {analysis.key_info.contacts.length > 0 && (
              <InfoCard title="Contacts" items={analysis.key_info.contacts} color="orange" />
            )}
          </div>
        </div>
      )}

      {/* Advice */}
      {analysis.advice && (
        <div>
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Contextual Advice</h3>
          <div className="bg-amber-50 border-l-4 border-amber-400 rounded-md p-4">
            <div className="flex">
              <div className="flex-shrink-0">
                <svg
                  className="h-5 w-5 text-amber-400"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z"
                    clipRule="evenodd"
                  />
                </svg>
              </div>
              <div className="ml-3">
                <p className="text-sm text-amber-800 whitespace-pre-wrap">{analysis.advice}</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

function InfoCard({
  title,
  items,
  color,
}: {
  title: string
  items: string[]
  color: string
}) {
  const colorClasses = {
    green: 'bg-green-50 border-green-200 text-green-800',
    blue: 'bg-blue-50 border-blue-200 text-blue-800',
    purple: 'bg-purple-50 border-purple-200 text-purple-800',
    orange: 'bg-orange-50 border-orange-200 text-orange-800',
  }

  return (
    <div className={`border rounded-md p-4 ${colorClasses[color as keyof typeof colorClasses]}`}>
      <h4 className="font-semibold mb-2">{title}</h4>
      <ul className="space-y-1">
        {items.map((item, index) => (
          <li key={index} className="text-sm">
            • {item}
          </li>
        ))}
      </ul>
    </div>
  )
}
