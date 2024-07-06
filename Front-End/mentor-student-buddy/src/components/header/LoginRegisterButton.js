/* eslint-disable prettier/prettier */
import React from 'react';
import {CButton} from "@coreui/react"
import { useNavigate } from 'react-router-dom'
export default function LoginRegisterButton(){
    const navigate= useNavigate()
    return(
        <CButton color="info" shape="rounded-pill" onClick={()=>{navigate("/login")}}>Login/Register</CButton>
    );
}
