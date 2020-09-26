import React, {Component} from 'react';
import { Redirect } from "react-router-dom";
import {PostData} from './PostData';

import {
  Tabs,
} from 'antd';

import './Trips.css';
import TripsOffloading from './TripsOffloading';
import TripsLoading from './TripsLoading';

const { TabPane } = Tabs;

class WholeTrip extends Component {
  _isMounted = false;

  constructor(props){
    super(props);
    this.state = {
      redirect:false,
      is_staff:false,
    }
  }

  componentDidMount(){
    this._isMounted = true;

    PostData('user','').then((resp) =>{
      if (this._isMounted) {
        this.setState({is_staff:resp.data.is_staff});
      }
    }).catch((err) =>{
      alert('unauthorised access')
      this.setState({is_staff:false})
    })

    if (sessionStorage.getItem("user")) {
      
    } else {
      this.setState({redirect:true})
    }
  }

  componentWillUnmount() {
    this._isMounted = false;
  }

  renderElement(){
   if(this.state.is_staff)
      return (
            <Tabs type="card" defaultActiveKey="1" centered>
              <TabPane tab="Start Trip" key="1">
                <TripsLoading />
              </TabPane>
              <TabPane tab="End Trip" key="2">
                <TripsOffloading  />
              </TabPane>
            </Tabs>
    );
   return (<h1>Oh pliss!!!!!! stop</h1>);
  }

  render(){
    if (this.state.redirect) {
      return (<Redirect to={"/login"} />)
    }

    return (
      <>
        <div className="trips col-md-5 m-auto" >
          <div className = 'card card-body mt-5'>
            { this.renderElement() }
          </div>
        </div>
      </>
    );
  }
}
export default WholeTrip;
