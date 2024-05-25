const input = document.querySelector("input")
const button = document.querySelector("button")
const p = document.querySelector("#cumprimento")

function cumprimentar() {
    // Obter o nome digitado no campo de entrada [INPUT]
    let nome = input.value
    p.textContent = `Prazer em conhecê-lo(a), ${nome}!`
}
// Clique no botao executa a funcao
button.onclick = cumprimentar