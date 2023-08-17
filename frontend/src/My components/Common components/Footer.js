import React from 'react'
import "./Footer.css"
import logo from "../Images/trekker logo.png"
import copyright from "../Images/copyright.png"

export const Footer = () => {
  return (
    <footer className='footer'> 
      <div className="footer_left">
        <ul>
        <p>SITEMAP</p>
          <li>Why with us?</li>
          <li>Our Way</li>
          <li>Testimonials</li>
          <li>Trekking Permit Fees</li>
          <li>Terms & Conditions</li>
          <li>Cancellation Policy</li>
        </ul>
      </div>

      <div className="footer_right">
        <ul>
          <li ><img src={logo} alt="logo" className='footer_tag logo'/></li>
          <li>Trek manager Nepal (P) Ltd.</li>
          <li>P.O.Box: 23092, Thamel, Kathmandu, Nepal</li>
          <li>(Hotel nothing second Floor)</li>
          <li>Near by Restaurant.</li>
          <li>Tel: +977 65354</li>
            
          <li > <img src={copyright} alt="copyright" className='footer_tag'/></li>
        </ul>
        
      </div>
    </footer>
  )
}
