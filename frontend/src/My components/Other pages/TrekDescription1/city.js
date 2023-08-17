import React from 'react'
import { ViewPoint } from './viewpoint'
import {Accomodation} from "./accomodation"
import "./city.css"

export const City = ({city_details}) => {
  return (
    <div>
        <div id="city_title">{city_details.city_name}</div>
        <div id="city_details_frame">
          <div id="city_desc">{city_details.city_description}</div>
          <div id="vp_acc_frame">
            <div>
              <div className="column">Viewpoints</div>
                {city_details.city_viewpoint.map((details)=>{
                    return (<ViewPoint cvp_desc={details}/>)})}
            </div>
            <div>
              <div className="column">Accomodations</div>
                {city_details.accomodation.map((details)=>{
                    return (<Accomodation acc_desc={details}/>)})}
            </div>
          </div>
        </div>

    </div>
  )
}
