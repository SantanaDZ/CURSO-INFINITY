let quantidade = 0
let text = prompt("Digite um texto: ")
let vogais = 'aeiouAEIOU'

for (let letra of text){
    if (vogais.includes(letra)){
        quantidade++

    }     
}

alert('O número de vogais é: ' +quantidade)