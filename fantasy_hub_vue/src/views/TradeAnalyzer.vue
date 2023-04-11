<template>
    <main class="flex flex-col flex-grow flex-shrink-0 items-center px-4 lg:px-16 pt-4">
        <div class="py-2 flex flex-col md:flex-row items-center md:items-start container">
            <div class="flex text-center md:text-start justify-center md:justify-start w-full">
                <div class="">
                    <h2 class="font-inter font-bold text-lg md:text-2xl text-light-text">Trade-Value Analyzer</h2>
                    <h4 class="font-inter font-medium text-sm md:text-base text-slate-500">Player data provided thanks to <span class="font-bold text-sky-700">FantasyPros</span>.</h4>
                </div>
            </div>
            <div class="mt-1 flex text-center justify-center md:justify-end w-full">
                <div class="flex flex-wrap justify-center">
                    <div class="flex flex-nowrap items-center space-x-4">
                        <PositionSwitch :filters="filters" :position="'QB'"></PositionSwitch>
                        <PositionSwitch :filters="filters" :position="'RB'"></PositionSwitch>
                        <PositionSwitch :filters="filters" :position="'WR'"></PositionSwitch>
                        <PositionSwitch :filters="filters" :position="'TE'"></PositionSwitch>
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="flex flex-col overflow-hidden border-b-slate-300">
                <div class="flex pb-4 border-b-slate-300 justify-center">
                    <span class="font-inter font-semibold text-zinc-600">Showing ({{ filteredPlayers.length }}) available players.</span>
                </div>
                <div 
                @click.stop
                class="py-6 grid grid-cols-fill-40 justify-center gap-4 overflow-auto max-h-[472px] shadow-inner border-b-2 border-zinc-400 bg-slate-300/50 scrollbar-thin scrollbar-thumb-slate-400 scrollbar-track-gray-300">
                    <TransitionGroup name="list">
                        <TradeValueCard
                        v-for="p in filteredPlayers" 
                                    :key="p.id"
                                    :headshot="p.Headshot"
                                    :name="p.Name"
                                    :position="p.Position"
                                    :value="p.Value"
                                    :team="p.Team"
                                    :change="p.Change"
                                    @click.stop="addCardtoSendBox(p)"
                        />
                    </TransitionGroup>
                </div>

            </div>
        </div>
    </main>
    <div class="px-4 lg:px-16 py-8">
        <!-- grid-rows-3? or just switch to flex? -->
        <div class="border-1 border-slate-400 shadow-md rounded-sm bg-stone-50">
            <div class="container grid md-lg:grid md-lg:grid-cols-3 py-6">
                <!-- trade away -->
                <div class="px-6 flex flex-col items-center justify-center">
                    <div
                    ref="sendBox"
                    @click="focusSendBox"
                    class="w-full relative group flex flex-col justify-center items-center cursor-pointer">
                        <div class="inline-flex items-center mb-3">
                            <ResetIcon
                                @click.stop="toSend = []"
                                v-if="toSend.length !== 0"
                                class="w-6 h-6 md-lg:w-7 md-lg:h-7 text-slate-400 absolute left-0 md-lg:left-0 hover:text-light-text/80"/>
                            <span class="font-inter font-semibold text-lg text-light-text pr-4">Send</span>
                            <RightArrow class="group-hover:translate-x-1 [transition:transform_0.2s] w-8 fill-current text-sky-600/70"/>
                        </div>
                        <div
                            class="relative px-4 py-6 w-full h-80 md-lg:h-[460px] md-lg:w-[248px] flex flex-row gap-3 flex-wrap content-start justify-center overflow-auto overflow-x-hidden shadow-inner shadow-gray-500/50 rounded-sm border-2 border-dashed border-gray-400 group-hover:border-gray-600 group-hover:bg-stone-50 bg-light-bg-primary cursor-pointer transition duration-500 ease-out"
                            :class="{'ring-4': sendBoxActive,
                                    'ring-sky-600/50': sendBoxActive,
                                    'bg-stone-50': sendBoxActive,
                                    'border-gray-600': sendBoxActive}">
                                <Transition>
                                    <span
                                        v-if="!sendBoxActive && toSend.length === 0"
                                        class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 font-inter font-medium text-light-text/60 group-hover:text-light-text text-sm text-center transition duration-150 ease-out">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-auto mb-2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.042 21.672L13.684 16.6m0 0l-2.51 2.225.569-9.47 5.227 7.917-3.286-.672zm-7.518-.267A8.25 8.25 0 1120.25 10.5M8.288 14.212A5.25 5.25 0 1117.25 10.5" />
                                        </svg>
                                        <span>Click here to add players.</span>
                                    </span>
                                    <span
                                        v-else-if="sendBoxActive && toSend.length === 0"
                                        class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 font-inter font-medium text-light-text text-sm text-center transition duration-150 ease-out">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-auto mb-2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 012.25-2.25h7.5A2.25 2.25 0 0118 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 004.5 9v.878m13.5-3A2.25 2.25 0 0119.5 9v.878m0 0a2.246 2.246 0 00-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0121 12v6a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 18v-6c0-.98.626-1.813 1.5-2.122" />
                                        </svg>
                                        Select a player card.
                                    </span>
                                </Transition>
                                <TransitionGroup name="list">
                                    <TradeValueTab
                                    v-for="p in toSend"
                                        :key="p.id"
                                        :name="p.Name"
                                        :position="p.Position"
                                        :value="p.Value"
                                        :team="p.Team"
                                        @delete="removeFromsendBox(p.id)"
                                    />
                                </TransitionGroup>
                        </div>
                    </div>
                </div>
                <!-- trade analysis -->
                <div class="relative flex flex-col py-12 px-6 md-lg:px-0">
                    <div class="rounded-t-sm border-b-0 border-1 border-slate-400 py-4 bg-[#F4F4F2] shadow-sm">
                        <div class="flex items-center justify-center mb-4">
                            <span class="font-inter font-semibold text-light-text underline underline-offset-8">Projected Trade Value</span>
                        </div>
                        <div class="flex flex-col min-w-full">
                            <div class="flex items-center text-center">
                                <div class="w-1/2 relative">
                                    <AnimatedNumber
                                    class="font-lato font-semibold text-zinc-600 text-3xl"
                                    :number="acquireSum"/>
                                    <span class="after:content-[''] h-[1.5px] w-3/5 absolute bg-gray-400 left-1/2 -translate-x-1/2 bottom-5 rounded-full"/>
                                    <div class="flex justify-center mt-4">
                                        <LeftArrow class="w-6 fill-current text-rose-400"/>
                                    </div>
                                </div>
                                <div class="w-1/2 relative">
                                    <AnimatedNumber
                                    class="font-lato font-semibold text-zinc-600 text-3xl"
                                    :number="sendSum"/>
                                    <span class="after:content-[''] h-[1.5px] w-3/5 absolute bg-gray-400 left-1/2 -translate-x-1/2 bottom-5 rounded-full"/>
                                    <div class="flex justify-center mt-4">
                                        <RightArrow class="w-6 fill-current text-sky-600/70"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <GaugeChart
                        class="flex justify-center border-x-1 border-slate-400 bg-[#F4F4F2]"
                        :options="chartOptions"
                        :chartSize="275"
                        :sendSum="sendSum"
                        :acquireSum="acquireSum"
                        :toSendSize="toSend.length"
                        :toAcquireSize="toAcquire.length"
                        @arc-color="setArcColor"
                        @loading="toggleSpinner"
                    />
                
                    <div class="md-lg:absolute md-lg:right-0 md-lg:bottom-2 min-w-full">
                        <div class="rounded-b-sm border-t-0 border-1 border-gray-400 py-4 bg-[#F4F4F2] h-40 shadow-sm">
                            <div class="flex flex-col">
                                <div class="flex items-center justify-center mb-3">
                                    <span class="font-inter font-semibold text-light-text underline underline-offset-8">Trade Analysis</span>
                                </div>
                                <!-- Trade main text -->
                                <div class="inline-flex items-center justify-center pb-2">
                                    <!-- red -->
                                    <div v-if="arcColor === 'red' && !loading" class="inline-flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-red-500 mr-2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M10.05 4.575a1.575 1.575 0 10-3.15 0v3m3.15-3v-1.5a1.575 1.575 0 013.15 0v1.5m-3.15 0l.075 5.925m3.075.75V4.575m0 0a1.575 1.575 0 013.15 0V15M6.9 7.575a1.575 1.575 0 10-3.15 0v8.175a6.75 6.75 0 006.75 6.75h2.018a5.25 5.25 0 003.712-1.538l1.732-1.732a5.25 5.25 0 001.538-3.712l.003-2.024a.668.668 0 01.198-.471 1.575 1.575 0 10-2.228-2.228 3.818 3.818 0 00-1.12 2.687M6.9 7.575V12m6.27 4.318A4.49 4.49 0 0116.35 15m.002 0h-.002" />
                                        </svg>
                                        <span class="font-inter text-lg font-semibold text-red-500">You're getting fleeced!</span>
                                    </div>
                                    <!-- yellow -->
                                    <div v-if="arcColor === 'yellow' && !loading" class="inline-flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-amber-500 mr-2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M7.5 15h2.25m8.024-9.75c.011.05.028.1.052.148.591 1.2.924 2.55.924 3.977a8.96 8.96 0 01-.999 4.125m.023-8.25c-.076-.365.183-.75.575-.75h.908c.889 0 1.713.518 1.972 1.368.339 1.11.521 2.287.521 3.507 0 1.553-.295 3.036-.831 4.398C20.613 14.547 19.833 15 19 15h-1.053c-.472 0-.745-.556-.5-.96a8.95 8.95 0 00.303-.54m.023-8.25H16.48a4.5 4.5 0 01-1.423-.23l-3.114-1.04a4.5 4.5 0 00-1.423-.23H6.504c-.618 0-1.217.247-1.605.729A11.95 11.95 0 002.25 12c0 .434.023.863.068 1.285C2.427 14.306 3.346 15 4.372 15h3.126c.618 0 .991.724.725 1.282A7.471 7.471 0 007.5 19.5a2.25 2.25 0 002.25 2.25.75.75 0 00.75-.75v-.633c0-.573.11-1.14.322-1.672.304-.76.93-1.33 1.653-1.715a9.04 9.04 0 002.86-2.4c.498-.634 1.226-1.08 2.032-1.08h.384" />
                                        </svg>
                                        <span class="font-inter text-lg font-semibold text-amber-500">Not an ideal trade for you.</span>
                                    </div>
                                    <!-- green -->
                                    <div v-if="arcColor === 'green' && !loading" class="inline-flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-lime-600 mr-2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v17.25m0 0c-1.472 0-2.882.265-4.185.75M12 20.25c1.472 0 2.882.265 4.185.75M18.75 4.97A48.416 48.416 0 0012 4.5c-2.291 0-4.545.16-6.75.47m13.5 0c1.01.143 2.01.317 3 .52m-3-.52l2.62 10.726c.122.499-.106 1.028-.589 1.202a5.988 5.988 0 01-2.031.352 5.988 5.988 0 01-2.031-.352c-.483-.174-.711-.703-.59-1.202L18.75 4.971zm-16.5.52c.99-.203 1.99-.377 3-.52m0 0l2.62 10.726c.122.499-.106 1.028-.589 1.202a5.989 5.989 0 01-2.031.352 5.989 5.989 0 01-2.031-.352c-.483-.174-.711-.703-.59-1.202L5.25 4.971z" />
                                        </svg>
                                        <span class="font-inter text-lg font-semibold text-lime-600">Fair trade for both sides.</span>
                                    </div>
                                    <!-- sky -->
                                    <div v-if="arcColor === 'sky' && !loading" class="inline-flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-sky-400 mr-2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M6.633 10.5c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 012.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 00.322-1.672V3a.75.75 0 01.75-.75A2.25 2.25 0 0116.5 4.5c0 1.152-.26 2.243-.723 3.218-.266.558.107 1.282.725 1.282h3.126c1.026 0 1.945.694 2.054 1.715.045.422.068.85.068 1.285a11.95 11.95 0 01-2.649 7.521c-.388.482-.987.729-1.605.729H13.48c-.483 0-.964-.078-1.423-.23l-3.114-1.04a4.501 4.501 0 00-1.423-.23H5.904M14.25 9h2.25M5.904 18.75c.083.205.173.405.27.602.197.4-.078.898-.523.898h-.908c-.889 0-1.713-.518-1.972-1.368a12 12 0 01-.521-3.507c0-1.553.295-3.036.831-4.398C3.387 10.203 4.167 9.75 5 9.75h1.053c.472 0 .745.556.5.96a8.958 8.958 0 00-1.302 4.665c0 1.194.232 2.333.654 3.375z" />
                                        </svg>
                                        <span class="font-inter text-lg font-semibold text-sky-400">Go for it.</span>
                                    </div>
                                    <!-- blue -->
                                    <div v-if="arcColor === 'blue' && !loading" class="inline-flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-sky-600 mr-2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />
                                        </svg>
                                        <span class="font-inter text-lg font-semibold text-sky-600">Absolutely yes.</span>
                                    </div>
                                </div>
                                <!-- divider-->
                                <hr v-show="arcColor && !loading" class="w-1/6 mx-auto border-t-gray-500 py-1"/>
                                <!-- spinner -->
                                <div v-show="loading" class="flex justify-center" role="status">
                                    <svg aria-hidden="true" class="inline w-8 h-8 text-gray-200 animate-spin fill-zinc-400" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                                        <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                                    </svg>
                                </div>
                                <!-- Trade subtext -->
                                <div class="flex items-center justify-center px-4">
                                    <span v-if="!arcColor" class="font-lato text-light-text font-medium text-center text-sm">Add players to both boxes to receive a recommendation.</span>
                                    <span v-if="arcColor === 'red' && !loading" class="font-lato text-light-text font-medium text-center text-sm">Do not make this trade under any circumstances!</span>
                                    <span v-if="arcColor === 'yellow' && !loading" class="font-lato text-light-text font-medium text-center text-sm">Though close, we certainly think you can do better!</span>
                                    <span v-if="arcColor === 'green' && !loading" class="font-lato text-light-text font-medium text-center text-sm">Both parties should be satisfied as we feel the packages are evenly valued.</span>
                                    <span v-if="arcColor === 'sky' && !loading" class="font-lato text-light-text font-medium text-center text-sm">We definitely like your side of the deal a little more, so we suggest making this trade.</span>
                                    <span v-if="arcColor === 'blue' && !loading" class="font-lato text-light-text font-medium text-center text-sm">But let's be real for a second. No one is making this trade with you, so keep dreaming.</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- acquire -->
                <div class="px-6 flex flex-col items-center justify-center">
                    <div
                    ref="acquireBox"
                    @click="focusAcquireBox"
                    class="w-full relative group flex flex-col justify-center items-center cursor-pointer">
                        <div class="inline-flex items-center mb-3">
                            <LeftArrow class="group-hover:-translate-x-1 [transition:transform_0.2s] w-8 fill-current text-rose-400"/>
                            <span class="font-inter font-semibold text-lg text-light-text pl-4">Acquire</span>
                            <ResetIcon
                                @click.stop="toAcquire = []"
                                v-if="toAcquire.length !== 0"
                                class="w-6 h-6 md-lg:w-7 md-lg:h-7 text-slate-400 absolute right-1 hover:text-light-text/80"/>
                        </div>
                        <div class="relative px-4 py-6 w-full h-80 md-lg:h-[460px] md-lg:w-[248px] flex flex-row gap-3 flex-wrap content-start justify-center overflow-auto overflow-x-hidden shadow-inner shadow-gray-500/50 rounded-sm border-2 border-dashed border-gray-400 group-hover:border-gray-600 group-hover:bg-stone-50 bg-light-bg-primary cursor-pointer transition duration-500 ease-out"
                        :class="{'ring-4': acquireBoxActive,
                                 'ring-rose-400/80': acquireBoxActive,
                                 'bg-stone-50': acquireBoxActive,
                                 'border-gray-600': acquireBoxActive}">
                            <Transition>
                                <span
                                    v-if="!acquireBoxActive && toAcquire.length === 0"
                                    class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 font-inter font-medium text-light-text/60 group-hover:text-light-text text-sm text-center transition duration-150 ease-out">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-auto mb-2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M15.042 21.672L13.684 16.6m0 0l-2.51 2.225.569-9.47 5.227 7.917-3.286-.672zm-7.518-.267A8.25 8.25 0 1120.25 10.5M8.288 14.212A5.25 5.25 0 1117.25 10.5" />
                                    </svg>
                                    <span>Click here to add players.</span>
                                </span>
                                <span
                                    v-else-if="acquireBoxActive && toAcquire.length === 0"
                                    class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 font-inter font-medium text-light-text text-sm text-center transition duration-150 ease-out">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-auto mb-2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 012.25-2.25h7.5A2.25 2.25 0 0118 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 004.5 9v.878m13.5-3A2.25 2.25 0 0119.5 9v.878m0 0a2.246 2.246 0 00-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0121 12v6a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 18v-6c0-.98.626-1.813 1.5-2.122" />
                                    </svg>
                                    <span>Select a player card.</span>
                                </span>
                            </Transition>
                            <TransitionGroup name="list">
                                <TradeValueTab
                                v-for="p in toAcquire"
                                    :key="p.id"
                                    :name="p.Name"
                                    :position="p.Position"
                                    :value="p.Value"
                                    :team="p.Team"
                                    @delete="removeFromAcquireBox(p.id)"
                                />
                            </TransitionGroup>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- <pre>{{ players }}</pre> -->
