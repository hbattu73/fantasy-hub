<template>
    <header class="grid grid-cols-3 py-12 pl-0 w-full container">
        <div class="">
            <button @click="storeAuth.logOutUser" class="py-3 px-2 bg-orange-600">Log Out {{ storeAuth.user.email }}</button>
        </div>
        <div class="flex flex-col items-center justify-center">
            <RouterLink :to="{ name:'home' }">
                <Logo class="w-40 md:w-48 cursor-pointer"/>
            </RouterLink>        
        </div>
        <slot name="auth-note-top"></slot>
    </header>
    <main class="flex flex-col flex-grow flex-shrink-0 items-center w-full pb-12">
        <slot name="h1"></slot>
        <slot name="h2"></slot>
        <div class="w-full max-w-md py-4 px-8">
            <form @submit.prevent="handleSubmit" class="mt-4" method="POST" novalidate>
                <button type="button" class="text-blue-500 bg-light-bg-primary border-2 border-blue-400 w-full rounded-md px-5 py-2.5 inline-flex items-center justify-center hover:ring-2 hover:ring-sky-600/40 focus:ring-4 focus:ring-sky-600/40 transition-all">
                    <GoogleIcon class="mr-3 -ml-1 w-5 h-5"/>
                    <span class="text-lg font-medium">Sign in with Google</span>
                </button>
                <button type="button" class="mt-4 text-zinc-600 bg-light-bg-primary border-2 border-zinc-500 w-full rounded-md px-5 py-2.5 inline-flex items-center justify-center hover:ring-2 hover:ring-stone-300 focus:ring-4 focus:ring-stone-300 transition-all">
                    <GithubIcon class="mr-3 -ml-1 w-5 h-5 fill-current text-zinc-600"/>
                    <span class="text-lg font-medium">Sign in with GitHub</span>
                </button>
                <div class="my-6 flex items-center">
                    <hr class="flex-grow m-0 border-t-1 border-stone-500">
                    <span class="px-5 text-gray-600 font-inter font-normal">OR</span>
                    <hr class="flex-grow m-0 border-t-1 border-stone-500">
                </div>
                <!-- Firebase Auth Errors -->
                <div v-show="emailAuthError" class="items-start text-center w-full justify-center inline-flex pb-6 px-3">
                    <ShieldIcon class="mr-2 w-5 h-5 text-rose-500"/>
                    <span class="font-inter font-medium text-sm text-rose-500">{{ emailAuthError }}</span>
                </div>
                <!-- Email -->
                <div class="relative font-inter">
                    <input v-model="emailCredentials.email" 
                           id="email" 
                           name="email" 
                           type="email" 
                           required 
                           class="px-2.5 pb-2.5 pt-4 w-full text-base text-gray-800 bg-transparent rounded-md border-1 border-zinc-400 appearance-none shadow-sm focus:outline-none focus:ring-1 focus:ring-sky-300 focus:shadow-md peer" 
                           :class="{'rounded-bl-none':!validEmail, 'rounded-br-none':!validEmail}"
                           placeholder=" "/>
                    <label for="email" class="absolute text-base text-gray-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-light-bg-primary px-2 peer-focus:px-2 peer-focus:text-slate-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 left-1">Email Address</label>
                </div>
                <!-- Error messages for invalid emails -->
                <div v-show="!validEmail" class="items-center inline-flex w-full bg-rose-100 border-1 border-rose-400 border-t-0 rounded rounded-tl-none rounded-tr-none py-3 px-3">
                    <ExclamationIcon class="w-4 h-4 text-slate-600 mr-2"/>
                    <span class="font-inter text-xs text-slate-600">{{ emailErrMessage }}</span>
                </div>
                <!-- Password -->
                <div class="mt-4 relative font-inter">
                    <!-- Show Password Button -->
                    <button type="button" class="absolute inset-y-0 right-2 flex items-center focus:outline-none" @click="togglePasswordVisibility">
                        <EyeIcon v-show="!showPassword" class="w-5 h-5 text-slate-500"/>
                        <EyeSlashIcon v-show="showPassword" class="w-5 h-5 text-slate-500"/>
                    </button>
                    <input v-model="emailCredentials.password" 
                           id="password" 
                           name="password" 
                           :type="passwordField" 
                           required 
                           class="px-2.5 pb-2.5 pt-4 w-full text-base text-gray-800 bg-transparent rounded-md border-1 border-zinc-400 appearance-none shadow-sm focus:outline-none focus:ring-1 focus:ring-sky-300 focus:shadow-md peer"
                           :class="{'rounded-bl-none':!validPassword, 'rounded-br-none':!validPassword}"
                           placeholder=" "/>
                    <label for="password" class="absolute text-base text-gray-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-light-bg-primary px-2 peer-focus:px-2 peer-focus:text-slate-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 left-1">Password</label>
                </div>
                <!-- Error messages for invalid passwords -->
                <div v-show="!validPassword" class="items-center inline-flex w-full bg-rose-100 border-1 border-rose-400 border-t-0 rounded rounded-tl-none rounded-tr-none py-3 px-3">
                    <ExclamationIcon class="w-4 h-4 text-slate-600 mr-2"/>
                    <span class="font-inter text-xs text-slate-600">{{ passwordErrMessage }}</span>
                </div>
                <slot name="button"></slot>
            </form>
            <slot name="auth-note-bottom"></slot>
        </div>
    </main>
