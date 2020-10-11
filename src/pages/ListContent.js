import React, {Component} from 'react';

class ListContent extends Component {

    constructor(props) {
        super(props)

        this.state = {
            loading: true,
        }
    }

    render() {
        var trip = this.props.trips
        if (trip.trip_offloading === null){
            trip.trip_offloading = {}
        }

        return (
                <div key={trip['id']}>
                    <div className="trip__details">
                        <div className="trip__detailsLoading">
                            <div className="trip__detailsTitle">
                                <h6>LOADING</h6>
                            </div>
                            <div className="table">
                              <tr>
                                  <td>Buying price</td>
                                  <td>{trip['buying_price_per_kg']}</td>
                              </tr>
                              <tr>
                                  <td>Weight bought</td>
                                  <td>{trip['total_weight_bought']}</td>
                              </tr>
                              <tr>
                                  <td>Total price</td>
                                  <td>
                                      <strong>{trip['total_buying_price']}</strong>
                                  </td>
                              </tr>
                              <tr>
                                  <td>Loading cost</td>
                                  <td>
                                      <strong>{trip['loading_cost']}</strong>
                                  </td>
                              </tr>
                              <tr>
                                  <td>Departure date</td>
                                  <td>{trip['departure_date']}</td>
                              </tr>
                              <tr>
                                  <td>{trip['comment']}</td>
                              </tr>
                            </div>
                        </div>
                        <div className="trip__detailsOffloading">
                            <div className="trip__detailsTitle">
                                <h6>OFFLOADING</h6>
                            </div>
                            <div className="table">
                              <tr>
                                  <td>Selling price</td>
                                  <td>{trip.trip_offloading.selling_price_per_kg}</td>
                              </tr>
                              <tr>
                                  <td>Weight sold</td>
                                  <td>{trip.trip_offloading.total_weight_sold}</td>
                              </tr>
                              <tr>
                                  <td>Total price</td>
                                  <td>
                                      <strong>{trip.trip_offloading.total_selling_price}</strong>
                                  </td>
                              </tr>
                              <tr>
                                  <td>Offloading cost</td>
                                  <td>
                                      <strong>{trip.trip_offloading.offloading_cost}</strong>
                                  </td>
                              </tr>
                              <tr>
                                  <td>Selling date</td>
                                  <td>{trip.trip_offloading.selling_date}</td>
                              </tr>
                              <tr>
                                  <td>{trip.trip_offloading.comment}</td>
                              </tr>
                            </div>
                        </div>
                    </div>
                    <div className="trip__details">
                        <div className="trip__detailsMore">
                            <div className="trip__detailsTitle">
                                <h6>MORE</h6>
                            </div>
                            <div className="table">
                            <tr>
                                <td>Transport Cost</td>
                                <td><strong>{trip.trip_offloading.transport_cost}</strong></td>
                            </tr>
                            <tr>
                                <td>Clearance Cost</td>
                                <td><strong>{trip.trip_offloading.clearance_cost}</strong></td>
                            </tr>
                            <tr>
                                <td>Broker Expense</td>
                                <td><strong>{trip.trip_offloading.broker_expenses}</strong></td>
                            </tr>
                            <br />
                            <tr>
                                <td><strong>Total Expense</strong></td>
                                <td><strong>{trip.trip_offloading.total_expenses}</strong></td>
                            </tr>
                            </div>

                        </div>
                        <div className="trip__shares">
                            <div className="trip__detailsTitle">
                                <h6>SHARES</h6>
                            </div>
                            <div className="table">
                            <tr>
                                <td><strong>Profit Margin</strong></td>
                                <td><strong>{trip.trip_offloading.profit_margin}</strong></td>
                            </tr>
                            <hr />
                                {trip.trip_offloading.profits && trip.trip_offloading.profits.map((profit,key) => (
                                <tr key={key}>
                                    <td>{profit.user}'s share</td>
                                    <td>{profit.profit_share}</td>
                                </tr>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
        )
    }
}


export default ListContent;
