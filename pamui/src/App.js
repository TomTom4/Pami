import React, { useState } from 'react';
import logo from './logo.svg';
import Signin from './components/signin'
import Main from './components/main'
import './App.css';

function App() {
	const [connected, setConnected] = useState(false)
	const connect = () =>{
		setConnected(connected?setConnected(false):setConnected(true))
	}
	const contained = connected?<Main connect={connect}/>:<Signin connect={connect}/>

	
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
	  {contained}
    </div>
  );
}

export default App;
