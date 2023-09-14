import React from 'react'
import {useNavigate, useLocation} from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useGoogleLogout } from 'react-google-login';


import "./home.css"

export default function Home() {
  const navigate = useNavigate();

  const {profilePicture} = useSelector((state) => state.user);
const clientId = "1044924794976-n418rqsvep3iiaiecfsqlkf1jf5895is.apps.googleusercontent.com";
const onFailure = () =>{
    console.log('failure')
  }

  const onLogoutSuccess = () =>{
    navigate('/auth')
    console.log('success')
  }
  const {signOut} = useGoogleLogout({
    clientId,
    onLogoutSuccess,
    onFailure
  }) 
 
    return (
        <div className="chat-bot__container">
        <div className="card">
        <div id="header">
            <div className="chat-bot__header-title">
            <h1>Chat box!</h1>          
            </div>
            <div className="chat-bot__icon-container">
                <div className="chat-bot__profile-icon">
                    <img src={profilePicture} alt="" />
                    
                </div>
                <div className="chat-bot__logout"
                onClick={()=>{
                    localStorage.clear();
                    signOut()
                }}
                >
                    <i className="fa fa-sign-out" aria-hidden="true"></i>
                    </div>
            </div>
        </div>
        <div id="message-section">
          <div className="message" id="bot"><span id="bot-response">Hello.. I'm listening! Go on..</span></div>
        </div>
        <div id="input-section">
          <input id="input" type="text" placeholder="Type a message" autoComplete="off" autoFocus="autofocus"/>
          <button className="send" onClick="sendMessage()">
            <div className="circle"><i className="zmdi zmdi-mail-send"></i></div>
          </button>
        </div>
      </div>      
      </div>
    )
}