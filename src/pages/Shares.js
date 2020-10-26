import React, { useEffect, useState } from 'react'

function Shares(props) {

  const [data, setData] = useState([])
  const [input, setInput] = useState({
    offloading:'1',
    user: "",
  })
  const [shares, setShares] = useState([])
  const [user, setUser] = useState([])


  useEffect(() => {
    const getData = async() => {
      // await fetch('http://127.0.0.1:8000/api/loading')
      await fetch('https://smokin-ace.herokuapp.com/api/loading')
      .then(resp => resp.json())
      .then(data => {
        setData(data)
      })
      .catch(err =>{
        console.log(err);
      })
    }

    getData();
  }, [])

  useEffect(() => {
    const getShares = async() => {
      // await fetch('http://127.0.0.1:8000/api/shares')
      await fetch('https://smokin-ace.herokuapp.com/api/shares')
      .then(resp => resp.json())
      .then(data => {
        setShares(data)
      })
      .catch(err =>{
        console.log(err);
      })
    }

    getShares();
  }, [input])

  useEffect(() => {
    const getUser = async() => {
      // await fetch('http://127.0.0.1:8000/account/users',{
        await fetch('https://smokin-ace.herokuapp.com/account/users',{
        headers: {
          'Authorization': `token ${sessionStorage.getItem('token')}`
        }
      })
      .then(resp => resp.json())
      .then(data => {
        setUser(data)
      })
      .catch(err =>{
        console.log(err);
      })
    }
    getUser();
  }, [])

  let optionItems = data.map((trip,id) =>
    <option key={id} value={trip.id}>{trip.title}</option>
  )

  let userName = user.map((user, id)=>(
    <option key={id} value={user.id}>{user.username}</option>
  ))

  const handleChange = (event) => {
    const value = event.target.value;
    setInput({
      ...input,
      [event.target.name]: value
    });
  }

  const handleSubmit = async(event) => {
    event.preventDefault()

    // fetch('http://localhost:8000/api/shares/', {
      fetch('https://smokin-ace.herokuapp.com/api/shares/', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(input),
    })
    .then(resp =>resp.json())
    .catch((err) => {
      // setState({redirect:false})
      console.log(err);
    })
  }

  const renderTable = shares.map((share,id) => 
    <tr key={id}>
      <td>{share.offloading}</td>
      <td>{share.name.username }</td>
      <td>{share.name.percentage }</td>
      <td>{share.profit_share}</td>
    </tr>
  )

  return (
    <div className='share container'>
      <div className="trips col-md m-auto" >
        <div className = 'card card-body mt-5'>
          <h3>Add shareholders to a particular Trip</h3>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Trip</label>
                <select
                  name="offloading"
                  value={input.offloading}
                  onChange={handleChange}>
                  {optionItems}
                </select>
            </div>
            <div className="form-group">
              <label>Member</label>
                <select
                  name="user"
                  value={input.user}
                  onChange={handleChange}>
                  {userName}
                </select>
            </div>
            <button className="btn btn-primary" type="submit">Add</button>
          </form>
          <br />
          <div>
            <table className="table">
              <tbody>
                <tr>
                  <th>Trip No.</th>
                  <th>Name</th>
                  <th>Percentage</th>
                  <th>Profit</th>
                </tr>
                {renderTable}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Shares;
