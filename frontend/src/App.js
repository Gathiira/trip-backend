import React from 'react';
import { Switch,Route} from "react-router-dom";

import './App.css';
import TripsTable from './pages/TripsTable';
import Trips from './pages/Trips'
import Login from './pages/Login';
import Sample from './pages/Sample';
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
          <Route component={Trips} path='/trip' />
          <Route component={Login} path='/login' />
          <Route component={Login} path='/logout' />
          <Route component={TripsTable} exact path='/' />
        </Switch>
      </MainLayout>

    )
  }
}

export default App;
