import React from 'react';

import { Layout, Menu } from 'antd';
import {
Link
} from "react-router-dom";


const { Header, Content, Footer } = Layout;


const LayoutWithRoute = ({ children }) => {
  return (
    <Layout className="layout">
      <Header>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
          <Menu.Item key="0">Welcome</Menu.Item>
          <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
          <Menu.Item key="2"><Link to="/login">Login</Link></Menu.Item>
          <Menu.Item key="3"><Link to="/logout">Logout</Link></Menu.Item>
          <Menu.Item key="4"><Link to="/trip">Start Trip</Link></Menu.Item>
        </Menu>
      </Header>
      <Content style={{ padding: '0 50px' }}>
        <div><br/></div>
        <div className="site-layout-content">{children}</div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>©2020</Footer>
    </Layout>
  );
};

export default LayoutWithRoute;
