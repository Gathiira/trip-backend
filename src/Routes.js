import React, {Component} from 'react';
import { Route, Switch } from 'react-router-dom';



import App from './App';
import TripRecording from './pages/TripRecording';
import Login from './pages/Login';
import MainLayout from './layout/MainLayout';

class BaseRouter extends Component {
  render(){
    return(
      <div>
        <Switch>
          <MainLayout>
            <Route component={TripRecording} path='/record' />
            <Route component={Login} path='/login' />
            <Route component={Login} path='/logout' />
            <Route component={App} exact path='/' />
          </MainLayout>
        </Switch>
      </div>
    );
  }
}

export default BaseRouter;
