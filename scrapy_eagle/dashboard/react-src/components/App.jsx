var React = require('react');
var ReactRouter = require('react-router');

var Link = ReactRouter.Link;

var App = React.createClass({
    render: function() {
        return (
            <div>
                <ul>
                    <li><Link to="/" activeClassName="active">/</Link></li>
                    <li><Link to="/monitoring" activeClassName="active">/Monitoring</Link></li>
                </ul>

                {this.props.children}

            </div>
        );
    }
});

module.exports = App;