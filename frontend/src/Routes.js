import React from 'react';
import { Route, Switch } from 'react-router-dom';



import TripsTable from './pages/TripsTable';
import WholeTrip from './pages/Trips'
import Login from './pages/Login';


const BaseRouter = () => (
  <div>
      <Switch>
        <Route component={WholeTrip} path='/trip' />
        <Route component={Login} path='/login' />
        <Route component={Login} path='/logout' />
        <Route component={TripsTable} exact path='/' />
      </Switch>
  </div>
)

export default BaseRouter;
