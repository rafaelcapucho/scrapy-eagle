var webpack = require('webpack');
var path = require('path');

var BUILD_JS_DIR = path.resolve(__dirname, 'templates/static/js');
var APP_DIR = path.resolve(__dirname, 'react-src');

var config = {
  entry: APP_DIR + '/main.jsx',
  output: {
    path: BUILD_JS_DIR,
    filename: 'bundle.js'
  },
  plugins: [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': JSON.stringify('production')
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compressor: {
        warnings: false
      }
    })
  ],
  module : {
    loaders : [
      {
        test : /\.jsx?/,
        include : APP_DIR,
        loader : 'babel'
      }
    ]
  }
};

module.exports = config;