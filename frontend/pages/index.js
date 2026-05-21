import { useEffect, useState } from 'react'
import Header from '../components/Header'

export default function Home() {
  const [status, setStatus] = useState(null)
  useEffect(() => {
    fetch('http://localhost:8000/health')
      .then((r) => r.json())
      .then(setStatus)
      .catch(() => setStatus({ status: 'unreachable' }))
  }, [])

  return (
    <div>
      <Header />
      <main style={{padding:20}}>
        <h1>Indian Wedding Planner</h1>
        <p>Frontend scaffold (Next.js). Backend health:</p>
        <pre>{JSON.stringify(status, null, 2)}</pre>
        <p>
          Visit <a href="/projects">Projects</a> to create or list projects (requires API and auth).
        </p>
      </main>
    </div>
  )
}
