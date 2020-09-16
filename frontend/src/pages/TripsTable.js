import React from 'react';
import { Table } from 'antd';

import './TripsTable.css';

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
    fetch('http://localhost:8000/api/trip/')
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
               <td>{trip.title}</td>
               <td>{trip.created_on}</td>
               <td>{trip.loading.buying_price_per_kg}</td>
               <td>{trip.loading.total_weight_bought}</td>
               <td>{trip.offloading.offloading_cost}</td>
               <td>{trip.tripInfo.total_expenses}</td>
               <td>{trip.tripInfo.profit_margin}</td>
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
              <th>title</th>
              <th>title</th>
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
