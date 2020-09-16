import React from 'react';
import { Switch,Route} from "react-router-dom";

import './App.css';
import TripsTable from './pages/TripsTable';
import WholeTrip from './pages/Trips'
import Login from './pages/Login';
import MainLayout from './layout/MainLayout';

class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {}
  }

  render(){

    return (
      <MainLayout>
        <Switch>
          <Route component={WholeTrip} path='/trip' />
          <Route component={Login} path='/login' />
          <Route component={Login} path='/logout' />
          <Route component={TripsTable} exact path='/' />
        </Switch>
      </MainLayout>

    )
  }
}

export default App;
