import React from 'react';
import {
  Form,
  Input,
  Button,
  DatePicker,
  InputNumber,
} from 'antd';

const { TextArea } = Input;

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 8,
  },
};


class WholeTrip extends React.Component {
    render(){
        return (
            <div className="container">
                <div id='task-container'>
                    <div id='form-wrapper'>
                      <Trips />
                      <Loading />
                      <Offloading />
                      <TripInfo />
                    </div>
                </div>
            </div>
        );
    }
}

class Trips extends React.Component {
    render(){
        return (
          <div>
            <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal">
            <Form.Item label="Trip name">
                <Input />
            </Form.Item>
            <Form.Item label="Date">
                <DatePicker />
            </Form.Item>
            <Form.Item label="Comment">
                <TextArea rows={4} />
            </Form.Item>
            <Form.Item {...tailLayout}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
            </Form>
          </div>
        );
    }
}

class Loading extends React.Component {
    render(){
        return (
            <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal">
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
            <Form.Item label="Comment">
                <TextArea rows={4} />
            </Form.Item>
            <Form.Item {...tailLayout}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
            </Form>
        );
    }
}

class Offloading extends React.Component {
    render(){
        return (
            <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal">
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
            <Form.Item label="Comment">
                <TextArea rows={4} />
            </Form.Item>
            <Form.Item {...tailLayout}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
            </Form>
        );
    }
}


class TripInfo extends React.Component {
    render(){
        return (
            <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal">
            <Form.Item label="Transport Cost">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Clearance Cost">
                <InputNumber />
            </Form.Item>
            <Form.Item label="Comment">
                <TextArea rows={4} />
            </Form.Item>
            <Form.Item {...tailLayout}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
            </Form>
        );
    }
}


export default WholeTrip;
