import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	{
		path: '/about',
		name: 'About',
		component: () =>
			import(/* webpackChunkName: "about" */ '@/views/About.vue'),
	},
	{
		path: '/join',
		name: 'Join',
		component: () => import(/* webpackChunkName: "Join" */ '@/views/Join.vue'),
	},
	{
		path: '/discontinue',
		name: 'Discontinue',
		component: () =>
			import(/* webpackChunkName: "Join" */ '@/views/Discontinue.vue'),
	},
	{
		path: '/details',
		name: 'Details',
		component: () =>
			import(/* webpackChunkName: "Details" */ '@/views/Details.vue'),
	},
	{
		path: '/my',
		name: 'My',
		component: () =>
			import(/* webpackChunkName: "My" */ '@/views/My.vue'),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
