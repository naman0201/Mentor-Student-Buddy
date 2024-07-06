/* eslint-disable prettier/prettier */
import React from 'react'
import CIcon from '@coreui/icons-react'
import {
  cilSpeedometer,
  cilCloudUpload
} from '@coreui/icons'
import { CNavGroup, CNavItem, CNavTitle } from '@coreui/react'

let _nav = [
  {
    component: CNavItem,
    name: 'Dashboard',
    to: '/',
    icon: <CIcon icon={cilSpeedometer} customClassName="nav-icon" />,
  }
]
localStorage.getItem("usertype")==="Teacher" && _nav.push({
  component:CNavItem,
  name: 'Upload File',
  to: '/UploadFile',
  icon:<CIcon icon={cilCloudUpload} customClassName="nav-icon" />,
})

export default _nav
