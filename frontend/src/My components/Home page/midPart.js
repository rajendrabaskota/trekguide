import "./mid_part.css"
import second_pic from "../Images/second_pic.png"
import {Carousel} from "./carousel"
import React from 'react'
import ABCpic from "../Images/ABC.png"
import tilichopic from "../Images/Tilicho.png"

export const MidPart = () => {
  let treks=[
    {
      title: "Annapurna Base Camp",
      image: ABCpic ,
      desc:"From ancient kingdoms to majestic mountain vistas, trek through the breathtaking Himalayan landscape of the Annapurna Ranges. Pass awe-inspiring glaciers, stay on the banks of pristine rivers, cross mountain pastures, dip into natural hot springs and encounter mule trains carrying supplies to remote villages.",
      alt_name: "ABC image"
    },
    {
      title: "Tilicho Lake",
      image: tilichopic ,
      desc:"On this 12-day journey through Nepal, experience the scenic and challenging Tilicho Lake Trek,one of the highest lakes in the world. Start in Kathmandu to get acquainted with the country, and do some sightseeing. Then, begin the journey through the Annapurna region.",
      alt_name: "Tilicho image"
    }
  ];

  return (
    <>
    <div className="second_part">
      <img src={second_pic} alt="" className="second_pic" />
      <p className="second_part_text">We are There With You at every step</p>
    </div>

    <div className="popular_treks">
      <p className="popular_treks_header">Popular Treks In Nepal</p>
      <p className="popular_treks_text">
        Though Nepal has plenty lots of trekking region and every hill offer unique experiences, we are presenting here some of the most popular trekking routes in the Himalayas.
      </p>
    </div>
    <Carousel data={treks}/>
    </>
  )
}
