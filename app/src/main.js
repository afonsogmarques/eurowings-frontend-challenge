import './style.css';
import App from './App.vue';
import pinia from './stores';
import { createApp } from 'vue';

createApp(App).use(pinia).mount('#app');
