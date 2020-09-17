import React from 'react';
import {
  Form,
  Select,
  Input,
  Button,
  DatePicker,
  InputNumber,
  Tabs,
} from 'antd';

const { TabPane } = Tabs;

const { TextArea } = Input;

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 8,
  },
};


class WholeTrip extends React.Component {
    render(){
        return (<div className='container'>
            <div className="card-container" >
              <Tabs type="card" defaultActiveKey="1" centered>
                <TabPane tab="Start Trip" key="1">
                  <TripLoading />
                </TabPane>
                <TabPane tab="End Trip" key="2">
                  <TripOffloading />
                </TabPane>
              </Tabs>
            </div>
            </div>
        );
    }
}

class TripLoading extends React.Component {
    render(){
        return (
          <div>
            <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal">
            <Form.Item label="Departure Date">
                <DatePicker />
            </Form.Item>
            <Form.Item label="Trip name">
                <Input />
            </Form.Item>
            <Form.Item label="Buying Price per kg">
                <InputNumber placeholder='16' />
            </Form.Item>
            <Form.Item label="Total Weight bought">
                <InputNumber placeholder='28000' />
            </Form.Item>
            <Form.Item label="Total Loading Cost">
                <InputNumber />
            </Form.Item>
          <Form.Item label="Comment">
              <TextArea placeholder='Enter relevant comment' rows={4} />
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

class TripOffloading extends React.Component {
    render(){
        return (
            <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal">
              <Form.Item label="Enter the trip to Offload">
                <Select>
                  <Select.Option value="trips">Trip 1</Select.Option>
                </Select>
              </Form.Item>
              <Form.Item label="Selling Date">
                  <DatePicker />
              </Form.Item>
              <Form.Item label="Selling Price per kg">
                  <InputNumber placeholder='21' />
              </Form.Item>
              <Form.Item label="Total Weight sold">
                  <InputNumber />
              </Form.Item>
              <Form.Item label="Offloading cost">
                  <InputNumber />
              </Form.Item>
              <Form.Item label="Transport Cost">
                  <InputNumber placeholder='80000' />
              </Form.Item>
              <Form.Item label="Clearance Cost">
                  <InputNumber placeholder='9000' />
              </Form.Item>
              <Form.Item label="Comment">
                  <TextArea placeholder='Enter relevant comment' rows={4} />
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
