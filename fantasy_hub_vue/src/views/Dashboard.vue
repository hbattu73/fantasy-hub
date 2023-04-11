<template>
    <main class="flex flex-col flex-grow flex-shrink-0 items-center px-4 lg:px-16 pt-4">
        <div class="pb-3 pt-1 flex flex-col md:flex-row items-center md:items-start container">
            <div class="flex text-center md:text-start justify-center md:justify-start w-full">
                <div class="">
                    <h2 class="font-inter font-bold text-lg md:text-2xl text-light-text">Player Lineup Dashboard</h2>
                    <h4 class="font-inter font-medium text-sm md:text-base text-slate-500">Track which players you should root for across <span class="text-slate-600 underline underline-offset-2 font-bold">all</span> your leagues.</h4>
                </div>
            </div>
            <div class="mt-1 flex text-center justify-center md:justify-end w-full">
                <div class="flex flex-wrap justify-center">
                    <div class="flex flex-nowrap items-center space-x-3 overflow-auto whitespace-nowrap">
                        <span class="font-inter text-light-text font-medium inline-flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="mr-1 w-5 h-5 text-teal-600">
                                <path fill-rule="evenodd" d="M9.315 7.584C12.195 3.883 16.695 1.5 21.75 1.5a.75.75 0 01.75.75c0 5.056-2.383 9.555-6.084 12.436A6.75 6.75 0 019.75 22.5a.75.75 0 01-.75-.75v-4.131A15.838 15.838 0 016.382 15H2.25a.75.75 0 01-.75-.75 6.75 6.75 0 017.815-6.666zM15 6.75a2.25 2.25 0 100 4.5 2.25 2.25 0 000-4.5z" clip-rule="evenodd" />
                                <path d="M5.26 17.242a.75.75 0 10-.897-1.203 5.243 5.243 0 00-2.05 5.022.75.75 0 00.625.627 5.243 5.243 0 005.022-2.051.75.75 0 10-1.202-.897 3.744 3.744 0 01-3.008 1.51c0-1.23.592-2.323 1.51-3.008z" />
                            </svg>
                            <span class="text-xs md:text-sm">Certified Stud</span>
                        </span>
                        <span class="font-inter text-light-text font-medium inline-flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="mr-1 w-5 h-5 text-sky-600">
                                <path fill-rule="evenodd" d="M14.615 1.595a.75.75 0 01.359.852L12.982 9.75h7.268a.75.75 0 01.548 1.262l-10.5 11.25a.75.75 0 01-1.272-.71l1.992-7.302H3.75a.75.75 0 01-.548-1.262l10.5-11.25a.75.75 0 01.913-.143z" clip-rule="evenodd" />
                            </svg>
                            <span class="text-xs md:text-sm">Boom/Bust</span>
                        </span>
                        <span class="font-inter text-light-text font-medium inline-flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="mr-1 w-5 h-5 text-rose-600">
                                <path fill-rule="evenodd" d="M1.72 5.47a.75.75 0 011.06 0L9 11.69l3.756-3.756a.75.75 0 01.985-.066 12.698 12.698 0 014.575 6.832l.308 1.149 2.277-3.943a.75.75 0 111.299.75l-3.182 5.51a.75.75 0 01-1.025.275l-5.511-3.181a.75.75 0 01.75-1.3l3.943 2.277-.308-1.149a11.194 11.194 0 00-3.528-5.617l-3.809 3.81a.75.75 0 01-1.06 0L1.72 6.53a.75.75 0 010-1.061z" clip-rule="evenodd" />
                            </svg>
                            <span class="text-xs md:text-sm">Slumping</span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        <div class="w-full container">
            <ul class="flex flex-row overflow-auto whitespace-nowrap scrollbar-thin scrollbar-thumb-slate-500/90 scrollbar-track-gray-300 rounded-sm shadow-lg">
                <li @click="handleCurrentWeek(n)" v-for="n in box_scores.length" class="border-r-1 border-slate-300 pb-3 pt-1 px-3 bg-slate-600 hover:bg-[#78acd8] cursor-pointer"
                :class="{'bg-[#78acd8]': n == currentWeek}">
                    <span class="font-inter text-sm text-white">Week {{ n }}</span>
                </li>
                <li v-for="n in 18 - Math.min(box_scores.length, 18)" class="border-r-1 border-slate-300 pb-3 pt-1 px-3 bg-slate-700/70 pointer-events-none">
                    <span class="font-inter text-sm text-light-bg-primary/60">Week {{ box_scores.length + n }}</span>
                </li>
            </ul>
        </div>
        <div class="w-full container grid gap-6 md:grid md:grid-cols-3 md:gap-0 max-h-[452px] scrollbar-thin scrollbar-thumb-slate-500/90 overflow-y-scroll"
            :class="{'border-b-1 border-slate-300': !loading }">
            <div class="flex flex-col">
                <div class="top-0 sticky bg-light-bg-primary/80 backdrop-blur z-50 flex flex-col items-center justify-center border-b-1 border-stone-300 py-2">
                    <span class="font-inter text-light-text font-semibold">Root For</span>
                </div>
                <div class="flex flex-col py-2 w-full space-y-3">
                    <ProjectedCard v-for="p in filteredScores.filter((obj) => obj['Status'] === 'ROOT')"
                        :headshot="p.Headshot"
                        :name="p.Name"
                        :position="p.Position"
                        :team="p.Team"
                        :projected="p.Projected"
                        :points="p.Points"
                        :bye="p.Bye"
                    />
                </div>
            </div>
            <div class="flex flex-col">
                <div class="top-0 sticky bg-light-bg-primary/80 backdrop-blur z-50 flex flex-col items-center justify-center border-b-1 border-stone-300 py-2">
                    <span class="font-inter text-light-text font-semibold">Conflicted</span>
                </div>
                <div class="flex flex-col pt-2 w-full space-y-3">
                    <ProjectedCard v-for="p in filteredScores.filter((obj) => obj['Status'] === 'CONFLICTED')"
                        :headshot="p.Headshot"
                        :name="p.Name"
                        :position="p.Position"
                        :team="p.Team"
                        :projected="p.Projected"
                        :points="p.Points"
                        :bye="p.Bye"
                    />
                </div>
            </div>
            <div class="flex flex-col">
                <div class="top-0 sticky bg-light-bg-primary/80 backdrop-blur z-50 flex flex-col items-center justify-center border-b-1 border-stone-300 py-2">
                    <span class="font-inter text-light-text font-semibold">Root Against</span>
                </div>
                <div class="flex flex-col pt-2 w-full space-y-3">
                    <ProjectedCard v-for="p in filteredScores.filter((obj) => obj['Status'] === 'BOO')"
                        :headshot="p.Headshot"
                        :name="p.Name"
                        :position="p.Position"
                        :team="p.Team"
                        :projected="p.Projected"
                        :points="p.Points"
                        :bye="p.Bye"
                    />
                </div>
            </div>
        </div>
        <div v-show="loading" class="flex justify-center py-8" role="status">
            <svg aria-hidden="true" class="inline w-16 h-16 text-gray-200 animate-spin fill-sky-700" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
        </div>
    </main>
    <!-- <pre>{{ filteredScores }}</pre> -->
