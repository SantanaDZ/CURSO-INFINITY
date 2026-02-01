// 1. Selecionar os elementos que vamos manipular
const input = document.querySelector('#inputTarefa');
const btnAdicionar = document.querySelector('#btnAdicionar');
const lista = document.querySelector('#listaTarefas');

// Função para adicionar tarefa
function adicionarTarefa() {
    const textoTarefa = input.value;

    if (textoTarefa.trim() === "") {
        alert("Por favor, digite uma tarefa!");
        return;
    }

    // 2. Criar o elemento <li> (o item da lista)
    const novoItem = document.createElement('li');
    
    // 3. Criar um span para o texto (ajuda a separar do botão de remover)
    const spanTexto = document.createElement('span');
    spanTexto.textContent = textoTarefa;

    // 4. Criar o botão de remover
    const btnRemover = document.createElement('button');
    btnRemover.textContent = 'Remover';
    btnRemover.classList.add('btn-remover');

    // 5. Adicionar os elementos dentro do <li>
    novoItem.appendChild(spanTexto);
    novoItem.appendChild(btnRemover);

    // 6. Adicionar o <li> na nossa <ul>
    lista.appendChild(novoItem);

    // Limpar o campo de entrada
    input.value = "";

    // EVENTO: Marcar como concluída (clicando no texto)
    spanTexto.addEventListener('click', function() {
        novoItem.classList.toggle('concluida');
    });

    // EVENTO: Remover tarefa
    btnRemover.addEventListener('click', function() {
        // Usando removeChild como solicitado no requisito (Pai remove o Filho)
        lista.removeChild(novoItem);
    });
}

// Escutar o clique no botão principal
btnAdicionar.addEventListener('click', adicionarTarefa);

// Bônus: Permitir adicionar apertando a tecla "Enter"
input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        adicionarTarefa();
    }
});