import React from 'react'

import { connect } from 'react-redux'
//import PureRenderMixin from 'react-addons-pure-render-mixin'

import JobsItem from './JobsItem.jsx'

require('./JobsConfig.scss');

class JobsConfig extends React.Component {

  constructor(props){
    super(props);
    //this.shouldComponentUpdate = PureRenderMixin.shouldComponentUpdate.bind(this);
    this.state = {};
  }

  componentDidMount(){
    this.updateSpiders();
  }

  updateSpiders(){

  }

  componentWillReceiveProps(nextProps) {
    // console.log('entro componentWillReceiveProps');
  }

  shouldComponentUpdate(nextProps, nextState) {
    return true;
    //return nextProps.id !== this.props.id;
  }

  render(){
    const { jobs } = this.props;

    // console.log('render!');

    var toggle_class = 'odd';

    // https://github.com/facebook/immutable-js/issues/667#issuecomment-220223640
    var list_jobs = jobs.entrySeq().map( ([key, value]) => {

      toggle_class = (toggle_class == 'odd')? 'even' : 'odd';

      return <JobsItem
          key={key}
          id={key}
          toggle_class={toggle_class}
          value={value}
      />;

    });

    return (
      <div className="container-fluid scheduler">
        <h1>Jobs Configuration</h1>

        {list_jobs}

        <div style={{'clear':'both'}}></div>

        <div className="box-legends">
          <h2>Legends</h2>
          <ul>
            <li><strong>Frequency</strong>: Amount of time in minutes defining when to trigger this action over time. Ex.: 60 means each hour</li>
            <li><strong>Max Concurrency</strong>: How many servers will be this action running.</li>
            <li><strong>Min Concurrency</strong>: Only dispatch this job when a minimum of resources are available.</li>
            <li><strong>Priority</strong>: Highest numbers is selected when the system need to choose between equals opportunities.</li>
            <li><strong>Max Memory</strong>: The processes are killed when reach this threshold (in megabytes) and could be reallocated in other server or in the same server.</li>
            <li><strong>Start URLs</strong>: A list of URLs to use as starting point.</li>
            <li><strong>Last started at</strong>: Last time this job was triggered.</li>
          </ul>
        </div>


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
      jobs: state.jobs
    }
  },
  mapDispatchToProps
)(JobsConfig)