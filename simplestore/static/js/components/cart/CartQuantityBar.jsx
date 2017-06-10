import React from 'react';


export default class CartQuantityBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 0,
    };
  }

  componentDidMount() {
    this.setState({ value: this.props.value });
  }

  fireInputEvent() {
    const event = new Event('input', { bubbles: true });
    this.textInput.dispatchEvent(event);
  }

  decreaseQty = () => {
    this.setState({ value: this.state.value > 1 ? --this.state.value : 1 }, () => {
      this.fireInputEvent();
    });
  };

  increaseQty = () => {
    this.setState({ value: ++this.state.value }, () => {
      this.fireInputEvent();
    });
  };

  render() {
    return (
      <div className="btn-group">
        <button type="button" className="btn btn-default btn-xs" onClick={this.decreaseQty}><i className="fa fa-minus"/>
        </button>
        <input
          readOnly="true"
          id="qty" type="text" className="pull-left cart_item_quantity" min="1" value={this.state.value}
          onChange={this.props.onChange} ref={(input) => {
          this.textInput = input;
        }}
        />
        <button type="button" className="btn btn-default btn-xs" onClick={this.increaseQty}><i className="fa fa-plus"/>
        </button>
      </div>
    );
  }

}
