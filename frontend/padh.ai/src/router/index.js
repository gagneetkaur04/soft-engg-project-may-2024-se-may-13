import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Dashboard from '../views/Dashboard.vue'
import Course from '../views/Course.vue'
import CourseHighlights from '../views/CourseHighlights.vue'
import axios from 'axios'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login',
      name: 'base',
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      beforeEnter() {
        if (localStorage.getItem('Auth-Token')) {
          return '/dashboard'
        }
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup,
      beforeEnter() {
        if (localStorage.getItem('Auth-Token')) {
          return '/dashboard'
        }
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      beforeEnter() {
        if (!localStorage.getItem('Auth-Token')) {
          return '/login'
        }
      } 
    },
    {
      path: '/course/:courseId',
      name: 'course',
      component: Course,
      props: ((route) => ({ contentId: route.params.contentId })),
      beforeEnter() {
        if (!localStorage.getItem('Auth-Token')) {
          return '/login'
        }
      }
    },
    {
      path: '/course/:courseId/highlights',
      name: 'highlights',
      component: CourseHighlights,
      beforeEnter() {
        if (!localStorage.getItem('Auth-Token')) {
          return '/login'
        } 
      }
    },
    {
      path: '/logout',
      name: 'logout',
      async beforeEnter() {
        let request = {
          url: __API_URL__ + 'logout',
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('Auth-Token')}`,
            'content-type': 'application/json'
          }
        }
        let response = await axios(request)
        if (response.status === 200) {
          localStorage.removeItem('Auth-Token')
          return '/login'
        }
        else {
          alert('Logout failed returning to dashboard')
          return '/dashboard'
        }
      }
    }
  ]
})

export default router

// login
// signup
// student dashboard
// course homepage & content_id
// course highlights
// logout