//REFACTOR: a lot of weird ideas mixed together. Remove: remove, findStudent functions as not requested.
//          some inspiration below.
export class GradeSchool {
    db;
    constructor() {
        this.db = new Map();
    }
    roster() {
        this.db.forEach(value => value.sort());
        let asObject = Object.fromEntries(this.db);
        return JSON.parse(JSON.stringify(asObject));
    }
    add(name, grade) {
        let userFound = this.findStudent(name);
        if (userFound[1] !== -1) {
            this.remove(name);
        }
        if (this.db.has(grade)) {
            let tmpNames = this.db.get(grade);
            tmpNames.push(name);
            this.db.set(grade, tmpNames);
        }
        else {
            this.db.set(grade, [name]);
        }
    }
    remove(name) {
        let userFound = this.findStudent(name);
        if (userFound[1] !== -1) {
            let tmpNames = this.db.get(userFound[0]);
            tmpNames.splice(userFound[1], 1);
            this.db.set(userFound[0], tmpNames);
        }
    }
    grade(grade) {
        if (this.db.has(grade)) {
            let names = this.db.get(grade).sort();
            return JSON.parse(JSON.stringify(names));
        }
        else {
            return [];
        }
    }
    findStudent(name) {
        for (let [gradeKey, value] of this.db.entries()) {
            let nameIndex = value.findIndex(x => x === name);
            if (nameIndex !== -1) {
                return [gradeKey, nameIndex];
            }
        }
        return [NaN, -1];
    }
}
//not mine solution (https://exercism.org/tracks/typescript/exercises/grade-school/solutions/bobahop)
// interface DB {
//   [key: number]: string[];
// }
//
// export class GradeSchool {
//   _roster: DB = {}
//   roster() { return JSON.parse(JSON.stringify(this._roster)) }
//   add(name: string, grade: number) {
//     this.deDupe(name)
//     this._roster[grade] ? this._roster[grade].push(name) : this._roster[grade] = [name]
//     this._roster[grade].sort()
//   }
//
//   grade(grade: number) { return this.roster()[grade] ?? [] }
//   deDupe(name: string) {
//     for (let grade in this._roster) {
//       let names = this._roster[grade]
//       if (names.indexOf(name) != -1) { names.splice(names.indexOf(name), 1); break }
//     }
//   }
// }
