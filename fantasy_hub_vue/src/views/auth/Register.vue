<template>
    <BaseAuthForm>
        <template #h1>
            <h1 class="text-center text-2xl md:text-3xl tracking-tight leading-9 font-bold font-inter text-light-text px-8 mb-4">First, provide a sign-in method.</h1>
        </template>
        <template #auth-note-top>
            <div class="hidden md:flex md:justify-end">
                <div class="flex flex-col text-right pr-10 text-base leading-tight">
                    <span class="font-normal text-slate-600">Already using fantasyhub?</span>
                    <RouterLink :to="{ name:'login' }">
                        <span class="font-bold text-sky-600 hover:underline cursor-pointer">Log in to an existing account!</span>
                    </RouterLink>
                </div>
            </div>
        </template>
        <template #h2>
            <h2 class="text-center font-inter font-medium text-base md:text-lg leading-7 text-stone-600 px-8">Register using your Google or Github account, or by an email address.</h2>
        </template>
        <template #button>
            <!-- <RouterLink :to="{ name:'platform_select' }"> -->
                <button type="submit" class="mt-4 group inline-flex justify-center items-center text-center text-light-bg-primary bg-sky-400 w-full rounded-md px-5 py-2.5 hover:bg-sky-500 [transition:background-color_0.5s]">
                    <span class="text-lg font-medium">Continue with Email</span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="group-hover:translate-x-2 [transition:transform_0.2s] ml-2 mt-[2px] w-5 h-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12.75 15l3-3m0 0l-3-3m3 3h-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                </button>
            <!-- </RouterLink> -->
        </template>
        <template #auth-note-bottom>
            <div class="md:hidden flex flex-col mt-6 text-center text-lg leading-tight">
                <span class="font-normal text-gray-500">Already using fantasyhub?</span>
                <RouterLink :to="{ name:'login' }">
                    <span class="font-bold text-sky-600 hover:underline cursor-pointer">Log in to an existing account!</span>
                </RouterLink>
            </div>
        </template>
    </BaseAuthForm>
</template>
<script setup>
import BaseAuthForm from './BaseAuthForm.vue'
</script>
