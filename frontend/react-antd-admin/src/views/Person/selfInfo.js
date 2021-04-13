import React from 'react';
import classes_2 from './selfInfo.module.css';
import TextField from '@material-ui/core/TextField';
import WebcamCapture from '../personInfo/imageCapture';
import Grid from '@material-ui/core/Grid';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Button from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';

//import './flex.css'
//import Webcam from "react-webcam";

const infoHandler = () => {};

export default function MultilineTextFields() {
	const [value, setValue] = React.useState('Controlled');

	const handleChange = event => {
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
	const handleChanges = event => {
		console.log('Was clicked.');
		setName(event.target.value);
		console.log(event.target.value);
		// this.setState(
		//   this.persons.name=event.target.value
		// )
		// console.log(this.state.persons)
	};

	return (
		<div>
			<div>
				<Grid container spacing={2} style={{ margin: 10 }} alignItems="center">
					<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag1}>
						<TextField id="standard-textarea" label="姓名" placeholder="Placeholder" multiline onChange={handleChanges} />
					</Grid>

					<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag2}>
						<TextField id="standard-textarea" label="身分證字號" placeholder="Placeholder" multiline />
					</Grid>
					<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag3}>
						<TextField id="standard-textarea" label="醫院名稱＆代號" placeholder="Placeholder" multiline />
					</Grid>
				</Grid>
			</div>
			<div>
				<div>
					<Grid container style={{ margin: 10 }} spacing={20} alignItems="center">
						<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag3}>
							<TextField id="filled-multiline-flexible" label="第幾次處方" multiline rowsMax={4} value={value} onChange={handleChange} variant="filled" />
						</Grid>
						<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag3}>
							<TextField id="filled-textarea" label="慢籤or一般籤" placeholder="Placeholder" multiline variant="filled" />
						</Grid>
						<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag3}>
							<TextField id="filled-multiline-static" label="過去病史" multiline rows={1} defaultValue="Default Value" variant="filled" />
						</Grid>
					</Grid>
				</div>

				<div>
					<Grid container style={{ margin: 10 }} spacing={80} alignItems="center">
						<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag3}>
							<TextField id="outlined-multiline-flexible" label="主訴＆ICD10" multiline rowsMax={1} value={value} onChange={handleChange} variant="outlined" />
						</Grid>
						<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag3}>
							<TextField id="outlined-textarea" label="Multiline Placeholder" placeholder="Placeholder" multiline variant="outlined" />
						</Grid>
						<Grid item xs={3} style={{ margin: 10 }} className={classes_2.tag3}>
							<TextField id="outlined-multiline-static" label="備註" multiline rows={1} defaultValue="Default Value" variant="outlined" />
						</Grid>
					</Grid>
				</div>
				<Grid container style={{ margin: 10 }} spacing={80} alignItems="center">
					<WebcamCapture />
				</Grid>
				<Grid item xs={3} style={{ margin: 10 }}>
					<Button
						onClick={() => {
							alert('clicked');
						}}
						variant="contained"
						color="primary"
						endIcon={<Icon></Icon>}
					>
						{' '}
						Send
					</Button>
				</Grid>
			</div>
		</div>
	);
}
