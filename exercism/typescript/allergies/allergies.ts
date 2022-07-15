export class Allergies {
  static allergens: string[] = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"];
  allAllergies: string[];

  constructor(allergenIndex: number) {
    let binaryArray: number[] = allergenIndex.toString(2).split("").map(x => parseInt(x)).reverse();
    this.allAllergies = [];
    for (let i = 0; i < binaryArray.length; i++) {
      if (i <= 7 && binaryArray[i] === 1) {
        this.allAllergies.push(Allergies.allergens[i]);
      }
    }
  }

  public list(): string[] {
    return this.allAllergies;
  }

  public allergicTo(allergen: string): boolean {
    return this.allAllergies.find(element => element === allergen) !== undefined;
  }
}
