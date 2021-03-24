import Vue from 'vue'
//import VueRouter from 'vue-router'
import App from './App.vue'
//import Gallery from './components/Gallery.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faFolder, faPlusCircle } from '@fortawesome/free-solid-svg-icons'

library.add(faFolder, faPlusCircle)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false



new Vue({
render: h=>h(App)
}).$mount('#app')

