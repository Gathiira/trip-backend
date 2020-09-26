import axios from "axios";

export function ApiCall(type, data) {

  let BaseUrl = "https://smokin-ace.herokuapp.com/api/"

  if (data==='') {
    return new Promise((resolve, reject) => {
      axios.get(BaseUrl + type)
      .then((response) => {
        resolve(response)
      })
      .catch((error) =>{
        reject(error);
        alert('Unable to fetch data')
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
        alert('Unable to send data, Try again')
      })
    });
  }
}
