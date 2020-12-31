import React, { useEffect, useState } from 'react';
import { Redirect } from "react-router-dom";

import {
  Tabs,
} from 'antd';

import './TripRecording.css';
import TripsOffloading from './TripsOffloading';
import TripsLoading from './TripsLoading';

const { TabPane } = Tabs;

function TripRecording() {

  const [user, setUser] = useState({is_staff:false})
  const [redirect, setRedirect] = useState(false)

  useEffect(() => {
    const getUser = async () => {
      await fetch("http://127.0.0.1:8000/account/user",{
      // await fetch("https://smokin-ace.herokuapp.com/account/user",{
        headers: {
          'Authorization': `token ${sessionStorage.getItem('token')}`
        }
      })
      .then((resp) => resp.json())
      .then((data) => {
        setUser({is_staff:data.is_staff})
      })
    }
    getUser();
  }, [])

  useEffect(() => {
    if (sessionStorage.getItem("user")) {

    } else {
      setRedirect(true)
    }
  },[])

  return (
    <div>
      {redirect ? (
        <Redirect to={"/login"} />
      ): (
        <div className="trips col-md-5 m-auto" >
          <div className = 'card card-body mt-5'>
            {user.is_staff && (
                <Tabs type="card" defaultActiveKey="1" centered>
                  <TabPane tab="Start Trip" key="1">
                    <TripsLoading />
                  </TabPane>
                  <TabPane tab="End Trip" key="2">
                    <TripsOffloading  />
                  </TabPane>
                </Tabs>
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export default TripRecording
