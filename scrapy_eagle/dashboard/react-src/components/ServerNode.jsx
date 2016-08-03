var React = require('react');
var ServerSubProcess = require('./ServerSubProcess.jsx');

var ServerNode = React.createClass({
  getInitialState: function() {
    return {
      pid: "",
      public_ip: "",
      cpu_percent: "",
      memory_available_mb: "",
      memory_total_mb: "",
      memory_used_mb: "",
      memory_used_server_mb: "",
      cpus: [],
      subprocesses: [],
      spiders: []
    };
  },
  componentWillMount: function() {

    this.socket = io.connect('http://' + this.props.public_ip + ':5000/resources');
    this.socket.on('resources_info', function (msg) {

      var buff = "[ ";
      for(var i = 0; i < msg.data.cpus.length; i++){
        if(i+1 == msg.data.cpus.length){
          buff += msg.data.cpus[i] + " ";

        } else {
          buff += msg.data.cpus[i] + " / ";
        }
      }
      buff += "]";

      this.setState({
        pid: msg.data.pid,
        public_ip: msg.data.public_ip,
        cpu_percent: msg.data.cpu_percent,
        memory_available_mb: msg.data.memory_available_mb,
        memory_total_mb: msg.data.memory_total_mb,
        memory_used_mb: msg.data.memory_used_mb,
        memory_used_server_mb: msg.data.memory_used_server_mb,
        cpus: buff,
        subprocesses: msg.data.sub,
        spiders: msg.data.spiders
      });

      // console.log(msg.data.cpus);

    }.bind(this));

  },
  componentWillUnmount: function(){

    this.socket.disconnect();

  },
  onClickExecCommand: function(e){

    $.get("http://" + this.state.public_ip + ":5000/processes/exec_command", function(data) {

    });

  },
  onClickStartWorker: function(e){

    $.get("http://" + this.state.public_ip + ":5000/processes/start_spider/" + this.state.selected_spider, function(data) {

    });

  },
  onChangeDataProvider: function(e){

    this.setState({'selected_spider': e.target.value});

  },
  render: function(){

    var listSubProcesses = this.state.subprocesses.map(function (item, i) {
      return <ServerSubProcess
        key={item.pid}
        pid={item.pid}
        cpu_percent={item.cpu_percent}
        spider={item.spider}
        public_ip={this.state.public_ip}
        base_dir={item.base_dir}
        command={item.command}
        memory_used_mb={item.memory_used_mb} />;
    }.bind(this));

    var listSpiders = this.state.spiders.map(function (item, i) {
      return (
          <option key={i} value={item}>{item}</option>
      );
    }.bind(this));

    return (
      <li id="server-node">
        <ul>
          <li>IP: {this.props.public_ip} ({this.props.hostname})</li>
          <li>PID: {this.state.pid}</li>
          <li>CPU Server: {this.state.cpus}%</li>
          <li>Memory Used Server : {this.state.memory_used_server_mb}mb</li>
          <li>CPU Process: {this.state.cpu_percent}%</li>
          <li>Memory Used Process: {this.state.memory_used_mb}mb</li>
          <li>Memory Available: {this.state.memory_available_mb}mb</li>
          <li>Memory Total: {this.state.memory_total_mb}mb</li>
          <li><button onClick={this.onClickExecCommand}>Exec Sample Command</button></li>
          <li>
            <select onChange={this.onChangeDataProvider}>
              <option value="">--- choose a spider</option>
              {listSpiders}
            </select>
            <button onClick={this.onClickStartWorker}>Start Worker</button></li>
          <ul>{listSubProcesses}</ul>
        </ul>
      </li>
    );

  }
});

module.exports = ServerNode;
