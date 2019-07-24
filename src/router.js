import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/upload',
      name: 'upload',
      component: () => import('@/views/Upload.vue')
    },
    {
      path: '/download',
      name: 'download',
      component: () => import('@/views/Download.vue')
    },
    {
      path: '/album/:id',
      name: 'album',
      component: () => import('@/views/Album.vue')
    },
    {
      path: '/photo/:id',
      name: 'photo',
      component: () => import('@/views/Photo.vue')
    }
  ]
})
