import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'
import VueLazyload from 'vue-lazyload'
import failedPNG from '@/assets/failed.png'

Vue.config.productionTip = false

Vue.use(VueLazyload, {
  error: failedPNG,
  attempt: 1
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
