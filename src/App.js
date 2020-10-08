import React from 'react';
import {Redirect } from "react-router-dom";

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import HomePage from './pages/HomePage';


class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      redirect:false,
    }
  }

  UNSAFE_componentWillMount(){
    if (sessionStorage.getItem("user")) {
      
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
        <HomePage />
      </div>
    )
  }
}

export default App;
