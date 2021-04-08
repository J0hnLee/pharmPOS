import React from 'react';
import * as classes_2 from './selfInfo.scss'
import TextField from '@material-ui/core/TextField';
import WebcamCapture from '../personInfo/imageCapture'
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { FixedSizeList } from 'react-window';
import Button from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';
import { makeStyles } from '@material-ui/core/styles';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import InputLabel from '@material-ui/core/InputLabel';
//import './flex.css'
//import Webcam from "react-webcam";
console.log('start')
console.log(classes_2)


const useStyles = makeStyles((theme) => ({
  // tag1: {
  //   flexGrow: 1,
  //   background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
  //   borderRadius: 2,
  //   border: 1,
  //   color: 'white',
  //   height: 60,
  //   padding: '0 50px',
  //   boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
  //   margin: 30,

  // },

  tag2: {
    flexGrow: 1,
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
    borderRadius: 5,
    border: 1,
    color: 'white',
    height: 80,
    padding: '0 30px',
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
    margin: 30,

  },
  tag3: {
    flexGrow: 1,
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E66 90%)',
    borderRadius: 5,
    border: 1,
    color: 'white',
    height: 80,
    padding: '0 30px',
    boxShadow: '0 3px 5px 2px rgba(205, 105, 135, .3)',
    margin: 30,

  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));


const infoHandler = () =>{

}


export default function MultilineTextFields() {
  //const classes = useStyles();
  
  

  const [value, setValue] = React.useState('Controlled');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  function renderRow(props) {
    const { index, style } = props;
  
    return (
      <ListItem button style={style} key={index}>
        <ListItemText primary={`Item ${index + 1}`} />
      </ListItem>
    );
  }
  
  // fetch( 'http://192.168.1.85:3001/:5000/pts', {method: "GET"}) /*設定使用GET*/
  //   .then(res => res.json()) 
  //   .then(data => {
  //     console.log('ha');
  //     /*接到request data後要做的事情*/
  //   })
  //   .catch(e => {
  //       /*發生錯誤時要做的事情*/
  //       console.log('nononon');
  //   });
  
  const classes = useStyles();

  // const sendMessage = ()=>{
  //   fetch( 'http://192.168.1.85:3001/:5000/pts', {method: "POST"}) /*設定使用GET*/
  //   .then(res => res.json()) 
  //   .then(data => {
  //     console.log('ha');
  //     /*接到request data後要做的事情*/
  //   })
  //   .catch(e => {
  //       /*發生錯誤時要做的事情*/
  //       console.log('nononon');
  //   });
  // }
   
  const [name, setName] = React.useState('Composed TextField');
  const handleChanges = (event) => {
    console.log("Was clicked.");
    setName(event.target.value);
    console.log(event.target.value);
    console.log(this.state.persons)
    // this.setState(
    //   this.persons.name=event.target.value
    // )
    // console.log(this.state.persons)

    
  };
  

  return (
    <div>
      <div class={classes_2.Test} ><style ></style></div>
      <button class={classes_2.Test} >hello{console.log(classes_2.Test)}</button>
      
      <div>
        <Grid container spacing={80} alignItems="center">
          <Grid item xs={3} className={classes_2.tag1}>
          <TextField 
            id="standard-textarea"
            label="姓名"
            placeholder="Placeholder"
            multiline 
            onChange={handleChanges}
            />
          </Grid>

        <Grid item xs={3} className={classes.tag2}>
          <TextField
            id="standard-textarea"
            label="身分證字號"
            placeholder="Placeholder"
            multiline />
          </Grid>
        <Grid item xs={3} className={classes.tag3}>
          <TextField
            id="standard-textarea"
            label="醫院名稱＆代號"
            placeholder="Placeholder"
            multiline />
          </Grid>
        </Grid>
        </div>
      <div>
       <div>
        <Grid container spacing={80} alignItems="center">
          <Grid item xs={3} className={classes.tag3}>
            <TextField
              id="filled-multiline-flexible"
              label="第幾次處方"
              multiline
              rowsMax={4}
              value={value}
              onChange={handleChange}
              variant="filled"
            />
          </Grid>
          <Grid item xs={3} className={classes.tag3}>
            <TextField
              id="filled-textarea"
              label="慢籤or一般籤"
              placeholder="Placeholder"
              multiline
              variant="filled"
            />
          </Grid>
          <Grid item xs={3} className={classes.tag3}>
            <TextField
              id="filled-multiline-static"
              label="過去病史"
              multiline
              rows={1}
              defaultValue="Default Value"
              variant="filled"
            />
          </Grid>
        </Grid>
         
       </div>
      
       <div>
       <Grid container spacing={80} alignItems="center">

       <Grid item xs={3} className={classes.tag3}>

         <TextField
          id="outlined-multiline-flexible"
          label="主訴＆ICD10"
          multiline
          rowsMax={1}
          value={value}
          onChange={handleChange}
          variant="outlined"
        />
        </Grid>
        <Grid item xs={3} className={classes.tag3}>
        <TextField
          id="outlined-textarea"
          label="Multiline Placeholder"
          placeholder="Placeholder"
          multiline
          variant="outlined"
        />
        </Grid>
        <Grid item xs={3} className={classes.tag3}>
         <TextField
          id="outlined-multiline-static"
          label="備註"
          multiline
          rows={1}
          defaultValue="Default Value"
          variant="outlined"
        />
        </Grid>
      </Grid>
      </div>
      <Grid container spacing={80} alignItems="center">
        <WebcamCapture />
      </Grid>
      <Grid item xs={3} >
          <Button onClick={() => { alert('clicked') }} variant="contained" color="primary"  endIcon={<Icon></Icon>}> Send</Button>
      </Grid>
    </div>
  </div>
        );
}
      
      
      