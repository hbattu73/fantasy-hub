import { defineStore } from "pinia"
import { auth, rtdb } from '../firebase'
import { ref, set, get, child } from 'firebase/database'
import { createUserWithEmailAndPassword, signInWithEmailAndPassword,
signOut, onAuthStateChanged } from "firebase/auth"
import { useEspnAuth } from "./storeEspn"
export const useStoreAuth = defineStore('storeAuth', {
    state: () => {
        return {
            user: {}
        }
    },
    persist: true,
    // getters:{
    //     async loggedIn(state) {
    //         return true ? state.user.id : false
    //     }
    // },
    actions: {
        init() {
            onAuthStateChanged (auth, async (user) => {
                if (user) {
                    // User is signed in, see docs for a list of available properties
                    this.user.id = user.uid
                    this.user.email = user.email
                    console.log('User cred set: ', this.user)
                } 
                else {
                    // User is signed out
                    const storeEspn = useEspnAuth() 
                    storeEspn.$reset()
                    this.$reset()
                    // this.router.replace('/')
                    console.log('User is logged out: ', user)
                }
            })
        },
        async registerUser(credentials) {
            try {
                const userCredential = await createUserWithEmailAndPassword(auth, credentials.email, credentials.password)
                set(ref(rtdb, 'users/' + userCredential.user.uid), {
                    email: userCredential.user.email
                })
                this.router.push({ name:'platform_select' })
                console.log('user registered', this.user)
                // this.router.push('/platform-select')
                // Registered
                 // TODO Redirect user to select platform page
            }
            catch(error) {
                console.log('Error: ', error)
                // Plausible registration auth errors
                switch(error.code) {
                    case "auth/email-already-in-use":
                        return "Authentication Error: Email already in use."
                    case "auth/weak-password":
                        return "Authentication Error: Try a stronger password."
                    default:
                        // Just display whatever error if not above two
                        return error.message
                }
            }
        },
        async loginUser(credentials) {
            try {
                await signInWithEmailAndPassword(auth, credentials.email, credentials.password)
                console.log('user logged in', this.user)
                // Logged in
                const storeEspn = useEspnAuth() 
                storeEspn.init()
                this.router.push({ name:'dashboard' })
            }
            catch(error) {
                console.log('Error: ', error)
                // Plausible registration auth errors
                switch(error.code) {
                    case "auth/invalid-email":
                        return "Authentication Error: Invalid email."
                    case "auth/user-not-found":
                        return "Authentication Error: Email does not exist."
                    case "auth/wrong-password":
                        return "Authentication Error: Wrong Password."
                    default:
                        return error.message
                }
            }
        },
        async logOutUser() {
            try {
                await signOut(auth)
                this.router.replace('/')
                // Sign-out successful.
                // TODO Redirect user back to hero section and unsubscribe from any rtdb listeners.
            }
            catch(error) {
                // Just alert whatever error happened.
                alert(error.message)
            }            
        }
    }
})