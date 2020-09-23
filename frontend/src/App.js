import React from 'react';
import { HashRouter as Router, Redirect } from "react-router-dom";

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MainLayout from './layout/MainLayout';
import BaseRouter from './Routes';


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
  }

  render(){
    if (this.state.redirect) {
      return (<Redirect to={"/login"} />)
    }
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
