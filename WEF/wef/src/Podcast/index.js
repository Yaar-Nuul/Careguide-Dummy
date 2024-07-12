import "./index.css";
import React from "react";
import soon from "../images/soon .jpeg"
import mbox from "../images/mbox .png"
import mic from "../images/mic.png"


import { FaPlay } from "react-icons/fa";

const Podcast = () => {
  return (
    <>
      <div className="podcast">
        <div className="landing-page">
          <h2 className="page-intro">LETS TALK CREATIVITY</h2>
          <div className="dot-top"></div>
          <div className="podcast-name">
            <span className="top-name"> PodCast</span>
            <div className="middle-section">
              <img src={mbox} alt="message box" className="m-box" />
              <span className="top-name"> Cre8ive</span>
            </div>
          </div>
          <div className="dot"></div>
        </div>
        <div className="release-date">
          <div className="container">
            <img src={soon} alt="Coming soon" className="release" />
            <div className="joinText">
              Join the comunity
              <FaPlay />
              <button className="episodes">Episodes</button>
            </div>
          </div>
          <img src={mic} alt="Mic" className="mic" />
        </div>
      </div>
    </>
  );
};

export default Podcast;