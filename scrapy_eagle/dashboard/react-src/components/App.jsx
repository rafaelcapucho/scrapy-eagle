import React from 'react'
import { Link, IndexLink } from 'react-router'

var Breadcrumbs = require('react-breadcrumbs');

export default class App extends React.Component {
  constructor(props){
    super(props);
  }

  render(){
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

            <h1>Distributed Scrapy</h1>
            <h2>Monitoring Dashboard</h2>

            <ul>
              <li><IndexLink to="/app/" activeClassName="active">/</IndexLink></li>
              <li><Link to="/app/servers/monitoring" activeClassName="active">/servers/monitoring</Link></li>
              <li><Link to="/app/spiders/config" activeClassName="active">/spiders/config</Link></li>
            </ul>

            {this.props.children}

          </section>

          <aside className="sidebar sidebar-left">

            <nav>
              <h5 className="sidebar-header">Navigation</h5>
              <ul className="nav nav-pills nav-stacked">

                <li className="nav-item">
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
                </li>

                <li className="nav-item">
                  <a className="nav-link" title="Dashboard" href="#">Dashboard</a>
                </li>

                <li className="nav-item nav-dropdown">
                  <a className="nav-link active" title="Dashboard 2" href="#">
                    Dashboard Drop
                  </a>
                  <ul className="nav-sub" data-index="0" style={{display: 'none'}}>
                    <li><a title="Buttons" href="#"> Buttons </a></li>
                    <li className="active"><a title="Buttons" href="#"> Buttons </a></li>
                    <li><a title="Buttons" href="#"> Buttons </a></li>
                    <li><a title="Buttons" href="#"> Buttons </a></li>
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
