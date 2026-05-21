import Link from 'next/link'

export default function Header() {
  return (
    <header style={{padding:20, borderBottom:'1px solid #eee'}}>
      <nav style={{display:'flex', gap:16}}>
        <Link href="/">Home</Link>
        <Link href="/projects">Projects</Link>
      </nav>
    </header>
  )
}
