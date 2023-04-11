<template>
    <SwitchGroup>
        <div class="flex items-center">
            <SwitchLabel class="mr-2 font-inter font-medium text-sm md:text-base"
                         :class="{'text-blue-500': position === 'QB',
                                  'text-lime-700': position === 'RB',
                                  'text-indigo-500': position === 'WR',
                                  'text-orange-400': position === 'TE'}">
                {{ position }}
            </SwitchLabel>
            <Switch
                v-model="filters[position]"
                class="relative inline-flex h-5 w-9 items-center rounded-full ui-not-checked:bg-gray-200"
                :class="{'ui-checked:bg-blue-400': position === 'QB',
                         'ui-checked:bg-lime-600': position === 'RB',
                         'ui-checked:bg-indigo-400': position === 'WR',
                         'ui-checked:bg-orange-400': position === 'TE'}">
                <span class="inline-block h-3 w-3 transform rounded-full bg-white transition ui-checked:translate-x-5 ui-not-checked:translate-x-1 ui-not-checked:ring-2 ring-gray-400/50"></span>
            </Switch>
        </div>
    </SwitchGroup>
</template>

<script setup>
import { Switch, SwitchGroup, SwitchLabel } from '@headlessui/vue'
import { ref, onMounted } from 'vue'
const props = defineProps(['filters', 'position'])
</script>
