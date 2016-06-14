var React = require('react');
var ListItem = require('./ListItem.jsx');
var HTTP = require('../services/httpservice');

var List = React.createClass({
    getInitialState: function() {
        return {resources: []};
    },
    componentWillMount: function() {

        this.socket = io.connect('http://127.0.0.1:5000/resources');
        this.socket.on('resources_info', function (msg) {
          this.setState({resources: msg.data.sub});
        }.bind(this));

    },
    render: function() {
        /*var listItems = this.state.resources.map(function(item) {
            return <ListItem
              key={item.pid}
              memory_used_mb={item.memory_used_mb}
              memory_available_mb={item.memory_available_mb} />;
        });

        return (<ul>{listItems}</ul>);*/
    }
});

module.exports = List;
