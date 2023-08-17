import React from 'react'
import "./viewpoint.css"

export const ViewPoint = ({cvp_desc}) => {
  return (
    <div id='vp_frame'>
        <div id='vp_name' className='vp'>{cvp_desc.viewpoint_name}</div>
        <div id='vp_details' className='vp'>{cvp_desc.viewpoint_description}</div>
    </div>
  )
}
