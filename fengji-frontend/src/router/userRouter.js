
const userRouter = [
  { path: '/login', component: () => import('../views/userLogin.vue') },
  { path: '/signup', component: () => import('../views/userSignup.vue') },
  { path: '/user',
    component: () => import('../views/userHome.vue'),
    children: [
      { path: '/user/item_list', component: () => import('../components/recordItemList.vue') },
      { path: '/user/guide', component: () => import('../components/user/userGuide.vue') },
    ]
  },

]

export default userRouter
