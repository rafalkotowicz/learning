export class Robot {
    _name;
    _usedNames;
    constructor() {
        this._usedNames = new Set();
        this._name = this.generateName();
    }
    get name() {
        return this._name;
    }
    resetName() {
        this._name = this.generateName();
    }
    static releaseNames() {
        //What this should do???
        //2022-07-08: some dead function, remove before release if purpose won't be found.
    }
    generateName() {
        let result = '';
        let letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        let digits = '0123456789';
        const MAX_NO_OF_TRIALS = 10;
        for (let z = 0; z < MAX_NO_OF_TRIALS; z++) {
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
