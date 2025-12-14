let nomes = [];

function adicionarNome(nome) {
  nomes.push(nome);
  console.log(`Nome "${nome}" adicionado com sucesso!`);
  console.log("Lista atualizada:", nomes);
}

function filtrarNomes(letra) {
  const nomesFiltrados = nomes.filter(
    (nome) => nome[0].toLowerCase() === letra.toLowerCase()
  );
  if (nomesFiltrados.length > 0) {
    console.log(`Nomes que começam com a letra "${letra}":`, nomesFiltrados);
  } else {
    console.log(`Nenhum nome encontrado que começa com a letra "${letra}".`);
  }
}

function buscarNomes(nomeBuscado) {
  const nomeEncontrado = nomes.find(
    (nome) => nome.toLowerCase() === nomeBuscado.toLowerCase()
  );
  if (nomeEncontrado) {
    console.log(`Nome encontrado: ${nomeEncontrado}`);
  } else {
    console.log(`Nome "${nomeBuscado}" não encontrado.`);
  }
}
function transformarNomes() {
  const nomesMaiusculos = nomes.map((nome) => nome.toUpperCase());
  console.log("Lista de nomes em maiúsculas: ", nomesMaiusculos);
}

function verificarCondicoes() {
  const resultado = nomes.every((nome) => nome.length > 3);
  console.log(`Todos os nomes têm mais de três caracteres? ${resultado}`);
}

const interagirComUsuario = () => {
  let sair = false;

  while (!sair) {
    const acao = prompt(
      "Escolha uma ação:\n1. Adicionar Nome\n2. Filtrar Nomes\n3. Buscar Nome\n4. Transformar Nomes em Maiúsculas\n5. Verificar se Todos os Nomes têm mais de 3 Caracteres\n6. Sair"
    );

    switch (acao) {
      case "1":
        const nomeAdicionar = prompt("Digite o nome para adicionar:");
        adicionarNome(nomeAdicionar);
        break;

      case "2":
        const letraFiltro = prompt("Digite a letra para filtrar os nomes:");
        filtrarNomes(letraFiltro);
        break;

      case "3":
        const nomeBusca = prompt("Digite o nome para buscar:");
        buscarNomes(nomeBusca);
        break;

      case "4":
        transformarNomes();
        break;

      case "5":
        verificarCondicoes();
        break;

      case "6":
        console.log("Saindo...");
        sair = true;
        break;

      default:
        console.log("Opção inválida! Tente novamente.");
        break;
    }
  }
};

// Chama a função para começar a interação com o usuário
interagirComUsuario();
