import React, {Component} from 'react';
import {
  Tabs,
} from 'antd';

import axios from "axios";

import './Trips.css';

const { TabPane } = Tabs;

class WholeTrip extends Component {
    render(){
        return (
          <div className="container m-auto" >
            <div className = 'card card-body'>
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

    this.state = {
      departure_date:'',
      buying_price_per_kg:'',
      total_weight_bought:'',
      loading_cost:'',
      title:'',
      comment:'',

    };
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange = e => {
    this.setState({[e.target.name]:e.target.value })
  }

  handleSubmit = event => {
    event.preventDefault();
    axios.post("http://localhost:8000/api/loading/",this.state)
    .then(res => {
      console.log(res.data)
      alert("relax now, Data Captured")
    })
    .catch((err) => {
      console.log(err)
      alert(err)
    })
  };

  render(){
    const {
      title,
      departure_date,
      buying_price_per_kg,
      total_weight_bought,
      loading_cost,
      comment
    } = this.state;
      return (
        <div className='form-container'>
          <form onSubmit={this.handleSubmit}>
            <label>Title:
              <input
                type="text"
                name="title"
                value={title}
                onChange={this.handleChange} />
            </label>
            <label>Buying Price:
              <input
                type="number"
                name="buying_price_per_kg"
                value={buying_price_per_kg}
                onChange={this.handleChange} />
            </label>
            <label>Weight Bought:
              <input
                type="number"
                name="total_weight_bought"
                value={total_weight_bought}
                onChange={this.handleChange} />
            </label>
            <label>Loading Cost:
              <input
                type="number"
                name="loading_cost"
                min="100"
                value={loading_cost}
                onChange={this.handleChange} />
            </label>
            <label>Comment:
              <textarea
                type="text"
                name="comment"
                value={comment}
                onChange={this.handleChange} />
            </label>
            <label>Departure date:
              <input
                type="date"
                name="departure_date"
                value={departure_date}
                onChange={this.handleChange} />
            </label>
            <button type="submit" value="submit">Submit</button>
          </form>
        </div>
      );
  }
}

class TripOffloading extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      trip_names:[],
      offloading:{
        'transport_cost':'80000',
        'selling_date':'2020-09-09',
        'comment':'lol',
        'clearance_cost':'9000',
        'selling_price_per_kg':'10',
        'total_weight_sold':'28000',
        'offloading_cost':'4500',
        'broker_expenses':'18000',
      },
    };
  }

  componentDidMount() {
    let initialTrips = [];
    axios.get("http://localhost:8000/api/loading/")
    .then(res => {
      res.data.map((trip,id) => {
        initialTrips.push(trip.title)
        return trip
      });
      this.setState({
          trip_names: initialTrips,
      });
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // handleChange = e => {
  //   // this.setState({...this.state.offloading, e.target.name: e.target.value})
  //   this.setState({offloading:{[e.target.name]:e.target.value }});
  // }

  handleChange(name) {
    return e => {
      this.setState(({ offloading }) => ({
        offloading: { ...offloading, [name]: e.target.value }
      }));
    };
  }

  handleSubmit = e => {
    e.preventDefault()
    console.log(this.state.offloading)
    axios.post("http://localhost:8000/api/offloading/",this.state.offloading)
    .then(res => {
      console.log(res.data)
      alert("relax now, Data Captured")
    })
    .catch((err) => {
      console.log(err)
      alert(err)
    })
  }

  render(){
    let optionItems = this.state.trip_names.map((name,i) =>
        <option key={i}>{name}</option>
    );
    const {
      comment,
      total_weight_sold,
      selling_price_per_kg,
      transport_cost,
      clearance_cost,
      offloading_cost,
      selling_date,
      broker_expenses,
    } = this.state.offloading;
      return (
        <div className='form-container'>
          <form onSubmit={this.handleSubmit}>
            <label> Enter the trip to Offload:
              <select>
                {optionItems}
              </select>
            </label>
            <label>Selling Price per Kg:
              <input
                type="number"
                name="selling_price_per_kg"
                value={selling_price_per_kg}
                onChange={this.handleChange("selling_price_per_kg")} />
            </label>
            <label>Total Weight Sold:
              <input
                type="number"
                name="total_weight_sold"
                value={total_weight_sold}
                onChange={this.handleChange("total_weight_sold")} />
            </label>
            <label>Offloading Cost:
              <input
                type="number"
                name="offloading_cost"
                value={offloading_cost}
                onChange={this.handleChange("offloading_cost")} />
            </label>
            <label>Transport Cost:
              <input
                type="number"
                name="transport_cost"
                min="10"
                value={transport_cost}
                onChange={this.handleChange("transport_cost")} />
            </label>
            <label>Clearance Cost:
              <input
                type="number"
                name="clearance_cost"
                min="10"
                value={clearance_cost}
                onChange={this.handleChange("clearance_cost")} />
            </label>
            <label>Broker Expense:
              <input
                type="number"
                name="broker_expenses"
                min="10"
                value={broker_expenses}
                onChange={this.handleChange("broker_expenses")} />
            </label>
            <label>Comments:
              <textarea
                type="text"
                name="comment"
                value={comment}
                onChange={this.handleChange("comment")} />
            </label>
            <label>Selling date:
              <input
                type="date"
                name="selling_date"
                value={selling_date}
                onChange={this.handleChange("selling_date")} />
            </label>
            <button type="submit" value="submit">Submit</button>
          </form>
        </div>
      );
  }
}

export default WholeTrip;
