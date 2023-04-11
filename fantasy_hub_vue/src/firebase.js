import { initializeApp } from 'firebase/app'
import { getAuth } from 'firebase/auth'
import { ref, getDatabase } from 'firebase/database'
// import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAc-p04OuN3jfeKwSATRr3PT7IFx_3mG9o",
  authDomain: "fantasy-hub-c58bf.firebaseapp.com",
  databaseURL: "https://fantasy-hub-c58bf-default-rtdb.firebaseio.com",
  projectId: "fantasy-hub-c58bf",
  storageBucket: "fantasy-hub-c58bf.appspot.com",
  messagingSenderId: "24916064767",
  appId: "1:24916064767:web:271a495e6c27778e6b0fca",
  measurementId: "G-ZZEMJKZMSQ"
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig)
const rtdb =  getDatabase(firebaseApp)
const auth = getAuth(firebaseApp)

export {
  rtdb,
  auth
}