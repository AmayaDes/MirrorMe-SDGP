import {Link, useMatch, useResolvedPath } from 'react-router-dom'
import React from 'react'
import '../Navbar/navbar.css'

function Navbar() {
  return (
    <nav className="navbar">
            <Link to="/" className="site-title">MirrorMe</Link>
            <ul>


                <CustomLink to="/About.jsx">About</CustomLink>
                <CustomLink to="/Contact.jsx">Contact</CustomLink>

            </ul>

        </nav>
  )
}
function CustomLink({to,children,...props}){
    //allows to take relative/ absolute path and combines with the actual pathand
    // gives the actual full path that will be accessing
    const resolvedPath = useResolvedPath(to)
    //useMatch-> compares the current location with the provided path.
    //compares the current path and checks whether the full path matches
    const isActive = useMatch({ path: resolvedPath.pathname, end: true })

    return(
        //add active class if active else no class
        <li className={isActive ? "active" : ""}>
            <Link to={to}{...props}>
                {children}
            </Link>
        </li>
    )
}

export default Navbar
