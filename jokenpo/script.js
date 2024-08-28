let score = { won: 0, lost: 0, draw: 0 };
let round = 1;
const maxRounds = 3;
let gamesToWin = Math.ceil(maxRounds / 2); // Para melhor de 3, são necessárias 2 vitórias para ser o vencedor geral
let userName = '';

document.getElementById('start-game').addEventListener('click', () => {
    userName = document.getElementById('user-name').value.trim();
    if (userName) {
        document.getElementById('user-name-container').style.display = 'none';
        document.querySelector('.game-container').style.display = 'flex';
    } else {
        alert('Por favor, digite seu nome.');
    }
});

function playGame(playerChoice) {
    if (round <= maxRounds && (score.won < gamesToWin && score.lost < gamesToWin)) {
        const choices = ['rock', 'paper', 'scissors'];
        const computerChoice = choices[Math.floor(Math.random() * 3)];

        document.querySelectorAll('.choice img').forEach(img => img.style.transform = ''); // Redefinir animações

        // Exibir animação
        const playerHand = document.getElementById(playerChoice).querySelector('img');
        playerHand.style.transform = 'scale(1.5)';

        // Determinar resultado
        const result = determineWinner(playerChoice, computerChoice);

        setTimeout(() => {
            updateScore(result);
            document.getElementById('game-result').textContent = `O computador escolheu ${computerChoice}. Você ${result}!`;
            checkForOverallWinner();
        }, 300); // Atraso para mostrar a animação

        round++;
    }
}

function determineWinner(player, computer) {
    if (player === computer) return 'draw';
    if ((player === 'rock' && computer === 'scissors') ||
        (player === 'paper' && computer === 'rock') ||
        (player === 'scissors' && computer === 'paper')) {
        return 'won';
    }
    return 'lost';
}

function updateScore(result) {
    if (result !== 'draw') {
        score[result]++;
    }
    document.getElementById('won').textContent = score.won;
    document.getElementById('lost').textContent = score.lost;
    document.getElementById('draw').textContent = score.draw;
}

function checkForOverallWinner() {
    if (score.won === gamesToWin || score.lost === gamesToWin || round > maxRounds) {
        let winnerMessage;
        if (score.won === gamesToWin) {
            winnerMessage = `Parabéns ${userName}, você venceu!`;
        } else if (score.lost === gamesToWin) {
            winnerMessage = 'O computador venceu!';
        } else {
            winnerMessage = 'O jogo acabou!';
        }
        
        document.getElementById('game-result').textContent = winnerMessage;
        showFinalScore();
        endGame();
    }
}

function showFinalScore() {
    document.getElementById('final-score').textContent = `Resultado final - Você: ${score.won}, Computador: ${score.lost}`;
}

function endGame() {
    document.querySelectorAll('.choice').forEach(choice => {
        choice.onclick = null; // Desabilitar cliques
    });

    // Mostrar botão Jogar Novamente
    const playAgainButton = document.getElementById('play-again');
    playAgainButton.style.display = 'block';
    playAgainButton.onclick = resetGame;
}

function resetGame() {
    score = { won: 0, lost: 0, draw: 0 };
    round = 1;
    document.getElementById('won').textContent = score.won;
    document.getElementById('lost').textContent = score.lost;
    document.getElementById('draw').textContent = score.draw;
    document.getElementById('game-result').textContent = '';
    document.getElementById('final-score').textContent = '';

    document.querySelectorAll('.choice').forEach(choice => {
        choice.onclick = () => playGame(choice.id); // Reabilitar cliques
    });

    document.getElementById('play-again').style.display = 'none'; // Ocultar botão Jogar Novamente
    document.getElementById('user-name-container').style.display = 'block'; // Mostrar o formulário de nome novamente
}
