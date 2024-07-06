/* eslint-disable prettier/prettier */
import React, { useState } from 'react'
import {
  CButton,
  CContainer,
} from '@coreui/react'
import 'font-awesome/css/font-awesome.min.css'
import './LandingPage.css'
import LoginForm from './Login.js'
import RegisterForm from './Register.js'
import log from './img/log.svg'
import register from './img/register.svg'


const Login = () => {
  const [signIn,setSignIn] =useState('');
  return (
    <CContainer className={`${signIn}`}>
      <div className="forms-container">
        <div className="signin-signup">
          <LoginForm></LoginForm>
          <RegisterForm></RegisterForm>
        </div>
      </div>
      <div className="panels-container">
        <div className="panel left-panel">
          <div className="content">
            <h3>New here ?</h3>
            <p>Welcome, Kindly register yourself if you don&apos;t already have an account</p>
            <CButton
              className="btn transparent"
              id="sign-up-btn"
              onClick={() => {
                setSignIn('sign-up-mode')
              }}
            >
              Sign up
            </CButton>
          </div>
          <img src={log} className="image" alt="" />
        </div>

        <div className="panel right-panel">
          <div className="content">
            <h3>One of us ?</h3>
            <p>Kindly, fill out and login with your details</p>
            <CButton
              className="btn transparent"
              id="sign-in-btn"
              onClick={() => {
                setSignIn('')
              }}
            >
              Sign in
            </CButton>
          </div>
          <img src={register} className="image" alt="" />
        </div>
      </div>
    </CContainer >
  )
}

export default Login
