
const userRouter = [
  { path: '/login', name: 'userLogin', component: () => import('../views/userLogin.vue') },
  { path: '/signup', name: 'userSignup', component: () => import('../views/userSignup.vue') },
  { path: '/user',
    name: 'user',
    component: () => import('../views/userHome.vue'),
    children: [
      { path: '/user/item_list', name: 'userItemList', component: () => import('../components/user/recordItemList.vue') },
      { path: '/user/guide', name: 'userGuide', component: () => import('../components/user/userGuide.vue') },
      { path: '/user/edit_tags', name: 'editTags', component: () => import('../components/item_tag/editTags.vue') },
      { path: '/user/create_report_group', name: 'createReportGroup', component: () => import('../components/report_group/createReportGroup.vue') },
    ],
    beforeEnter: (to, from, next) => {
      if (to.path === '/login') next({ path: '/login' })
      else next()
    }

  },

]

export default userRouter
