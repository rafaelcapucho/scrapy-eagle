import React from 'react'

import { connect } from 'react-redux'
//import PureRenderMixin from 'react-addons-pure-render-mixin'

import cx from 'classnames'

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

    var toggle = 'odd';

    // https://github.com/facebook/immutable-js/issues/667#issuecomment-220223640
    var list_jobs = jobs.entrySeq().map( ([key, value]) => {

      toggle = (toggle == 'odd')? 'even' : 'odd';

      return (
        <div className={cx('col-sm-4', toggle)} key={key}>
          <div className="jobTitle">{key}</div>
          <form method="GET" action="">

            <div className="form-group row">
              <label htmlFor="frequency_minutes" className="col-xs-3 col-form-label">Frequency</label>
              <div className="col-xs-9">
                <input className="form-control" name="frequency_minutes" type="text" defaultValue={value.frequency_minutes} id="frequency_minutes" />
              </div>
            </div>

            <div className="form-group row">
              <label htmlFor="max_concurrency" className="col-xs-3 col-form-label">Max Concurrency</label>
              <div className="col-xs-9">
                <input className="form-control" name="max_concurrency" type="text" defaultValue={value.max_concurrency} id="max_concurrency" />
              </div>
            </div>

            <div className="form-group row">
              <label htmlFor="min_concurrency" className="col-xs-3 col-form-label">Min Concurrency</label>
              <div className="col-xs-9">
                <input className="form-control" name="min_concurrency" type="text" defaultValue={value.min_concurrency} id="min_concurrency" />
              </div>
            </div>

            <div className="form-group row">
              <label htmlFor="priority" className="col-xs-3 col-form-label">Priority</label>
              <div className="col-xs-9">
                <select className="form-control" id="priority">
                  <option>0</option>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                  <option>6</option>
                  <option>7</option>
                  <option>8</option>
                  <option>9</option>
                  <option>10</option>
                </select>
              </div>
            </div>

            <div className="form-group row">
              <label htmlFor="max_memory_mb" className="col-xs-3 col-form-label">Max Memory</label>
              <div className="col-xs-9">
                <input className="form-control" name="max_memory_mb" type="text" defaultValue={value.max_memory_mb} id="max_memory_mb" />
                {/*<small id="emailHelp" className="form-text text-muted">The processes are killed when reach this threshold (megabytes).</small>*/}
              </div>
            </div>

            <div className="form-group row">
              <label htmlFor="start_urls" className="col-xs-3 col-form-label">Start URLs</label>
              <div className="col-xs-9">
                <textarea className="form-control" name="start_urls" id="start_urls" rows="3">{value.start_urls}</textarea>
              </div>
            </div>

            <div className="form-group row">
              <label htmlFor="example-text-input" className="col-xs-3 col-form-label">Last started at</label>
              <div className="col-xs-6">
                <small id="emailHelp" style={{'margin-top': '0.5rem', 'display':'block', 'color':'white'}}>16 minutes ago</small>
              </div>
              <div className="col-xs-3">
                <button className="btn btn-outline-success btn-sm" style={{'float': 'right'}} type="submit">SAVE</button>
              </div>

            </div>

          </form>
        </div>
      );
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