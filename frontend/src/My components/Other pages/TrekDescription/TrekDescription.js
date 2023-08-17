import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom'
import "./TrekDescription.css"
import {Route} from "./Route"
import { Transport } from './Transport'
import axios from 'axios'

export const TrekDescription = () => {
  const params = useParams();

  // let user_input = params.title.toLocaleLowerCase().split(" ");
  let user_input = params.title;

  let temp = 0



  const [destination_info, setDestination_info] = useState([]);
  const [route_info, setRoute_info] = useState([]);
  const [season, setSeason_info] = useState([]);

  // setDestination_info(fetchDestination())
  // async function fetchDestination() {
  //   try {
  //     const response = await axios.get(`http://127.0.0.1:8000/api/destination/?dest_name=${user_input[0]}`);
  //     // console.log(response.data)
  //     return response.data
  //     // setDestination_info(response.data);

  //     // console.log(response.data.dest_id)
  //     console.log(destination_info);
  //   } catch (err) {
  //     console.log(err);
  //   }
  // }
  // fetchDestination()

  // useEffect(() => {
  //   // const fetchDestination = async () => {
  //   //   const data = await fetch(`http://127.0.0.1:8000/api/destination/?dest_name=${user_input[0]}`);
  //   //   const json = await data.json();
  //   //   setDestination_info(json)
  //   //   setDest_id(json.dest_id)
  //   //   console.log(destination_info)
  //   // }};

  //   // const fetchRoute = async () => {
  //   //   const data = await fetch(`http://127.0.0.1:8000/api/route-info/?dest_name=${user_input[0]}`);
  //   //   const json = await data.json()
  //   //   setRoute_info(json)
  //   //   console.log(route_info)
  //   // };


  //   async function fetchDestination() {
  //     try {
  //       const response = await axios.get(`http://127.0.0.1:8000/api/destination/?dest_name=${user_input[0]}`);
  //       // console.log(response.data)
  //       setDestination_info(response.data);
  //       // console.log(response.data.dest_id)
  //       console.log(destination_info);
  //     } catch (err) {
  //       console.log(err);
  //     }
  //   }

  //   async function fetchRoute() {
  //     try {
  //       const response = await axios.get(`http://127.0.0.1:8000/api/route-info/?dest_name=${user_input[0]}`);
  //       // console.log(response.data)
  //       // await new Promise(resolve => setTimeout(resolve, 1000));
  //       setRoute_info(response.data);
  //       // await new Promise(resolve => setTimeout(resolve, 1000));
  //       console.log(route_info)
  //     } catch (err) {
  //       console.log(err);
  //     }
  //   }

  //   fetchDestination();
  //   fetchRoute();
        
  // }, []);

  useEffect(() => {
    getDestination();
    getRoutes();
    getSeason();
  }, [user_input]);

  const getDestination = () => {
    axios.get(`http://127.0.0.1:8000/api/destination/?dest_name=${user_input}`)
    .then((response) => {
      const ourDestination = response.data;
      setDestination_info(ourDestination);
    })
    .catch(error => console.log(`Error: ${error}`));
  }

  const getRoutes = () => {
    axios.get(`http://127.0.0.1:8000/api/route-info/?dest_name=${user_input}`)
    .then((response) => {
      const ourRoutes = response.data;
      setRoute_info(ourRoutes);
    })
    .catch(error => console.log(`Error: ${error}`));
  }

  const getSeason = () => {
    axios.get(`http://127.0.0.1:8000/api/destination-season/?dest_name=${user_input}`)
    .then((response) => {
      const seasons = response.data;
      setSeason_info(seasons.months);
    })
    .catch(error => console.log(`Error: ${error}`));
  }

  // async function fetchDestination() {
  //     try {
  //       const response = await axios.get(`http://127.0.0.1:8000/api/destination/?dest_name=${user_input[0]}`);
  //       // console.log(response.data)
  //       return response.data
  //       // setDestination_info(response.data);
  
  //       // console.log(response.data.dest_id)
  //       // console.log(destination_info);
  //     } catch (err) {
  //       console.log(err);
  //     }
  //   }

  // console.log(fetchDestination())
  
  // setDestination_info(fetchDestination());

  let desc = {

    // destination: {
    //   title: "Annapurna Base Camp",
    //   description: `Annapurna Base Camp Trek probably the best legendary and classical treks in the world offers breathe stopping Mountain View, give opportunity to experience the typical Nepali village, local people and their way of living traditional life in Himalaya of Nepal. The Annapurna Base Camp route goes passing through spectacular and tranquil landscapes, charming Gurung and Magar villages, lush green Rhododendron, bamboo and alpine forests.Mt. Annapurna (8091m) of Nepal is the 10th highest mountain in the world and the journey to its base camp, which is at 4130m/13549ft height, is one of the most popular walks on earth. Moreover, we reach our destination via Mt. Machapuchhre (Fishtail) which is revered by the Nepalese for its unique beauty. Furthermore, thanks to the well-groomed itinerary of the Annapurna Base Camp trekking package, it is a popular choice among diverse outdoor enthusiasts, from a solo female traveler to hikers traveling in groups to Nepal.`,
    //   pic: "https://img.traveltriangle.com/blog/wp-content/uploads/2018/11/cover-for-Annapurna-Base-Camp-Trek.jpg",
    //   elevation:"4130",
    //   difficulty:"Moderate",
    //   length:"8 Days",
    // }, 
    destination: destination_info,
    route: route_info,
    // route:[
    // {
    //   route_name:"Route 1",
    //   route_desc:"Trekking to Annapurana Base Camp is offered by several agencies in Pokhara as an all inclusive package with a guide and porters. It is also popular to do this trek by hiring your own staff, guides and porters are easy to find in Pokhara and this way is cheaper than a package trek. Trekking completely independent is the cheapest way to get to Annapurana Base Camp and if you can carry your own backpack the route is well marked and easy to follow.",
    //   route_pic:"https://tibetanencounter.com/wp-content/uploads/2017/10/ghandruk-trek1.jpg",
    //   packages:[
    //     {
    //       package_name: "Economy",
    //       package_cost:"8000",
    //       package_details:[
    //         "Day 1: Pokhara to Jhinu Danda via Nayapul (Trekking: approximately 4 hours)",
    //         "Day 2: Jhinu Danda to Bamboo (Trekking: approximately 6 hours)",
    //         "Day 3: Bamboo to Deurali (Trekking: approximately 5 hours)",
    // "Day 4: Deurali to Annapurna Base Camp (4130m)",
    //         "Day 5: Annapurna Base Camp to Bamboo",
    //         "Day 6: Bamboo to Zhinu Danda(1610m) Natural Hot Spring",
    //         "Day 7: Jhinu to Pokhara via Nayapul"
    //       ],
    //       guide:{
    //           guide_name:"Paras pujara",
    //           guide_number:"98625120",
    //         }
    //     },
    //   ],
    //   city:[
    //     {
    //       city_name:"Ghandruk",
    //       city_desc:"Ghandruk is a common place for treks in the Annapurna range of Nepal (Annapurna Base camp and Annapurna Circuit treks, in particular). The peaks of Mt Annapurna, Mt Machapuchare, Gangapurna and Mt Hiunchuli can be seen from the village, and it is also the gateway to the Poon hill.",

    //       city_viewpoint:[
    //       {
    //         cvp_name:"viewpoint",
    //         cvp_details:"can see sun"
    //       },
    //       {
    //         cvp_name:"culture",
    //         cvp_details:"can experience the culture of ghandruk"
    //       }],

    //       accomodation:
    //       [{
    //         hotel_name:"ghandruk hotel",
    //         phone_number:"986562655",
    //         email:"kasutub@gmail.com",
    //         price:"1000"
    //       },
    //       {
    //         hotel_name:"hotel de ghnadruk",
    //         phone_number:"",
    //         email:"",
    //         price:""
    //       }]

    //     },
    //     {
    //       city_name:"Chhomrong",
    //       city_desc:"Ghandruk is a common place for treks in the Annapurna range of Nepal (Annapurna Base camp and Annapurna Circuit treks, in particular). The peaks of Mt Annapurna, Mt Machapuchare, Gangapurna and Mt Hiunchuli can be seen from the village, and it is also the gateway to the Poon hill.",
    //       city_viewpoint:
    //       [{
    //         cvp_name:"",
    //         cvp_details:""
    //       },
    //       {
    //         cvp_name:"",
    //         cvp_details:""
    //       }],

    //     accomodation:[
    //       {
    //         hotel_name:"",
    //         phone_number:"",
    //         email:""
    //       },
    //       {
    //         hotel_name:"",
    //         phone_number:"",
    //         email:""
    //       }]
    //     }]
    // },
    // ],

    season: season,

    transport:[{
      destination_city: "Ghandruk",
      origin_city:["kathmandu"],
      medium:["VIA Car Cost:10000","VIA Bus Cost:2000"]
    },
    {
      destination_city: "Ghandruk",
      origin_city:["pokhara"],
      medium:["VIA Car Cost:3000","VIA Bus Cost:1000"]
    },]
  };

  return (
    <div className="trekdescription">
  
        <>
        <div>
          <div className="description_title">{desc.destination.dest_name}</div>
          <div className='description_flex'>
            <div className="description_text">{desc.destination.description}</div>
            <div className="description_pic"><img src={desc.destination.image_link} alt="abc" id='desc_carousel_pic'/></div> 
          </div> 
          <div className="trek_info">
            <div className="facts">Facts</div>
            <div className="facts_container">
              <div className='trek_info_title'> Max Elevation  </div>
              <div className='trek_info_desc'>{desc.destination.max_elevation}</div>
            </div>
            <div className="facts_container">
              <div className='trek_info_title'> Duration  </div>
              <div className='trek_info_desc'>{desc.destination.min_duration}</div>
            </div>
            <div className="facts_container">
              <div className='trek_info_title'> Difficulty  </div>
              <div className='trek_info_desc'>{desc.destination.difficulty}</div>
            </div>
          
          </div>
        </div>
        <div className="route_frame">
          <div id="routes">Routes</div>
          <div>
          {desc.route.length ? desc.route.map((route_number)=> {
            return <Route route_details={route_number}/>
          }): console.log("hello")}
          </div>
        </div>
        
        <div className="transport_frame ">
          <div id='transport_header'>Transportation</div>
          <div>
            {desc.transport.map((p)=>{
              return <Transport medium_desc={p}/>
            })}
          </div>
          
        </div>

        <div className="season_frame">
        <span id="season">Favourable Seasons:</span>
          <span>{desc.season.map((s)=>{
            return (<span id='season_name'>{s}</span>)
          })}</span>
        </div>

        </>
    </div>
  )
}
