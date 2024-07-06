/* eslint-disable prettier/prettier */
/* eslint-disable react/prop-types */
import React from 'react'
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';


export default function DateTime(props) {
  const [value, setValue] = React.useState("");

  const handleChange = (newValue) => {
    setValue(newValue);
    props.onDateTimeChange(new Date(newValue));
  };
  
  function disablePrevDates(startDate) {
    const startSeconds = Date.parse(startDate);
    return (date) => {
      return Date.parse(date) < startSeconds;
    }
  }
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Stack spacing={3}>
        <DateTimePicker
        shouldDisableDate={disablePrevDates(new Date())}
          value={value}
          onChange={handleChange}
          renderInput={(params) => <TextField {...params} />}
        />
      </Stack>
    </LocalizationProvider>
  );
}
