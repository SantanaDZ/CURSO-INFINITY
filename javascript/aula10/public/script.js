 const pMensagem = document.getElementById("mensagem");
      const produtoForm = document.getElementById("produto-form");
      const produtosTable = document.getElementById("produtos-table");

      function mostrarMensagem(text, type) {
        pMensagem.innerText = text;

        pMensagem.style.fontWeight = "bold";
        pMensagem.style.color = type == "success" ? "green" : "red";
      }

      function adicionarProdutoTabela(produto) {
        const tableData = produtosTable.querySelector("tbody");
        tableData.innerHTML += `
            <tr>
              <td>${produto.nome}</td>
              <td>${produto.preco.toLocaleString("pt-BR", {
                style: "currency",
                currency: "BRL",
              })}</td>
              <td>${produto.categoria}</td>
            </tr>
        `;
      }

      produtoForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const produto = {
          nome: produtoForm.nome.value.trim(),
          preco: produtoForm.preco.value.trim(),
          categoria: produtoForm.categoria.value,
        };

        if (produto.nome === "") {
          mostrarMensagem("O campo nome é obrigatório.", "error");
          return;
        }

        if (produto.preco === "") {
          mostrarMensagem("O campo preço é obrigatório.", "error");
          return;
        }

        produto.preco = Number(produto.preco);

        if (produto.preco <= 0) {
          mostrarMensagem("O preço deve ser maior que zero.", "error");
          return;
        }

        produto.categoria = produto.categoria === "" ? null : produto.categoria;

        mostrarMensagem("Produto cadastrado com sucesso.", "success");
        adicionarProdutoTabela(produto);

        produtoForm.reset();
      });