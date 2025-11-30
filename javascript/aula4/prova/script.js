let listaCompras = [];

while (true) {
    // Menu de opções
    let opcao = prompt(
        "=== Lista de Compras ===\n" +
        "1 - Adicionar item\n" +
        "2 - Remover item\n" +
        "3 - Atualizar item\n" +
        "4 - Exibir lista\n" +
        "5 - Sair\n\n" +
        "Digite o número da opção desejada:"
    );

    if (opcao === null || opcao === "5") {
        console.log("Encerrando o programa...");
        break;
    }

    switch (opcao) {
        case "1": // Adicionar item
            let novoItem = prompt("Digite o item a ser adicionado:");
            if (novoItem !== null && novoItem.trim() !== "") {
                listaCompras.push(novoItem.trim());
                console.log(`Item "${novoItem}" adicionado à lista.`);
            } else {
                console.log("Valor inválido. Item não adicionado.");
            }
            break;

        case "2": // Remover item
            if (listaCompras.length === 0) {
                console.log("A lista está vazia.");
                break;
            }
            let indiceRemover = prompt("Digite o índice do item a ser removido (começa em 0):");
            indiceRemover = Number(indiceRemover);
            if (!isNaN(indiceRemover) && indiceRemover >= 0 && indiceRemover < listaCompras.length) {
                let removido = listaCompras.splice(indiceRemover, 1);
                console.log(`Item "${removido}" removido da lista.`);
            } else {
                console.log("Índice inválido.");
            }
            break;

        case "3": // Atualizar item
            if (listaCompras.length === 0) {
                console.log("A lista está vazia.");
                break;
            }
            let indiceAtualizar = prompt("Digite o índice do item a ser atualizado (começa em 0):");
            indiceAtualizar = Number(indiceAtualizar);
            if (!isNaN(indiceAtualizar) && indiceAtualizar >= 0 && indiceAtualizar < listaCompras.length) {
                let novoValor = prompt("Digite o novo valor do item:");
                if (novoValor !== null && novoValor.trim() !== "") {
                    listaCompras[indiceAtualizar] = novoValor.trim();
                    console.log(`Item atualizado para "${novoValor}"`);
                } else {
                    console.log("Valor inválido. Atualização cancelada.");
                }
            } else {
                console.log("Índice inválido.");
            }
            break;

        case "4": // Exibir lista
            if (listaCompras.length === 0) {
                console.log("A lista está vazia.");
            } else {
                console.log("=== Lista de Compras ===");
                for (let i = 0; i < listaCompras.length; i++) {
                    console.log(`${i}: ${listaCompras[i]}`);
                }
            }
            break;

        default:
            console.log("Opção inválida. Digite um número entre 1 e 5.");
    }
}
