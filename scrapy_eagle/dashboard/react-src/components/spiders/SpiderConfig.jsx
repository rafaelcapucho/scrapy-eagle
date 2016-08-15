import React from 'react'

export default class SpiderConfig extends React.Component {

  constructor(props){
    super(props);
    this.state = {};
  }

  componentDidMount(){
    this.updateSpiders();
  }

  updateSpiders(){

    // this.serversRequest = $.ajax({
    //   url: "http://" + document.domain + ":5000/spiders/list",
    //   type: 'GET',
    //   dataType: 'json',
    //   cache: false
    // }).done((data) => {
    //
    //   $.each(data, (key, value) => {
    //     console.log(key, value);
    //   })
    //
    // }).always(() => {
    //   // that.setState({'server_set': server_set_new});
    // });

  }

  render(){
    return (
      <div>Spiders Configuration</div>
    );
  }

}
