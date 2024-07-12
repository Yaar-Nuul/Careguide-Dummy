import './index.css'
import thumbnail from '../images/thumbnail.png'
import { FaPlayCircle } from "react-icons/fa";

const VideoSection = () => {
    return (
        <div className='aboutVideo'>
          <div className='container'>
          <h1 className="heading">Explore Our Diverse Video Collection</h1>
            <div>
              <img src={thumbnail} alt="musicPic" className="videopic" />
            </div>
            <strong className='videoHeading'>Watch, Learn, and Be Captivated</strong>
            <div className='welcomeText'>
              Crafted with unparalleled skill and vision, this video
              stands a testament to the power of video storytelling. Delve into
              a captavating exploration of spotify that transcends time and trends,
              offering a timeless perspective that will resonate with viewers for years
              to come.
            </div>
            <button className='watchButton'><FaPlayCircle size={30} />Watch </button>
          </div>
        </div>
      );
    }
export default VideoSection;