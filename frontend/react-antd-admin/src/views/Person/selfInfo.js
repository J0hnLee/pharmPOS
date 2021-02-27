import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles((theme) => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: '25ch',
    },
  },
}));

export default function MultilineTextFields() {
  const classes = useStyles();
  const [value, setValue] = React.useState('Controlled');

  const handleChange = (event) => {
    setValue(event.target.value);
  };
  
  fetch( 'http://127.0.0.1:5000/pts', {method: "GET"}) /*設定使用GET*/
    .then(res => res.json()) 
    .then(data => {
      console.log('ha');
      /*接到request data後要做的事情*/
    })
    .catch(e => {
        /*發生錯誤時要做的事情*/
        console.log('nononon');
    })
  


  return (
    <form className={classes.root} noValidate autoComplete="off">
      <div>
        <TextField
          id="standard-multiline-flexible"
          label="姓名"
          multiline
          rowsMax={4}
          value={value}
          onChange={handleChange}
        />
        <TextField
          id="standard-textarea"
          label="身分證字號"
          placeholder="Placeholder"
          multiline
        />
        <TextField
          id="standard-multiline-static"
          label="醫院名稱＆代號"
          multiline
          rows={4}
          defaultValue="Default Value"
        />
      </div>
      <div>
        <TextField
          id="filled-multiline-flexible"
          label="第幾次處方"
          multiline
          rowsMax={4}
          value={value}
          onChange={handleChange}
          variant="filled"
        />
        <TextField
          id="filled-textarea"
          label="慢籤or一般籤"
          placeholder="Placeholder"
          multiline
          variant="filled"
        />
        <TextField
          id="filled-multiline-static"
          label="過去病史"
          multiline
          rows={4}
          defaultValue="Default Value"
          variant="filled"
        />
      </div>
      <div>
        <TextField
          id="outlined-multiline-flexible"
          label="主訴＆ICD10"
          multiline
          rowsMax={4}
          value={value}
          onChange={handleChange}
          variant="outlined"
        />
        <TextField
          id="outlined-textarea"
          label="Multiline Placeholder"
          placeholder="Placeholder"
          multiline
          variant="outlined"
        />
        <TextField
          id="outlined-multiline-static"
          label="備註"
          multiline
          rows={4}
          defaultValue="Default Value"
          variant="outlined"
        />
      </div>
    </form>
  );
}
