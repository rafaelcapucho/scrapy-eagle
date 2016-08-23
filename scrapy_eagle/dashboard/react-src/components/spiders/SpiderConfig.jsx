import React from 'react'

import { connect } from 'react-redux'
import PureRenderMixin from 'react-addons-pure-render-mixin'

require('./style.scss');

class SpiderConfig extends React.Component {

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
    console.log('entro componentWillReceiveProps');
  }

  shouldComponentUpdate(nextProps, nextState) {
    return true;
    //return nextProps.id !== this.props.id;
  }

  render(){
    const { jobs } = this.props;

    console.log('render!');

    // https://github.com/facebook/immutable-js/issues/667#issuecomment-220223640
    var list_jobs = jobs.entrySeq().map( ([key, value]) => {
      return (
        <div style={{border: '2px solid pink'}} className="col-sm-4" key={key}>
          {key} -> {value.getPriority()}
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
              <label htmlFor="example-text-input" className="col-xs-3 col-form-label">Text</label>
              <div className="col-xs-9">
                <input className="form-control" type="text" defaultValue="Artisanal kale" id="example-text-input" />
                <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
              </div>
            </div>

            <div className="form-group row">
              <label htmlFor="max_memory_mb" className="col-xs-3 col-form-label">Max Memory (MB)</label>
              <div className="col-xs-9">
                <input className="form-control" name="max_memory_mb" type="text" defaultValue="200" id="max_memory_mb" />
                <small id="emailHelp" className="form-text text-muted">The processes are killed when reach this threshold.</small>
              </div>
            </div>

          </form>
        </div>
      );
    });

    return (
      <div className="container-fluid scheduler" style={{border: '2px solid blue'}}>
        <h1>Spiders Configuration</h1>
        {list_jobs}
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
)(SpiderConfig)