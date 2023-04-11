<template>
    <!-- <div v-show="navActive" class="md:hidden relative"> -->
        <!-- took out z-60 in below div -->
        <!-- <div class="absolute w-full h-screen px-8 right-0 left-0 top-0 overflow-y-auto bg-light-bg-primary border-b-1 border-light-border shadow-lg"> 
            <div class="flex flex-col mx-auto max-w-[288px] pt-8 pb-24">
                <div class="flex flex-col font-inter text-lg font-medium text-light-text">
                    <a class="py-3 border-b-1 border-light-border">About</a>
                    <a class="py-3 border-b-1 border-light-border">Register</a>
                    <a class="py-3 border-b-1 border-light-border">Log In</a>
                </div>
                <div class="flex items-center justify-between rounded-lg my-4 py-3 px-4 bg-zinc-200">
                    <p class="font-inter text-base font-normal text-slate-600">Appearance</p>
                    <button class="btn-header">
                        <MoonIcon class="w-5 fill-current text-blue-400"/>
                    </button>
                </div>
                <div class="flex justify-center space-x-6 mt-3">
                    <button class="btn-header">
                        <GithubIcon class="w-6 fill-current text-light-text"/>
                    </button>
                    <button class="btn-header">
                        <LinkedInIcon class="w-6 fill-current text-light-text"/>
                    </button>
                    <button class="btn-header">
                        <DiscordIcon class="w-6 fill-current text-light-text"/>
                    </button>
                </div>
            </div>
        </div>
    </div> -->
    
    <!-- <Teleport to="body">
        <div v-show="navActive" class="absolute w-full h-screen px-8 right-0 left-0 top-14 bottom-0 bg-light-bg-primary border-b-1 border-light-border shadow-lg">
            <div class="flex flex-col mx-auto max-w-[288px] pt-8 pb-24">
                <div class="flex flex-col font-inter text-lg font-medium text-light-text">
                    <a class="py-3 border-b-1 border-light-border">About</a>
                    <a class="py-3 border-b-1 border-light-border">Register</a>
                    <a class="py-3 border-b-1 border-light-border">Log In</a>
                </div>
                <div class="flex items-center justify-between rounded-lg my-4 py-3 px-4 bg-zinc-200">
                    <p class="font-inter text-base font-normal text-slate-600">Appearance</p>
                    <button class="btn-header">
                        <MoonIcon class="w-5 fill-current text-blue-400"/>
                    </button>
                </div>
                <div class="flex justify-center space-x-6 mt-3">
                    <button class="btn-header">
                        <GithubIcon class="w-6 fill-current text-light-text"/>
                    </button>
                    <button class="btn-header">
                        <LinkedInIcon class="w-6 fill-current text-light-text"/>
                    </button>
                    <button class="btn-header">
                        <DiscordIcon class="w-6 fill-current text-light-text"/>
                    </button>
                </div>
            </div>
        </div>
    </Teleport> -->

    <Teleport to="body">
        <div v-show="navActive" class="z-50 fixed right-0 left-0 top-14">
            <div class="absolute overflow-y-auto w-full h-screen px-8 bg-light-bg-primary border-b-1 border-light-border shadow-lg">
                <div class="flex flex-col mx-auto max-w-[288px] pt-8 pb-24">
                    <div class="flex flex-col font-inter text-lg font-medium text-light-text">
                        <a class="py-3 border-b-1 border-light-border">About</a>
                        <a class="py-3 border-b-1 border-light-border">Register</a>
                        <a class="py-3 border-b-1 border-light-border">Log In</a>
                    </div>
                    <div class="flex items-center justify-between rounded-lg my-4 py-3 px-4 bg-zinc-200">
                        <p class="font-inter text-base font-normal text-slate-600">Appearance</p>
                        <button class="btn-header">
                            <MoonIcon class="w-5 fill-current text-blue-400"/>
                        </button>
                    </div>
                    <div class="flex justify-center space-x-6 mt-3">
                        <button class="btn-header">
                            <GithubIcon class="w-6 fill-current text-light-text"/>
                        </button>
                        <button class="btn-header">
                            <LinkedInIcon class="w-6 fill-current text-light-text"/>
                        </button>
                        <button class="btn-header">
                            <DiscordIcon class="w-6 fill-current text-light-text"/>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </Teleport>
</template>

<script setup>
// Icons
import MoonIcon from './svg/MoonIcon.vue'
import GithubIcon from './svg/GithubIcon.vue'
import LinkedInIcon from './svg/LinkedInIcon.vue'
import DiscordIcon from './svg/DiscordIcon.vue'

const props = defineProps({
    navActive: {
        type: Boolean,
        default: false
    }
})
</script>