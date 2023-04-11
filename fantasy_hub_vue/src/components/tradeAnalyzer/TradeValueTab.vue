<template>
    <div class="relative min-w-[156px] max-h-[100px] overflow-hidden rounded-lg shadow-md hover:shadow-lg hover:ring-1 hover:ring-gray-200 cursor-pointer">
        <div class="bg-stone-50 p-3 flex flex-col justify-end font-inter border-t-4 space-y-3"
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
                    <!-- TODO: stop event propagation -->
                    <TrashIcon @click.stop="$emit('delete')" class="w-4 h-4 text-gray-700 hover:scale-110"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
// Icons

import TrashIcon from '../svg/TrashIcon.vue';

// Accept prop
const props = defineProps(['name', 'position', 'value', 'team'])
// Helper Functions
function splitName(name) {
    return [name.substring(0, name.indexOf(' ')), name.substring(name.indexOf(' ') + 1)]
}
</script>