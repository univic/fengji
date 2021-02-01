
const userRouter = [
  { path: '/login', name: 'userLogin', component: () => import('../views/userLogin.vue') },
  { path: '/signup', name: 'userSignup', component: () => import('../views/userSignup.vue') },
  { path: '/user',
    name: 'user',
    component: () => import('../views/userHome.vue'),
    children: [
      { path: '/user/item_list', name: 'userItemList', component: () => import('../components/recordItemList.vue') },
      { path: '/user/guide', name: 'userGuide', component: () => import('../components/user/userGuide.vue') },
    ],
    beforeEnter: (to, from, next) => {
      if (to.path === '/login') next({ path: '/login' })
      else next()
    }

  },

]

export default userRouter
