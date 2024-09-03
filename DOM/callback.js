function cumprimentar(nome, callback) {
    console.log("Olá, " + nome + "!");
    callback();
}

function despedida() {
    console.log("Até logo!");
}

cumprimentar ("Rodrigo", despedida);


function processaArray(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
        arr[i] = callback(arr[i]);
    }
    return arr;
}

const resultado = processaArray([1, 2, 3, 4, 5], (num) => num * 4);
console.log(resultado);