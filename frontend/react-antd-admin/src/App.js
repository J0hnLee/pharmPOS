import React from 'react';
import { Provider } from 'react-redux';
import { hot } from 'react-hot-loader/root';
import Router from './router';
import store from '@/redux/store';
import './assets/css/app';
import './assets/css/common';
// import PrimarySearchAppBar from './views/Person/searchBar'

class App extends React.Component {
	render() {
		return (
			<Provider store={store}>
				<Router />
			</Provider>
		);
	}
}

export default hot(App);
