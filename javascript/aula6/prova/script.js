// Lista de tarefas
let tarefas = [];

// Função anônima para adicionar tarefas
const adicionarTarefa = function(tarefa) {
    tarefas.push({ descricao: tarefa, concluida: false });
    console.log(`Tarefa adicionada: ${tarefa}`);
};

// Arrow function para listar todas as tarefas
const listarTarefas = () => {
    console.log("Lista de Tarefas:");
    if (tarefas.length === 0) {
        console.log("Nenhuma tarefa cadastrada.");
    } else {
        tarefas.forEach((tarefa, index) => {
            const status = tarefa.concluida ? " ✅ Concluída" : "";
            console.log(`${index + 1}. ${tarefa.descricao}${status}`);
        });
    }
};

// Função de callback para manipular a lista de tarefas
const manipularTarefa = (acao, indice, novaTarefa) => {
    if (acao === 'remover') {
        tarefas.splice(indice, 1);
        console.log(`Tarefa removida: ${indice + 1}`);
    } else if (acao === 'atualizar') {
        tarefas[indice].descricao = novaTarefa;
        console.log(`Tarefa atualizada: ${indice + 1} para "${novaTarefa}"`);
    } else if (acao === 'concluir') {
        tarefas[indice].concluida = true;
        console.log(`Tarefa concluída: ${indice + 1}`);
    } else {
        console.log('Ação desconhecida');
    }
};

// Função para interagir com o usuário
const interagirComUsuario = () => {
    let sair = false;  // Variável para controlar o loop de interação

    while (!sair) {
        // Exibe as opções para o usuário
        const acao = prompt("Escolha uma ação: (adicionar, listar, remover, atualizar, concluir, sair)");

        if (acao === 'adicionar') {
            const tarefa = prompt("Digite a tarefa a ser adicionada:");
            adicionarTarefa(tarefa);
        } else if (acao === 'listar') {
            listarTarefas();
        } else if (acao === 'remover') {
            listarTarefas();
            const indice = parseInt(prompt("Digite o número da tarefa a ser removida:")) - 1;
            manipularTarefa('remover', indice);
        } else if (acao === 'atualizar') {
            listarTarefas();
            const indice = parseInt(prompt("Digite o número da tarefa a ser atualizada:")) - 1;
            const novaTarefa = prompt("Digite a nova descrição da tarefa:");
            manipularTarefa('atualizar', indice, novaTarefa);
        } else if (acao === 'concluir') {
            listarTarefas();
            const indice = parseInt(prompt("Digite o número da tarefa a ser concluída:")) - 1;
            manipularTarefa('concluir', indice);
        } else if (acao === 'sair') {
            console.log("Saindo...");
            sair = true;  // Define sair como true para encerrar o loop
        } else {
            console.log("Ação não reconhecida.");
        }
    }
};

// Chama a função de interação com o usuário
interagirComUsuario();
