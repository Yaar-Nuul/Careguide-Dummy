import React from 'react';
import './index.css';
import Nairat from '../images/Nairat.png'
import Yaar from '../images/Yaar.png';
import KC from '../images/KC.png';
import Bridget from '../images/Bridget.png';
import Martha from '../images/Martha.png';


const LandingPage = () => {
  return (
    <div className='container'>
      <div className='landing-page-text'>
        <h3>Unlock a world of creativity, knowledge, and inspiration on Dhakii  </h3>
        <p>Welcome to Dhakii, where creativity, knowledge, and inspiration converge.
     Here, you'll find a captivating blend of multimedia content that caters to a wide range of interests and passions.</p>
        <br>
        </br>
        
        <div className='get-started'>
            <button className='btnGetStarted'>Get Started</button>
            <button className='btnLearnMore'>Learn More</button>
        </div> 
      </div>

      <div className='landing-page-image'>

        <div className='front-row-image'>
        <img src={Nairat} alt='' className='front-student'/>
        <img src={Yaar} alt='' className='front-student'/>
        </div>
        
        <div className='image-last-row'>
        <img src={KC} alt='' className='image-students'/>
        <img src={Bridget} alt='' className='image-students'/>
        <img src={Martha} alt='' className='image-students'/>
       
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
