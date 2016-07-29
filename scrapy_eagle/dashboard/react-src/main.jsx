import React from 'react'
import { render } from 'react-dom'
import { Router, Route, hashHistory, IndexRoute, browserHistory } from 'react-router'


var ServerSet = require('./components/ServerSet.jsx');
var Home = require('./components/Home.jsx');
var App = require('./components/App.jsx');

render((
  <Router history={browserHistory}>

    <Route path="/app/" component={App}>

        <IndexRoute component={Home}/>

        <Route path="monitoring" component={ServerSet}/>

    </Route>

  </Router>
), document.getElementById('app'))