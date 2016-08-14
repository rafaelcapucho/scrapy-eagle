import React from 'react'
import { render } from 'react-dom'
import { Router, Route, IndexRoute, browserHistory } from 'react-router'

import { createStore } from 'redux'
import { Provider } from 'react-redux'

import App from './components/App.jsx'
import Home from './components/Home.jsx'
import ServerSet from './components/servers/ServerSet.jsx'
import ServerRoot from './components/servers/Root.jsx'

import SpiderConfig from './components/spiders/SpiderConfig.jsx'
import SpiderRoot from './components/spiders/Root.jsx'

import stats from './reducers/stats.jsx'

const store = createStore(stats);

render((
  <Provider store={store}>
    <Router history={browserHistory}>

      <Route name="Dashboard" path="/app/" component={App}>

        <IndexRoute component={Home}/>

        <Route name="Spiders" path="spiders" component={SpiderRoot}>
          <Route name="Config" path="config" component={SpiderConfig}/>
        </Route>

        <Route name="Servers" path="servers" component={ServerRoot}>
          <Route name="Monitoring" path="monitoring" component={ServerSet}/>
        </Route>

      </Route>

    </Router>
  </Provider>
), document.getElementById('app'));
