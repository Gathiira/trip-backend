import React from 'react';

import { Layout } from 'antd';
import {
Link
} from "react-router-dom";

import { Navbar,Nav,NavDropdown } from 'react-bootstrap';


const { Content, Footer } = Layout;


const LayoutWithRoute = ({ children }) => {
  return (
    <Layout className="layout">
      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Navbar.Brand style={{ padding: '0 50px' }}  href="/">SMOKIN' ACE</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="navbar-nav ml-auto mt-2 mt-lg-0">
            <Link className='nav-link' to="/">Home</Link>
            <Link className='nav-link' to="/login">Login</Link>
            <Link className='nav-link' to="/logout">Logout</Link>
            <NavDropdown style={{ padding: '0 50px 0 0' }} title="More" id="collasible-nav-dropdown">
              <NavDropdown.Item ><Link to="/">Shares</Link></NavDropdown.Item>
              <NavDropdown.Item ><Link to="/trip">Record</Link></NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <Content style={{ padding: '0 20px' }}>
        <div className="container-fluid">
          {children}
        </div>
      </Content>
      <Footer className='text-center'>©2020</Footer>
    </Layout>
  );
};

export default LayoutWithRoute;
