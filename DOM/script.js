// 1. Selecionando Elementos do DOM

// Seleciona o elemento <h1> pelo ID "titulo"
const titulo = document.getElementById('titulo');
console.log(titulo); // Imprime o elemento <h1> no console

// Seleciona todos os elementos <p> com a classe "texto"
const paragrafos = document.getElementsByClassName('texto');
console.log(paragrafos); // Imprime uma HTMLCollection com todos os <p> com classe "texto"

// Seleciona todos os elementos <li> dentro do <ul> com ID "lista"
const itensLista = document.querySelectorAll('#lista li');
console.log(itensLista); // Imprime uma NodeList com todos os <li> dentro do <ul>

// 2. Modificando Conteúdo de Elementos

// Modifica o texto do elemento <h1> selecionado
titulo.textContent = 'Título De CRIAA';
// `textContent` altera apenas o texto interno do elemento

// Modifica o conteúdo HTML do primeiro parágrafo
paragrafos[0].innerHTML = '<strong>Texto atualizado com HTML pprt</strong>';
// `innerHTML` permite alterar o conteúdo HTML interno de um elemento

// 3. Alterando Atributos de Elementos

// Seleciona o botão pelo ID "botao"
const botao = document.getElementById('botao');

// Altera o texto exibido no botão
botao.textContent = 'Novo Texto do Botão';
botao.style.background = 'orange';

// Adiciona um novo atributo "title" ao botão
botao.setAttribute('title', 'Este é um botão');
// `setAttribute` é usado para definir ou alterar um atributo de um elemento

// 4. Adicionando e Removendo Elementos

// Adicionando um novo item à lista
const novoItem = document.createElement('li'); // Cria um novo elemento <li>
novoItem.textContent = 'OOOO'; // Define o conteúdo do novo <li>
document.getElementById('lista').appendChild(novoItem); // Adiciona o novo <li> ao <ul> com ID "lista"
// `createElement` cria um novo elemento e `appendChild` adiciona esse elemento como último filho do elemento selecionado

// Removendo o segundo item da lista
const itemParaRemover = document.querySelector('#lista li:nth-child(2)');
itemParaRemover.remove(); // Remove o elemento <li> selecionado
// `remove` é um método que remove o elemento do DOM

// 5. Manipulando Estilos de Elementos

// Adiciona um estilo de cor ao título
titulo.style.color = 'orange';
// `style` permite acessar e definir estilos CSS diretamente no elemento

// Altera o estilo de fundo do primeiro parágrafo
paragrafos[0].style.backgroundColor = 'white';
// `backgroundColor` altera a cor de fundo do elemento selecionado

// 6. Manipulando Classes CSS

// Adiciona uma nova classe ao título
titulo.classList.add('novo-estilo');
// `classList.add` adiciona uma nova classe CSS ao elemento

// Remove a classe do título
titulo.classList.remove('novo-estilo');
// `classList.remove` remove uma classe CSS do elemento

// Alterna a presença de uma classe no botão
botao.classList.toggle('ativo');
// `classList.toggle` adiciona a classe se ela não estiver presente e a remove se estiver presente
botao.classList.add('styles.css')
// 7. Eventos do DOM

// Adiciona um evento de clique ao botão
botao.addEventListener('click', () => {
    alert('Voce clicou no botao man!');
});
// `addEventListener` adiciona um ouvinte de evento ao elemento selecionado. Neste caso, exibe um alerta quando o botão é clicado.

