import { defineStore } from "pinia"
import { useStoreAuth } from "./storeAuth"
import { rtdb } from "../firebase"
import { ref, set, onValue } from 'firebase/database'
export const useEspnAuth = defineStore('storeEspn', {
    state: () => {
        return {
            leagueIDs: [],
            espn_s2: '',
            swid: ''
        }
    },
    actions: {
        init() {
            // TODO: account for any error handling when these cred. may not be available at database
            // DO THIS BY TRY-CATCH and call init in init of storeAuth or during app mount
            // TODO: get league ids as well from db
            const storeAuth = useStoreAuth()
            const espnS2Ref = ref(rtdb, 'users/' + storeAuth.user.id + '/platforms/espn/cookies/espn_s2')
            onValue(espnS2Ref, (snapshot) =>{
                this.espn_s2 = snapshot.val();
            })
            const swidRef = ref(rtdb, 'users/' + storeAuth.user.id + '/platforms/espn/cookies/swid')
            onValue(swidRef, (snapshot) =>{
                this.swid = snapshot.val();
                console.log('swid', this.swid)
            })
        },
        registerCredentials(ids, cookies) {
            const storeAuth = useStoreAuth()
            this.leagueIDs = ids
            this.espn_s2 = cookies.espn_s2
            this.swid = cookies.swid
            let path = 'users/'+storeAuth.user.id+'/platforms/espn'
            set(ref(rtdb, path+'/cookies'), {
                espn_s2: this.espn_s2,
                swid: this.swid
            })
            set(ref(rtdb, path+'/leagues'), {
                ids: this.leagueIDs
            })
            this.router.push({ name:'dashboard' })
        }
    }
})