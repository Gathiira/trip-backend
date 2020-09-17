import React from 'react';

class TripsTable extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      tripsList:[],
    }

    this.renderTableData = this.renderTableData.bind(this)
  }
  componentWillMount(){
    this.fetchTrips()
  }

  fetchTrips(){
    fetch('http://localhost:8000/api/loading/')
    .then(response => response.json())
    .then(data =>
      this.setState({
        tripsList:data
      })
    )
  }

  renderTableData(){
    return this.state.tripsList.map((trip, index) => {//destructuring

         return (
            <tr key={trip.id}>
               <td>{trip.departure_date}</td>
               <td>{trip.title}</td>
               <td>{trip.buying_price_per_kg}</td>
               <td>{trip.total_weight_bought}</td>
               <td>{trip.loading_cost}</td>
               <td>{trip.trip_offloading.transport_cost}</td>
               <td>{trip.trip_offloading.selling_price_per_kg}</td>
               <td>{trip.trip_offloading.profit_margin}</td>
            </tr>
         )
      })
  }

  render (){
    return (
      <div>
        <h1 id='title'>Trip Information Center</h1>
        <table id='trips'>
          <thead>
            <tr>
              <th>Date</th>
              <th>Name</th>
              <th>Buying Price</th>
              <th>title</th>
              <th>title</th>
              <th>title</th>
              <th>title</th>
              <th>title</th>
            </tr>
          </thead>
           <tbody>
              <tr></tr>
              {this.renderTableData()}
           </tbody>
        </table>
     </div>
    )
  }
}

export default TripsTable;
