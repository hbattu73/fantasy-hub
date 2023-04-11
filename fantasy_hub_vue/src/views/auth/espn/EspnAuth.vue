<template>
    <header class="grid grid-cols-3 py-12 pl-0 w-full container">
        <div class=""></div>
        <div class="flex flex-col items-center justify-center">
            <RouterLink :to="{ name:'home' }">
                <Logo class="w-40 md:w-48 cursor-pointer"/>
            </RouterLink>     
        </div>
        <div></div>
    </header>
    <main class="flex flex-col flex-grow flex-shrink-0 items-center w-full">
        <h1 class="text-center text-2xl md:text-3xl tracking-tight leading-9 font-bold font-inter text-light-text px-8 mb-4">Lastly, just a couple more things.</h1>
        <div class="w-full max-w-xs md:max-w-md py-4 px-8">
            <div class="text-center flex flex-col">
                <h2 class="text-center inline-flex items-center justify-center font-inter font-semibold text-base md:text-lg leading-7 text-light-text px-8">
                    ESPN league IDs
                </h2>
                <div class="flex flex-col items-center justify-center">
                    <div class="px-10 overflow-x-hidden overflow-y-auto max-h-40 border-slate-400 scrollbar-thin scrollbar-thumb-slate-500/90 scrollbar-track-gray-300"
                            :class="{ 'border-b-1': numLeagues > 2 }">
                        <ul class="relative space-y-3 py-2">
                            <li class="relative">
                                <button @click="addInput" type="button" class="absolute -left-10 top-1 hover:scale-110 [transition:transform_0.2s] cursor-pointer"
                                :disabled="numLeagues > 3"
                                :class="{ 'pointer-events-none': numLeagues > 3 }"
                                >
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="text-light-text w-7 h-7"
                                    :class="{ 'text-light-text/40': numLeagues > 3 }"
                                    >
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </button>
                                <input v-model="leagues[0].leagueID" type="number" class="py-1.5 px-1.5 text-base  text-zinc-600 font-semibold font-lato bg-transparent rounded border-1 border-zinc-400 appearance-none shadow-sm focus:outline-none placeholder:text-gray-500 placeholder:font-normal focus:ring-1 focus:ring-sky-600 focus:shadow-md" placeholder="League ID"/>
                            </li>
                            <TransitionGroup name="list">
                                <li v-for="l in leagues.slice(1)" :key="l.idx" class="relative">
                                    <button @click="removeInput(l.idx)" type="button" class="absolute inset-y-0 right-2 flex items-center focus:outline-none">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="text-rose-300 hover:text-rose-400 w-5 h-5">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                    </button>
                                    <input v-model="l.leagueID" type="number" class="py-1.5 px-1.5 text-base text-zinc-600 font-semibold font-lato bg-transparent rounded border-1 border-zinc-400 appearance-none shadow-sm focus:outline-none placeholder:text-gray-500 placeholder:font-normal focus:ring-1 focus:ring-sky-600 focus:shadow-md" placeholder="League ID"/>
                                </li>
                            </TransitionGroup>
                        </ul>
                    </div>
                    <Transition>
                        <span v-if="numLeagues > 3" class="mt-2 mb-1 text-sm font-semibold font-inter text-sky-800">League limit (4) reached!</span>
                    </Transition>
                    <div v-show="!validLeagueInput" class="px-10 items-center inline-flex">
                        <ExclamationIcon class="w-5 h-5 text-red-500 mr-2"/>
                        <span class="font-inter text-xs text-red-500 font-medium">Enter at least one league ID.</span>
                    </div>
                </div>
            </div>
            <div class="my-4 flex items-center">
                <hr class="flex-grow m-0 border-t-1 border-stone-500">
                <span class="px-5 text-gray-600 font-inter font-normal">AND</span>
                <hr class="flex-grow m-0 border-t-1 border-stone-500">
            </div>
            <div class="flex flex-col items-center justify-center">
                <h2 class="text-center inline-flex items-center justify-center font-inter font-semibold text-normal md:text-lg leading-7 text-light-text px-8">
                    ESPN session cookies
                </h2>
                <div class="flex flex-col space-y-3 pt-2">
                    <input
                        v-model="cookies.swid"
                        type="text" 
                        class="py-1.5 px-1.5 text-base text-zinc-600 font-semibold font-lato bg-transparent rounded border-1 border-zinc-500 appearance-none shadow-sm focus:outline-none placeholder:text-gray-500 placeholder:font-normal focus:ring-1 focus:ring-sky-600 focus:shadow-md" placeholder="SWID"/>
                    <input
                        v-model="cookies.espn_s2"
                        type="text" 
                        class="py-1.5 px-1.5 text-base text-zinc-600 font-semibold font-lato bg-transparent rounded border-1 border-zinc-500 appearance-none shadow-sm focus:outline-none placeholder:text-gray-500 placeholder:font-normal focus:ring-1 focus:ring-sky-600 focus:shadow-md" placeholder="ESPN_S2"/>
                </div>
                <div v-show="!validCookieInput" class="px-10 pt-2 items-center inline-flex">
                    <ExclamationIcon class="w-5 h-5 text-red-500 mr-2"/>
                    <span class="font-inter text-xs text-red-500 font-medium">Enter both session cookie info.</span>
                </div>
            </div>
        </div>
        <div class="max-w-xs w-full mx-auto">
            <button
                @click="handleSubmit"
                type="button"
                :disabled="loading"
                class="inline-flex my-4 justify-center items-center text-center text-light-bg-primary bg-sky-400 w-full rounded-md px-5 py-2.5 hover:bg-sky-500 [transition:background-color_0.5s]">
                <span v-if="!loading" class="text-lg font-medium">Finish</span>
                <svg v-else-if="loading" aria-hidden="true" class="inline w-7 h-7 text-gray-200 animate-spin fill-sky-700" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                </svg>
            </button>
        </div>
    </main>
    <!-- <pre>{{ leagues }}</pre> -->
    <!-- <pre>{{ cookies }}</pre> -->
