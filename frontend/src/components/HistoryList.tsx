'use client'

import { useEffect, useState } from 'react'
import { getHistory } from '@/lib/api'

export default function HistoryList() {
  const [history, setHistory] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadHistory()
  }, [])

  const loadHistory = async () => {
    try {
      const data = await getHistory()
      setHistory(data)
    } catch (error) {
      console.error('Failed to load history:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <p className="text-gray-500">Loading history...</p>
      </div>
    )
  }

  if (history.length === 0) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <p className="text-gray-500">No history yet. Upload a document to get started!</p>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">History</h2>
      <div className="space-y-4">
        {history.map((item) => (
          <div key={item.id} className="border-b pb-4 last:border-b-0">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="font-semibold text-gray-900">{item.document_type}</h3>
                <p className="text-sm text-gray-600">{item.summary}</p>
              </div>
              <span className="text-xs text-gray-500">{item.timestamp}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
