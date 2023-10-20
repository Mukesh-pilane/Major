import { useRef, useState, useEffect} from "react";
import SpeechRecognition, { useSpeechRecognition } from "react-speech-recognition";

function SpeechToText({setMessage}) {
  const { transcript, resetTranscript } = useSpeechRecognition();
  const [isListening, setIsListening] = useState(false);
  const microphoneRef = useRef(null);
  useEffect(()=>{
    setMessage(transcript)
  }, [transcript])
  if (!SpeechRecognition.browserSupportsSpeechRecognition()) {
    return (
      <div className="mircophone-container">
        Browser is not Support Speech Recognition.
      </div>
    );
  }
  const handleListing = () => {
    setIsListening(true);
    SpeechRecognition.startListening({
      continuous: true,
    });
  };
  const stopHandle = () => {
    setIsListening(false);
    SpeechRecognition.stopListening();
    setMessage(transcript)
  };
  // const handleReset = () => {
  //   stopHandle();
  //   resetTranscript();
  // };
  // console.log(transcript);
  return (
    <div className="microphone-wrapper">
      <div className="mircophone-container">
       
       {!isListening &&
        <div
        className="microphone-icon-container microphone-stop_btn"
        ref={microphoneRef}
        onClick={handleListing}
      >

        <i class="fa-solid fa-microphone"></i>

      </div>
       } 
    
        {isListening && (
          <button className="microphone-stop_btn" onClick={stopHandle}>
            <i class="fa-solid fa-stop"></i>
          </button>
        )}
      </div>
      {/* {transcript && (
        <div className="microphone-result-container">
          <div className="microphone-result-text">transcript:{transcript}</div>
          <button className="microphone-reset_btn" onClick={handleReset}>
            Reset
          </button>
        </div>
      )} */}
    </div>
  );
}
export default SpeechToText;