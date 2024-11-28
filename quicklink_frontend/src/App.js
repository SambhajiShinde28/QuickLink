import './App.css';
import React,{ useRef,useState } from 'react';
import axios from "axios";

function App() {

  const url = useRef()
  const [shortUrl, setShortUrl] = useState("");

  const ShortURLBTNClicked=async()=>{
    if (url.current.value !== "") {

      try {
        const response = await axios.post("http://127.0.0.1:8000/api/create/", { long_url: url.current.value });
        setShortUrl(response.data.short_url);
      } catch (error) {
        console.error("Error creating short URL:", error);
      }
    }
  }

  const CopyBtnClicked=()=>{
    navigator.clipboard.writeText(shortUrl)
      .then(() => {
        alert("URL copied to clipboard!");
      })
      .catch((err) => {
        console.error("Failed to copy: ", err);
      });
  }

  return (
    <>
      <div className="Main-container">
        <header className="header">
          <h1>QuickLink</h1>
        </header>
        <main className="container">
          <div className="hero-section">
            <h4>Transform long URLs efficiently and effortlessly.</h4>
            <h1>Shorten Your <br></br>URLs In Seconds!</h1>
            <p>Experience quick and reliable URL shortening with just one click. Simplify Sharing Today!</p>
          </div>

          <div className="url-section">
            <input type="text" id="long-url" ref={url} placeholder="Enter URL" />
            <button id="shorten-btn" onClick={ShortURLBTNClicked}>Short URL</button>
          </div>

          <div className="display-section">
            <h1>Your shorted urlis below:</h1>
            <div className="urlcopy">
              <input type="text" value={shortUrl} readOnly placeholder='Enter URL' />
              <button type="button" id="copyBTN" onClick={CopyBtnClicked}>Copy</button>
            </div>
          </div>
        </main>
      </div>
    </>
  );
}

export default App;
