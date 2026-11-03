// type alias
type StringOrNum = string | number;
type ObjWithNum = { name: string, uid: StringOrNum };

// function signature
type MathOperation = (a: number, b: number, c: number|string, d?: number) => void;

// function example
const add: MathOperation = (a: number, b: number, c: number | string = 10, optional?: number): void => {
  console.log(a+b);
  console.log(c);
}

// use "tsc sandbox.ts --watch"
// use "tsc --init" to create config file