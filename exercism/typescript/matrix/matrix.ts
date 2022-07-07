export class Matrix {
  _rows: number[][];
  _columns: number[][];

  //Well... It is ugly as fuck, but at least I learned a few things about arrays in TS ;)
  constructor(input: string) {
    let stringRows: string[] = input.split("\n");
    let parsedRows: number[][] = [];
    for (let stringRow of stringRows) {
      parsedRows.push(stringRow.split(" ").map(x => parseInt(x)));
    }
    this._rows = Object.assign([], parsedRows);


    let parsedCols: number[][] = [];
    for (let col = 0; col < parsedRows[0].length; col++) {
      parsedCols[col] = [];
      for (let row = 0; row < parsedRows.length; row++) {
        parsedCols[col][row] = parsedRows[row][col];
      }
    }
    this._columns = Object.assign([], parsedCols);
  }

  get rows(): number[][] {
    return this._rows;
  }

  get columns(): number[][] {
    return this._columns;
  }
}
