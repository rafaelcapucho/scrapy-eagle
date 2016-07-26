var React = require('react');
var ReactRouter = require('react-router');

var Link = ReactRouter.Link;
var IndexLink = ReactRouter.IndexLink;

var App = React.createClass({
    render: function() {
        return (
            <div>
                <ul>
                    <li><IndexLink to="/app/" activeClassName="active">/</IndexLink></li>
                    <li><Link to="/app/monitoring" activeClassName="active">/Monitoring</Link></li>
                </ul>

                {this.props.children}

            </div>
        );
    }
});

module.exports = App;