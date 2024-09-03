function soma(a,b) {
    return a+b;
}

const somaArrow = (a, b) => a + b;

console.log(soma(15, 3));
console.log(somaArrow(15, 3));

const dobrarNumeros = (numeros) => numeros.map(num => num * 2);
console.log(dobrarNumeros([1, 2, 3, 4]));