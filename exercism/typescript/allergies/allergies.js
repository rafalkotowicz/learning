export class Allergies {
    static allergens = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"];
    allAllergies;
    constructor(allergenIndex) {
        let binaryArray = allergenIndex.toString(2).split("").map(x => parseInt(x)).reverse();
        this.allAllergies = [];
        for (let i = 0; i < binaryArray.length; i++) {
            if (i <= 7 && binaryArray[i] === 1) {
                this.allAllergies.push(Allergies.allergens[i]);
            }
        }
    }
    list() {
        return this.allAllergies;
    }
    allergicTo(allergen) {
        return this.allAllergies.find(element => element === allergen) !== undefined;
    }
}
