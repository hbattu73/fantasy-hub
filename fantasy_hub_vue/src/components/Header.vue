<template>
    <header class="sticky top-0 bg-light-bg-primary/80 backdrop-blur z-50">
        <!-- Primary Nav -->
        <nav class="flex items-center h-14 md:h-16 py-4 px-4 lg:px-16 border-b-1 border-light-border">       
            <div class="flex items-center container">
                <!-- Logo -->
                <div class="flex flex-1">
                    <RouterLink :to="{ name:'home' }">
                        <Logo class="w-40 md:w-44 cursor-pointer"/>
                    </RouterLink>
                </div>
                <!-- Hamburger Menu Icon -->
                <div class="justify-end md:hidden">
                    <button class="flex justify-center items-center w-10 h-16 cursor-pointer" @click="toggleMobileNav">
                        <span class="relative w-4 h-[14px] overflow-hidden cursor-pointer">
                            <span class="absolute rounded-full w-4 h-[2px] bg-light-text left-0 [transition:transform_0.25s,background-color_0.5s,top_0.25s]" 
                                :class="{'top-0':!navActive,
                                        'top-[6px]':navActive,
                                        'translate-x-0':navActive,
                                        'rotate-[225deg]':navActive,
                                        'opacity-70': navActive}">
                            </span>
                            <span class="absolute rounded-full w-4 h-[2px] bg-light-text top-[6px] left-0 [transition:transform_0.25s,background-color_0.5s,top_0.25s]" 
                                :class="{'translate-x-4': navActive}">
                            </span>
                            <span class="absolute rounded-full w-4 h-[2px] bg-light-text left-0 [transition:transform_0.25s,background-color_0.5s,top_0.25s]" 
                                :class="{'top-3':!navActive,
                                        'top-[6px]':navActive,
                                        'translate-x-0':navActive,
                                        'rotate-[135deg]':navActive,
                                        'opacity-70': navActive}">
                            </span>
                        </span>
                    </button>
                </div>
                <!-- Primary Nav Attributes -->
                <div class="hidden md:flex items-center">
                    <!-- About, Register, Log In -->
                    <div class="flex items-center space-x-6 font-inter text-sm font-medium text-light-text">
                        <a class="cursor-pointer hover:opacity-50 duration-200">About</a>
                        <!-- TODO create an account page and display user info + ability to delete account -->
                        <span v-if="storeAuth.user.id" class="cursor-pointer hover:opacity-50 duration-200">
                            Account
                        </span>
                        <span v-else>
                            <RouterLink :to="{ name:'register' }" class="cursor-pointer hover:opacity-50 duration-200">
                                Register
                            </RouterLink>
                        </span>
                        <span v-if="storeAuth.user.id">
                            <button @click="storeAuth.logOutUser" class="cursor-pointer hover:opacity-50 duration-200">
                                Log Out
                            </button>
                        </span>
                        <span v-else>
                            <RouterLink :to="{ name:'login' }" class="cursor-pointer hover:opacity-50 duration-200">
                                Log In
                            </RouterLink>
                        </span>
                        <!-- <a class="cursor-pointer hover:opacity-50 duration-200">Log In</a> -->
                    </div>
                    <!-- Appearance Div -->
                    <div class="flex items-center h-6 px-3 mx-6 border-x-1 border-light-border">
                        <!-- Appearance Button -->
                        <button class="btn-header">
                            <MoonIcon class="w-5 text-sky-900 hover:fill-current hover:text-sky-700"/>
                        </button>
                    </div>
                    <!-- Social Icons -->
                    <div class="flex items-center space-x-5">
                        <!-- Github Button -->
                        <button class="btn-header">
                            <GithubIcon class="w-[21px] fill-current text-light-text"/>
                        </button>
                        <!-- Discord Button -->
                        <!-- <button class="btn-header">
                            <DiscordIcon class="w-5 fill-current text-light-text"/>
                        </button> -->
                        <!-- LinkedIn Button -->
                        <!-- <button class="btn-header">
                            <LinkedInIcon class="w-5 fill-current text-light-text"/>
                        </button> -->
                    </div>
                </div>
            </div>
        </nav>
        <!-- Primary Nav for Mobile -->
        <MobileHeader :navActive="navActive"/>
        <!-- Secondary Nav After Authentication -->
        <SecondaryNav v-if="storeAuth.user.id && route.name !== 'home'"/>
        <!-- <SecondaryNav /> -->
    </header>
    <!-- <MobileHeader :navActive="navActive"/> -->
</template>

<script setup>
import Logo from './svg/Logo.vue'
import LogoComponent from './svg/LogoLight2.svg?component'
import Logo2 from './svg/LogoLight3.svg?component'
import SecondaryNav from './SecondaryNav.vue'
import MobileHeader from './MobileHeader.vue'
import Hero from '../views/Hero.vue'
// Icons
import MoonIcon from './svg/MoonIcon.vue'
import GithubIcon from './svg/GithubIcon.vue'
import LinkedInIcon from './svg/LinkedInIcon.vue'
import DiscordIcon from './svg/DiscordIcon.vue'

import { useResponsive } from '../composables/window.js'
import { ref, watch } from 'vue'
import { useStoreAuth } from '../stores/storeAuth'
import { useRoute } from 'vue-router'
const route = useRoute()
// Pinia Store for User Authentication
const storeAuth = useStoreAuth()

const { width } = useResponsive()
const navActive = ref(null)

function toggleMobileNav() {
    navActive.value = !navActive.value
}

watch(
    () => width.value, 
    (screen) => {
        if (screen >= 768) {
            navActive.value = false
        }
    }
)
</script>

<style lang="scss" scoped>

</style>
