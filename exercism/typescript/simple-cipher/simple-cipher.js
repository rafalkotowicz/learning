const letters = "abcdefghijklmnopqrstuvwxyz";
export class SimpleCipher {
    key;
    constructor(key) {
        if (key) {
            this.key = key;
        }
        else {
            const KEY_LENGTH = 100;
            let randomKey = "";
            for (let i = 0; i < KEY_LENGTH; i++) {
                randomKey += letters.charAt(Math.floor(Math.random() * letters.length));
            }
            this.key = randomKey;
        }
    }
    encode(toEncode) {
        let encoded = "";
        let toShift = 0;
        for (let i = 0; i < toEncode.length; i++) {
            toShift = letters.indexOf(this.key[i % this.key.length]);
            encoded += letters[(letters.indexOf(toEncode[i]) + toShift) % 26];
        }
        return encoded;
    }
    decode(toDecode) {
        let decoded = "";
        let toShift = 0;
        for (let i = 0; i < toDecode.length; i++) {
            toShift = letters.indexOf(this.key[i % this.key.length]);
            decoded += letters[(letters.indexOf(toDecode[i]) - toShift + 26) % 26];
        }
        return decoded;
    }
}
