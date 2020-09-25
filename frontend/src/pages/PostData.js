import axios from "axios";

export function PostData(type, userData) {

  let BaseUrl = "http://localhost:8000/account/"

  return new Promise((resolve, reject) => {
    axios.post(BaseUrl + type, userData)
    .then((response) => response.data)
    .then((responseJson) => {
      resolve(responseJson);
      console.log(responseJson)
    })
    .catch((error) =>{
      reject(error);
      alert('Wrong credentials, Please try again')
    })
  });

}
