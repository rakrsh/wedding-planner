import { useState, useEffect } from 'react'
import Header from './components/Header'
import Home from './pages/Home'
import Projects from './pages/Projects'

export default function App(){
  const [route, setRoute] = useState('home')
  return (
    <div>
      <Header navigate={setRoute} />
      {route === 'home' ? <Home /> : <Projects />}
    </div>
  )
}
