import React from 'react'

export default class SpiderRoot extends React.Component {
  constructor(props){
    super(props);
  }

  render(){
    return this.props.children;
  }
}