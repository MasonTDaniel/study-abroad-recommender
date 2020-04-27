import React from 'react';
//import { useOktaAuth } from '@okta/okta-react';
import { NavLink, Link } from 'react-router-dom'
import Logo from '../img/su-logo.png'

/* A basic navbar with tabs Browse, How To, Contact Us, Admin, and Log Out (only if admin user is logged in */
const NavBar = () => {

    return (
        <div id="nav" className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 border-bottom shadow-sm">
            <Link to="/" className="my-0 mr-md-auto align-self-start"><img style={{ "width": "15rem" }} src={Logo} alt="" /></Link>
            <NavLink to="/" className="btn" >Search</NavLink>
            <a className="btn" href="https://masontdaniel.github.io" target="_blank" rel="noopener noreferrer">Contact Us</a>
            <NavLink to="/admin-dashboard" className="btn" >Admin</NavLink>
        </div>
    );
}

export default NavBar;
