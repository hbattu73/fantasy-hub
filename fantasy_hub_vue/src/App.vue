<template>
  <div class="flex flex-col min-h-screen bg-light-bg-primary">
    <Header v-show="!isAuthComponent"/>
    <RouterView></RouterView>
  </div>
</template>

<script setup>
import Header from "./components/Header.vue"
import { computed, onMounted } from "vue"
import { useRoute } from 'vue-router'
import { useStoreAuth } from "./stores/storeAuth"
// import router from "./router"
const route = useRoute()
const isAuthComponent = computed(() => {
    return route.name === 'login' || route.name === 'register' || route.name === 'platform_select' || route.name === 'espn_auth'
})

const storeAuth = useStoreAuth()
onMounted(() => {
    console.log('app mounted')
    storeAuth.init()
})


</script>