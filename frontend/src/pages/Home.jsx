import { useEffect, useState } from 'react'

export default function Home(){
  const [status, setStatus] = useState(null)
  useEffect(()=>{
    fetch('http://localhost:8000/health')
      .then(r=>r.json())
      .then(setStatus)
      .catch(()=>setStatus({ status: 'unreachable' }))
  },[])

  return (
    <main className="container">
      <h1>Indian Wedding Planner</h1>
      <p>Frontend scaffold (React). Backend health:</p>
      <pre>{JSON.stringify(status, null, 2)}</pre>
      <p>Visit Projects to create or list projects (requires API and auth).</p>
    </main>
  )
}
