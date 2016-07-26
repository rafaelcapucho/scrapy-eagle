var React = require('react');
var ReactDOM = require('react-dom');
var ReactRouter = require('react-router');

var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var hashHistory = ReactRouter.hashHistory;

var List = require('./components/List.jsx');
var ServerNode = require('./components/ServerNode.jsx');
var ServerSet = require('./components/ServerSet.jsx');

var About = require('./components/About.jsx');

// ReactDOM.render(<List />, document.getElementById('ingredients'));
// ReactDOM.render(<ServerNode public_ip="127.0.0.1" />, document.getElementById('server_node'));
//ReactDOM.render(<ServerSet />, document.getElementById('server_set'));
ReactDOM.render((
  <Router history={hashHistory}>
    <Route path="/" component={ServerSet}/>
    <Route path="/about" component={About}/>
  </Router>
), document.getElementById('app'))