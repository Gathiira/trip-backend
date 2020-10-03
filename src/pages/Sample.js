import React, { Component } from 'react';
import { ApiCall } from './ApiCall';

import './Sample.css';

class Sample extends Component {

    constructor(props) {
        super(props)

        this.state = {
            data:[],
            selected:'',
            trips:[],
            loaded:false,
        }

        this.renderOptions = this.renderOptions.bind(this)
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
        ApiCall("loading/",'').then(result =>{
            this.setState({data:result.data});
        })
        .catch((err) => {
            console.log(err);
        })
    }

    renderOptions () {
        return (
            <>
            <option key={0.1}> Select trip to display</option>
            {this.state.data && this.state.data.length > 0
                ? this.state.data.map((trip, id )=> {
                    return <option key={id}>{trip.id}</option>
                    })
                : "Loading..."}
            </>
        )
    }

    handleChange(event) {
        this.setState({selected: event.target.value}); 
        
        
        ApiCall("loading/"+event.target.value +"/",'')
        .then(result =>{
            this.setState({trips:result.data});
            this.setState({loaded:true})
            console.log(this.state.trips);
        })
        .catch((err) => {
            console.log(err);
        })
    }

    handleSubmit(event) {
        event.preventDefault();

        ApiCall("loading/"+this.state.selected +"/",'')
        .then(result =>{
            this.setState({trips:result.data});
            this.setState({loaded:true})
            console.log(this.state.trips);
        })
        .catch((err) => {
            console.log(err);
        })
    }
    

    render() {
        return (
            <>
            <div className='trip container'>
                <div>
                    <form onSubmit={this.handleSubmit}>
                        <label>Select A trip to display Information</label>        
                        <div className="trip__select">
                            <div className="trip__selectDropdown">
                                <select value={this.state.value} onChange={this.handleChange}>
                                    {this.renderOptions()}
                                </select>
                            </div>
                            <div className="trip__selectSubmit">
                                <input type="submit" value="Submit" />
                            </div>
                        </div>
                    </form>
                </div>
                {this.state.loaded && (
                    <ListContent trips={this.state.trips}/>
                )}
            </div>
            </>
        );
    }
}

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
            trip.trip_offloading['selling_price_per_kg'] = 0
            trip.trip_offloading['broker_expenses'] = 0
            trip.trip_offloading['comment'] = 'Bado mzigo hijauzwa'
            trip.trip_offloading['offloading_cost'] = 0
            trip.trip_offloading['profit_margin'] = 0
            trip.trip_offloading['selling_date'] = 0
            trip.trip_offloading['total_expenses'] = 0
            trip.trip_offloading['total_selling_price'] = 0
            trip.trip_offloading['total_weight_sold'] = 0
            trip.trip_offloading['transport_cost'] = 0
        }

        return (
            <div>
                <div key={trip['id']}>
                    <div className="trip__details">  
                        <div className="trip__detailsLoading">
                            <div className="trip__detailsMore__title">
                                <h6>LOADING DETAILS</h6>
                            </div>
                            <div>
                                <h6>Buying price: <span>{trip['buying_price_per_kg']}</span></h6>
                            <h6>Weight bought: <span>{trip['total_weight_bought']}</span></h6>
                                <h6>Total buying price: <span>{trip['total_buying_price']}</span></h6>
                                <h6>Loading cost: <span>{trip['loading_cost']}</span></h6>
                                <h6>Departure date: <span>{trip['departure_date']}</span></h6>
                                <hr />
                                <h6><span>{trip['comment']}</span></h6>
                            </div>
                        </div>
                        <div className="trip__detailsOffloading">
                            <div className="trip__detailsMore__title">
                                <h6>OFFLOADING DETAILS</h6>
                            </div>
                            <div>
                                <h6>Selling price: <span>{trip.trip_offloading.selling_price_per_kg}</span></h6>
                                <h6>Weight sold: <span>{trip.trip_offloading.total_weight_sold}</span></h6>
                                <h6>Total selling price: <span>{trip.trip_offloading.total_selling_price}</span></h6>
                                <h6>Offloading cost: <span>{trip.trip_offloading.offloading_cost}</span></h6>
                                <h6>Selling date: <span>{trip.trip_offloading.selling_date}</span></h6>
                                <hr />
                                <h6><span>{trip.trip_offloading.comment}</span></h6>
                            </div>
                        </div>
                    </div>
                    <div className="trip__details">
                    <div className="trip__detailsMore">
                        <div className="trip__detailsMore__title">
                            <h6>MORE DETAILS</h6>
                        </div>
                        <div className="trip__detailsMore__body">
                            <h6>Transport Cost: <span>{trip.trip_offloading.transport_cost}</span></h6>
                            <h6>Clearance Cost: <span>{trip.trip_offloading.clearance_cost}</span></h6>
                            <h6>Broker Expense: <span>{trip.trip_offloading.broker_expenses}</span></h6>
                            <hr />
                            <h6>Total Expense: <span>{trip.trip_offloading.total_expenses}</span></h6>
                        </div>
                        
                    </div>
                    <div className="trip__shares">
                        <div className="trip__detailsMore__title">
                            <h6>SHARES DETAILS</h6>
                        </div>
                        <div>
                            <h6>Profit Margin: <span>{trip.trip_offloading.profit_margin}</span></h6>
                            <hr />
                            <h6>Duncan share: <span>0</span></h6>
                            <h6>Martin share: <span>0</span></h6>
                            <h6>Ken share: <span>0</span></h6>
                            <h6>Jose share: <span>0</span></h6>
                        </div>
                    </div>
                </div>
                </div>
            </div>
        )
    }
}


export default Sample;