</template>

<script setup>
import Logo from '../../../components/svg/Logo.vue'
import ExclamationIcon from '../../../components/svg/ExclamationIcon.vue'
import { ref, reactive, watch, computed } from 'vue'
import { useEspnAuth } from '../../../stores/storeEspn'
import { useStoreAuth } from '../../../stores/storeAuth'
import { auth } from '../../../firebase'
import axios from 'axios'

const storeEspn = useEspnAuth()
const storeAuth = useStoreAuth()

let idx = 0
const numLeagues = ref(1)
const leagues = ref([{ idx: idx++, leagueID: ''}])
const cookies = reactive({
    swid: '',
    espn_s2: ''
})
const validLeagueInput = ref(true)
const validCookieInput = ref(true)

const showInputErrMessages = reactive({
    leagueInput: false,
    cookieInput: false
})

const loading = ref(false)

function addInput() {
    leagues.value.push({ idx: idx++, leagueID: ''})
    numLeagues.value += 1
}
function removeInput(idx) {
    leagues.value = leagues.value.filter((l) => l.idx !== idx)
    numLeagues.value -= 1
}

async function handleSubmit() {
    loading.value = true
    showInputErrMessages.leagueInput = false
    showInputErrMessages.cookieInput = false
    validLeagueInput.value = leagues.value.some(l => l.leagueID)
    validCookieInput.value = cookies.swid && cookies.espn_s2 ? true : false
    if (validLeagueInput.value && validCookieInput.value) {
        let ids = []
        leagues.value.forEach(l => { ids.push(l.leagueID) })
        const token = await auth.currentUser.getIdToken(true)
        const options = {
            headers: { "Authorization": token },
            params: { 
                "swid": cookies.swid,
                "espn_s2": cookies.espn_s2,
                "leagues": JSON.stringify(ids),
                "uid": storeAuth.user.id }
        }
        try {
            const res = await axios.get('https://function-1-le6lonisya-uc.a.run.app', options)
            if (res.status === 200) {
                storeEspn.registerCredentials(ids, cookies)
            }
        }
        catch (error) {
            console.log(error)
            // TODO: Not all errors have data field i guess
            alert(error.response.data)
        }
        loading.value = false
    }
    loading.value = false
    showInputErrMessages.leagueInput = true
    showInputErrMessages.cookieInput = true
}

watch(
  () => leagues.value,
  (newLeaguesValue, oldLeaguesValue) => {
    if (showInputErrMessages.leagueInput) {
        validLeagueInput.value = newLeaguesValue.some(l => l.leagueID)
    }
  },
  { deep: true }
)
watch(
  () => cookies,
  (newCookiesValue, oldCookiesValue) => {
    if (showInputErrMessages.cookieInput) {
        validCookieInput.value = newCookiesValue.swid && newCookiesValue.espn_s2 ? true : false
    }
  },
  { deep: true }
)
</script>
<style>
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

</style>