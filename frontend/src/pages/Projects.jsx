import { useEffect, useState } from 'react'

export default function Projects(){
  const [projects, setProjects] = useState([])
  const [title, setTitle] = useState('')
  const [token, setToken] = useState('')
  const [message, setMessage] = useState(null)

  useEffect(()=>{
    if(!token) return
    fetch('http://localhost:8000/projects', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(r=> r.json())
      .then(setProjects)
      .catch(()=>setProjects([]))
  }, [token])

  async function createProject(e){
    e.preventDefault()
    setMessage(null)
    try{
      const res = await fetch('http://localhost:8000/projects', {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ title })
      })
      const data = await res.json()
      if(!res.ok) throw new Error(data.detail || 'Failed')
      setMessage('Created')
      setProjects(p=>[...p, data])
      setTitle('')
    }catch(err){
      setMessage(err.message)
    }
  }

  return (
    <main className="container">
      <h1>Projects</h1>
      <p>Paste a valid Keycloak access token below to interact with the protected API.</p>
      <div style={{maxWidth:600}}>
        <input placeholder="Paste access token (Bearer)" value={token} onChange={e=>setToken(e.target.value)} style={{width:'100%', padding:8, margin:'8px 0'}} />
        <form onSubmit={createProject}>
          <input placeholder="Project title" value={title} onChange={e=>setTitle(e.target.value)} style={{width:'100%', padding:8, margin:'8px 0'}} />
          <button type="submit">Create Project</button>
        </form>
        {message && <div style={{marginTop:8}}>{message}</div>}
        <h2>Your projects</h2>
        <ul>
          {projects.map(p=> (
            <li key={p.id}>{p.title} — {p.status}</li>
          ))}
        </ul>
      </div>
    </main>
  )
}
