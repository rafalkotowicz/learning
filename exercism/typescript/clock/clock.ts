export class Clock {
  _hour: number;
  _minute: number;

  constructor(hour: number, minute?: number) {
    let minutes: number = hour * 60 + (minute ?? 0);
    if (minutes < 0) {
      minutes = 1440 - Math.abs(minutes) % 1440;
    }
    this._hour = Math.floor(minutes / 60) % 24;
    this._minute = minutes % 60;
  }

  public toString(): string {
    let h: number = this._hour;
    let m: number = this._minute;
    return `${h < 10 ? "0" + h : h}:${m < 10 ? "0" + m : m}`;
  }

  public plus(minutes: number): Clock {
    return new Clock(this._hour, this._minute + minutes);
  }

  public minus(minutes: number): Clock {
    return new Clock(this._hour, this._minute - minutes);
  }

  public equals(other: Clock): boolean {
    return this._hour === other._hour && this._minute === other._minute;
  }
}
