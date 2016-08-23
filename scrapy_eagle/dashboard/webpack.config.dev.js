var webpack = require('webpack');
var path = require('path');

var ExtractTextPlugin = require('extract-text-webpack-plugin');

var BUILD_JS_DIR = path.resolve(__dirname, 'templates/static/js');
var APP_DIR = path.resolve(__dirname, 'react-src');

var config = {
  entry: APP_DIR + '/main.jsx',
  output: {
    path: BUILD_JS_DIR,
    filename: 'bundle.js'
  },
  module : {
    loaders : [
      {
        test : /\.jsx?/,
        include : APP_DIR,
        loader : 'babel'
      },
      {
        test: /\.scss$/,
        //loaders: ['style', 'css', 'sass']
        loader: ExtractTextPlugin.extract('css!sass')
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin('../css/bundle.css', {
      allChunks: true
    })
  ]
};

module.exports = config;