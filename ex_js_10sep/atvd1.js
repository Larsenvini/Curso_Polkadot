const carro = {
    marca: "Toyota",
    modelo: "Corolla",
    cor: "Prata",
    ano: "2022"
};

console.log(carro.marca);
console.log(carro.modelo);
console.log(carro.cor);
console.log(carro.ano);

carro.cor = "Preto"
console.log("Cor atualizada: ", carro.cor)

const {marca, modelo} = carro;
console.log(marca);
console.log(modelo);

