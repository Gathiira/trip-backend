import React from 'react';
import {Redirect } from "react-router-dom";

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import TripsTable from './pages/TripsTable';
import Sample from './pages/Sample';


class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      redirect:false,
    }
  }

  UNSAFE_componentWillMount(){
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
      <div className="App">
        {/* <TripsTable /> */}
        <Sample />
      </div>
    )
  }
}

export default App;
