<template>
    <div ref="gaugeArea"></div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import * as GaugeChart from 'https://unpkg.com/gauge-chart@next/dist/bundle.mjs'
// import GaugeChart from 'gauge-chart'
const props = defineProps(['sendSum', 'acquireSum', 'toSendSize', 'toAcquireSize', 'options', 'chartSize'])
const emit = defineEmits(['loading', 'arcColor'])

const gaugeArea = ref(null)
const chart = ref(null)
function initChart(options) {
   // Drawing and updating the chart
   chart.value = GaugeChart.gaugeChart(gaugeArea.value, props.chartSize, options)
}
function calcPercentDiff(a, b) {
    return 100*(a - b)/((a + b)/2)
}
// map interval [a, b] onto interval [c, d]
function mapInterval(a, b, c, d, percDiff) {
    return c + ((d - c)/(b - a))*(percDiff - a)
}
// show loading spinner for about 1 second
function activateSpinner() {
    emit('loading', true)
    window.setTimeout(() => {
        emit('loading', false)
    }, 1000)
}
onMounted(() => {
    initChart(props.options)
})

watch(() => ([props.sendSum, props.acquireSum]), () => {
    let percDiff = calcPercentDiff(props.acquireSum, props.sendSum)
    if (props.toSendSize >= 1 && props.toAcquireSize >= 1) {
        console.log('percDiff', percDiff)
        activateSpinner()
        // green bar
        if (percDiff >= -5.0 && percDiff <= 5.0) {
            let map = mapInterval(-5.0, 5.0, 41.0, 60.0, percDiff)
            // let map = 41 + ((60-41)/(5.0+5.0))*(percDiff+5.0)
            console.log(map)
            emit('arcColor', 'green')
            chart.value.updateNeedle(Math.floor(map))
        }
        // yellow bar
        else if (percDiff >= -20.0 && percDiff < -5.0) {
            let map = mapInterval(-20.0, -5.0, 11.0, 40.0, percDiff)
            // let map = 11 + ((40-11)/(-5.0+20.0))*(percDiff+20.0)
            console.log(map)
            emit('arcColor', 'yellow')
            chart.value.updateNeedle(Math.floor(map))
        }
        // sky bar
        else if (percDiff > 5.0 && percDiff <= 20.0) {
            let map = mapInterval(5.0, 20.0, 61.0, 90.0, percDiff)
            // let map = 61 + ((90-61)/(20.0-5.0))*(percDiff-5.0)
            console.log(map)
            emit('arcColor', 'sky')
            chart.value.updateNeedle(Math.floor(map))
        }
        // red bar
        else if (percDiff < -20.0) {
            let map = mapInterval(-30.0, -20.0, 0.0, 10.0, percDiff)
            // let map = 0 + ((10-0)/(-20.0+30.0))*(percDiff+30.0)
            console.log(map)
            emit('arcColor', 'red')
            chart.value.updateNeedle(Math.floor(map))
        }
        // blue bar
        else if (percDiff > 20.0) {
            let map = mapInterval(20.0, 30.0, 91.0, 100.0, percDiff)
            // let map = 91 + ((100-91)/(30.0-20.0))*(percDiff-20.0)
            console.log(map)
            emit('arcColor', 'blue')
            chart.value.updateNeedle(Math.floor(map))
        }
    }
    else {
            emit('arcColor', null)
            chart.value.updateNeedle(0)
    }
})
</script>