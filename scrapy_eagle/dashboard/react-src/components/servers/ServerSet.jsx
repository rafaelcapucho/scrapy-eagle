var React = require('react');
var ServerNode = require('./ServerNode.jsx');

var SetIntervalMixin = {
  componentWillMount: function() {
    this.intervals = [];
  },
  setInterval: function() {
    this.intervals.push(setInterval.apply(null, arguments));
  },
  componentWillUnmount: function() {
    this.intervals.forEach(clearInterval);
  }
};

var ServerSet = React.createClass({

  mixins: [SetIntervalMixin],

  getInitialState: function() {
    return {server_set: new Array()};
  },

  componentDidMount:function(){
    this.setInterval(this.updateServers, 3000);
  },

  updateServers: function() {

    var that = this;

    var server_set_new = new Array();

    this.serversRequest = $.ajax({
      url: "http://" + document.domain + ":5000/servers/list",
      type: 'GET',
      dataType: 'json',
      cache: false
    }).done(function(data) {
      data.forEach(function(elem, index){
        server_set_new.push({public_ip: elem.public_ip, hostname: elem.hostname})
      })
    }).always(function () {
      that.setState({'server_set': server_set_new});
    });

  },

  componentWillUnmount: function() {
    // Ref: https://facebook.github.io/react/tips/initial-ajax.html
    this.serversRequest.abort();
  },
  render: function(){
    var listServers = this.state.server_set.map(function(item) {
        return <ServerNode
          key={item.public_ip}
          hostname={item.hostname}
          public_ip={item.public_ip} />;
    });

    return (
      <div>
        <p>ServerSet</p>
        <ul>{listServers}</ul>
      </div>
    );
  }
});

module.exports = ServerSet;
