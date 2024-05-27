const input_item = document.querySelector("#item")
const input_uni = document.querySelector("#uni")
const input_prec = document.querySelector("#prec")
const list = document.querySelector("#lista")
const button = document.querySelector("#but")

function add_item() {
    let new_item = input_item.value
    let uni = input_uni.value
    let preco = input_prec.value

    // Cria o elemento LI
    let li = document.createElement("li")

    // Add na LIST o LI
    list.appendChild(li)
    li.textContent = `Item: ${new_item} | Quantidade: ${uni} | Preco: ${preco}`

    // Risca o item [LI] quando clica nele
    li.onclick = function marcar() {
        li.style.textDecoration = "line-through"
    }

    // Deleta o item [LI] quando clica 2x nele
    li.ondblclick = function remover() {
        list.removeChild(li)
    }

    // Zera o valor dos inputs
    input_item.value = ""
    input_uni.value = ""
    input_prec.value = ""
}
button.onclick = add_item