export class Gigasecond {
  _date: Date;
  constructor(date: Date) {
    this._date = date;
  }
  public date() : Date {
    return new Date(this._date.getTime() + 1000000000000);
  }
}
