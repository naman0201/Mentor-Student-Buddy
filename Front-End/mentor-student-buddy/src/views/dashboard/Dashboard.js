/* eslint-disable prettier/prettier */
import React from 'react'
import {
  CButton,
  CCard,
  CCardBody,
  CCardFooter,
  CCardGroup,
  CCardHeader,
  CCardImage,
  CCardLink,
  CCardSubtitle,
  CCardText,
  CCardTitle,
  CListGroup,
  CListGroupItem,
  CNav,
  CNavItem,
  CNavLink,
  CCol,
  CRow,
} from '@coreui/react'
import ViewFileEveryOne from '../ViewFile/ViewFileEveryOne'
import ViewFileSpecific from '../ViewFile/ViewFileSpecific'

const Cards = () => {
  console.log("hello");
  
  return (
    <CRow>
      <CCol xs={12}>
        {localStorage.length ===0 ? <ViewFileEveryOne/>:<ViewFileSpecific/>}
      </CCol>
    </CRow>
  )
}

export default Cards
