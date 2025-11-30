let negativos = 0
for (let i = 0; i < 4; i++){
    let num = Number(prompt("Digite um número: "))
    if (num < 0){
       negativos++
    }
}    
alert("O número de negativos é: " +negativos )
