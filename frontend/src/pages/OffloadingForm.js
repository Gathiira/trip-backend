import React,{ Component } from 'react';
import axios from 'axios';

class OffloadingForm extends Component {

  constructor(props){
    super(props);
    this.state = {
        trip_loading:'',
        transport_cost:'',
        selling_date:'',
        comment:'',
        clearance_cost:'',
        selling_price_per_kg:'',
        total_weight_sold:'',
        offloading_cost:'',
        broker_expenses:'',
    };
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange = e => {
    this.setState({[e.target.name]:e.target.value })
  }

  handleSubmit = e => {
    e.preventDefault()
    console.log(this.state)
    axios.post("http://localhost:8000/api/offloading/",this.state)
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
    let optionItems = this.props.trips.map((id,i) =>
        <option key={i}>{id}</option>
    );
    const {
      trip_loading,
      comment,
      total_weight_sold,
      selling_price_per_kg,
      transport_cost,
      clearance_cost,
      offloading_cost,
      selling_date,
      broker_expenses,
    } = this.state;
      return (
        <div className='load-container'>
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label> Enter the trip to Offload</label>
                <select
                  name="trip_loading"
                  value={trip_loading}
                  onChange={this.handleChange}>
                  <option>choose trip number below</option> 
                  {optionItems}
                </select>
            </div>
            <div className="form-group">
              <label> Selling Price per Kg</label>
                <input
                  type="number"
                  name="selling_price_per_kg"
                  value={selling_price_per_kg}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label> Total Weight Sold</label>
                <input
                  type="number"
                  name="total_weight_sold"
                  value={total_weight_sold}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label> Offloading Cost</label>
                <input
                  type="number"
                  name="offloading_cost"
                  value={offloading_cost}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label> Transport Cost</label>
                <input
                  type="number"
                  name="transport_cost"
                  min="10"
                  value={transport_cost}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label> Clearance Cost</label>
                <input
                  type="number"
                  name="clearance_cost"
                  min="10"
                  value={clearance_cost}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label> Broker Expense</label>
                <input
                  type="number"
                  name="broker_expenses"
                  min="10"
                  value={broker_expenses}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label> Comments</label>
                <textarea
                  type="text"
                  name="comment"
                  value={comment}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label> Selling date</label>
                <input
                  type="date"
                  name="selling_date"
                  value={selling_date}
                  onChange={this.handleChange} />
            </div>
            <button type="submit" className='btn btn-primary' value="submit">Submit</button>
          </form>
        </div>
      );
  }
}

export default OffloadingForm;
