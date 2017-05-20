import React from 'react';
import CartRow from './CartRow';

export default class CartTable extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const createCartRow = item => (<CartRow key={item.id} data={item} onDelete={this.props.onDelete} onQtyChange={this.props.onQtyChange} />);

    if (this.props.data.items.length > 0) {
      return (<div>
        <table id="cart" className="table table-hover table-condensed">
          <thead>
            <tr>
              <th width="50%">Product</th>
              <th width="10%">Price</th>
              <th width="15%">Quantity</th>
              <th className="text-center">Subtotal</th>
            </tr>
          </thead>
          <tbody>
            {this.props.data.items.map(createCartRow)}
          </tbody>
          <tfoot>
            <tr className="visible-xs">
              <td className="text-center">Total: ${this.props.data.price_subtotal}</td>
            </tr>
            <tr>
              <td>
                <a href="/" className="btn btn-default">Continue shopping</a>
              </td>
              <td colSpan="2" className="hidden-xs">&nbsp;</td>
              <td className="hidden-xs text-center">
                <strong>Total</strong> ${this.props.data.price_subtotal}
              </td>
              <td>
                <a href="/checkout" className="btn btn-primary btn-block">Checkout</a>
              </td>
            </tr>
          </tfoot>
        </table>
      </div>);
    }

    return (
      <div>
        <h3>Your cart is empty.</h3><a className="btn btn-primary" href="/">Go Shopping!</a>
      </div>
    );
  }
}
