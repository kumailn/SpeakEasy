import Vue from 'vue';
import './plugins/vuetify';
import App from './App.vue';
import router from './router';
import store from './store';
import Trend from 'vuetrend';
import VueApexCharts from 'vue-apexcharts';
 
Vue.use(VueApexCharts);
Vue.use(Trend);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
