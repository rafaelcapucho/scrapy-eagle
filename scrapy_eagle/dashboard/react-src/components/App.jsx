import React from 'react'
import { Link, IndexLink } from 'react-router'

import { connect } from 'react-redux'

var Breadcrumbs = require('react-breadcrumbs');

class App extends React.Component {
  constructor(props){
    super(props);
  }

  componentWillMount(){
    this.intervals = [];
  }

  setInterval() {
    this.intervals.push(setInterval.apply(null, arguments));
  }

  componentWillUnmount(){
    this.intervals.forEach(clearInterval);
    
    // Ref: https://facebook.github.io/react/tips/initial-ajax.html
    this.clientsRequest.abort();
  }

  ajax_get_spiders_info(){

    this.clientsRequest = $.ajax({
      url: window.location.protocol + "//" + document.domain + ":" + location.port + "/spiders/list",
      type: 'GET',
      dataType: 'json',
      cache: false
    }).done((data) => {

      $.each(data, (key, value) => {
        console.log(key, value);
      })

    }).always(() => {
      // that.setState({'server_set': server_set_new});
    });

  }

  componentDidMount(){
    this.ajax_get_spiders_info();
    this.setInterval(this.ajax_get_spiders_info, 5000);
  }

  render(){
    const { servers_qty } = this.props;
    return (
      <div>

        <div className="container-fluid subheader">
          <Breadcrumbs
            routes={this.props.routes}
            params={this.props.params}
          />
        </div>

        <div className="flexbox">

          <section className="main-content-wrapper">

            {/*<h1>Distributed Scrapy</h1>

            <a onClick={() => {this.props.SET_SERVER_QTY(7)}}>{servers_qty}</a>
            => <button onClick={() => { this.props.dispatch({type: 'SET_SERVER_QTY', qty:10}); }}>{servers_qty}</button>

            <ul>
              <li><IndexLink to="/app/" activeClassName="active">/</IndexLink></li>
              <li><Link to="/app/servers/monitoring" activeClassName="active">/servers/monitoring</Link></li>
              <li><Link to="/app/spiders/config" activeClassName="active">/spiders/config</Link></li>
            </ul>
            */}

            {this.props.children}

          </section>

          <aside className="sidebar sidebar-left">

            <nav>
              <h5 className="sidebar-header">Navigation</h5>
              <ul className="nav nav-pills nav-stacked">

                {/*<li className="nav-item">
                  <a className="nav-link" href="#">
                    Option 1
                    <span className="pull-right tag tag-pill tag-primary">8</span>
                  </a>
                </li>

                <li className="nav-item">
                  <a className="nav-link" href="#">
                    Option 2
                    <span className="pull-right tag tag-danger">new</span>
                  </a>
                </li>*/}

                <li className="nav-item">
                  <IndexLink to="/app/" className="nav-link direct" activeClassName="active">Main</IndexLink>
                </li>

                <li className="nav-item nav-dropdown">
                  <Link to="/app/servers" className="nav-link" activeClassName="active">
                    Servers
                    <span className="pull-right tag tag-pill tag-primary">{ servers_qty }</span>
                  </Link>
                  <ul className="nav-sub">
                    <li><Link to="/app/servers/monitoring" activeClassName="active">Monitoring</Link></li>
                  </ul>
                </li>

                <li className="nav-item nav-dropdown">
                  <Link to="/app/spiders" className="nav-link" activeClassName="active">Spiders & Commands</Link>
                  <ul className="nav-sub">
                    <li><Link to="/app/spiders/config" activeClassName="active">Configuration</Link></li>
                  </ul>
                </li>

              </ul>

            </nav>

          </aside>

        </div>

      </div>
      );
  }
}

var mapDispatchToProps = function(dispatch){
  return {
    dispatch,
  }
};

export default connect(
  (state) => {
    return {
      servers_qty: state.servers_qty
    }
  },
  mapDispatchToProps
)(App)