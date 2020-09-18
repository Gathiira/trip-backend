import React from 'react';
import { HashRouter as Router } from "react-router-dom";

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MainLayout from './layout/MainLayout';
import BaseRouter from './Routes';


class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {}
  }

  render(){

    return (
      <div className="App">
        <Router>
          <MainLayout>
            <BaseRouter />
          </MainLayout>
        </Router>
      </div>

    )
  }
}

export default App;
