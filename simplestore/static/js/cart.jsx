import React from 'react';
import { render } from 'react-dom';
import Cart from './components/cart';

const cartElement = document.getElementById('react-app');

render(<Cart apiUrl={cartElement.getAttribute('data-apiurl')} />, cartElement);
