var React = require('react');
var ReactRouter = require('react-router');

var Link = ReactRouter.Link;

var App = React.createClass({
    render: function() {
        return (
            <ul>
                <li><Link to="/">/</Link></li>
                <li><Link to="/monitoring">/Monitoring</Link></li>
            </ul>
        );
    }
});

module.exports = App;