import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import History from './views/History.vue';
import Login from './views/Login.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/history',
      name: 'history',
      component: History,
    },
    {
      path:'/login',
      name: 'login',
      component: Login,
    },
  ],
});
