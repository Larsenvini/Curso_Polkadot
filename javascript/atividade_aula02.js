const readline = require('readline');

// Configuração do readline para capturar entrada do usuário
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Variáveis iniciais
let saldoUsuario = 200.00;
let transacoes = [];

// Função para solicitar a entrada do usuário
function solicitarEntrada(mensagem) {
    return new Promise(resolve => {
        rl.question(mensagem, resposta => {
            resolve(resposta.trim());
        });
    });
}

// Função para realizar uma transação
async function realizarTransacao() {
    let nomeUsuario = await solicitarEntrada("Digite o nome do usuário: ");
    let quantidadeTokens = parseFloat(await solicitarEntrada("Digite a quantidade de tokens para transferir: "));
    let enderecoCartiraDestino = await solicitarEntrada("Digite o endereço da carteira de destino: ");

    let taxaTransacao = quantidadeTokens * 0.02;
    let valorTotalTransacao = quantidadeTokens + taxaTransacao;

    if (saldoUsuario >= valorTotalTransacao) {
        saldoUsuario -= valorTotalTransacao;
        transacoes.push({ nomeUsuario, quantidadeTokens, enderecoCartiraDestino, transacaoComfirmada: true });
        console.log("\nTransação confirmada com sucesso!");
    } else {
        console.log("\nErro: Saldo INSUFICIENTE para realizar a transação");
    }
}

// Menu interativo
async function menuInterativo() {
    while (true) {
        let opcao = await solicitarEntrada("\nEscolha uma opção:\n1. Realizar uma nova transação\n2. Ver saldo atual\n3. Ver transações\n4. Sair\n");

        switch (opcao) {
            case "1":
                await realizarTransacao();
                break;
            case "2":
                console.log("\nSeu saldo atual é: " + saldoUsuario.toFixed(2));
                break;
            case "3":
                if (transacoes.length === 0) {
                    console.log("\nNenhuma transação realizada ainda.");
                } else {
                    console.log("Transações:");
                    transacoes.forEach(transacao => {
                        // Aqui está a modificação
                        const confirmadaStr = transacao.transacaoComfirmada ? "Sim" : "Não";
                        console.log(`Nome: ${transacao.nomeUsuario}, Tokens: ${transacao.quantidadeTokens}, Endereço: ${transacao.enderecoCartiraDestino}, Confirmada: ${confirmadaStr}`);
                    });
                }
                break;
            case "4":
                console.log("Saindo...");
                rl.close();
                return; // Sai do loop e termina o programa
            default:
                console.log("Opção inválida! Por favor, escolha uma opção válida.");
                break;
        }
    }
}

// Inicia o menu interativo
menuInterativo();
