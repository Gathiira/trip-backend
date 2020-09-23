import React, {Component} from 'react'
import axios from "axios";

class Login extends Component {

  constructor(props){
    super(props);
    this.state = {
      username: '',
      password: '',
    };
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleSubmit = e => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/login/', this.state)
    .then(res=>{
      console.log(res.data)
    })
    .catch(err=>{
      console.log(err)
    })
  }

  handleChange = e =>{
    this.setState({[e.target.name]: e.target.value});
  }

  render() {
    const { username, password } = this.state;

    return (
      <div className="col-md-6 m-auto" >
        <div className = 'card card-body mt-5'>
          <h2 className='text-center'>Login</h2>
          <form onSubmit={this.handleSubmit}>
              <input
              type="text"
              name="username"
              value={username}
              placeholder='Enter your username'
              onChange={this.handleChange}/>
              <input
              type="password"
              name="password"
              value={password}
              placeholder='**********'
              onChange={this.handleChange}/>
              <button type="submit" className='btn btn-primary' value="submit"> Login </button>
          </form>
        </div>
    </div>
    );
  }
}

export default Login;