</template>

<script setup>
// SVG
import Logo from '../../components/svg/Logo.vue'
import GithubIcon from '../../components/svg/GithubIcon.vue'
import GoogleIcon from '../../components/svg/GoogleIcon.vue'
import ExclamationIcon from '../../components/svg/ExclamationIcon.vue'
import EyeIcon from '../../components/svg/EyeIcon.vue'
import EyeSlashIcon from '../../components/svg/EyeSlashIcon.vue'
import ShieldIcon from '../../components/svg/ShieldIcon.vue'
// Vue/Firebase
import { ref, reactive, watch, computed } from 'vue'
import { useStoreAuth } from '../../stores/storeAuth'
import { useRoute } from 'vue-router'
// Pinia Store for User Authentication
const storeAuth = useStoreAuth()

// regex check for email validity
let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
// password visibility state variables
const showPassword = ref(null)
const passwordField = ref('password')
// toggle password visibility
function togglePasswordVisibility() {
    showPassword.value = !showPassword.value
    passwordField.value = passwordField.value === 'password' ? 'text' : 'password'
}

// email/pass credentials
const emailCredentials = reactive({
    email: '',
    password: ''
})
// email and pass error-handling state variables
const emailAuthError = ref('')
const validEmail = ref(true)
const validPassword = ref(true)
const showErrorMessages = ref(false)

const route = useRoute()
// validate email/pass before submitting and show firebase-auth error if needed
const handleSubmit = async() => {
    validEmail.value = re.test(emailCredentials.email)
    validPassword.value = emailCredentials.password.length > 5
    emailAuthError.value = ''
    if (validEmail.value && validPassword.value) {
        if (route.name === 'register') {
            emailAuthError.value = await storeAuth.registerUser(emailCredentials)
        }
        else {
            emailAuthError.value = await storeAuth.loginUser(emailCredentials)
        }
    }
    showErrorMessages.value = true && !emailAuthError.value
}
// watch for valid email try after first click fail of submit button
watch(() => emailCredentials.email, (email) => {
        if (showErrorMessages.value) {
            validEmail.value = re.test(email)
        }
    })
// watch for valid password try after first click fail of submit button
watch(() => emailCredentials.password, (password) => {
        if (showErrorMessages.value) {
            validPassword.value = password.length > 5
        }
    })
// change email error message depending on value of current email input
// after first click fail
const emailErrMessage = computed(() => {
    if (!emailCredentials.email) {
        return "Please fill out your email." 
    }
    else if (!validEmail.value) {
        return "That doesn't seem to be a valid email - check again." 
    }
})
// change password error message depending on value of current password input
// after first click fail
const passwordErrMessage = computed(() => {
    if (!emailCredentials.password) {
        return 'Please fill out your password.'
    }
    else if (!validPassword.value) {
        return 'Password must be atleast 6 characters.'
    }
})
</script>