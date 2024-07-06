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
    CAlert,
    CFormSelect,
} from '@coreui/react'
import 'font-awesome/css/font-awesome.min.css'
import { setTimeout } from 'core-js'
import {setSignIn} from './LandingPage'
import Swal from 'sweetalert2'

const RegisterForm = () => {
    const navigate = useNavigate()
    const [errorMessage, setErrorMessage] = useState('')
    const [errorClass, setErrorClass] = useState('')
    const [shwMessage, setShwMessage] = useState(false)
    const [signUpName, setSignUpName] = useState('')
    const [signUpUsername, setSignUpUsername] = useState('')
    const [signUpPassword, setSignUpPassword] = useState('')
    const [signUpCnfPassword, setSignUpCnfPassword] = useState('')
    const [signUpUserId, setSignUpUserId] = useState('')
    const [signUpUserType,setSignUpUserType]=useState('')
    const PwdMatch = () => {
        if(signUpPassword==="" || signUpCnfPassword=="")
        return true;
        return  signUpPassword === signUpCnfPassword;
    }
    const onSignUpUserTypeChange=(evt)=>{
        setSignUpUserType(evt.target.value)
    }
    const onSignUpUserIDChange = (evt) => {
        setSignUpUserId(evt.target.value)
    }
    const onSignupNameChange = (evt) => {
        setSignUpName(evt.target.value)
    }
    const onSignupUsernameChange = (evt) => {
        setSignUpUsername(evt.target.value)
    }
    const onSignupPasswordChange = (evt) => {
        setSignUpPassword(evt.target.value)
    }
    const onSignupCnfPasswordChange = (evt) => {
        setSignUpCnfPassword(evt.target.value)
    }
    const onSignupSubmit = async (evt) => {
        evt.preventDefault()
        const form = evt.currentTarget
        setShwMessage(true)
        if (form.checkValidity() === false) {
            evt.stopPropagation()
        }
        let endPoint = 'http://127.0.0.1:8000/api/register'
        const data = {
            u_ID:signUpUserId,
            usertype:signUpUserType,
            name: signUpName,
            email: signUpUsername,
            password: signUpPassword,
            password2: signUpCnfPassword,
        }
        console.log(data)

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        }
        let result = await fetch(endPoint, options)
        result = await result.json()
        console.log(result)
        if (result.status === '200') {
            await Swal.fire(
                'Success!',
                // 'Successfully registered Please Login',
                'Successfully Shared details with Admin to proceed your request.',
                'success'
              ).then((result) => {
                if (result.isConfirmed)
                  window.location.reload();
              })
            window.location.reload()
        } else if (result.status === '420') {
            setErrorClass('alert alert-danger')
            setErrorMessage(result.message)
        }
    }

    return (
        <CForm
            noValidate
            validated={shwMessage}
            className="sign-up-form"
            onSubmit={onSignupSubmit}
        >
            <h2 className="title">Sign up</h2>

            <CCol md={8} className="position-relative input-field">
                <i className="fa fa-user"></i>
                <CFormSelect
                    id="validationTooltip02"
                    value={signUpUserType}
                    required
                    onChange={onSignUpUserTypeChange}
                >
                    <option value='' disabled=''>Select Your UserType</option>
                    <option value='Student'>Student</option>
                    <option value='Teacher'>Teacher</option>
                </CFormSelect>
                <CFormFeedback tooltip invalid>
                    Please select valid UserType
                </CFormFeedback>
            </CCol>
            <CCol md={8} className="position-relative input-field">
                <i className="fa fa-user"></i>
                <CFormInput
                    type="text"
                    id="validationTooltip02"
                    required
                    placeholder="Enrollment NO./Employement ID"
                    onChange={onSignUpUserIDChange}
                />
                <CFormFeedback tooltip invalid>
                    Please fill your Id
                </CFormFeedback>
            </CCol>

            <CCol md={8} className="position-relative input-field">
                <i className="fa fa-user"></i>
                <CFormInput
                    type="text"
                    id="validationTooltip01"
                    required
                    placeholder="Name"
                    onChange={onSignupNameChange}
                />
                <CFormFeedback tooltip invalid>
                    Please fill a name
                </CFormFeedback>
            </CCol>

            <CCol md={8} className="position-relative input-field">
                <i className="fa fa-envelope"></i>
                <CFormInput
                    type="email"
                    id="validationTooltip02"
                    required
                    placeholder="Email"
                    onChange={onSignupUsernameChange}
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
                    onChange={onSignupPasswordChange}
                />
                <CFormFeedback tooltip invalid>
                    Please enter a valid password
                </CFormFeedback>
            </CCol>

            <CCol md={8} className="position-relative input-field">
                <i className="fa fa-lock"></i>
                <CFormInput
                    type="password"
                    id="validationTooltip02"
                    required
                    placeholder="Confirm Password"
                    onChange={onSignupCnfPasswordChange}
                />
                <CFormFeedback tooltip invalid>
                    Please enter a valid password
                </CFormFeedback>
            </CCol>

            {PwdMatch() ? null : <CAlert color="danger">Password Mismatch!</CAlert>}

            <CButton color="info" className="px-4" type="submit">
                Sign Up
            </CButton>
            <div className={`${errorClass}`}>{errorMessage}</div>
        </CForm>

    )
}

export default RegisterForm
