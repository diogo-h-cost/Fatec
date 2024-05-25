let idade = prompt("Idade: ")
const idad = document.querySelector("#idad")

if (idade <= 18) {
    alert("Não pode dirigir")
}
else {
    alert("Pode dirigir")
}

let Pergunta = prompt("Quantas vezes o Brasil foi campeão do mundo: ")
let mundial = 5
const pergunta = document.querySelector(`#Pergunta`)

if (pergunta == mundial){
    alert("Você acertou")
}
else {
    alert("Você errou")
}

// F12 > Console (No Chrome)
console.log(`idade ${idade}`)
console.log(`Mundial do Brasil ${mundial}`)
console.log(`pergunta ${pergunta}`)