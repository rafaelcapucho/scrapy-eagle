var React = require('react');

var ListItem = React.createClass({

    render: function() {
        return (
            <li>
                <h4>{this.props.memory_used_mb} - {this.props.memory_available_mb}</h4>
            </li>
        );
    }
    
});

module.exports = ListItem;
