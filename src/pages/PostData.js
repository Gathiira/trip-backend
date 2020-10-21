import axios from "axios";

export function PostData(type, data) {

  // let BaseUrl = "https://smokin-ace.herokuapp.com/account/"
  let BaseUrl = "http://127.0.0.1:8000/account/"

  if (data==='') {
    return new Promise((resolve, reject) => {
      axios.get(BaseUrl + type, {
      headers: {
        'Authorization': `token ${sessionStorage.getItem('token')}`
      }
    })
      .then((response) => {
        resolve(response);
      })
      .catch((error) =>{
        reject(error);
      })
    });
  }
  else {
    return new Promise((resolve, reject) => {
      axios.post(BaseUrl + type, data)
      .then((response) => response.data)
      .then((responseJson) => {
        resolve(responseJson);
      })
      .catch((error) =>{
        reject(error);
        alert('Wrong credentials, Please try again')
      })
    });
  }

}
