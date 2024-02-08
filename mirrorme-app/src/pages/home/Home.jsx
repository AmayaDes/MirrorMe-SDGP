import React from 'react'
import '../home/home.css'
import { Link } from 'react-router-dom';


function Home() {
  return (
    <div>
        <div className='home-container'>
            <div className='hero-txt'>
                <h1>Discover Your Perfect Fit with MirrorMe: Revolutionizing Online Apparel Shopping!</h1>
                <p className='sub-txt'><i>Experience the Future of Fashion from the Comfort of Your Home</i></p>
                <Link to="/">
                    <button className='start-btn'>Get Started</button>
                </Link>
            </div>
            <div className='hero-img'>
                <img src="/banner-img.png" alt="shoping-woman" />
            </div>

        </div>
    </div>
  )
}

export default Home
