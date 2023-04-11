import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import Hero from '../views/Hero.vue'
import SelectPlatform from '../views/auth/SelectPlatform.vue'
import Login from '../views/auth/Login.vue'
import Register from '../views/auth/Register.vue'
import EspnAuth from '../views/auth/espn/EspnAuth.vue'
import Dashboard from '../views/Dashboard.vue'
import TradeAnalyzer from '../views/TradeAnalyzer.vue'
import PowerRankings from '../views/PowerRankings.vue'
import { useStoreAuth } from '../stores/storeAuth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Hero,
      meta: { requiresAuth: false }
    },
    {
      path: '/platform-select',
      name: 'platform_select',
      component: SelectPlatform,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: { requiresAuth: false }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: { requiresAuth: false }
    },
    {
      path: '/espn-auth',
      name: 'espn_auth',
      component: EspnAuth,
      meta: { requiresAuth: true }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: { requiresAuth: true }
    },
    {
      path: '/trade-analyzer',
      name: 'trade_analyzer',
      component: TradeAnalyzer,
      meta: { requiresAuth: true }
    },
    {
      path: '/power-rankings',
      name: 'power_rankings',
      component: PowerRankings,
      meta: { requiresAuth: true }
    }
  ]
})
router.beforeEach(async (to, from) => {
    console.log('router accessed')
    const storeAuth = useStoreAuth()
    console.log('store called', storeAuth.user.id)
    if (storeAuth.user.id && (to.name === 'register' || to.name === 'login')) {
        return { name:'dashboard' }
    }
    if (to.meta.requiresAuth && !storeAuth.user.id) {
      return { name:'login' }
    }
})
export default router
