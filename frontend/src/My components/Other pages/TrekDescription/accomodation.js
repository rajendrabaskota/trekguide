import React from 'react'
import "./accomodation.css"

export const Accomodation = ({acc_desc}) => {
  return (
    <div id='acc_frame'>
      <div className='vp' id='acc_name'>{acc_desc.hotel_name}</div>
      <div className='vp'>{"Number: "+acc_desc.phone_number}</div>
      <div className='vp'>{"Email: "+acc_desc.email}</div>
      <div className='vp'>{"Price: "+acc_desc.price}</div>
    </div>
  )
}
