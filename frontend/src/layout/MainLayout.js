import React,{Component} from 'react';
import {Redirect } from "react-router-dom";
import {PostData} from '../pages/PostData';
import { Layout } from 'antd';
import { Link } from "react-router-dom";
import { Navbar,Nav } from 'react-bootstrap';

const { Content, Footer } = Layout;

class MainLayout extends Component {
  render(){
    return(
      <>
        {(sessionStorage.getItem("user"))?(
            <Header />
        ) : (
          <Layout className="header">
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
              <Navbar.Brand href="">SMOKIN' ACE</Navbar.Brand>
              <Navbar.Toggle aria-controls="responsive-navbar-nav" />
              <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="navbar-nav ml-auto mt-2 mt-lg-0">
                <Link className='nav-link' to="/">Home</Link>
                <Link className='nav-link' to="/login">Login</Link>
                </Nav>
              </Navbar.Collapse>
            </Navbar>
          </Layout>
        )}
        <Body content={this.props.children}/>
      </>
    );
  }
}
class Header extends Component {
  constructor(props){
    super(props);
    this.state = {
      redirect:false,
      is_staff:false,
      username:''
    }

    this.handleLogout = this.handleLogout.bind(this)
  }

  componentDidMount(){
    if (sessionStorage.getItem("user")) {
      console.log("user is authenticated, call user feed")

      PostData('user','').then((resp) =>{
        this.setState({is_staff:resp.data.is_staff, username:resp.data.username})
      }).catch((err) =>{
        alert('unauthorised access')
      })
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
    console.log(this.state.is_staff)

    if (this.state.redirect) {
      return (<Redirect to={"/login"} />)
    }
    return(
        <Layout className="header">
          <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand href="">SMOKIN' ACE</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
              <Nav className="navbar-nav ml-auto mt-2 mt-lg-0">
              <Link className='nav-link' >Welcome, {this.state.username}</Link>
              <Link className='nav-link' to="/">Home</Link>
              {this.state.is_staff && (
                <Link className='nav-link' to="/trip">Record</Link>
              )}
              <Link className='nav-link' to="/">Shares</Link>
              <Link className='nav-link' onClick={this.handleLogout} to="/login">Logout</Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      </Layout>
    );
  }
}

class Body extends Component {
  render(){
    return(
      <div>
      <Layout>
          <Content>
              {this.props.content}
          </Content>
          <Footer className='text-center'>©2020</Footer>
      </Layout>
      </div>
    );
  }
}

export default MainLayout;
