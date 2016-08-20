import React from 'react'

import { connect } from 'react-redux'

class SpiderConfig extends React.Component {

  constructor(props){
    super(props);
    this.state = {};
  }

  componentDidMount(){
    this.updateSpiders();
  }

  updateSpiders(){


  }

  render(){
    const { spiders } = this.props;

    // https://github.com/facebook/immutable-js/issues/667#issuecomment-220223640
    var list_spiders = spiders.entrySeq().map( ([key, value]) => {
        return <li key={key}>{key}</li>;
    });

    return (
      <div>Spiders Configuration
      <ul>{list_spiders}</ul>
      </div>
    );
  }

}

var mapDispatchToProps = function(dispatch){
  return {
    dispatch
  }
};

export default connect(
  (state) => {
    return {
      spiders: state.spiders
    }
  },
  mapDispatchToProps
)(SpiderConfig)