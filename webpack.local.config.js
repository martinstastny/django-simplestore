const webpack = require('webpack');
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');

const baseConfig = require('./webpack.base.config.js');

const localConfig = {
  output:{
    publicPath: '/',
  },
  devtool: 'source-map',
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
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(sass|scss)$/,
        use: [{
          loader: 'style-loader',
        }, {
          loader: 'css-loader',
          options: {
            sourceMap: true,
          },
        }, {
          loader: 'sass-loader',
          options: {
            sourceMap: true,
          },
        }],
      },
    ],
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('development'),
      },
    }),
    new BundleTracker({filename: './webpack-stats.json'}),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
    }),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NamedModulesPlugin(),
    new BrowserSyncPlugin({
      host: 'localhost',
      port: '8002',
      proxy: 'http://localhost:8080',
      open: false,
    }, {reload: false}),
  ],

};

const config = Object.assign({}, baseConfig.config, localConfig);

module.exports = config;
