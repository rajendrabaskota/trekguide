import './App.css'

import {Footer} from "./My components/Common components/Footer"
import {Navbar} from "./My components/Common components/Navbar"
import {HeroSection} from "./My components/Home page/HeroSection"
import {MidPart} from './My components/Home page/midPart'
import { AboutUs } from './My components/Other pages/About/About_us'
import {Contact} from "./My components/Other pages/Contact/Contact"
import {Guides} from "./My components/Other pages/Guides/Guides"
import {SignUp} from "./My components/Other pages/SignUp/SignUp"
import {Login} from "./My components/Other pages/Login/Login"
import {TrekDescription} from "./My components/Other pages/TrekDescription/TrekDescription"
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";

function App() {
  return (
    <div className='main_body'>
    <Router>
    <Navbar/>
    <Routes>
      <Route exact path="/" element={
        <>
          <HeroSection/>
          <MidPart/>
        </>
      }/>
      <Route exact path="/About_us" element={
        <>
        <AboutUs/>
        </>
      }/>
      <Route exact path="/Contact" element={
        <>
        <Contact/>
        </>
      }/>
      <Route exact path="/Guides" element={
        <>
        <Guides/>
        </>
      }/>
      <Route exact path="/SignUp" element={
        <>
        <SignUp/>
        </>
      }/>
      <Route exact path="/Login" element={
        <>
        <Login/>
        </>
      }/>
      <Route exact path="/TrekDescription:title" element={
        <>
        <TrekDescription/>
        </>
      }/>
    </Routes>
    <Footer/>
    </Router>
    </div>
  )
}

export default App;
