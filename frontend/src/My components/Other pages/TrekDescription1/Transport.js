import React from 'react'
import "./transport.css"

export const Transport = ({medium_desc}) => {
  return (
    <div>
        <div id='medium_frame'>
          <div id='medium_origin_city'>{"Origin City: " + medium_desc.origin_city}</div>
           <div id='medium_destination_city'>{"Destination City: "+medium_desc.destination_city}</div>
          <div>
            {medium_desc.medium.map((p)=>{
              return(
                <div  id='medium_cost'>{p}</div>          
              )
            })}
          </div>
        </div>
    </div>
  )
}
