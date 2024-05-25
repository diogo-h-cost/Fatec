// prompt (funcao) > Janela com input
let num1 = Number(prompt("Numero 1: "))
// Variavel que recebe o retorno do prompt

/*
O retorno do PROMPT é uma String, entao tem que converter
Number > Converte p/ numero
!!! Se não converter ele concatena -> 20 + 20 = 2020 (String)
*/
let num2 = Number(prompt("Numero 2: "))

let resul = num1 + num2
alert(`Soma -> ${num1} + ${num2} = ${resul.toFixed(2)}`)

resul = num1 - num2
alert(`Subtração -> ${num1} - ${num2} = ${resul.toFixed(2)}`)

resul = num1 * num2
alert(`Multiplicação -> ${num1} x ${num2} = ${resul.toFixed(2)}`)

resul = num1 / num2
alert(`Divisão-> ${num1} / ${num2} = ${resul.toFixed(2)}`)