</template>

<script setup>
import { ref, reactive, computed, toRaw, onMounted, watch } from 'vue'
import { rtdb } from '../firebase'
import { ref as fbRef, onValue, query, orderByChild } from 'firebase/database'
import TradeValueCard from '../components/tradeAnalyzer/TradeValueCard.vue'
import TradeValueTab from '../components/tradeAnalyzer/TradeValueTab.vue'
import PositionSwitch from '../components/tradeAnalyzer/PositionSwitch.vue'
import AnimatedNumber from '../components/tradeAnalyzer/AnimatedNumber.vue'
import GaugeChart from '../components/tradeAnalyzer/GaugeChart.vue'
// Icons
import RightArrow from '../components/svg/RightArrow.vue'
import LeftArrow from '../components/svg/LeftArrow.vue'
import ResetIcon from '../components/svg/ResetIcon.vue'

import useDetectOutsideClick from '../composables/detectOutsideClick.js'

const chartOptions = {
    hasNeedle: true,
    needleColor: '#64748b',
    needleUpdateSpeed: 1000,
    arcColors: [
        '#f87171',
        '#fde047',
        '#a3e635',
        '#7dd3fc',
        '#0ea5e9',
    ],
    arcDelimiters: [10, 40, 60, 90],
    arcPadding: 2,
    arcPaddingColor: '#f5f5f4',
    arcOverEffect: false,
    needleStartValue: 0,
}
const arcColor = ref(null)
const loading = ref(false)

