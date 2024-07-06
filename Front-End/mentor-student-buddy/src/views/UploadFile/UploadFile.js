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
} from '@coreui/react'
import Swal from 'sweetalert2'
import DragDrop from './DragDropUpload/DragDrop'
import DateTime from './DateTime/DateTime'
import CategorySelection from './CategorySelection/CategorySelection'
const formData = { UserID: localStorage.getItem('B_Userid'), ShareWithEveryOne: false, toShareWith: [], tobeDelete: false, DateName: "2030-10-05", TimeName: "05:02" };
const sendData = async(fileArr) => {
  let endPoint1 = 'http://127.0.0.1:8000/Buddyshare/ShareGetApi/FileRelatedInfoSave'
  let endPoint2 = 'http://127.0.0.1:8000/Buddyshare/ShareGetApi/APIFileShare'
  var fileData = new FormData()
  fileArr.forEach(file => { fileData.append('files', file) })

  const options1={ 
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': "{{csrf_token}}"
    },
    body: JSON.stringify(formData)
  }
  const options2={ 
    method: 'POST',
    headers: {
      'X-CSRFToken': "{{csrf_token}}"
    },
    body: fileData
  }

  let result1=await fetch(endPoint1,options1);
  result1=await result1.json()
  if(result1.status==='200'){
    fileData.append('FileDataId',result1.File_Data)
    let result2=await fetch(endPoint2,options2);
    result2=await result2.json()
    if(result2.status==='200'){
      return true;
    }
    else{
      return false;
    }
  }
  else{
    return false;
  }
}

const UploadFile = () => {
  const [category, setCategory] = useState("")
  const [isDeleted, setIsDeleted] = useState(false)
  const [validated, setValidated] = useState(false)
  const [fileArr, onFileArrChange] = useState([])
  const [dateTime, onDateTimeChange] = useState(null)
  const [colleagues, setColleagues] = useState([])
  const [colleaguesVisible, setColleaguesVisible] = useState(false)
  const [studentsVisible, setStudentsVisible] = useState(false)
  const [students, setStudents] = useState([])

  //testing 
  const onFileChange = (files) => {
    onFileArrChange(files)
  }

  const predicateValidity = () => {
    if ((category === "2") && students.length === 0)
      return false;
    if ((category === "3") && colleagues.length === 0)
      return false;
    if ((category === "4") && (students.length === 0 || colleagues.length === 0))
      return false;
    if (fileArr.length === 0)
      return false;
    if (isDeleted === true && dateTime === "")
      return false
    return true;
  }
  const handleSubmit = (event) => {
    event.preventDefault()
    event.stopPropagation()
    const form = event.currentTarget
    if (predicateValidity() === false) {
      Swal.fire({
        icon: 'error',
        title: 'Incomplete data',
        text: 'Kindly fill all the data first',
      })
      return;
    }
    if (form.checkValidity() === false) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Some inputs are may be wrong!',
      })
    }
    else {
      if (dateTime != null) {
        formData.DateName = dateTime.getFullYear() + "-" + (dateTime.getMonth() + 1) + "-" + dateTime.getDate()
        formData.TimeName = dateTime.toLocaleTimeString('en-GB', { hour: "numeric", minute: "numeric" });
      }
      // console.log(dateTime);
      formData.tobeDelete = isDeleted;
      const users = []
      students.forEach(user => user.hasOwnProperty('value') && users.push(user.value))
      colleagues.forEach(user => user.hasOwnProperty('value') && users.push(user.value))
      // console.log(users);
      if (users.length !== 0)
        formData.toShareWith = users.toString();
      if (category === "1") {//everyone
        formData.ShareWithEveryOne = true
        formData.toShareWith = ","
      }
      console.log(formData);
      
      Swal.fire({
        title: 'Are you sure?',
        text: "You want to save the files?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirm!'
      }).then((result) => {
        if (result.isConfirmed) {
          sendData(fileArr) && Swal.fire(
            'Success!',
            'Successfully received the data',
            'success'
          ).then((result) => {
            if (result.isConfirmed)
              window.location.reload();
          })

        }
      })
    }
    setValidated(true)
  }

  useEffect(() => {
    if (category === "2" || category === "4") {
      setStudentsVisible(true);
    }
    else {
      setStudents([])
      setStudentsVisible(false);
    }
    if (category === "3" || category === "4") {
      setColleaguesVisible(true)
    }
    else {
      setColleagues([])
      setColleaguesVisible(false);
    }
  }, [category])

  useEffect(() => {
    if (isDeleted === false) {
      formData.TimeName = "05:02";
      formData.DateName = "2030-10-05";
      onDateTimeChange(null);
    }
    if (isDeleted === true && dateTime == null) {
      onDateTimeChange("");
    }
  }, [isDeleted, dateTime])
  const handleSelectCategoryChange = (e) => {
    setCategory(e.target.value)
  }
  return (
    <CForm
      className="row g-3 needs-validation"
      noValidate
      validated={validated}
      onSubmit={handleSubmit}
    >
      <CRow>
        {/* share with */}
        <CCol md={6} className="position-relative">
          <CFormLabel htmlFor="validationTooltip01">To Share With:</CFormLabel>
          <CFormSelect id="validationTooltip02" value={category} onChange={handleSelectCategoryChange} required>
            <option defaultValue hidden value="">
              Select category
            </option>
            <option value="1">Everyone</option>
            <option value="2">Select Students</option>
            <option value="3">Select Colleagues</option>
            <option value="4">Custom</option>
          </CFormSelect>
          <CFormFeedback tooltip invalid>
            Please provide a valid category.
          </CFormFeedback>
          <CFormFeedback tooltip valid>
            Looks Good!
          </CFormFeedback>
        </CCol>
        {/* to delete */}
        <CCol md={2} className="position-relative">
          <CFormLabel htmlFor="validationTooltip01"></CFormLabel>
          <CFormSwitch label="To Delete?" id="formSwitchCheckDefault" onChange={() => { setIsDeleted(!isDeleted) }} />
        </CCol>
        {/* date and time selection */}
        <CCol md={3} className="position-relative">
          <CFormLabel htmlFor="validationTooltip01"></CFormLabel>
          {isDeleted && <DateTime onDateTimeChange={(dateTime) => onDateTimeChange(dateTime)} />}
        </CCol>
      </CRow>

      <CRow>
        {/* select students */}
        <CCol md={6} className="position-relative">
          {studentsVisible && <CategorySelection selected={students} setSelected={setStudents} name="Students" />}
        </CCol>
      </CRow>



      <CRow>
        {/* select colleagues */}
        <CCol md={6} className="position-relative">
          {(colleaguesVisible) && <CategorySelection selected={colleagues} setSelected={setColleagues} name="Colleagues" />}
        </CCol>
      </CRow>

      {/* uploading files */}
      <CCol md={12} className="d-flex justify-content-center">
        <CCard className="mb-3">
          <DragDrop onFileChange={(files) => onFileChange(files)} />
        </CCard>
      </CCol>

      <CRow>
        <CCol md={12} className="d-flex  justify-content-center">
          <CButton color="info" type="submit">
            Submit
          </CButton>
        </CCol>
      </CRow>
    </CForm>
  )
}
export default UploadFile