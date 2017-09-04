const webpack = require('webpack');
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');

const baseConfig = require('./webpack.base.config.js');

const localConfig = {
  cache: true,
  output: {
    publicPath: '/',
    filename: 'js/[name].js',
  },
  devtool: false,
  devServer: {
    hot: true,
    host: 'localhost',
    port: 8080,
    compress: true,
    proxy: {
      '*': baseConfig.paths.SERVER_URL,
    },
  },
  stats: {
    colors: true,
    timings: true,
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader?cacheDirectory',
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(sass|scss)$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
    ],
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('development'),
      },
    }),
    new webpack.ProvidePlugin({
      'window.jQuery': 'jquery',
      'window.$': 'jquery',
      'jQuery': 'jquery',
      '$': 'jquery'
    }),
    new BundleTracker({ filename: './webpack-stats.json' }),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NamedModulesPlugin(),
    new BrowserSyncPlugin({
      host: 'localhost',
      port: '8002',
      proxy: 'http://localhost:8080',
      open: false,
    }, { reload: false }),
  ],

};

const config = Object.assign({}, baseConfig.config, localConfig);

module.exports = config;
