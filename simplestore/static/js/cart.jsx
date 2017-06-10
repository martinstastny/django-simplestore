import React from 'react';
import { render } from 'react-dom';
import CartContainer from './containers/CartContainer';

const cartElement = document.getElementById('react-app');

render(<CartContainer apiUrl={cartElement.getAttribute('data-apiUrl')} />, cartElement);
