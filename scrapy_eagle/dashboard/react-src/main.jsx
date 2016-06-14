var React = require('react');
var ReactDOM = require('react-dom');
var List = require('./components/List.jsx');

var ServerNode = require('./components/ServerNode.jsx');
var ServerSet = require('./components/ServerSet.jsx');

// ReactDOM.render(<List />, document.getElementById('ingredients'));
// ReactDOM.render(<ServerNode public_ip="127.0.0.1" />, document.getElementById('server_node'));
ReactDOM.render(<ServerSet />, document.getElementById('server_set'));