// load trade value data from database
const playersRef = fbRef(rtdb, 'trade_values/')
const queryByValue = query(playersRef, orderByChild('Value'))
const initial = ref([])
onValue(queryByValue, (snapshot) => {
    const db = []
    snapshot.forEach((childSnapshot) => {
        const data = childSnapshot.val()
        data.id = childSnapshot.key
        db.push(data)
    })
    initial.value = db
})

// toggle to filter players by position
const filters = reactive({
    QB: false,
    RB: false,
    WR: false,
    TE: false
})
const filterBy = computed(() => {
    let positions = []
    if (filters.QB) {
        positions.push('QB')
    }
    if (filters.RB) {
        positions.push('RB')
    }
    if (filters.WR) {
        positions.push('WR')
    }
    if (filters.TE) {
        positions.push('TE')
    }
    return positions
})
const players = computed(() => {
    return initial.value.reverse()
})
const filteredPlayers = computed(() => {
    let filtered = players.value
    if (filters.QB || filters.RB || filters.WR || filters.TE) {
        filtered = filtered.filter(function(p) {
            return filterBy.value.includes(p.Position)
        })
    }
    // TODO: Figure out something more efficient
    filtered = filtered.filter(x => !toSend.value.filter(y => y.id === x.id).length)
    filtered = filtered.filter(x => !toAcquire.value.filter(y => y.id === x.id).length)
    return filtered
})
//
const sendSum = computed(() => {
    let sum = 0
    toSend.value.forEach((p) => {
        sum += p.Value
    })
    return sum
})
const acquireSum = computed(() => {
    let sum = 0
    toAcquire.value.forEach((p) => {
        sum += p.Value
    })
    return sum
})
const sendBoxActive = ref(null)
const acquireBoxActive = ref(null)

