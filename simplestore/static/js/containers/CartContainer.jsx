import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

import CartTable from 'components/cart/CartTable';


export default class CartContainer extends React.Component {

  static propTypes = {
    apiUrl: PropTypes.string.isRequired,
  };

  constructor(props) {
    super(props);
    this.state = {};
  }

  /**
   * Event handler for deleting Cart Item
   * @param {event} event
   * @param {number} cartItemId - The Cart Item Id
   */
  onCartItemDelete = (event, cartItemId) => {
    this.deleteCartItem(cartItemId);
  };

  /**
   * Event handler for updating Cart Item
   * @param event
   * @param cartItemId
   */
  onCartItemQuantityChange = (event, cartItemId) => {
    this.updateCartItemQuantity(event, cartItemId);
  };

  /**
   * Get Cart
   */
  getCart() {
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
      .then(() => {
        this.getCart();
      });
  }

  componentDidMount() {
    this.getCart();
  }

  render() {
    if (this.state.data) {
      return (
        <CartTable
          onDelete={this.onCartItemDelete}
          onQtyChange={this.onCartItemQuantityChange}
          data={this.state.data}
        />
      );
    }

    return (<div>Loading...</div>);
  }

}
