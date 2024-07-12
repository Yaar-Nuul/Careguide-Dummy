
import './App.css';
import Navbar from './Navbar';
import LandingPage from './Landing-page/Index';
import Podcast from './Podcast/index.js'
import VideoSection from './Video/index.js';

function App() {
  return (
    <div className="App">
     <Navbar/>
     <LandingPage/>
     <Podcast/>
     <VideoSection/>
    </div>
  );
}

export default App;
