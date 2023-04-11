<template>
    <div class="flex mx-auto w-72 h-14 border-1 rounded bg-zinc-50 shadow-md border-slate-200 hover:shadow-lg">
        <div class="basis-12 flex-grow-0 flex-shrink-0 flex flex-col h-full justify-center px-2">
            <div class="items-center rounded-full flex justify-center overflow-hidden w-12 h-12 shadow-md bg-stone-100 border-1 border-slate-200">
                <img class="object-contain"
                     :class="{'min-w-[66px] min-h-[48px] scale-105': position !== 'D/ST' && position !== 'HC'}"
                     :src="headshot"
                     :alt="name"/>
            </div>
        </div>
        <div class="border-l-4 px-2 flex flex-col font-inter w-full justify-center space-y-1"
            :class="{'border-blue-400': position === 'QB',
                     'border-lime-600': position === 'RB',
                     'border-indigo-400': position === 'WR',
                     'border-orange-400': position === 'TE',
                     'border-stone-500': position === 'D/ST',
                     'border-rose-400': position === 'K',
                     'border-cyan-500': position === 'HC'}">
            <div class="w-full flex items-center justify-between">
                <span class="text-sm font-medium text-zinc-700">{{ splitName(name)[0] }} <span class="text-sm font-bold">{{ splitName(name)[1] }}</span></span>
                <svg v-if="calcIcon(projected, points) === 'STUD'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4 text-teal-600">
                    <path fill-rule="evenodd" d="M9.315 7.584C12.195 3.883 16.695 1.5 21.75 1.5a.75.75 0 01.75.75c0 5.056-2.383 9.555-6.084 12.436A6.75 6.75 0 019.75 22.5a.75.75 0 01-.75-.75v-4.131A15.838 15.838 0 016.382 15H2.25a.75.75 0 01-.75-.75 6.75 6.75 0 017.815-6.666zM15 6.75a2.25 2.25 0 100 4.5 2.25 2.25 0 000-4.5z" clip-rule="evenodd" />
                    <path d="M5.26 17.242a.75.75 0 10-.897-1.203 5.243 5.243 0 00-2.05 5.022.75.75 0 00.625.627 5.243 5.243 0 005.022-2.051.75.75 0 10-1.202-.897 3.744 3.744 0 01-3.008 1.51c0-1.23.592-2.323 1.51-3.008z" />
                </svg>
                <svg v-else-if="calcIcon(projected, points) === 'BOOM/BUST'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4 text-sky-600">
                    <path fill-rule="evenodd" d="M14.615 1.595a.75.75 0 01.359.852L12.982 9.75h7.268a.75.75 0 01.548 1.262l-10.5 11.25a.75.75 0 01-1.272-.71l1.992-7.302H3.75a.75.75 0 01-.548-1.262l10.5-11.25a.75.75 0 01.913-.143z" clip-rule="evenodd" />
                </svg>
                <svg v-else-if="calcIcon(projected, points) === 'SLUMPING'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4 text-rose-600">
                    <path fill-rule="evenodd" d="M1.72 5.47a.75.75 0 011.06 0L9 11.69l3.756-3.756a.75.75 0 01.985-.066 12.698 12.698 0 014.575 6.832l.308 1.149 2.277-3.943a.75.75 0 111.299.75l-3.182 5.51a.75.75 0 01-1.025.275l-5.511-3.181a.75.75 0 01.75-1.3l3.943 2.277-.308-1.149a11.194 11.194 0 00-3.528-5.617l-3.809 3.81a.75.75 0 01-1.06 0L1.72 6.53a.75.75 0 010-1.061z" clip-rule="evenodd" />
                </svg>
            </div>
            <div class="w-full flex items-center justify-between">
                <div class="flex text-sm text-zinc-600 font-medium">
                    <span>
                        <span class="font-semibold"
                            :class="{'text-blue-500': position === 'QB',
                                    'text-lime-600': position === 'RB',
                                    'text-indigo-500': position === 'WR',
                                    'text-orange-500': position === 'TE',
                                    'text-stone-500': position === 'D/ST',
                                    'text-rose-500': position === 'K',
                                    'text-cyan-600': position === 'HC'}">{{ position }}</span> | {{ team }}
                    </span>
                </div>
                <div v-if="!bye" class="flex text-xs text-zinc-600 font-medium">
                    <span>Projected: {{ projected.toFixed(1) }}</span>
                </div>
                <div v-else class="flex text-xs text-red-600 font-medium">
                    <span>BYE</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
// Accept prop
const props = defineProps(['headshot', 'name', 'position', 'team', 'projected', 'points', 'bye'])
// Helper Functions
function splitName(name) {
    return [name.substring(0, name.indexOf(' ')), name.substring(name.indexOf(' ') + 1)]
}
function calcIcon(projected, points) {
    let percDiff = 100*(Math.abs(projected - points)/((projected + points)/2))
    if (projected >= 8 && projected <= 15) {
        if (percDiff >= 50) {
            return 'BOOM/BUST'
        }
    }
    if (projected >= 15) {
        if (points > projected && percDiff >= 40) {
            return 'STUD'
        }
        if (points < projected && percDiff >= 50) {
            return 'SLUMPING'
        }
    }
    return 'NONE'
}
</script>