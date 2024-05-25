const inp_num1 = document.querySelector("#num1")
const inp_num2 = document.querySelector("#num2")
const but_adi = document.querySelector("#but_adi")
const but_sub = document.querySelector("#but_sub")
const but_div = document.querySelector("#but_div")
const but_mult = document.querySelector("#but_mult")
const p_resul = document.querySelector("#resultado")

function input() {
    let n1 = Number(inp_num1.value)
    let n2 = Number(inp_num2.value)
    return [n1, n2]
}

function somar() {
    // Converter p/ nº, se nao concatena [n1 e n2]
    list = input()
    let calculo = list[0] + list[1]
    p_resul.textContent = `Resultado da soma = ${calculo}`
}
// Associar a funcao c/ o click nao vai ( )
but_adi.onclick = somar

function subtrair() {
    list = input()
    let calculo = list[0] - list[1]
    p_resul.textContent = `Resultado da subtração = ${calculo}`
}
but_sub.onclick = subtrair

function dividir() {
    list = input()
    if (list[1] == 0) {
        p_resul.textContent = "ERRO dividir por 0"
    }
    else {
        let calculo = list[0] / list[1]
        p_resul.textContent = `Resultado da divisão = ${calculo}`
    }
}
but_div.onclick = dividir

function multiplicar() {
    list = input()
    let calculo = list[0] * list[1]
    p_resul.textContent = `Resultado da multiplicação = ${calculo}`
}
but_mult.onclick = multiplicar