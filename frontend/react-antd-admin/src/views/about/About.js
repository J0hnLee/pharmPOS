import React from 'react';

const About = props => {
	return (
		<div className="shadow-radius">
			<h1 style={styles.title}>简介</h1>
			<p>React-Antd-Admin，一個 JavaScript 應用，項目由業界最優秀的 React 應用開發工具 create-react-app 初始化創建， 搭配 Antd 開箱即用的高質量 React 組件，非常適合後台產品。 </p>
			<p>React-Antd-Admin 同時也是個很好的前端腳手架學習示例，如果你在學習 React 或即將學習 React，它應該可以做為教程給你一些幫助。如果你準備使用 React 全家桶開發應用，它能夠快速給你提供項目腳手架，為你節省前期部分工作。讓我們一起享受整個 React 生態圈和工具鏈帶來的愉悅開發體驗。 </p>
			<p>在開始之前，推薦先學習 React、 ES2015、ES6、Node.js、Webpack 等知識，並正確安裝和配置了 Node.js 環境。 </p>
			<h1 style={styles.title}>技術論壇</h1>
			<ul style={styles.list}>
				<li>
					<a href="https://facebook.github.io/create-react-app/docs/getting-started" target="_blank" rel="noopener noreferrer">
						Create React App
					</a>
				</li>
				<li>
					<a href="https://ant.design/index-cn" target="_blank" rel="noopener noreferrer">
						Ant Design
					</a>
				</li>
				<li>
					<a href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
						React
					</a>
				</li>
				<li>
					<a href="https://reacttraining.com/react-router/" target="_blank" rel="noopener noreferrer">
						React-Router
					</a>
				</li>
				<li>
					<a href="https://react-redux.js.org" target="_blank" rel="noopener noreferrer">
						React-Redux
					</a>
				</li>
				<li>
					<a href="https://www.webpackjs.com" target="_blank" rel="noopener noreferrer">
						Webpack
					</a>
				</li>
				<li>
					<a href="http://es6.ruanyifeng.com" target="_blank" rel="noopener noreferrer">
						ECMAScript 6
					</a>
				</li>
				<li>
					<a href="https://babeljs.io" target="_blank" rel="noopener noreferrer">
						Babel
					</a>
				</li>
			</ul>
			<h1 style={styles.title}>Github</h1>
			<ul style={styles.list}>
				<li>
					<a href="https://github.com/chenjun1127/react-antd-manager" target="_blank" rel="noopener noreferrer">
						Github
					</a>
				</li>
			</ul>
			<h1 style={styles.title}>thanks</h1>
			<ul style={styles.list}>
				<li>
					<a href="https://facebook.github.io/create-react-app/docs/getting-started" target="_blank" rel="noopener noreferrer">
						Create React App
					</a>
				</li>
				<li>
					<a href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
						React
					</a>
				</li>
				<li>
					<a href="https://ant.design/index-cn" target="_blank" rel="noopener noreferrer">
						Ant Design
					</a>
				</li>
			</ul>
			<p>
				welcome{' '}
				<a href="https://github.com/chenjun1127/react-antd-manager" target="_blank" rel="noopener noreferrer">
					star
				</a>{' '}
				和{' '}
				<a href="https://github.com/chenjun1127/react-antd-manager" target="_blank" rel="noopener noreferrer">
					watch
				</a>{' '}
				支持
			</p>
		</div>
	);
};

const styles = {
	title: {
		color: '#333'
	},
	list: {
		padding: 0,
		marginLeft: '40px',
		lineHeight: '2.2em'
	}
};

export default About;
