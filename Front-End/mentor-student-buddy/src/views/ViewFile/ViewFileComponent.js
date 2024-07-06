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
    CCardSubtitle,
    CCardBody,
    CCardText,
    CCardLink,
    CCardFooter,
    CAccordion,
    CAccordionHeader,
    CAccordionItem,
    CAccordionBody,
    CHeader,
} from '@coreui/react'

import Swal from 'sweetalert2';
export default function ViewFileComponent({ title, fileDataArr }) {
    return (
        <>
            <CCard>
                <CAccordion activeItemKey={2} >
                    <CAccordionItem itemKey={1}>
                        <CAccordionHeader><h5>{title}</h5></CAccordionHeader>
                        <CAccordionBody>
                            <>
                                {
                                    fileDataArr.map((item, index) => (
                                        <CCard key={index} style={{ margin: "10px", borderRadius: '10px', boxShadow: "rgb(143, 172, 222,0.3) 0px 0px 0px 3px", backgroundColor: "rgb(98, 172, 181, 0.3)" }} >
                                            <div className="d-flex justify-content-around" style={{ margin: "10px" }}>
                                                <CCardSubtitle className="mb-2 text-medium-emphasis">Uploaded By: {item.UserID}</CCardSubtitle>
                                                <CCardSubtitle className="mb-2 text-medium-emphasis">Date of Deletion: {item.tobeDelete ? item.TimeForDeletion.replace("T", " Time: ") : "No Expiration"}</CCardSubtitle>
                                            </div>
                                            <CCardBody>
                                                <blockquote className="blockquote mb-0">
                                                    <CRow>
                                                        {item.countImglist.map((file, index2) => (
                                                            <CCol key={index2} md={6}>
                                                                <CCard style={{ justifyContent: "center", alignItems: "center", marginBottom: "20px", boxShadow: "rgb(42, 52, 70,0.3) 0px 0px 0px 3px", backgroundColor: "rgb(77, 92, 120,0.3)" }}>
                                                                    <CCardText>{file.substring(file.indexOf("/") + 1)}</CCardText>
                                                                    <CButton shape="rounded-pill" style={{ margin: "auto", marginBottom: "5px", backgroundColor: "rgb(74, 96, 96,0.7)", border: "none" }}>
                                                                        <CCardLink target="_blank" style={{ textDecoration: "none", color: "#fff" }} href={`http://localhost:8000/media/${file}`}>View Document</CCardLink>
                                                                    </CButton>
                                                                </CCard>
                                                            </CCol>
                                                        ))}
                                                    </CRow>
                                                </blockquote>
                                            </CCardBody>
                                            <CCardFooter>
                                                <div className="d-flex justify-content-between" style={{ alignItems: "center", margin: "10px" }}>
                                                    <CCardSubtitle className="mb-2 text-medium-emphasis">Uploaded On: {item.created_at}</CCardSubtitle>
                                                    <CButton color="info" shape="rounded-pill" style={{ marginBottom: "5px" }}>
                                                        <CCardLink target="_blank" style={{ textDecoration: "none", color: "#fff" }} href={`http://localhost:8000/public/static/zip/${item.folder_id}.zip`}>Download as Zip</CCardLink>
                                                    </CButton>
                                                </div>
                                            </CCardFooter>
                                        </CCard>
                                    ))
                                }
                            </>
                        </CAccordionBody>
                    </CAccordionItem>
                </CAccordion>
            </CCard>
        </>
    )
}