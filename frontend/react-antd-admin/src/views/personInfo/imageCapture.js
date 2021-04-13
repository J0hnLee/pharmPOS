import React from 'react';
import Webcam from 'react-webcam';
import Grid from '@material-ui/core/Grid';
const WebcamCapture = () => {
	const webcamRef = React.useRef(null);
	const [imgSrc, setImgSrc] = React.useState(null);

	const capture = React.useCallback(() => {
		const imageSrc = webcamRef.current.getScreenshot({ width: 640, height: 480 });
		setImgSrc(imageSrc);
	}, [webcamRef, setImgSrc]);

	return (
		<>
			<button onClick={capture}>拍攝處方簽</button>
			<Grid>
				<Webcam audio={false} ref={webcamRef} screenshotFormat="image/jpeg" />
			</Grid>
			<Grid>{imgSrc && <img src={imgSrc} />}</Grid>
		</>
	);
};
// https://www.npmjs.com/package/react-webcam

export default WebcamCapture;
