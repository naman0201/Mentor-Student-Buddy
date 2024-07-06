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

import ViewFileComponent from './ViewFileComponent'
import DocViewer from "react-doc-viewer";
import Swal from 'sweetalert2';

export default function ViewFileEveryOne(props) {
    let everyOneEndpoint = "http://127.0.0.1:8000/Buddyshare/ShareGetApi/APIBuddyEveryOneView"
    const [fileDataArr, setFileDataArr] = useState([])
    useEffect(() => {
        fetch(everyOneEndpoint)
            .then(response => response.json())
            .then(response => {
                if (response.status == '200') {
                    setFileDataArr(response.data.EveryOneFileDataObjWithOutLogin)
                } else {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Error on Server!',
                    })
                }
            });
    }, [])
    // let test = "http://localhost:8000/media/64dbe7e2-1343-4794-a17d-ac123aa0776c/Naman_Tiwariwithout_Photo_latest.pdf";
    return (
        // <a href={test} target="_blank" 
        // rel="noreferrer" download="true">Click Here</a>
        // <CCard>
        //     <CCardHeader component="h5">File For Everyone</CCardHeader>
        <>
            {fileDataArr ? <ViewFileComponent title="Files For Everyone" fileDataArr={fileDataArr} />:<p>No Files to Show</p>}
        </>
    );
}