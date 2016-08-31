import React from 'react'
import { connect } from 'react-redux'

import cx from 'classnames'

class BaseComponent extends React.Component {
  _bind(...methods) {
    methods.forEach( (method) => this[method] = this[method].bind(this) );
  }
}

class JobsItem extends React.Component {

  constructor(props){
    super(props);
    // this._bind('_handleClick', '_handleFoo');
    this.handleSave = this.handleSave.bind(this);
    this.onBlurFrequency = this.onBlurFrequency.bind(this);
    this.onBlurMaxConcurrency = this.onBlurMaxConcurrency.bind(this);
    this.onBlurMinConcurrency = this.onBlurMinConcurrency.bind(this);
    this.onChangePriority = this.onChangePriority.bind(this);
    this.onBlurMaxMemory = this.onBlurMaxMemory.bind(this);
    this.onBlurStartURLs = this.onBlurStartURLs.bind(this);
    this.state = {
      'key': this.props.id,
      'active': this.props.value.active,
      'job_type': this.props.value.job_type,
      'frequency_minutes': this.props.value.frequency_minutes,
      'max_concurrency': this.props.value.max_concurrency,
      'min_concurrency': this.props.value.min_concurrency,
      'priority': this.props.value.priority,
      'max_memory_mb': this.props.value.max_memory_mb,
      'start_urls': this.props.value.start_urls
    };
  }

  onBlurFrequency(e){ this.setState({'frequency_minutes': e.target.value}); }
  onBlurMaxConcurrency(e){ this.setState({'max_concurrency': Number(e.target.value)}); }
  onBlurMinConcurrency(e){ this.setState({'min_concurrency': Number(e.target.value)}); }
  onChangePriority(e){ this.setState({'priority': e.target.value}); }
  onBlurMaxMemory(e){ this.setState({'max_memory_mb': e.target.value}); }
  onBlurStartURLs(e){ this.setState({'start_urls': e.target.value}); }

  handleSave(){
    console.log(this.state);
    //alert('save');
  }

  render(){
    return (
      <div className={cx('col-sm-4', this.props.toggle_class)} key={this.props.id}>
        <div className="jobTitle">{this.props.id}</div>
        <form method="GET" action="">

          <div className="form-group row">
            <label htmlFor="frequency_minutes" className="col-xs-3 col-form-label">Frequency</label>
            <div className="col-xs-9">
              <input className="form-control" name="frequency_minutes" type="text" onBlur={this.onBlurFrequency} defaultValue={this.props.value.frequency_minutes} id="frequency_minutes" />
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="max_concurrency" className="col-xs-3 col-form-label">Max Concurrency</label>
            <div className="col-xs-9">
              <input className="form-control" name="max_concurrency" type="text" onBlur={this.onBlurMaxConcurrency} defaultValue={this.props.value.max_concurrency} id="max_concurrency" />
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="min_concurrency" className="col-xs-3 col-form-label">Min Concurrency</label>
            <div className="col-xs-9">
              <input className="form-control" name="min_concurrency" type="text" onBlur={this.onBlurMinConcurrency} defaultValue={this.props.value.min_concurrency} id="min_concurrency" />
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="priority" className="col-xs-3 col-form-label">Priority</label>
            <div className="col-xs-9">
              <select className="form-control" id="priority" onChange={this.onChangePriority}>
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
              <input className="form-control" name="max_memory_mb" onBlur={this.onBlurMaxMemory} type="text" defaultValue={this.props.value.max_memory_mb} id="max_memory_mb" />
              {/*<small id="emailHelp" className="form-text text-muted">The processes are killed when reach this threshold (megabytes).</small>*/}
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="start_urls" className="col-xs-3 col-form-label">Start URLs</label>
            <div className="col-xs-9">
              <textarea className="form-control" name="start_urls" onBlur={this.onBlurStartURLs} id="start_urls" rows="3">{this.props.value.start_urls}</textarea>
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="example-text-input" className="col-xs-3 col-form-label">Last started at</label>
            <div className="col-xs-6">
              <small id="emailHelp" style={{'margin-top': '0.5rem', 'display':'block', 'color':'white'}}>16 minutes ago</small>
            </div>
            <div className="col-xs-3">
              <button onClick={this.handleSave} className="btn btn-outline-success btn-sm" style={{'float': 'right'}} type="button">Save</button>
            </div>

          </div>

        </form>
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
      //jobs: state.jobs
    }
  },
  mapDispatchToProps
)(JobsItem)