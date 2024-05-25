/*
>> Eventos
1º Declarar o elemento HTML no JavaScript
2º Funcao que sera executada quando o evento acontecer no elemento
3º Associar a funcao com o evento do elemento
*/

const h1 = document.querySelector("h1") // 1º
const h2 = document.querySelector("h2")
const button = document.querySelector("button")

function clicou() { // 2º
    alert("Segredo descoberto!")
}
h1.onclick = clicou // 3º

function cliqueBot() {
    let newText = prompt("Novo texto: ")
    h2.textContent = newText
}
button.onclick = cliqueBot