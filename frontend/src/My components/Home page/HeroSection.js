import React from 'react'
import "./HeroSection.css"
import picture from "../Images/lets roam nepal.png"

export const HeroSection = () => {
  return (
    <div className='main_section'>
      <div className='HeroSection'>
        <h1 className='center_text_trek'>Trek</h1>
        <h1 className='center_text_manager'>Manager</h1>
      </div>

      
      <div className="lets_roam">
        <div className="lets_roam_right">
            <img src={picture} alt="Lets Roam Nepal" className="lets_roam_picture" />
        </div>
        <div className="lets_roam_left">
          Trekking in the Himalayas opens up new horizons of awareness, blending physical challenge  with mental relaxation and a spiritual elation inspired by splendid scenery and heartwarming human encounters. 
          Different trekking routes offer a different range 
          of lengths and difficulties. Some trekking routes are just a day hiking trip and some are very long and high altitude exploration over the mountain pass. 
          It depends on the your own choice to fulfill your dream.
        </div>
      </div>
  </div>
  )
}
