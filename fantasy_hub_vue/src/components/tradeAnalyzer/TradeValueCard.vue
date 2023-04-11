<template>
    <div class="relative max-w-[156px] overflow-hidden rounded-lg shadow-md border-1 border-slate-300 hover:ring-2 hover:ring-slate-400 hover:shadow-lg cursor-pointer">
        <img class="hidden md:block w-full bg-stone-100" 
             :src="headshot" 
             :alt="name"/>
        <div class="bg-zinc-100 p-3 flex flex-col justify-end font-inter border-t-4 space-y-3"
            :class="{'border-blue-400 ': position === 'QB',
                        'border-lime-600 ': position === 'RB',
                        'border-indigo-400 ': position === 'WR',
                        'border-orange-400 ': position === 'TE'}">
            <div class="flex">
                <div class="flex flex-col text-zinc-700">
                    <span class="text-sm font-medium truncate">{{ splitName(name)[0] }}</span>
                    <span class="text-sm font-bold truncate">{{ splitName(name)[1] }}</span>
                </div>
                <div class="absolute right-3">
                    <span class="text-slate-600 font-semibold text-base">{{ value }}</span>
                </div>
            </div>
            <div class="flex">
                <span class="text-sm text-zinc-600 font-medium">
                    <span class="font-semibold"
                        :class="{'text-blue-500': position === 'QB',
                                    'text-lime-600': position === 'RB',
                                    'text-indigo-500': position === 'WR',
                                    'text-orange-500': position === 'TE'}">{{ position }}</span> | {{ team }}
                </span>
                <div class="inline-flex flex-1 justify-end items-center">
                    <TrendingUpIcon v-if="change.charAt(0) === '+'" class="text-green-600 w-5 h-5"/>
                    <TrendingDownIcon v-else-if="change.charAt(0) === '-'" class="text-red-600 w-5 h-5"/>
                    <NoChangeIcon v-else class="text-yellow-600 w-5 h-5"/>
                    <span class="text-xs leading-none ml-1"
                        :class="{'text-green-600': change.charAt(0) === '+',
                                    'text-red-600': change.charAt(0) === '-',
                                    'text-yellow-600': change.charAt(0) === '0'}">{{ parseSign(change) }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
// Icons
import TrendingUpIcon from '../svg/TrendingUpIcon.vue'
import TrendingDownIcon from '../svg/TrendingDownIcon.vue'
import NoChangeIcon from '../svg/NoChangeIcon.vue'
// Accept prop
const props = defineProps(['headshot', 'name', 'position', 'value', 'team', 'change'])
// Helper Functions
function parseSign(change) {
    if (isNaN(change.charAt(0))) {
        return change.slice(1)
    }
    return change
}
function splitName(name) {
    return [name.substring(0, name.indexOf(' ')), name.substring(name.indexOf(' ') + 1)]
}
</script>
