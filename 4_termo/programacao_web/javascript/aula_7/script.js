const h2 = document.querySelector("h2")
const but_aum = document.querySelector("#aum")
const but_dim = document.querySelector("#dim")
const but_zerar = document.querySelector("#zerar")

let cont = 0

function aumentar() {
    cont ++
    h2.textContent = cont
}
but_aum.onclick = aumentar

function diminuir() {
    if (cont > 0) {
        cont --
    }
    else {
        cont = 0
    }
    h2.textContent = cont
}
but_dim.onclick = diminuir

function zera_cont() {
    cont = 0
    h2.textContent = cont
}
but_zerar.onclick = zera_cont