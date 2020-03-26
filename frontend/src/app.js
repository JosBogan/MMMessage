import React from 'react'
import ReactDOM from 'react-dom'
import './styles/main.scss'
import './styles/messages.scss'

import Home from './components/Home'


const chatSocket = new WebSocket(
  'ws://localhost:8000/boards/1/'
)

chatSocket.onmessage = function(event) {
  const data = JSON.parse(event.data)
  console.log(data)
}

chatSocket.onclose = function(event) {
  console.error('Chat socket closed unexpectedly')
}


class App extends React.Component {
  render() {
    return (
      <Home chatSocket={chatSocket}/>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)