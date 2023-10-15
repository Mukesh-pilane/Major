import 'regenerator-runtime/runtime';
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter as Router } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store/store';
import { SpeechRecognitionProvider } from 'react-speech-recognition';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* <SpeechRecognitionProvider> */}

      <Router>
        <Provider store={store}>

          <App />

        </Provider>
      </Router>
    {/* </SpeechRecognitionProvider> */}

  </React.StrictMode>
);
