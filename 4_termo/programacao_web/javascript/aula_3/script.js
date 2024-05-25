let titulo = prompt("Novo titulo: ")

/*
const > Constante [variavel]
H1 é o elemento como todo [<h1>Este título ....</h1>]
document.querySelector("Seletor") > Procura dentro do HTML (ou CSS) o elemento
 HTML ou CSS   Busca
Seletor > [Tag] / [#id] / [.Class]
*/
const h1 = document.querySelector("h1")

// O conteudo de texto do H1 será trocado
h1.textContent = titulo

let paragrafo = prompt("Primeiro paragrafo: ")
const p1 = document.querySelector("p")
p1.textContent = paragrafo

let paragrafo2 = prompt("Segundo paragrafo: ")

// Se usar uma Tag geral ele pega a 1º
const p2 = document.querySelector("#segundo")
p2.textContent = paragrafo2