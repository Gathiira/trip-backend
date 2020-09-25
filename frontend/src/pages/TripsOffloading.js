import React, { Component } from 'react';
import { ApiCall } from './ApiCall';

import OffloadingForm from './OffloadingForm';

class TripsLoading extends Component {

  constructor(props){
    super(props);
    this.state = {trips:[],};
  }


  componentDidMount() {
    let initialTrips = [];
    ApiCall("loading/",'')
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
