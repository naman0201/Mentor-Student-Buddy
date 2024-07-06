/* eslint-disable prettier/prettier */
/* eslint-disable react/prop-types */
import React, { useState } from "react";
import { MultiSelect } from "react-multi-select-component";
import { CFormLabel } from '@coreui/react'
const MultiSelectInput = ({ options, selected, setSelected,name }) => {
  return (
    <>
    <CFormLabel htmlFor="validationTooltip01">Select {name}:</CFormLabel>
      <MultiSelect
        options={options}
        value={selected}
        onChange={setSelected}
        labelledBy="Select..."
      />
    </>
  );
};

export default MultiSelectInput;
