import React from 'react';
import {Redirect } from "react-router-dom";

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import TripsTable from './pages/TripsTable';


class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      redirect:false,
    }

    this.handleLogout = this.handleLogout.bind(this)
  }

  UNSAFE_componentWillMount(){
    if (sessionStorage.getItem("user")) {
      console.log("user is authenticated, call user feed")
    } else {
      this.setState({redirect:true})
    }
  }

  handleLogout() {
    sessionStorage.setItem("user","");
    sessionStorage.clear();
    this.setState({redirect:true})
  }

  render(){
    if (this.state.redirect) {
      return (<Redirect to={"/login"} />)
    }
    return (
      <div className="App">
        <TripsTable />
        <button onClick={this.handleLogout}>Logout</button>
      </div>
    )
  }
}

export default App;
