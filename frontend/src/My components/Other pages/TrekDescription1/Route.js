import React from 'react'
import "./Route.css"
import {City} from "./city"
import { Package } from './package'

export const Route = ({route_details}) => {
  console.log(route_details.packages)
  return (
    <div className='route_details'>
      <div id="route_name">{route_details.route_name}</div>
      <div className="route_box">
        <div id="route_desc">{route_details.route_description}</div>
        <div id="route_pic_container"><img src={route_details.route_pic} alt="" id='route_pic'/></div>
      </div>
      <div className="packages">
        Trek Packages
        <div id="package_frame">
          {route_details.packages.map((p)=>{
            return <Package details={p}/>
          })}
        </div>
      </div>
      <div id="city_in_the_route">Cities in the Route</div>
      <div id='city_frame'>
        {route_details.cities.map((cities)=>{
        return <City city_details={cities} />})
        }
      </div>
    </div>
  )
}
