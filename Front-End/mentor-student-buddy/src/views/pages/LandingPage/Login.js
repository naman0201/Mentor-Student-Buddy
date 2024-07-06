/* eslint-disable prettier/prettier */
import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  CButton,
  CFormLabel,
  CFormFeedback,
  CCard,
  CCardBody,
  CCardGroup,
  CCol,
  CContainer,
  CForm,
  CFormInput,
  CInputGroup,
  CInputGroupText,
  CRow,
} from '@coreui/react'
import 'font-awesome/css/font-awesome.min.css'
const LoginForm = () => {
  const navigate = useNavigate()
  const [signInUsername, setSignInUsername] = useState('')
  const [signInPassword, setSignInPassword] = useState('')
  const [errorMessage, setErrorMessage] = useState('')
  const [errorClass, setErrorClass] = useState('')
  const [shwMessage, setShwMessage] = useState(false)
  const onSigninUsernameChange = (evt) => {
    setSignInUsername(evt.target.value)
  }
  const onSigninPasswordChange = (evt) => {
    setSignInPassword(evt.target.value)
  }
  const onSigninSubmit = async (evt) => {
    evt.preventDefault()
    const form = evt.currentTarget
    setShwMessage(true)
    if (form.checkValidity() === false) {
      evt.stopPropagation()
    }
    let endPoint = 'http://127.0.0.1:8000/api/login'
    const data = { email: signInUsername, password: signInPassword }

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    }
    let result = await fetch(endPoint, options)
    result = await result.json()
    if (result.status === '200') {
      localStorage.setItem("B_Userid",result.userDetail.B_Userid)
      localStorage.setItem("u_ID",result.userDetail.u_ID)
      localStorage.setItem("email",result.userDetail.email)
      localStorage.setItem("usertype",result.userDetail.usertype)
      navigate('/')
    } else if (result.status === '420') {
      setErrorClass('alert alert-danger')
      setErrorMessage(result.message)
    }
  }
  return (
    <CForm
      className="sign-in-form"
      noValidate
      validated={shwMessage}
      onSubmit={onSigninSubmit}
    >
      <h2 className="title">Sign in</h2>
      <CCol md={8} className="position-relative input-field">
        <i className="fa fa-user"></i>
        <CFormInput
          type="email"
          id="validationTooltip02"
          required
          placeholder="Username"
          onChange={onSigninUsernameChange}
        />
        <CFormFeedback tooltip invalid>
          Please fill a valid email
        </CFormFeedback>
      </CCol>
      <CCol md={8} className="position-relative input-field">
        <i className="fa fa-lock"></i>
        <CFormInput
          type="password"
          id="validationTooltip02"
          required
          placeholder="Password"
          onChange={onSigninPasswordChange}
        />
        <CFormFeedback tooltip invalid>
          Please enter a valid password
        </CFormFeedback>
      </CCol>
      <CButton color="info" className="px-4" type="submit">
        Sign in
      </CButton>
      <div className={`${errorClass}`}>{errorMessage}</div>
    </CForm>
  )
}

export default LoginForm
