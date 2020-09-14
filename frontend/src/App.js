import React from 'react';
import './App.css';

class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      todoList:[],
      activeItem: {
        id:null,
        title:'',
        completed:false,
      },
      editing:false,
    }

    this.fetchTasks = this.fetchTasks.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.getCookie = this.getCookie.bind(this)
    this.startEdit = this.startEdit.bind(this)
    this.deleteItem = this.deleteItem.bind(this)
    this.strikeCompleted = this.strikeCompleted.bind(this)
  }

  getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

  componentWillMount(){
    this.fetchTasks()
  }

  fetchTasks(){
    fetch('http://localhost:8000/api/task-list/')
    .then(response => response.json())
    .then(data => 
      this.setState({
        todoList:data
      })
    )
  }

  handleChange(e){
    var name = e.target.name
    var value = e.target.value
    console.log('Name ', name)
    console.log('Value ', value)
    this.setState({
      activeItem:{
        ...this.state.activeItem,
        title:value
      }
    })
  }

  handleSubmit(e){
    e.preventDefault()
    var csrftoken = this.getCookie('csrftoken')
    var url = 'http://localhost:8000/api/task-create/'

    if(this.state.editing === true){
      url = `http://localhost:8000/api/task-update/${this.state.activeItem.id}/`
      this.setState({
        editing:false
      })
    }

    fetch(url, {
      method:'POST',
      headers: {
        'Content-type':'application/json',
        'X_CSRFToken':csrftoken,
      },
      body:JSON.stringify(this.state.activeItem)
    }).then((response)=> {
      this.fetchTasks()
      this.setState({
        activeItem:{
          id:null,
          title:'',
          completed:false,
        }
      })
    }).catch(function(error) {
      console.log('ERROR :', error)
    })
  }

  startEdit(task){
    this.setState({
      activeItem:task,
      editing:true,
    })
  }

  deleteItem(task){
    var csrftoken = this.getCookie('csrftoken')
    var url = `http://localhost:8000/api/task-delete/${task.id}/`
    fetch(url, {
      method:'DELETE',
      headers: {
        'Content-type':'application/json',
        'X_CSRFToken':csrftoken,
      },
    }).then((response)=> {
      this.fetchTasks()
    })
  }

  strikeCompleted(task){
    task.completed = !task.completed
    var csrftoken = this.getCookie('csrftoken')
    var url = `http://localhost:8000/api/task-update/${task.id}/`

    fetch(url, {
      method:'POST',  
      headers: {
        'Content-type':'application/json',
        'X_CSRFToken':csrftoken,
      },
      body:JSON.stringify({
        'title':task.title,
        'completed':task.completed,
      })
    }).then((response)=> {
      this.fetchTasks()
    })
  }

  render(){
    var tasks = this.state.todoList
    var self = this

    return (
      <div className='container'>
        <div id='task-container'>
          <div id='form-wrapper'>
            <form onSubmit={this.handleSubmit} id='form'>
              <div className='flex-wrapper'>
                <div style={{flex:6}}>
                  <input onChange={this.handleChange} className='form-control' id='title' value={this.state.activeItem.title} type='text' name='title' placeholder='Add tasks' />
                </div>
                <div style={{felx:1}}>
                  <input id='submit' className='btn btn-warning' type='submit' name='add'/>
                </div>
              </div>
            </form>
          </div>
          <div id='list-wrapper'>
            {tasks.map(function(task,index){
              return (
                <div key={index} className='task-wrapper flex-wrapper'>
                  <div onClick={() => self.strikeCompleted(task)} style={{flex:7}}>
                    {task.completed ===false ?(
                      <span>{ task.title}</span>
                    ):(
                      <strike>{ task.title}</strike>
                    )}
                    
                  </div>
                  <div style={{flex:1}}>
                    <button onClick={() => self.startEdit(task)} className='btn btn-sm btn-outline-info'>Edit</button>
                  </div>
                  <div style={{flex:1}}>
                  <button onClick={() => self.deleteItem(task)} className='btn btn-sm btn-outline-dark delete'>-</button>
                  </div>
                </div>
              )
            })}
          </div>
        </div>
      </div>
    )
  }
}

export default App;
