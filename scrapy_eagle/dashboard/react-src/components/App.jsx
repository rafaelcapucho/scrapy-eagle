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
                    <li><Link to="/app/servers/monitoring" activeClassName="active">/servers/monitoring</Link></li>
                    <li><Link to="/app/spiders/config" activeClassName="active">/spiders/config</Link></li>
                </ul>

                {this.props.children}

            </div>
        );
    }
});

module.exports = App;