import React, {Component} from 'react'
import { Form, Input, Button} from 'antd';
import axios from "axios";



const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 8,
  },
};
const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 8,
  },
};

class Login extends Component {

  state = {
    username: '',
    password: '',
  }

  onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

handleSubmit = e => {
  e.preventDefault();

  const data = {
    username:this.username,
    password: this.password
  }

  axios.post('http://localhost:8000/api/login/', data)
  .then(res=>{
    console.log(res)
  })
  .catch(err=>{
    console.log(err)
  })
}

onChange = e => this.setState({[e.target.name]: e.target.value});



  render() {
    const { username, password } = this.state;

    return (
      <div className="col-md-6 m-auto" >
        <div className = 'card card-body mt-5'>
          <h2 className='text-center'>Login</h2>
          <Form {...layout} name="nest-messages" initialValues={{remember: true,}}
            onFinishFailed={this.onFinishFailed} onSubmit={this.handleSubmit}>
            <Form.Item label="Username" name="username"
              rules={[
                {
                  required: true,
                  message: 'Please input your username!',
                }, ]}>
                <Input value={username} placeholder='Enter your username' onChange={this.onChange}/>
            </Form.Item>

            <Form.Item label="Password" name="password"
              rules={[
                {
                  required: true,
                  message: 'Please input your password!',
                },]}>
               <Input.Password value={password} placeholder='**********' onChange={this.onChange}/>
            </Form.Item>

            <Form.Item {...tailLayout}>
              <Button type="submit" htmlType="submit"> Login </Button>
            </Form.Item>
          </Form>
        </div>
    </div>
    );
  }
}

export default Login;
