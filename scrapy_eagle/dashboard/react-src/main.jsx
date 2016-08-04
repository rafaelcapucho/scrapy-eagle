import React from 'react'
import { render } from 'react-dom'
import { Router, Route, IndexRoute, browserHistory } from 'react-router'

import App from './components/App.jsx'
import Home from './components/Home.jsx'
import ServerSet from './components/servers/ServerSet.jsx'
import SpiderConfig from './components/SpiderConfig.jsx'

render((
  <Router history={browserHistory}>

    <Route path="/app/" component={App}>

      <IndexRoute component={Home}/>

      <Route path="monitoring" component={ServerSet}/>
      
      <Route path="spiderconfig" component={SpiderConfig}/>

    </Route>

  </Router>
), document.getElementById('app'));