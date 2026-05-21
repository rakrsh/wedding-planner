export default function Header({ navigate }){
  return (
    <header>
      <nav>
        <a href="#" onClick={(e)=>{e.preventDefault(); navigate('home')}}>Home</a>
        <a href="#" onClick={(e)=>{e.preventDefault(); navigate('projects')}}>Projects</a>
      </nav>
    </header>
  )
}
