export class Clock {
    _hour;
    _minute;
    constructor(hour, minute) {
        let minutes = hour * 60 + (minute ?? 0);
        if (minutes < 0) {
            minutes = 1440 - Math.abs(minutes) % 1440;
        }
        this._hour = Math.floor(minutes / 60) % 24;
        this._minute = minutes % 60;
    }
    toString() {
        let h = this._hour;
        let m = this._minute;
        return `${h < 10 ? "0" + h : h}:${m < 10 ? "0" + m : m}`;
    }
    plus(minutes) {
        return new Clock(this._hour, this._minute + minutes);
    }
    minus(minutes) {
        return new Clock(this._hour, this._minute - minutes);
    }
    equals(other) {
        return this._hour === other._hour && this._minute === other._minute;
    }
}
