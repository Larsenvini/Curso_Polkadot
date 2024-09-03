let pessoa = {
    nome: "Rodrigo",
    idade: 42,
    profissao: "Professor"
};

Object.keys(pessoa).forEach((key) => {
    console.log(key + ": " + pessoa[key]);
});

let { nome, idade } = pessoa;
console.log(`Nome: ${nome}, Idade: ${idade}`);
