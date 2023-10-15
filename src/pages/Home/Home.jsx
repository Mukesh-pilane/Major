import React, {useState, useEffect, useRef} from 'react'
import {useNavigate, useLocation} from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useGoogleLogout } from 'react-google-login';
import axios from 'axios'
import SpeechToText from '../../components/SpeechToText';
import "./home.css"

export default function Home() {
  const navigate = useNavigate();
  const [message, setMessage] = useState('');
  const [chatData, setChatData] = useState({
    existingMessages: [],
    responseMessage: '',
  });
  const messageAreaRef = useRef();
  
  const [flag, setFlag] = useState(true)
  const serverEndpoint = `https://chatbotapi-hw03.onrender.com/messages`;
  const {profilePicture} = useSelector((state) => state.user);
const clientId = "423801836330-a83v044m2fg4rbqusrd6t86d795mco2g.apps.googleusercontent.com";
const onFailure = () =>{
    console.log('failure')
  }


  function scrollToBottom() {
    if (messageAreaRef.current) {
      messageAreaRef.current.scrollTop = messageAreaRef.current.scrollHeight ;
    }
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
 

  const handleMessageChange = (e) => {
    setMessage(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();


    // Define your server endpoint where you want to send the message
  // Replace with your actual endpoint

    // Create a data object with the message to send
    const data = { message };

    // Send a POST request to the server
    axios.post(serverEndpoint, data,{headers:{
      "Authorization": localStorage.getItem('tokenId')
  }
  })
      .then((response) => {
        // Handle the success response from the server
        const newChatData = {
          ...chatData,
          responseMessage: response.data.message,
        };
        setChatData(newChatData);
        setFlag(!flag)
        // Clear the message input
        setMessage('');
      })
      .catch((error) => {
        // Handle errors here
        console.error('Error sending message:', error);
      });
      scrollToBottom()
  };

  const fetchExistingMessages = () => {
    // Define your server endpoint to fetch existing messages

    axios.get(serverEndpoint,{headers:{
      "Authorization": localStorage.getItem('tokenId')
  }
  })
      .then((response) => {
        // Handle the success response by updating the existingMessages property of chatData
        const newChatData = {
          ...chatData,
          existingMessages: response.data,
        };
        setChatData(newChatData);

      })
      .catch((error) => {
        // Handle errors here
        console.error('Error fetching messages:', error);
      });
  };

  useEffect(() => {
    // Fetch existing messages when the component mounts
    fetchExistingMessages();
  }, [flag]); 
  useEffect(() => {
    if(!localStorage.getItem('tokenId')){
      navigate('/auth')
    }
  })

    return (
        <div className="chat-bot__container">
        <div className="card">
        <div id="header">
            <div className="chat-bot__header-title">
            <h1>Chat box!</h1>          
            </div>
            <div className="chat-bot__icon-container" ref={messageAreaRef}>
                <div className="chat-bot__profile-icon">
                    <img src={profilePicture? profilePicture : ""} alt="" />
                    
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
        <div id="message-section" >
          {
            chatData.existingMessages?.map((res,i)=>{
              return(
                <React.Fragment key={i}>
                <div className="message" id="user"><span id="user-message">{res.message}</span></div>
                <div className="message" id="bot"><span id="bot-response">{res.botResponse}</span></div>
                </React.Fragment>
              )
            })
          }
          {/* <div className="message" id="bot"><span id="bot-response">{chatData.responseMessage}</span></div>
          <div className="message" id="user"><span id="user-message">{message}</span></div> */}
        </div>
        <div id="input-section">
          <input onChange={handleMessageChange} value={message} id="input" type="text" placeholder="Type a message" autoComplete="off" autoFocus="autofocus"/>
          <button className="send" onClick={handleSubmit}>
            <div className="circle"><i className="zmdi zmdi-mail-send"></i></div>
          </button>
        </div>
      </div>      
      <SpeechToText />

      </div>
    )
}