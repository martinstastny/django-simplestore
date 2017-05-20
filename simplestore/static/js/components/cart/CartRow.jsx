import React from 'react';
import CartQuantityBar from './CartQuantityBar';

export default class CartRow extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <tr>
        <td data-th="Product">
          <div className="row">
            <div className="col-sm-2 hidden-xs">
              <a href={this.props.data.url}><img
                className="img-responsive"
                src={this.props.data.image}
                alt={this.props.data.name}
              /> </a>
            </div>
            <div className="col-sm-10">
              <h4>{this.props.data.name}</h4>
              <p>{this.props.data.perex}</p>
            </div>
          </div>
        </td>

        <td data-th="Price">
          ${this.props.data.price}
        </td>

        <td data-th="Quantity">
          <CartQuantityBar value={this.props.data.quantity}
                           onChange={event => this.props.onQtyChange(event, this.props.data.id)}/>
        </td>

        <td data-th="Subtotal" className="text-center">${this.props.data.total_price}</td>

        <td className="actions text-center">
          <button
            type="button" className="btn btn-danger btn-sm"
            onClick={event => this.props.onDelete(event, this.props.data.id)}
          ><i
            className="fa fa-trash-o"
          /></button>
        </td>
      </tr>
    );
  }

}
