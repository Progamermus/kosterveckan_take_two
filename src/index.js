import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import firebase from 'firebase';

var config = {
    apiKey: "AIzaSyCHUsQ_f7-2gfGKBtTtCHbrNCt-4dmMAFs",
    authDomain: "kosterveckan.firebaseapp.com",
    databaseURL: "https://kosterveckan.firebaseio.com",
    projectId: "kosterveckan",
    storageBucket: "kosterveckan.appspot.com",
    messagingSenderId: "152411542473"
  };
firebase.initializeApp(config);

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
