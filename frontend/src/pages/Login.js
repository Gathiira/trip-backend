import React, {Component} from 'react';
import { Redirect } from "react-router-dom";
import { PostData } from './PostData';

class Login extends Component {

  constructor(props){
    super(props);
    this.state = {
      username: '',
      password: '',
      redirect:false,
    };
    this.handleSubmit = this.handleLogin.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleLogin = e => {
    e.preventDefault();
    if (this.state.username && this.state.password) {
      PostData("login/",this.state).then((result) =>{
        let responseJson = result;
        if (responseJson.user) {
          sessionStorage.setItem('user',responseJson);
          this.setState({redirect:true})
        } else {
          console.log("Wrong credentials")
        }
      })
    } else {
      console.log("All fields are required")
    }
  }

  handleChange = e =>{
    this.setState({[e.target.name]: e.target.value});
  }

  render() {
    if (this.state.redirect) {
      return (<Redirect to={"/"} />)
    } else if (sessionStorage.getItem("user")) {
      return (<Redirect to={"/"} />)
    } else {
      return (
        <div className="col-md-6 m-auto" >
          <div className = 'card card-body mt-5'>
            <h2 className='text-center'>Login</h2>
            <form onSubmit={this.handleLogin}>
                <input
                  required={true}
                  type="text"
                  name="username"
                  placeholder='Username'
                  onChange={this.handleChange}/>
                <input
                  required={true}
                  type="password"
                  name="password"
                  placeholder='**********'
                  onChange={this.handleChange}/>
                <button type="submit" className='btn btn-primary' value="submit"> Login </button>
            </form>
          </div>
      </div>
      );
    }
  }
}

export default Login;
