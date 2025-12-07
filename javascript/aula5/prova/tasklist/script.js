const input = document.getElementById("inputTarefa");
    const lista = document.getElementById("lista");
    const btnAdd = document.getElementById("btnAdd");

    let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];

    const salvar = () =>
        localStorage.setItem("tarefas", JSON.stringify(tarefas));

    const atualizarLista = () => {
        lista.innerHTML = "";

        tarefas.forEach((t, i) => {
            const li = document.createElement("li");

            li.innerHTML = `
                <span class="${t.concluida ? "concluida" : ""}">${t.descricao}</span>
                <div class="botoes">
                    <button class="btn-ok">✔</button>
                    <button class="btn-remove">🗑</button>
                </div>
            `;

            li.querySelector(".btn-ok").onclick = () => concluirTarefa(i);
            li.querySelector(".btn-remove").onclick = () => removerTarefa(i);

            lista.appendChild(li);
        });
    };

    const adicionarTarefa = () => {
        const texto = input.value.trim();
        if (!texto) return alert("Digite uma tarefa!");

        tarefas.push({ descricao: texto, concluida: false });

        salvar();
        atualizarLista();

        input.value = "";
        input.focus();
    };

    const removerTarefa = (i) => {
        tarefas.splice(i, 1);
        salvar();
        atualizarLista();
    };

    const concluirTarefa = (i) => {
        tarefas[i].concluida = !tarefas[i].concluida;
        salvar();
        atualizarLista();
    };

    // Permitir adicionar usando ENTER
    input.addEventListener("keypress", e => {
        if (e.key === "Enter") adicionarTarefa();
    });

    btnAdd.onclick = adicionarTarefa;

    atualizarLista();
    input.focus();