import React, {useState, useEffect, useRef} from 'react'
import {useNavigate, useLocation} from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useGoogleLogout } from 'react-google-login';
import axios from 'axios'
import SpeechToText from '../../components/SpeechToText';
import "./home.css"
import { useSpeechSynthesis } from "react-speech-kit";



export default function Home() {
  const navigate = useNavigate();
  const [message, setMessage] = useState('');
  const { speak } = useSpeechSynthesis();
  const [isAudio, setIsAudio] = useState(false)
  const [isloaded, setIsLoaded] = useState(false)

  const [chatData, setChatData] = useState({
    existingMessages: [],
    userMessage: null,
    responseMessage: null,
  });

  const handleAudio = ()=>{
    setIsAudio(!isAudio);
  }
  
  const messageAreaRef = useRef();
  const messageSectionRef = useRef(null);
  
  const serverEndpoint = `https://chatbotapi-hw03.onrender.com/messages`;
  const {profilePicture} = useSelector((state) => state.user);
const clientId = "423801836330-a83v044m2fg4rbqusrd6t86d795mco2g.apps.googleusercontent.com";
const onFailure = () =>{
    console.log('failure')
  }


  function scrollToBottom(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
      element.scrollTop = element.scrollHeight+200;
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


    const data = { message };


    axios.post(serverEndpoint, data,{headers:{
      "Authorization": localStorage.getItem('tokenId')
  }
  })
      .then((response) => {

        if(chatData.responseMessage){
          const updatedChatData = { ...chatData };

          // Update the existingMessages property with the new message
          updatedChatData.existingMessages.push({message: chatData.userMessage, botResponse:chatData.responseMessage});
  
          setChatData(updatedChatData);
        }
        if(isAudio){
          speak({ text: response.data })
        }
          const newChatData = {
          ...chatData,
          userMessage :message,
          responseMessage: response.data,
        };
        console.log(newChatData);
        setChatData(newChatData);
        setMessage('');
        scrollToBottom('message-section');

      })
      .catch((error) => {
        console.error('Error sending message:', error);
      });

  };

  const fetchExistingMessages = () => {

    axios.get(serverEndpoint,{headers:{
      "Authorization": localStorage.getItem('tokenId')
  }
  })
      .then((response) => {
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

    // console.log(messageSection.scrollTop, messageSection.scrollHeight)
  }, []); 
  useEffect(() => {
    if(!localStorage.getItem('tokenId')){
      navigate('/auth')
    }

  },[])

  useEffect(() => {
    // Set showLoader to true when the component mounts
    setIsLoaded(true);

    // Use setTimeout to hide the loader after 2 seconds
    const loaderTimeout = setTimeout(() => {
      setIsLoaded(false);
    }, 2000); // 2000 milliseconds = 2 seconds

    // Clear the timeout when the component unmounts to avoid memory leaks
    return () => {
      clearTimeout(loaderTimeout);
    };
  }, []);
  if(isloaded){
    return (
    <div className='chat-bot__loader__container'>
    <div class="loader"></div> ;
    </div>
    )
  }
    return (
        <div className="chat-bot__container">
        <div className="card">
        <div id="header">
            <div className="chat-bot__header-title">
            <h1>Chat box!</h1>          
            </div>
            <div className="chat-bot__icon-container" ref={messageAreaRef}>
                <div className="chat-bot__profile-icon">
                    <img src={profilePicture? profilePicture : "https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png"} alt="" />
                    
                </div>
                <div className={isAudio?"audio_icon audio_Active":"audio_icon"}
                onClick={()=>{
                  handleAudio()
                }}>
                <i className="fa-solid fa-volume-high"></i>
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
        <div id="message-section" ref={messageSectionRef}>
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
          {chatData.responseMessage &&
          <>
          <div className="message" id="user"><span id="user-message">{chatData.userMessage}</span></div>
          <div className="message" id="bot"><span id="bot-response">
          
              {chatData.responseMessage}
            
            </span></div>
          </>
          }
        
        </div>
        <div id="input-section">
          <input onChange={handleMessageChange} value={message} id="input" type="text" placeholder="Type a message" autoComplete="off" autoFocus="autofocus"/>
          <button className="send" onClick={handleSubmit}>
            <div className="circle"><i className="zmdi zmdi-mail-send"></i></div>
          </button>
      <SpeechToText setMessage={setMessage}/>
        </div>
      </div>      

      </div>
    )
}