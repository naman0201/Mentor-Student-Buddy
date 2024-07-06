/* eslint-disable prettier/prettier */
/* eslint-disable react/prop-types */
import React, { useState, useEffect } from 'react'
import {
  CButton,
  CCard,
  CCol,
  CForm,
  CFormFeedback,
  CFormLabel,
  CFormSelect,
  CRow,
  CFormSwitch,
  CCardHeader,
} from '@coreui/react'

import DocViewer from "react-doc-viewer";
import ViewFileComponent from './ViewFileComponent';
import Swal from 'sweetalert2';

export default function ViewFileSpecific(props) {
  let specificEndpoint = "http://127.0.0.1:8000/Buddyshare/ShareGetApi/APIBuddyView"
  const options={ 
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': "{{csrf_token}}"
    },
    body: JSON.stringify({B_Userid:localStorage.getItem('B_Userid')})
  }
  const [everyOneFileDataArr, setEveryOneFileDataArr] = useState([])
  const [specificFileDataArr, setSpecificFileDataArr] = useState([])
    useEffect(() => {
        fetch(specificEndpoint,options)
            .then(response => response.json())
            .then(response => {
                if (response.status == '200') {
                    setEveryOneFileDataArr(response.data.EveryOneFileOutLogin)
                    setSpecificFileDataArr(response.data.specificuserLoggedIn)
                } else {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Error on Server!',
                    })
                }
            });
    }, [])
  return (
    // <a href={test} target="_blank" 
    // rel="noreferrer" download="true">Click Here</a>
    <>
    {everyOneFileDataArr && (everyOneFileDataArr.length>0 ? <ViewFileComponent title="Files For Everyone" fileDataArr={everyOneFileDataArr}/>:null)}
    <p></p>
    {specificFileDataArr && (specificFileDataArr.length>0 ? <ViewFileComponent title="Files For You" fileDataArr={specificFileDataArr}/>:null)}
    </>
  );
}