</template>
<script setup>
import { ref, computed } from 'vue'
import { rtdb } from '../firebase'
import { ref as fbRef, onValue } from 'firebase/database'
import { useStoreAuth } from '../stores/storeAuth'
import ProjectedCard from '../components/dashboard/ProjectedCard.vue'

const storeAuth = useStoreAuth()
const statsRef = fbRef(rtdb, 'stats/' + storeAuth.user.id)
const initial = ref([])
const currentWeek = ref(null)
const loading = ref(true)
onValue(statsRef, (snapshot) => {
    const db = []
    snapshot.forEach((childSnapshot) => {
        const data = childSnapshot.val()
        db.push(data)
    })
    initial.value = db
    currentWeek.value = initial.value.length
    loading.value = false
})  
const box_scores = computed(() => {
    return initial.value
})
// TODO: Error Handling for users who might not have finished inputting user credentials
//       and thus don't have dashboard displayed
const filteredScores = computed(() => {
    let scores = []
    if (!loading.value) {
        scores = Object.values(box_scores.value[currentWeek.value - 1])
        scores = scores.sort(function(a, b) {
            let projA = a['Projected']
            let projB = b['Projected']
            if (projA < projB) return 1
            if (projA > projB) return -1
            return 0
        })
        return scores
    }
    return scores
})

function handleCurrentWeek(n) {
    currentWeek.value = n
}
</script>

<style lang="scss" scoped>

</style>
