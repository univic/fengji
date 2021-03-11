
const userRouter = [
  { path: '/login', name: 'userLogin', component: () => import('../views/userLogin.vue') },
  { path: '/signup', name: 'userSignup', component: () => import('../views/userSignup.vue') },
  { path: '/user',
    name: 'user',
    component: () => import('../views/userHome.vue'),
    children: [
      { path: '/user/workbench', name: 'userWorkbench', component: () => import('../components/user/userWorkbench.vue') },
      { path: '/user/guide', name: 'userGuide', component: () => import('../components/user/userGuide.vue') },
      { path: '/user/edit_tags', name: 'editTags', component: () => import('../components/item_tag/editTags.vue') },
      { path: '/user/create_report_group', name: 'createReportGroup', component: () => import('../components/report_group/createReportGroup.vue') },
      { path: '/user/manage_report_group', name: 'manageReportGroup', component: () => import('../components/report_group/manageReportGroup.vue') },
      { path: '/user/my_report_group', name: 'myReportGroup', component: () => import('../components/report_group/myReportGroup.vue') },
    ],
    beforeEnter: (to, from, next) => {
      if (to.path === '/login') next({ path: '/login' })
      else next()
    }

  },

]

export default userRouter
