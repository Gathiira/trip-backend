import React, {Component} from 'react';
import {
  Form,
  Select,
  Input,
  Button,
  DatePicker,
  InputNumber,
  Tabs,
} from 'antd';

import axios from "axios";


const { TabPane } = Tabs;

const { TextArea } = Input;

const tailLayout = {
  wrapperCol: {
    offset: 5,
    span: 5,
  },
};


class WholeTrip extends Component {
    render(){
        return (
          <div className="col-md-6 m-auto" >
            <div className = 'card card-body mt-5'>
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

class TripLoading extends Component {

  constructor(props){
    super(props);

    this.state = {};
    this.handleFormSubmit = this.handleFormSubmit.bind(this)
  }

  handleFormSubmit = event => {
  event.preventDefault();
  console.log("Pressed")

  const postObj = {
    d_date : event.target.elements.d_date.value,
    trip_name : event.target.elements.trip_name.value,
    buying_price_per_kg : event.target.elements.buying_price_per_kg.value,
    total_weight_bought : event.target.elements.total_weight_bought.value,
    loading_cost : event.target.elements.loading_cost.value,
    comment : event.target.elements.comment.value,
  }

  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
  axios.defaults.xsrfCookieName = "csrftoken";
  axios.defaults.headers = {
    "Content-Type": "application/json",
    Authorization: `Token ${this.props.token}`,
  };

     axios.post("http://localhost:8000/api/loading/", postObj)
      .then(res => {
        if (res.status === 201) {
          this.props.history.push(`/`);
        }
      })
};

  render(){
      return (
        <div className='container'>
          <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal" method="post" onSubmit={this.handleFormSubmit} >
            <Form.Item label="Departure Date">
                <DatePicker name='d_date' style={{ width: '100%' }} />
            </Form.Item>
            <Form.Item label="Trip name">
                <Input name='trip_name' style={{ width: '100%' }} />
            </Form.Item>
            <Form.Item label="Buying Price per kg">
                <InputNumber name='buying_price_per_kg' style={{ width: '100%' }} placeholder='16' />
            </Form.Item>
            <Form.Item label="Total Weight bought">
                <InputNumber name='total_weight_bought'  style={{ width: '100%' }} placeholder='28000' />
            </Form.Item>
            <Form.Item label="Loading Cost">
                <InputNumber name='loading_cost'  style={{ width: '100%' }} placeholder='41000' />
            </Form.Item>
            <Form.Item label="Comment">
                <TextArea name='comment' style={{ width: '100%' }} placeholder='Enter relevant comment' rows={4} />
            </Form.Item>
            <Form.Item  {...tailLayout}>
             <Button style={{marginRight: '10px'}} type="primary" htmlType="submit">Submit</Button>
            </Form.Item>
          </Form>
        </div>
      );
  }
}

class TripOffloading extends React.Component {
    render(){
        return (
          <div className='container'>
            <Form labelCol={{span: 5,}} wrapperCol={{span: 12,}} layout="horizontal">
              <Form.Item label="Enter the trip to Offload">
                <Select style={{ width: '100%' }} >
                  <Select.Option value="trips">Trip 1</Select.Option>
                </Select>
              </Form.Item>
              <Form.Item label="Selling Date">
                  <DatePicker style={{ width: '100%' }}  />
              </Form.Item>
              <Form.Item label="Selling Price per kg">
                  <InputNumber style={{ width: '100%' }}  placeholder='21' />
              </Form.Item>
              <Form.Item label="Total Weight sold">
                  <InputNumber style={{ width: '100%' }}  />
              </Form.Item>
              <Form.Item label="Offloading cost">
                  <InputNumber style={{ width: '100%' }}  />
              </Form.Item>
              <Form.Item label="Transport Cost">
                  <InputNumber style={{ width: '100%' }}  placeholder='80000' />
              </Form.Item>
              <Form.Item label="Clearance Cost">
                  <InputNumber style={{ width: '100%' }}  placeholder='9000' />
              </Form.Item>
              <Form.Item label="Comment">
                  <TextArea style={{ width: '100%' }} placeholder='Enter relevant comment' rows={4} />
              </Form.Item>
              <Form.Item {...tailLayout}>
                <Button style={{marginRight: '10px'}}  type="primary" htmlType="submit">
                  Submit
                </Button>
              </Form.Item>
            </Form>
          </div>
        );
    }
}

export default WholeTrip;
