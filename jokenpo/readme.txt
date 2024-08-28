### Changes made in Jokenpo Game

# Change 1: Removed <button class="choice" id="Polkadot">Polkadot</button> and <button class="choice" id="CodigoBrazuca">Código Brazuca</button> in "index.html".
# Reason: We no longer need buttons for the options as they are being removed

# Change 2: Removed "Polkadot", "CodigoBrazuca" in const escolhas = ["Pedra", "Papel", "Tesoura", "Polkadot", "CodigoBrazuca"]; in line 3 of script.js
# Reason: We mean to remove these choices as the user's feedback told us. So we shouldn't have them in the choices const.

# Change 3: Changed function determinarVencedor to only handle new logic (without "Polkadot" and "CodigoBrazuca)
# Reason: As we no longer have those choices the program should calculate who won only with the remaining options

# Change 4: in script.js function jogarJogo, added:

 if (pontosJogador == 3) {
        document.getElementById("resultado-jogo").textContent = 'Você ganhou!!'
    } else if (escolhaComputador == 3) {
        document.getElementById("resultado-jogo").textContent = 'Você perdeu!'

# Reason: After 3 rounds a overall winner is determined, because thats just how it works.