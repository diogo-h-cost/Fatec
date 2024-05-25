const input = document.querySelector("#item")
const but_add = document.querySelector("#add")
const ul_list = document.querySelector("#list")

function add_list() {
    // Pega o conteudo digitado no input
    let item = input.value

    // Cria um novo elemento HTML na pagina
    let li = document.createElement("li")

    // Adiciona o LI dentro da lista
    ul_list.appendChild(li)

    // Coloca o [item] digitado como texto do LI
    li.textContent = item
}
but_add.onclick = add_list