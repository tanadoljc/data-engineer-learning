// Object: 
var obj = {};

// 1. How to check that there is the key property
obj['bark'] = 'eiei';
console.log(obj.hasOwnProperty('bark')); // true

// 2. deep copy
var deepCopyObj = JSON.parse(JSON.stringify(obj));

// 3. if exist
obj['name'] = obj['name'] || "most"; // if not exist -> || 

// 4. const still edit detail so use "freeze"
const obj_const = {
    "name":"most"
};
Object.freeze(obj_const);
try{
    obj_const['name'] = 'test';
} catch(ex){
    console.log(ex);
}

// ---------------------------------------------------------------------------
// Array:
var arr = [1,2,3,4];

// 1. shift & unshift -> push & pop but in front

// 2. length
var len = arr.length;

// ---------------------------------------------------------------------------
// Additional:

// 1. parseInt
var str = "10011";
var integer = parseInt(str, 2); // str and base

// 2. == and ===
console.log(10 == '10')  // true
console.log(10 === '10') // false -> check type also

// 3. "usestrict" -> must declare type of variables (ver, let)

// 4. var and let
// var -> function scope, can declare again (overwrite)
// let -> block scope inside {}, cannot declare again

// 5. spread operator
arr1 = [1,2,3,4,5];
arr2 = arr1       // wrong
arr2 = [...arr1]; // right

function arg(...args){
    return args; // arr
}

// 6. destructuring assignment
const forecastTemp = {
    today: 10,
    tomorrow: {
        max: 50,
        min: 5
    }
}
// so we declare 2 var: todayTemp & maxTempTomorrow
const {today: todayTemp, tomorrow: {max: maxTempTomorrow}} = forecastTemp;
console.log(todayTemp, maxTempTomorrow);


// 7. swap using destructuring assignment
const src = [1,2,3,4,5,6];
const [ , , ...tmp] = src;

let a = 1, b = 2;
[a,b] = [b,a];
console.log(a,b)

// 8. template literal (add code and new line in text)
const person = {
    name: "most",
    age: 22
};

const greeting = `Hello, my name is ${person.name},
I'm ${person.age} years old.`;

console.log(greeting);