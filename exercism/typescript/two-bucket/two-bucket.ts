export class TwoBucket {
  bucketOneSize: number;
  bucketTwoSize: number;
  goal: number;
  starterBucket: string;
  movesCount: number;
  goalBucketName: string;
  otherBucketFill: number;


  constructor(bucketOneSize: number, bucketTwoSize: number, goal: number, starterBucket: string) {
    this.bucketOneSize = bucketOneSize;
    this.bucketTwoSize = bucketTwoSize;
    this.goal = goal;
    this.starterBucket = starterBucket;
    this.movesCount = -1;
    this.goalBucketName = 'NOT FOUND';
    this.otherBucketFill = -1;
    this.measure();
  }

  // definition from the exercise
  get goalBucket(): string {
    return this.goalBucketName;
  }

  // definition from the exercise
  get otherBucket(): number {
    return this.otherBucketFill;
  }

  measure(): void {
    const visited: Set<string> = new Set();
    const queue: Array<[number, number, number]> = [];
    let invalidState: [number, number];

    if (this.starterBucket == 'one') {
      queue.push([this.bucketOneSize, 0, 1]);
      invalidState = [0, this.bucketTwoSize];
    } else {
      queue.push([0, this.bucketTwoSize, 1]);
      invalidState = [this.bucketOneSize, 0];
    }

    while (queue.length > 0) {
      const tuple = queue.pop();
      if (!tuple) {
        throw new Error(`Problem reading queue: ${queue}`);
      }
      const b1: number = tuple[0];
      const b2: number = tuple[1];
      const step: number = tuple[2];

      if (b1 == this.goal) {
        this.movesCount = step;
        this.goalBucketName = 'one';
        this.otherBucketFill = b2;
        return;
      }
      if (b2 == this.goal) {
        this.movesCount = step;
        this.goalBucketName = 'two';
        this.otherBucketFill = b1;
        return;
      }

      if (visited.has(JSON.stringify([b1, b2])) || areTuplesEqual([b1, b2], invalidState)) {
        continue;
      }
      visited.add(JSON.stringify([b1, b2]));

      queue.push([Math.min(b1 + b2, this.bucketOneSize), b2 - (Math.min(b1 + b2, this.bucketOneSize) - b1), step + 1]);
      queue.push([b1 - (Math.min(b1 + b2, this.bucketTwoSize) - b2), Math.min(b1 + b2, this.bucketTwoSize), step + 1]);

      // Emptying a bucket and doing nothing to the other.
      queue.push([b1, 0, step + 1]);
      queue.push([0, b2, step + 1]);

      // Filling a bucket and doing nothing to the other.
      queue.push([this.bucketOneSize, b2, step + 1]);
      queue.push([b1, this.bucketTwoSize, step + 1]);
    }

    // if we reach here, we have not found a solution
  }

  // definition from the exercise
  moves(): number {
    if (this.movesCount == -1) {
      throw new Error('No solution found');
    }
    return this.movesCount;
  }
}

function areTuplesEqual<T extends readonly unknown[]>(tuple1: T, tuple2: T): boolean {
  if (tuple1.length !== tuple2.length) {
    return false;
  }

  for (let i = 0; i < tuple1.length; i++) {
    if (tuple1[i] !== tuple2[i]) {
      return false;
    }
  }

  return true;
}



