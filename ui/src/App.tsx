import { useState } from 'react'
import './App.css'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

function App() {
  const [message, setMessage] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<string>('')

  const handleCallAPI = async () => {
    setLoading(true)
    setError('')
    setMessage('')
    
    try {
      const response = await fetch(`${API_BASE_URL}`, {
        method: 'GET',
        headers: {
          'accept': 'application/json',
        },
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      setMessage(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <h1>Demo API Call</h1>
      <div className="card">
        <button 
          onClick={handleCallAPI} 
          disabled={loading}
          className="api-button"
        >
          {loading ? 'Loading...' : 'Call API - Hello World'}
        </button>
        
        {message && (
          <div className="result success">
            <h3>✅ Response from Backend:</h3>
            <p>{message}</p>
          </div>
        )}
        
        {error && (
          <div className="result error">
            <h3>❌ Error:</h3>
            <p>{error}</p>
          </div>
        )}
        
        <div className="info">
          <p>API Endpoint: <code>GET {API_BASE_URL}/</code></p>
        </div>
      </div>
    </div>
  )
}

export default App
