
import React from 'react';
import Navbar from './components/Navbar/Navbar'
import Home from './pages/home/home'
import About from './pages/about/About'
import Demo from './pages/demo/Demo';
import Contact from './pages/contact/Contact'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';



function App() {


  return (
    <>
    <Router>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/About.jsx' element={<About />} />
          <Route path='/Contact.jsx' element={<Contact />} />
        </Routes>
      </div>
    </Router>
    </>
  )
}

export default App
