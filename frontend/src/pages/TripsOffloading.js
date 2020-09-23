import React, { Component } from 'react';
import axios from 'axios';

import OffloadingForm from './OffloadingForm';

class TripsLoading extends Component {

  constructor(props){
    super(props);
    this.state = {trips:[],};
  }


  componentDidMount() {
    let initialTrips = [];
    axios.get("http://localhost:8000/api/loading/")
    .then(res => {
      res.data.map((trip,id) => {
        initialTrips.push(trip.id)
        return trip
      });
      this.setState({
          trips: initialTrips,
      });
    })
    .catch((err) => {
      console.log(err)
    })
  }
  render(){
    return (
      <div>
        <OffloadingForm trips={this.state.trips} />
      </div>
    )
  }
}

export default TripsLoading;
