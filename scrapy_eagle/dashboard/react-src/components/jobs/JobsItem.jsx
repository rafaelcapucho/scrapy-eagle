import React from 'react'
import { connect } from 'react-redux'

import cx from 'classnames'

class JobsItem extends React.Component {

  constructor(props){
    super(props);
    this.handleSave = this.handleSave.bind(this);
    this.state = {};
  }

  handleSave(){
    alert('save');
  }

  render(){
    return (
      <div className={cx('col-sm-4', this.props.toggle_class)} key={this.props.key}>
        <div className="jobTitle">{this.props.key}</div>
        <form method="GET" action="">

          <div className="form-group row">
            <label htmlFor="frequency_minutes" className="col-xs-3 col-form-label">Frequency</label>
            <div className="col-xs-9">
              <input className="form-control" name="frequency_minutes" type="text" defaultValue={this.props.value.frequency_minutes} id="frequency_minutes" />
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="max_concurrency" className="col-xs-3 col-form-label">Max Concurrency</label>
            <div className="col-xs-9">
              <input className="form-control" name="max_concurrency" type="text" defaultValue={this.props.value.max_concurrency} id="max_concurrency" />
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="min_concurrency" className="col-xs-3 col-form-label">Min Concurrency</label>
            <div className="col-xs-9">
              <input className="form-control" name="min_concurrency" type="text" defaultValue={this.props.value.min_concurrency} id="min_concurrency" />
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
              <input className="form-control" name="max_memory_mb" type="text" defaultValue={this.props.value.max_memory_mb} id="max_memory_mb" />
              <small id="emailHelp" className="form-text text-muted">The processes are killed when reach this threshold (megabytes).</small>
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="start_urls" className="col-xs-3 col-form-label">Start URLs</label>
            <div className="col-xs-9">
              <textarea className="form-control" name="start_urls" id="start_urls" rows="3">{this.props.value.start_urls}</textarea>
            </div>
          </div>

          <div className="form-group row">
            <label htmlFor="example-text-input" className="col-xs-3 col-form-label">Last started at</label>
            <div className="col-xs-6">
              <small id="emailHelp" style={{'margin-top': '0.5rem', 'display':'block', 'color':'white'}}>16 minutes ago</small>
            </div>
            <div className="col-xs-3">
              <button onClick={this.handleSave} className="btn btn-outline-success btn-sm" style={{'float': 'right'}} type="button">SAVE</button>
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