const sendBox = ref()
const acquireBox = ref()
useDetectOutsideClick(sendBox, () => { 
    sendBoxActive.value = false
})
useDetectOutsideClick(acquireBox, () => { 
    acquireBoxActive.value = false
})

function focusSendBox() {
    acquireBoxActive.value = false
    sendBoxActive.value = true
} 
function focusAcquireBox() {
    acquireBoxActive.value = true
    sendBoxActive.value = false
}
function addToSend(p) {
    toSend.value.push(structuredClone(toRaw(p)))
}
function addToAcquire(p) {
    toAcquire.value.push(structuredClone(toRaw(p)))
}
function addCardtoSendBox(p) {
    // this is where we call addToSend and addToAcquire
    if (sendBoxActive.value) {
        addToSend(p)
    }
    else if (acquireBoxActive.value) {
        addToAcquire(p)
    }
}
function removeFromsendBox(id) {
    toSend.value = toSend.value.filter((p) => p.id !== id)
}
function removeFromAcquireBox(id) {
    toAcquire.value = toAcquire.value.filter((p) => p.id !== id)
}
function setArcColor(color) {
    arcColor.value = color
    // console.log(arcColor.value)
}
function toggleSpinner(active) {
    loading.value = active
}
const toSend = ref([])
const toAcquire = ref([])

</script>
<style>
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>