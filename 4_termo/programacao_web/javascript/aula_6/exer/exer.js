const resul = document.querySelector("#resul")
const but1 = document.querySelector("#but1")
const but2 = document.querySelector("#but2")

function input() {
    let n1 = Number(prompt("Número 1: "))
    let n2 = Number(prompt("Número 2: "))
    return [n1, n2]
}

function soma() {
    const lista = input()
    let soma = lista[0] + lista[1]
    resul.textContent = `Resultado [soma]: ${soma}`
}
but1.onclick = soma

function multi() {
    const lista = input()
    resul.textContent = `Resultado [multiplicação]: ${lista[0] * lista[1]}`
}
but2.onclick = multi