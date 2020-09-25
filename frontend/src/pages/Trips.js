import React, {Component} from 'react';
import { Redirect } from "react-router-dom";
import {
  Tabs,
} from 'antd';

import './Trips.css';
import TripsOffloading from './TripsOffloading';
import TripsLoading from './TripsLoading';

const { TabPane } = Tabs;

class WholeTrip extends Component {

  constructor(props){
    super(props);
    this.state = {
      redirect:false,
    }
  }

  componentDidMount(){
    if (sessionStorage.getItem("user")) {
      console.log("user is authenticated, call user feed")
    } else {
      this.setState({redirect:true})
    }
  }

  render(){
    if (this.state.redirect) {
      return (<Redirect to={"/login"} />)
    }
    return (
      <div className="trips col-md-5 m-auto" >
        <div className = 'card card-body mt-5'>
          <Tabs type="card" defaultActiveKey="1" centered>
            <TabPane tab="Start Trip" key="1">
              <TripsLoading />
            </TabPane>
            <TabPane tab="End Trip" key="2">
              <TripsOffloading  />
            </TabPane>
          </Tabs>
        </div>
      </div>
    );
  }
}
export default WholeTrip;
