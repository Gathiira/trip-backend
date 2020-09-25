import React,{Component} from 'react';
import { Layout } from 'antd';
import { Link } from "react-router-dom";
import { Navbar,Nav } from 'react-bootstrap';

const { Content, Footer } = Layout;

class MainLayout extends Component {
  render(){
    return(
      <>
        <Layout className="header">
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
              <Navbar.Brand href="/">SMOKIN' ACE</Navbar.Brand>
              <Navbar.Toggle aria-controls="responsive-navbar-nav" />
              <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="navbar-nav ml-auto mt-2 mt-lg-0">
                  <Link className='nav-link' to="/">Home</Link>
                  <Link className='nav-link' to="/trip">Record</Link>
                  <Link className='nav-link' to="/">Shares</Link>
                  {(sessionStorage.getItem("user"))?(
                    <Link className='nav-link' to="/login">Logout</Link>
                  ) : (
                    <Link className='nav-link' to="/login">Login</Link>
                  )}
                </Nav>
              </Navbar.Collapse>
            </Navbar>
        </Layout>
        <Body content={this.props.children}/>
      </>
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
