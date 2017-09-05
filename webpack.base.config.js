const webpack = require('webpack');
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

const STATIC_ROOT = './simplestore/static/';

let baseConfig = {};

/* STATIC PATHS AND URLS */
baseConfig.paths = {
  BUNDLE_ROOT_DEV: path.join(STATIC_ROOT, 'bundles/dev/'),
  BUNDLE_ROOT_PROD: path.join(STATIC_ROOT, 'bundles/prod/'),
  STATIC_URL_DEV: 'http://localhost:8001/static/bundles/dev/',
  STATIC_URL_PROD: 'https://static.appstaging.online/bundles/prod/',
  SERVER_URL: 'http://localhost:8001/', /* Your backend server url */
};

baseConfig.config = {
  cache: true,
  context: path.resolve(__dirname, STATIC_ROOT),
  entry: {
    main: 'js/main.js',
  },
  output: {
    path: path.resolve(__dirname, baseConfig.paths.BUNDLE_ROOT_DEV),
    publicPath: baseConfig.paths.STATIC_URL_DEV,
    filename: 'js/[name].js',
  },
  resolve: {
    extensions: [
      '.js',
      '.jsx',
      '.json',
      '.coffee',
      '.sass',
      '.scss',
      '.css',
    ],
    modules: [
      path.resolve(STATIC_ROOT),
      path.join(STATIC_ROOT, 'js'),
      path.join(STATIC_ROOT, 'sass'),
      path.join(__dirname, "node_modules"),
      path.join(STATIC_ROOT, 'css'),
      'node_modules',
      'bower_components',
    ],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader?cacheDirectory',
        exclude: [/node_modules/, /bower_components/],
      },
      {
        test: /\.json$/,
        loader: 'json',
      },
      {
        test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
        loader: 'file-loader',
      },
    ],
  }
};

const config = Object.assign({}, baseConfig);

module.exports = config;
