<template>
    <!-- took out z-10 -->
    <nav class="flex items-center px-4 lg:px-16 border-b-1 border-light-border">
        <div class="flex items-center container space-x-8 md:space-x-14 font-inter text-sm font-medium text-light-text">
            <RouterLink :to="{ name:'dashboard' }">
                <div class="py-2 flex group items-center cursor-pointer"
                    :class="{'border-b-2 border-sky-600': route.name === 'dashboard'}">
                    <span class="mr-2 md:mr-4 rounded-md p-1 ring-1 ring-slate-900/5 shadow-sm
                                group-hover:shadow
                                group-hover:ring-slate-900/10
                                group-hover:shadow-blue-200">
                        <LineupIcon class="w-[18px] h-[18px] fill-current text-blue-400 group-hover:text-blue-500"/>
                    </span>
                    <!-- the negative z needs to be there so text isnt above mobile header -->
                    <span class="flex -z-10 relative space-x-1 transition-all
                                before:content-['']
                                before:absolute
                                before:-bottom-[1px]
                                before:left-1/2
                                before:-translate-x-1/2
                                before:w-0 
                                before:h-[1.5px]
                                before:rounded-full
                                before:opacity-80
                                before:transition-all
                                before:duration-275
                                before:bg-gradient-to-r
                                before:from-light-text
                                before:to-light-text
                                group-hover:before:w-full
                                group-hover:before:opacity-80"
                            :class="{'before:h-[1px]': route.name !== 'dashboard'}">
                        <span class="flex">Lineup</span>
                        <span class="hidden md:flex">Dashboard</span>
                    </span>
                </div>
            </RouterLink>
            <RouterLink :to="{ name:'trade_analyzer' }">
                <div class="py-2 flex group items-center cursor-pointer"
                    :class="{'border-b-2 border-sky-600': route.name === 'trade_analyzer'}">
                    <span class="mr-2 md:mr-4 rounded-md p-1 ring-1 ring-slate-900/5 shadow-sm
                                group-hover:shadow
                                group-hover:ring-slate-900/10
                                group-hover:shadow-violet-200">
                        <TradeIcon class="w-[18px] h-[18px] fill-current text-violet-400 group-hover:text-violet-500"/>
                    </span>
                    <span class="flex -z-10 relative space-x-1 transition-all
                                before:content-['']
                                before:absolute
                                before:-bottom-[1px]
                                before:left-1/2
                                before:-translate-x-1/2
                                before:w-0 
                                before:h-[1.5px]
                                before:rounded-full
                                before:opacity-80
                                before:transition-all
                                before:duration-275
                                before:bg-gradient-to-r
                                before:from-light-text
                                before:to-light-text
                                group-hover:before:w-full
                                group-hover:before:opacity-80"
                            :class="{'before:h-[1px]': route.name !== 'trade_analyzer'}">
                        <span class="flex">Trade</span>
                        <span class="hidden md:flex">Analyzer</span>
                    </span>
                </div>
            </RouterLink>
            <RouterLink :to="{ name:'power_rankings' }">
                <div class="py-2 flex group items-center cursor-pointer"
                    :class="{'border-b-2 border-sky-600': route.name === 'power_rankings'}">
                    <span class="mr-2 md:mr-4 rounded-md p-1 ring-1 ring-slate-900/5 shadow-sm
                                group-hover:shadow
                                group-hover:ring-slate-900/10
                                group-hover:shadow-fuchsia-200">
                        <RankingIcon class="w-[18px] h-[18px] fill-current text-pink-400 group-hover:text-pink-500"/>
                    </span>
                    <span class="flex -z-10 relative space-x-1 transition-all
                                before:content-['']
                                before:absolute
                                before:-bottom-[1px]
                                before:left-1/2
                                before:-translate-x-1/2
                                before:w-0
                                before:h-[1.5px]
                                before:rounded-full
                                before:opacity-80
                                before:transition-all
                                before:duration-275
                                before:bg-gradient-to-r
                                before:from-light-text
                                before:to-light-text
                                group-hover:before:w-full
                                group-hover:before:opacity-80"
                            :class="{'before:h-[1px]': route.name !== 'power_rankings'}">
                        <span class="flex">Power</span>
                        <span class="hidden md:flex">Rankings</span>
                    </span>
                </div>
            </RouterLink>
        </div>
    </nav>
</template>

<script setup>
import LineupIcon from './svg/LineupIcon.vue'
import RankingIcon from './svg/RankingIcon.vue'
import TradeIcon from './svg/TradeIcon.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
</script>