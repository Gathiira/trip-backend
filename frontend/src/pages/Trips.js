import React, {Component} from 'react';
import {
  Tabs,
} from 'antd';

import './Trips.css';
import TripsOffloading from './TripsOffloading';
import TripsLoading from './TripsLoading';

const { TabPane } = Tabs;

class WholeTrip extends Component {

  render(){
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
