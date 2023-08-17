import "./carousel.css"
import React from 'react'
import { useState } from "react"
import {Link} from "react-router-dom"

export const Carousel = (props) => {

  let len=(props.data).length;

  let previous = () => {
    if(index===0){setindex(len-1);}
    else{setindex(index-1);}
  };

  let next = () => {
    if(index===(len-1)){setindex(0);}
    else{setindex(index+1);}
  };

  const [index, setindex] = useState(0);

  return (
    <div className="carousel">
      <button className="carousel_button carousel_prev"  onClick={previous}>&#8656;</button>
      <button className="carousel_button carousel_next"  onClick={next}>&#8658;</button>
      <Link to={`/TrekDescription${props.data[index].title}`}>
        <div className="carousel_ul">
          <div className="carousel_slide carousel_active">
            <p className="carousel_name">{props.data[index].title}</p>
            <div className="carousel_info">
              <img src={props.data[index].image} alt={props.data[index].alt_name} className="carousel_image"/>
              <div className="carousel_desc">
                {props.data[index].desc}
              </div>
            </div>
          </div>
        </div>
      </Link>
    </div>

  )
}
