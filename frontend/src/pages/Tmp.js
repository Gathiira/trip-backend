import { Table } from 'antd';

import React from 'react';

class Tmp extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      tripsList:[],
      columns: [
        {
          title: 'Trip',
          width: 100,
          dataIndex: 'title',
          key: 'name',
          fixed: 'left',
        },
        {
          title: 'Date',
          width: 100,
          dataIndex: 'created_on',
          key: 'age',
        },
        {
          title: 'Price/KG',
          dataIndex: 'loading',
          key: '1'
        },
        {
          title: 'Column 2',
          dataIndex: 'address',
          key: '2'
        },
        {
          title: 'Column 3',
          dataIndex: 'address',
          key: '3'
        },
        { title: 'Column 4', dataIndex: 'address', key: '4' },
        { title: 'Column 5', dataIndex: 'address', key: '5' },
        { title: 'Column 6', dataIndex: 'address', key: '6' },
        { title: 'Column 7', dataIndex: 'address', key: '7' },
        { title: 'Column 8', dataIndex: 'address', key: '8' },
        {
          title: 'Profit Margin',
          key: 'operation',
          fixed: 'right',
          width: 100,
        },
      ],
    }
  }
  componentWillMount(){
    this.fetchTrips()
  }

  fetchTrips(){
    fetch('http://localhost:8000/api/trip/')
    .then(response => response.json())
    .then(data =>
      this.setState({
        tripsList:data
      })
    )
  }

  render (){
       return (
          <Table columns={this.state.columns} dataSource={this.state.tripsList} scroll={{ x: 1300 }} />
       )
  }
}

export default Tmp;




// const data = [
//   {
//     key: '1',
//     name: 'John Brown',
//     age: 32,
//     address: 'New York Park',
//   },
//   {
//     key: '2',
//     name: 'Jim Green',
//     age: 40,
//     address: 'London Park',
//   },
// ];
