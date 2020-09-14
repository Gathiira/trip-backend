import React, { useState } from 'react';
import {
  Form,
  Input,
  DatePicker,
  InputNumber,
} from 'antd';
  
const Trips = () => {
    const [componentSize, setComponentSize] = useState('default');
  
    const onFormLayoutChange = ({ size }) => {
      setComponentSize(size);
    };
    return (
        <>
            <Form labelCol={{span: 4,}} wrapperCol={{span: 14,}} layout="horizontal" 
            initialValues={{ size: componentSize,}} onValuesChange={onFormLayoutChange}
            size={componentSize} >
            <Form.Item label="Trip name">
                <Input />
            </Form.Item>
            <Form.Item label="Buying Price per kg">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Total Weight bought">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Total Loading Cost">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Departure Date">
                <DatePicker />
            </Form.Item>
            <Form.Item label="Selling Price per kg">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Total Weight sold">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Offloading cost">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Selling Date">
                <DatePicker />
            </Form.Item>
            <Form.Item label="Transport Cost">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Clearance Cost">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Broker Expenses">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Comment">
                <Input />
            </Form.Item>
            </Form>
        </>
        );
}

export default Trips;