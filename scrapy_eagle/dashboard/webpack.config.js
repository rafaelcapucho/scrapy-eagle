var webpack = require('webpack');
var path = require('path');

var BUILD_JS_DIR = path.resolve(__dirname, 'templates/static/js');
var APP_DIR = path.resolve(__dirname, 'react-src');

var config = {
  entry: APP_DIR + '/main.jsx',
  output: {
    path: BUILD_JS_DIR,
    filename: 'bundle.js'
  }
};

module.exports = config;

