export class DnDCharacter {
  hitpoints: number;
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;

  constructor() {
    this.strength = DnDCharacter.generateAbilityScore();
    this.dexterity = DnDCharacter.generateAbilityScore();
    this.constitution = DnDCharacter.generateAbilityScore();
    this.intelligence = DnDCharacter.generateAbilityScore();
    this.wisdom = DnDCharacter.generateAbilityScore();
    this.charisma = DnDCharacter.generateAbilityScore();
    this.hitpoints = 10 + DnDCharacter.getModifierFor(this.constitution);
  }


  public static generateAbilityScore(): number {

    let rolls: number[] = []
    for (let i = 0; i < 4; i++) {
      rolls.push(Math.floor(Math.random() * 7));
    }
    // [Math.floor(Math.random() * 7),Math.floor(Math.random() * 7),Math.floor(Math.random() * 7),Math.floor(Math.random() * 7)]
    // [0,0,0,0].map(_ => Math.floor(Math.random() * 7))
    return rolls.sort().slice(1).reduce((x, y) => x + y);
  }

  public static getModifierFor(abilityValue: number): number {
    return Math.floor(abilityValue / 2) - 5;
  }
}
