<template>
    <BaseAuthForm>
        <template #h1>
            <h1 class="text-2xl md:text-4xl tracking-tight leading-9 font-bold font-inter text-light-text mb-4">Log in to fantasyhub</h1>
        </template>
        <template #auth-note-top>
            <div class="hidden md:flex md:justify-end">
                <div class="flex flex-col text-right pr-10 text-base leading-tight">
                    <span class="font-normal text-slate-600">New to fantasyhub?</span>
                    <RouterLink :to="{ name:'register' }">
                        <span class="font-bold text-sky-600 hover:underline cursor-pointer">Register here!</span>
                    </RouterLink>
                </div>
            </div>
        </template>
        <template #button>
            <button type="submit" class="mt-4 text-light-bg-primary bg-sky-400 w-full rounded-md px-5 py-2.5 inline-flex items-center justify-center hover:bg-sky-500 [transition:background-color_0.5s]">
                <span class="text-lg font-medium">Log in with Email</span>
            </button>
        </template>
        <template #auth-note-bottom>
            <div class="md:hidden mt-6 text-center text-lg leading-tight">
                <span class="font-normal text-gray-500">New to fantasyhub? </span>
                <RouterLink :to="{ name:'register' }">
                    <span class="font-bold text-sky-600 hover:underline cursor-pointer">Register here</span>
                </RouterLink>
            </div>
        </template>
    </BaseAuthForm>
</template>
<script setup>
import BaseAuthForm from './BaseAuthForm.vue'
</script>