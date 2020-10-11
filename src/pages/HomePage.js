import React, { useState, useEffect } from 'react';
import { ApiCall } from './ApiCall';

import './HomePage.css';
import ListContent from './ListContent'

import {
  FormControl,
  Select,
  MenuItem,
  Card
} from '@material-ui/core';

function HomePage() {
  const [data, setData] = useState([])
  const [selected, setSelected] = useState('1')
  const [trips, setTrips] = useState({})
  const [loaded, setLoaded] = useState(false)

  useEffect(() => {
    const getData = async() =>{
      await ApiCall("loading/",'').then(result =>{
          setData(result.data);
      })
      .catch((err) => {
          console.log(err);
      })
    }

    getData();
  }, [])

  useEffect(() => {
    const loadData = async() =>{
      await ApiCall(`loading/${selected}/`,'')
      .then(result =>{
          setTrips(result.data);
          setLoaded(true)
      })
      .catch((err) => {
          console.log(err);
      })
    }

    loadData();
  },[selected])

  const handleChange = async (event) => {
    const sValue = event.target.value

    await ApiCall(`loading/${sValue}/`,'')
    .then(result =>{
        setTrips(result.data);
        setLoaded(true)
        setSelected(sValue)
    })
    .catch((err) => {
        console.log(err);
    })
  }

  return (
      <div className='container col-md-10'>
        <div className="trip__select">
          <div className="trip__selectTitle">
            <h3>Select Trip to display Information </h3>
          </div>
          <div className="trip__selectDropdown">
            <FormControl>
                <Select
                variant="outlined"
                value={selected}
                onChange={handleChange}>
                    {data.map((trip) => (
                      <MenuItem key={trip.id} value={trip.id}>{trip.title}</MenuItem>
                    ))}
                </Select>
            </FormControl>
          </div>
          </div>
          {loaded && (
            <Card>
              <ListContent trips={trips} />
            </Card>
          )}
      </div>
  );

};

export default HomePage;
