import React, { Component } from 'react';
import axios from 'axios';

class TripsLoading extends Component {

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
        <div className='load-container'>
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label>Title</label>
                <input
                  type="text"
                  name="title"
                  value={title}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label>Buying Price per Kg</label>
                <input
                  type="number"
                  name="buying_price_per_kg"
                  value={buying_price_per_kg}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label>Total weight Bought</label>
                <input
                  type="number"
                  name="total_weight_bought"
                  value={total_weight_bought}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label>Loading Cost</label>
                <input
                  type="number"
                  name="loading_cost"
                  value={loading_cost}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label>Comment</label>
                <textarea
                  type="text"
                  name="comment"
                  value={comment}
                  onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label>Departure Date</label>
                <input
                  type="date"
                  name="departure_date"
                  value={departure_date}
                  onChange={this.handleChange} />
            </div>
            <button type="submit" className='btn btn-primary' value="submit">Submit</button>
          </form>
        </div>
      );
  }
}

export default TripsLoading;
