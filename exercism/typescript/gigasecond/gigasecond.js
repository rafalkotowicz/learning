export class Gigasecond {
    _date;
    constructor(date) {
        this._date = date;
    }
    date() {
        return new Date(this._date.getTime() + 1000000000000);
    }
}
