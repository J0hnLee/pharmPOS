import React, { useState } from 'react';
import { Select, Row, Col, TreeSelect } from 'antd';

const { Option } = Select;
const treeData = [
	{
		title: '嬰品',
		key: '嬰品',
		value: '440000',
		children: [
			{
				title: '奶嘴',
				value: '奶嘴',
				key: '440300',
				children: [
					{
						title: 'chicco',
						value: 'chicco',
						key: '440304'
					},
					{
						title: 'mamaway',
						value: 'mamaway',
						key: '440305'
					},
					{
						title: '貝親',
						value: '貝親',
						key: '440306'
					}
				]
			},
			{
				title: 'test1',
				value: 'test1',
				key: '440100',
				children: [
					{
						title: 'test2',
						value: 'test2',
						key: '440103'
					},
					{
						title: 'test3',
						value: 'test3',
						key: '440104'
					},
					{
						title: 'test4',
						value: 'test4',
						key: '440105'
					}
				]
			}
		]
	},
	{
		title: 'test5',
		value: 'test5',
		key: '430000',
		children: [
			{
				title: 'test6',
				value: 'test6',
				key: '430100'
			},
			{
				title: 'test7',
				value: 'test7',
				key: '430200'
			},
			{
				title: 'test8',
				value: 'test8',
				key: '430300'
			}
		]
	}
];

const SelectDemo = () => {
	const handleChange = () => {};
	const children = (children = []) => {
		for (let i = 10; i < 36; i++) {
			children.push(<Option key={i.toString(36) + i}>{i.toString(36) + i}</Option>);
		}
		return children;
	};
	return (
		<Select mode="multiple" style={{ width: '100%' }} placeholder="Please select" onChange={handleChange} allowClear={true}>
			{children()}
		</Select>
	);
};

const SelectTreeDemo = () => {
	const [value, setValue] = useState(null);
	const onChange = (value, label, extra) => {
		console.log(label, extra);
		setValue(value);
	};

	return <TreeSelect showSearch treeCheckable style={{ width: '100%' }} value={value} dropdownStyle={{ maxHeight: 400, overflow: 'auto' }} placeholder="Please select" allowClear multiple treeDefaultExpandAll onChange={onChange} treeData={treeData} />;
};
const BasicSelect = () => {
	return (
		<div className="shadow-radius">
			<Row gutter={16}>
				<Col span={12} offset={6}>
					<h1 style={styles}>多選框</h1>
					<SelectDemo />
				</Col>
				<Col span={12} offset={6}>
					<h1 style={styles}>樹狀選擇框</h1>
					<SelectTreeDemo />
				</Col>
			</Row>
		</div>
	);
};

const styles = {
	padding: '15px 0',
	margin: 0
};

export default BasicSelect;
