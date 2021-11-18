import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
// Importing bootstrap first 
import BootstrapVue from "bootstrap-vue";

Vue.config.productionTip = false;
Vue.use(BootstrapVue)

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
