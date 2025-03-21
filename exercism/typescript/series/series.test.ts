import {Series} from './series'

describe('Series', () => {
  it('slices of one from one', () => {
    expect(new Series('1').slices(1)).toEqual([[1]])
  })

  it('slices of one from two', () => {
    expect(new Series('12').slices(1)).toEqual([[1], [2]])
  })

  it('slices of two', () => {
    expect(new Series('35').slices(2)).toEqual([[3, 5]])
  })

  it('slices of two overlap', () => {
    expect(new Series('9142').slices(2)).toEqual([
      [9, 1],
      [1, 4],
      [4, 2],
    ])
  })

  it('slices can include duplicates', () => {
    expect(new Series('777777').slices(3)).toEqual([
      [7, 7, 7],
      [7, 7, 7],
      [7, 7, 7],
      [7, 7, 7],
    ])
  })

  it('slices of long series', () => {
    expect(new Series('918493904243').slices(5)).toEqual([
      [9, 1, 8, 4, 9],
      [1, 8, 4, 9, 3],
      [8, 4, 9, 3, 9],
      [4, 9, 3, 9, 0],
      [9, 3, 9, 0, 4],
      [3, 9, 0, 4, 2],
      [9, 0, 4, 2, 4],
      [0, 4, 2, 4, 3],
    ])
  })

  it('slice length is too large', () => {
    expect(() => {
      new Series('12345').slices(6)
    }).toThrow(new Error('slice length cannot be greater than series length'))
  })

  it('slice length cannot be zero', () => {
    expect(() => {
      new Series('12345').slices(0)
    }).toThrow(new Error('slice length cannot be zero'))
  })

  it('slice length cannot be negative', () => {
    expect(() => {
      new Series('123').slices(-1)
    }).toThrow(new Error('slice length cannot be negative'))
  })

  it('empty series is invalid', () => {
    expect(() => {
      new Series('').slices(1)
    }).toThrow(new Error('series cannot be empty'))
  })
})
