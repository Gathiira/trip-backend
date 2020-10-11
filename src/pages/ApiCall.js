import axios from "axios";

export function ApiCall(type, data) {

  // let BaseUrl = "https://smokin-ace.herokuapp.com/api/"
  let BaseUrl = "http://127.0.0.1:8000/api/"

  if (data==='') {
    return new Promise((resolve, reject) => {
      axios.get(BaseUrl + type)
      .then((response) => {
        resolve(response)
      })
      .catch((error) =>{
        reject(error);
      })
    });
  } else {
    return new Promise((resolve, reject) => {
      axios.post(BaseUrl + type, data)
      .then((response) => {
        resolve(response)
      })
      .catch((error) =>{
        reject(error);
      })
    });
  }
}
