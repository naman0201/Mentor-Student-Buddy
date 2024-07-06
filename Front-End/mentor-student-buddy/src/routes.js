import React from 'react'

const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'))
const UploadFile = React.lazy(() => import('./views/UploadFile/UploadFile'))
const routes = [
  { path: '/', name: 'Dashboard', element: Dashboard },
  { path: '/UploadFile', name: 'Upload File', element: UploadFile },
]
export default routes
