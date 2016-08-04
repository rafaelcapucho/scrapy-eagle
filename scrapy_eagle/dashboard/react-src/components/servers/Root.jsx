import React from 'react'

export default class ServerRoot extends React.Component {
  constructor(props){
    super(props);
  }

  render(){
    return this.props.children;
  }
}
