const nome = document.querySelector("#nome")
const nasc = document.querySelector("#nascimento")
const endereco = document.querySelector("#endereco")
const cidade = document.querySelector("#cidade")
const estado = document.querySelector("#estado")

let l1 = prompt("Nome: ")
nome.textContent = `Nome: ${l1}`

let l2 = prompt("Data de Nascimento: ")
nasc.textContent = `Data de Nascimento: ${l2}`

let l3 = prompt("Endereço: ")
endereco.textContent = `Endereço: ${l3}`

let l4 = prompt("Cidade: ")
cidade.textContent = `Cidade: ${l4}`

let l5 = prompt("Estado: ")
estado.textContent = `Estado: ${l5}`