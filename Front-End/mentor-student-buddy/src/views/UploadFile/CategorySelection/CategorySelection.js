/* eslint-disable prettier/prettier */
/* eslint-disable react/prop-types */
import { CSpinner } from '@coreui/react';
import React, { useState, useEffect } from 'react'
import MultiSelectInput from '../MultiSelectInput/MultiSelectInput'
const CategorySelection = ({selected,setSelected,name}) => {
    let endPoint = 'http://127.0.0.1:8000/Buddyshare/ShareGetApi/getAllusers'
    const [users, setUsers] = useState([])
    useEffect(() => {
        fetch(endPoint)
            .then(response => response.json())
            .then(data => setUsers(data));
      }, [endPoint])
      let userArr=[];
    users.forEach(user => {
        if(name==="Students"){
            user.usertype==="Student" && userArr.push({label:user.name+"("+user.u_ID+")",value:user.B_Userid});
        }
        if(name==="Colleagues"){
            user.usertype==="Teacher" && userArr.push({label:user.name+"("+user.u_ID+")",value:user.B_Userid});
        }
    });
    return (
        <>
        {users.length!==0 ? <MultiSelectInput options={userArr} selected={selected} setSelected={setSelected} name={name} /> : <CSpinner className="spinner-border text-info"/>}
        </>
    );
}
export default CategorySelection