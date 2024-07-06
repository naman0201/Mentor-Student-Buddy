/* eslint-disable prettier/prettier */
import React, { useState,useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'

import { CSidebar, CSidebarBrand, CSidebarNav, CSidebarToggler } from '@coreui/react'
import CIcon from '@coreui/icons-react'

import { AppSidebarNav } from './AppSidebarNav'

import logo  from 'src/assets/images/logo.png'
import { sygnet } from 'src/assets/brand/sygnet'

import SimpleBar from 'simplebar-react'
import 'simplebar/dist/simplebar.min.css'
// sidebar nav config
import navigation from '../_nav'
import { CNavGroup, CNavItem, CNavTitle } from '@coreui/react'
import {
  cilSpeedometer,
  cilCloudUpload
} from '@coreui/icons'

const AppSidebar = () => {
  const newNav=[
    {
      component: CNavItem,
      name: 'Dashboard',
      to: '/',
      icon: <CIcon icon={cilSpeedometer} customClassName="nav-icon" />,
    },
    {
      component:CNavItem,
      name: 'Upload File',
      to: '/UploadFile',
      icon:<CIcon icon={cilCloudUpload} customClassName="nav-icon" />,
    }
  ]
  const dispatch = useDispatch()
  const unfoldable = useSelector((state) => state.sidebarUnfoldable)
  const sidebarShow = useSelector((state) => state.sidebarShow)
  const [sideBarArr,setSideBarArr]=useState(navigation);
  useEffect(() =>{
    localStorage.getItem("usertype")==="Teacher"  && setSideBarArr(newNav)
  },[])
  return (
    <CSidebar
      position="fixed"
      unfoldable={unfoldable}
      visible={sidebarShow}
      onVisibleChange={(visible) => {
        dispatch({ type: 'set', sidebarShow: visible })
      }}
    >
      <CSidebarBrand className="d-none d-md-flex" to="/">
        <CIcon className="sidebar-brand-full" icon={logo} height={35}  />
        {/* <CIcon icon={cilSpeedometer} height={35} /> */}
        <CIcon className="sidebar-brand-narrow" icon={sygnet} height={35} />
      </CSidebarBrand>
      <CSidebarNav>
        <SimpleBar>
          <AppSidebarNav items={sideBarArr} />
        </SimpleBar>
      </CSidebarNav>
      <CSidebarToggler
        className="d-none d-lg-flex"
        onClick={() => dispatch({ type: 'set', sidebarUnfoldable: !unfoldable })}
      />
    </CSidebar>
  )
}

export default React.memo(AppSidebar)
