import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // Amount getter and setter
  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = value;
  }

  // Amount getter and setter
  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  // Method to display amount with currency
  displayFullPrice() {
    return `${this._amount} ${Currency.displayFullCurrency}`;
  }
}
