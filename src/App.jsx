import React, {useState, useEffect} from 'react';
import Auth from "./pages/Auth/Auth"
import Home from "./pages/Home/Home"
import {Routes, Route, useLocation} from 'react-router-dom'

// import DetailedSummary from './pages/DetailedSummary/DetailedSummary';
// import Allsummaries from './containers/Allsummaries'
// import Uploader from './containers/CreateSummary'
import { useDispatch } from "react-redux";
import {verify } from "./features/userSlice";



function App() {
const dispatch = useDispatch();

useEffect(() => {
  if(localStorage.getItem('tokenId')){
  dispatch(verify());
  }
  }
  
  , [])

  return (
    <div className="App">
    <Routes>
                <Route path="/" element={<Home />} >
                </Route>
                <Route path="/auth" element={<Auth />} />
        </Routes>
    </div>
  );
}

export default App;
