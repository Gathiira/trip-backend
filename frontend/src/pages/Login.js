import React from 'react'
import { Form, Input, Button} from 'antd';
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

const Login = () => {
  const onFinish = (values) => {
    console.log('Success:', values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <div className="container" >
    <div className="form-container" >
    <Form {...layout} name="basic" initialValues={{remember: true,}} onFinish={onFinish}
      onFinishFailed={onFinishFailed}>
      <Form.Item label="Username" name="username"
        rules={[
          {
            required: true,
            message: 'Please input your username!',
          }, ]}>
          <Input placeholder='Enter your username'/>
      </Form.Item>

      <Form.Item label="Password" name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },]}>
         <Input.Password placeholder='**********'/>
      </Form.Item>

      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit"> Submit </Button>
      </Form.Item>
    </Form>
  </div>
  </div>
  );
};

export default Login;
