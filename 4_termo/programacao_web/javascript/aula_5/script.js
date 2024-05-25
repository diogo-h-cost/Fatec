const n1 = document.querySelector("#n1")
const n2 = document.querySelector("#n2")
const med = document.querySelector("#med")
const resul = document.querySelector("#resul")

function calc_med(n1, n2) {
    let media = (n1 + n2) / 2.0

    med.textContent = `Média: ${media}`

    let resultado
    if (media >= 6.0) {
        resultado = "APROVADO(A)"
    }
    else {
        resultado = "REPROVADO(A)"
    }

    resul.textContent = `Resultado: ${resultado}`

    // alert(`Sua média de notas é ${media}: ${resultado}`)
}

// prompt > recebe tudo como String
let not1 = prompt("Primeira nota: ")
let not2 = prompt("Segunda nota: ")

n1.textContent = `Nota 1: ${not1}`
n2.textContent = `Nota 2: ${not2}`

calc_med(Number(not1), Number(not2))