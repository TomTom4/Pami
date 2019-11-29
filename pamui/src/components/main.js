import React from 'react'
import Container from '@material-ui/core/Container'
import Button from '@material-ui/core/Button'
import axios from 'axios'

export default (props) =>{

	const handleClick = (event) =>{
		event.preventDefault()
		const config = {headers:{'Access-Control-Allow-Origin': 'http://localhost:5000/api/*'}}
		axios.get('http://localhost:5000/api/logout', config).then(function(response){
			props.connect()
		})
	}

	return(
		<Container maxWidth='md'>
			<Button onClick={handleClick}> 
				Logout bro
			</Button>
		</Container>
	)

}
