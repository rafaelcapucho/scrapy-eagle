import React from 'react'
import { render } from 'react-dom'
import { Router, Route, IndexRoute, browserHistory } from 'react-router'

import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'

import App from './components/App.jsx'
import Home from './components/Home.jsx'
import ServerSet from './components/servers/ServerSet.jsx'
import ServerRoot from './components/servers/Root.jsx'

import JobsConfig from './components/jobs/JobsConfig.jsx'
import JobsRoot from './components/jobs/Root.jsx'

import servers from './reducers/servers.jsx'
import jobs from './reducers/jobs.jsx'

var reducers = combineReducers({
  servers: servers,
  jobs: jobs
});

const store = createStore(reducers);

render((
  <Provider store={store}>
    <Router history={browserHistory}>

      <Route name="Dashboard" path="/app/" component={App}>

        <IndexRoute component={Home}/>

        <Route name="Jobs" path="jobs" component={JobsRoot}>
          <Route name="Config" path="config" component={JobsConfig}/>
        </Route>

        <Route name="Servers" path="servers" component={ServerRoot}>
          <Route name="Monitoring" path="monitoring" component={ServerSet}/>
        </Route>

      </Route>

    </Router>
  </Provider>
), document.getElementById('app'));
