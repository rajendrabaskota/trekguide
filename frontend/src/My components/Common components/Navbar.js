import React, {useRef, useState}from 'react'
import "./Navbar.css"
import img_logo from "../Images/trekker logo.png"
import cancel from "../Images/cancel.png"
import search from "../Images/Search.png"
import menu from "../Images/Menu.png"
import axios from 'axios'
// import {suggestions} from "./search_suggestions"
import {
    Link, useNavigate
} from "react-router-dom";
import { useEffect } from "react"

export const Navbar = () => {

    const [toggle_dropdown, settoggle_dropdown] = useState(false);
    const [suggestions, setSuggestions] = useState([]);
    const [search_value, setsearch_value] = useState("");


    let search_dropdown = () => {
        !toggle_dropdown ? settoggle_dropdown(true):settoggle_dropdown(false);
    };

    let menuRef = useRef();

    useEffect(() => 
    {
        getTitles();
        let handler = (event) => 
        {
            if(!menuRef.current.contains(event.target))
            {
                settoggle_dropdown(false);
            }
        }  
         document.addEventListener("mousedown", handler);
         return (() => {document.removeEventListener("mousedown", handler)})
    }, [search_value]);

    const getTitles = () => {
        axios.get(`http://127.0.0.1:8000/api/destination-title/`)
        .then((response) => {
          const titles = response.data;
          setSuggestions(titles);
        })
        .catch(error => console.log(`Error: ${error}`));
      }


    const [toggle_menu, settoggle_menu] = useState(false);

    let open_menu = () => {
        !toggle_menu ? settoggle_menu(true): settoggle_menu(false);
    };

    
    let search_onchange = (event)=>{
        settoggle_dropdown(true);
        let userdata=event.target.value;
        setsearch_value(userdata);
        let emptyarray= [];

        if (userdata){
            emptyarray=suggestions.filter(
                (data)=>{return data.toLocaleLowerCase().startsWith(userdata.toLocaleLowerCase());}
            );
            emptyarray=emptyarray.map((data)=>{return data = '<li>'+data+'</li>'});
        }
        showsuggestions(emptyarray);
    };

    let showsuggestions = (list) => {
        let search_bar = document.querySelector(".navbar_searchBar");
        let search_dropdown = search_bar.querySelector(".search_dropdown");
        let search_list = search_dropdown.querySelector(".search_list");
        if(!list.length){

        }
        else{list= list.join('');}
        
        search_list.innerHTML = list;

        let list_items=search_list.querySelectorAll("li");
        for (let i=0;i< list_items.length;i++) {
            list_items[i].addEventListener("click",() => {select(list_items[i])});
        }
    };

    let navigate = useNavigate();

    let select = (element) => {
        setsearch_value(element.innerText);
        navigate(`/TrekDescription${element.innerText}`);
        settoggle_dropdown(false);
    };

  return (
    <div className='navbar_container'>
        <Link to="/">
        <div className="navbar_title" onClick={`localhost:3000/`}>
            <img src={img_logo} alt="logo_image" className="navbar_logo_image" />
            <div className='navbar_title_text'>
                <p>Trek</p>
                <p>Manager</p>
            </div>
        
        </div>
        </Link>
        <div className="navbar_searchBar" ref={menuRef}>
            <img src={search} alt="Search_icon" className="navbar_search_icon" />
            <input className="navbar_search_text" type="text" placeholder='Search for destinations' onClick={search_dropdown} value={search_value} onChange={search_onchange}/>
            <div className={toggle_dropdown ? "search_dropdown search_dropdown_active":"search_dropdown search_dropdown_inactive" }>
                <ul className='search_list'></ul>
            </div> 
        </div>
        <ul className="navbar_wrapper">
            <li><Link to="/">Home</Link></li>
            <li><Link to="/about_us">About Us</Link></li>  
            <li><Link to="/Contact">Contact</Link></li>
            <li><Link to="/SignUp">Sign Up</Link></li>
            <li><Link to="/Login">Login</Link></li>
            <li><Link to="/Guides">Guides</Link></li>
        </ul>
        <div className='navbar_menu' onClick={open_menu}>
            <img src={!toggle_menu? menu : cancel} alt="menu_icon" className="navbar_menu_icon"/>
        </div>
    </div>
  )
}
