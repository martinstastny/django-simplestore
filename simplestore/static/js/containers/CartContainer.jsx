import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';


export default class CartContainer extends React.Component {

  static propTypes = {
    apiUrl: PropTypes.string.isRequired,
  };

  constructor(props) {
    super(props);
  }

  /**
   * Get Cart
   * @param {string} url - The Cart API URL endpoint
   */
  getCart(url) {
    axios.get(this.props.apiUrl)
      .then((response) => {
        this.setState({ data: response.data });
      })
      .catch((error) => {
        console.log(`There was an error with your request. ${error}`);
      });
  }

  /**
   * Delete Cart Item
   * @param {number} id - The Cart Item ID
   */
  deleteCartItem(id) {
    axios.delete(`${this.props.apiUrl}${id}/`)
      .then(() => {
        this.getCart();
      })
      .catch((error) => {
        console.log(`There was an error with deleting cart item: ${id}. ${error}`);
      });
  }

  /**
   * Update Cart Item Quantity
   * @param {event} event
   * @param id
   */
  updateCartItemQuantity(event, id) {
    const qty = event.target.value;
    axios.patch(`${this.props.apiUrl}${id}/`, { quantity: qty })
      .then((response) => {
        this.getCart();
      });
  }

  render() {
    return(
      <CartTable></CartTable>
    )
  }

}
