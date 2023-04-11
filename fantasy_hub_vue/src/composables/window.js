import { computed, onMounted, onUnmounted, ref } from 'vue'
// minimum width of medium screen
// const mdBreakpoint = 768

export function useResponsive() {
    const windowWidth = ref(window.innerWidth)
    function onResize() {
        windowWidth.value = window.innerWidth
    }
    onMounted(() => window.addEventListener('resize', onResize))
    onUnmounted(() => window.removeEventListener('resize', onResize))

    const width = computed(() => {
        // return windowWidth.value < mdBreakpoint
        return windowWidth.value
    })
    return { width }
}