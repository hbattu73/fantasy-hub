<template>
     <span>{{ animatedNumber }}</span>
</template>

<script setup>
import { ref, watch, onMounted, computed } from 'vue'
// Accept prop
const props = defineProps({
    number: {
        type: Number,
        default: 0
    }
})
const counter = ref(false)
const animatedNumber = ref(0)
const number = computed(() => {
    return props.number
})

onMounted(() => {
    animatedNumber.value = props.number ? props.number : 0
})

watch(number, () => {
    clearInterval(counter.value)
    if (props.number === animatedNumber.value) {
        return
    }
    counter.value = window.setInterval(() => {
        if (Math.floor(animatedNumber.value) !== Math.floor(props.number)) {
            var change = (props.number - animatedNumber.value) / 4
            change = change >= 0 ? Math.ceil(change) : Math.floor(change)
            // console.log('change', change)
            animatedNumber.value = Math.round((animatedNumber.value + change)*10)/10
            // console.log('animated', animatedNumber.value)
        }
        else {
            animatedNumber.value = Math.round(props.number*10)/10
            // console.log('in else', animatedNumber.value)
            clearInterval(counter.value)
        }
    }, 20)
})
</script>