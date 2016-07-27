var React = require('react');
var ReactDOM = require('react-dom');
var ReactRouter = require('react-router');

var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var IndexRoute = ReactRouter.IndexRoute;
var hashHistory = ReactRouter.hashHistory;
var browserHistory = ReactRouter.browserHistory;

var ServerSet = require('./components/ServerSet.jsx');
var Home = require('./components/Home.jsx');
var App = require('./components/App.jsx');

// ReactDOM.render(<ServerNode public_ip="127.0.0.1" />, document.getElementById('server_node'));
//ReactDOM.render(<ServerSet />, document.getElementById('server_set'));
ReactDOM.render((
  <Router history={browserHistory}>

    <Route path="/app/" component={App}>

        <IndexRoute component={Home}/>

        <Route path="monitoring" component={ServerSet}/>

    </Route>

  </Router>
), document.getElementById('app'))