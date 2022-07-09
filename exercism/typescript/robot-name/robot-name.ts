export class Robot {
  _name: string;
  _usedNames: Set<string>;
  constructor() {
    this._usedNames = new Set();
    this._name = this.generateName();
  }

  public get name(): string {
    return this._name;
  }

  public resetName(): void {
    this._name = this.generateName();
  }

  public static releaseNames(): void {
    //What this should do???
    //2022-07-08: some dead function, remove before release if purpose won't be found.
  }
  
  private generateName() : string {
    let result           = '';
    let letters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let digits           = '0123456789';
    const MAX_NO_OF_TRIALS = 10;

    for ( let z = 0 ; z < MAX_NO_OF_TRIALS; z++) {
      for (let i = 0; i < 2; i++) {
        result += letters.charAt(Math.floor(Math.random() * letters.length));
      }
      for (let i = 0; i < 3; i++) {
        result += digits.charAt(Math.floor(Math.random() * digits.length));
      }
      if (!this._usedNames.has(result)) {
        this._usedNames.add(result);
        break;
      }
    }

    return result;
  }
}
