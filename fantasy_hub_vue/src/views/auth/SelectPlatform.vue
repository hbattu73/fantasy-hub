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
    <main class="flex flex-col flex-grow flex-shrink-0 items-center w-full pb-12">
        <h1 class="text-center text-2xl md:text-3xl tracking-tight leading-9 font-bold font-inter text-light-text px-8 mb-4">Now, select a platform.</h1>
        <!-- <section class="text-center pt-4 pb-12 px-8"> -->
        <section class="text-center w-full py-4 px-8">
            <!-- <h2 class="text-xl md:text-2xl lg:text-3xl leading-tight font-bold pb-8 md:pb-14">
                Select your platform
            </h2> -->
            <ul class="mt-4 flex flex-col md:flex-row items-center md:items-start justify-center space-y-10 md:space-y-0 md:space-x-20 lg:space-x-24">
                <div class="flex flex-col space-y-4">
                    <RouterLink :to="{ name:'espn_auth' }">
                        <div class="bg-espn rounded-2xl w-20 h-20 md:w-24 md:h-24 cursor-pointer shadow-md ring-2 ring-gray-200 hover:scale-105 hover:ring-sky-400/70 hover:ring-4 [transition:transform_0.25s,box-shadow_0.25s]">
                        </div>
                    </RouterLink>
                    <h3 class="font-inter text-light-text font-bold text-base md:text-lg lg:text-xl">ESPN</h3>
                </div>
                <div class="flex flex-col space-y-4">
                    <div class="bg-sleeper rounded-2xl w-20 h-20 md:w-24 md:h-24 shadow-md pointer-events-none"> 
                    </div>
                    <div class="flex flex-col items-center justify-center">
                        <h3 class="font-inter text-light-text font-bold text-base md:text-lg lg:text-xl">Sleeper</h3>
                        <LockIcon class="fill-current text-stone-600 w-5 h-5 mt-2"/>
                    </div>
                </div>
                <div class="flex flex-col space-y-4">
                    <div class="bg-yahoo rounded-2xl w-20 h-20 md:w-24 md:h-24 shadow-md pointer-events-none"> 
                    </div>
                    <div class="flex flex-col items-center justify-center">
                        <h3 class="font-inter text-light-text font-bold text-base md:text-lg lg:text-xl">Yahoo</h3>
                        <LockIcon class="fill-current text-stone-600 w-5 h-5 mt-2"/>
                    </div>
                </div>
            </ul>
            <a class="mt-12 md:mt-20 inline-flex justify-between items-center py-1 px-1 pr-4 mb-7 text-slate-600 bg-stone-100 rounded-full hover:bg-stone-200 cursor-pointer">
                <span class="text-xs md:text-sm bg-sky-500 rounded-full text-light-bg-primary px-4 py-1.5 mr-3">Coming Soon!</span> <span class="text-xs md:text-sm font-medium">Support for Sleeper and Yahoo Fantasy leagues.</span> 
                <svg class="ml-2 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
            </a>
        </section>
    </main>
</template>

<script setup>
import Logo from '../../components/svg/Logo.vue'
import LockIcon from '../../components/svg/LockIcon.vue'
import { useStoreAuth } from '../../stores/storeAuth'
import { useRoute } from 'vue-router'
// Pinia Store for User Authentication
const storeAuth = useStoreAuth()
function addPlatform(platform) {
    // if platforms list exists
    if (storeAuth.user.platform) {
        storeAuth.user.platform.push(platform)
    }
    // else create new list and add this platforms
    else {
        storeAuth.user.platform = [platform]

    }
}
</script>