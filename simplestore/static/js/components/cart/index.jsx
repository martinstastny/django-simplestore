import React from 'react';
import CartTable from './CartTable';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default class Cart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  getCart() {
    axios.get(this.props.apiurl, { withCredentials: true })
      .then((response) => {
        this.setState({ data: response.data });
      })
      .catch((error) => {
        console.log(`There was an error with your request. ${error}`);
      });
  }

  deleteItem(id) {
    axios.delete(`${this.props.apiurl}${id}/`, { withCredentials: true })
      .then(() => {
        this.getCart();
      })
      .catch((error) => {
        console.log(`There was an error with deleting item: ${id}. ${error}`);
      });
  }

  updateQuantity(event, id) {
    const qty = event.target.value;
    axios.patch(`${this.props.apiurl}${id}/`, { quantity: qty })
      .then((response) => {
        this.getCart();
      });
  }

  componentDidMount() {
    this.getCart();
  }

  onQuantityChange = (event, id) => {
    this.updateQuantity(event, id);
  };

  onDelete = (e, id) => {
    this.deleteItem(id);
  };

  render() {
    if (this.state.data) {
      return (
        <CartTable
          onDelete={this.onDelete}
          onQtyChange={this.onQuantityChange}
          data={this.state.data}
        />
      );
    }

    return (<div>Loading...</div>);
  }
}

