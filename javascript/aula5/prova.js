let tarefas = [];
function AdcionarTarefa (tarefa){
    tarefa = prompt("Qual tarefa deseha adicionar a sua lista? ")
    tarefas.push(tarefa)
    
}



function ListarTarefas(){
    for (i in tarefas){
    console.log(`${i} - ${tarefas[i]}`)
} 
}

function RemoverTarefa(i){
    i = prompt("Qual índice da tarefa que deseja remover? ")
    tarefas.splice(i, 1)
}

function ConcluirTarefa(i){
    i = prompt("Qual índice da tarefa que deseja concluir ? ")
    
}

while (true){
    opcao = Number(prompt("Digite a opção que deseja \n 1.Adicionar Tarefa \n 2.Listar Tarefa \n 3.Remover Tarefa \n 4.Sair"))

    if (opcao==1){
        AdcionarTarefa()

    }
    if (opcao==2){
        ListarTarefas()

    }
    if (opcao==3){
        RemoverTarefa()

    }
     if (opcao==4){
        break

    }
}


