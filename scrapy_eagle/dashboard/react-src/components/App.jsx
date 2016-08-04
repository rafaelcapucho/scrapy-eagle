import React from 'react'
import { Link, IndexLink } from 'react-router'

export default class App extends React.Component {
  constructor(props){
    super(props);
  }

  render(){
    return (
      <div>
        <ul>
          <li><IndexLink to="/app/" activeClassName="active">/</IndexLink></li>
          <li><Link to="/app/servers/monitoring" activeClassName="active">/servers/monitoring</Link></li>
          <li><Link to="/app/spiders/config" activeClassName="active">/spiders/config</Link></li>
        </ul>

        {this.props.children}

      </div>
      );
  }
}
