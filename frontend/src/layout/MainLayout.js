import React from 'react';

import { Layout } from 'antd';
import {
Link
} from "react-router-dom";

import { Navbar,Nav } from 'react-bootstrap';


const { Content, Footer } = Layout;


const LayoutWithRoute = ({ children }) => {
  return (
    <Layout className="layout">
      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Navbar.Brand href="/">SMOKIN' ACE</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="navbar-nav ml-auto mt-2 mt-lg-0">
            <Link className='nav-link' to="/">Home</Link>
            <Link className='nav-link' to="/trip">Record</Link>
            <Link className='nav-link' to="/">Shares</Link>
            <Link className='nav-link' to="/login">Login</Link>
            <Link className='nav-link' to="/logout">Logout</Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <Content>
          {children}
      </Content>
      <Footer className='text-center'>©2020</Footer>
    </Layout>
  );
};

export default LayoutWithRoute;
