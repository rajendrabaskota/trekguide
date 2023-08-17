import React from 'react'
import "./package.css"

export const Package = ({details}) => {
  return (
    <div>
        <div>
            <div id="package_name" className='package_text'>{"Package Name: "+details.package_name}</div>
            <div id="package_cost" className='package_text'>{"Package Cost: "+details.price}</div>
        </div>
        <div  id='package_details' className='package_text'>Details</div>
        <div className="package_desc package_text">{details.package_description.map((day)=>{
            return (
            <>
            <div>{day}</div>
            </>)
        })}</div>
        <div id="package_guide">
    
            <div id='guides_text' className='package_text'>Guides</div>
            <span className="guide_name package_text" >{details.guide_name}</span>
            <span className="guide_number package_text">{"Number: "+details.phone_number}</span>
            
        </div>
    </div>
  )
}
