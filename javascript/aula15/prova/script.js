document.getElementById('btnCarregar').addEventListener('click', carregarUsuarios);

async function carregarUsuarios() {
    const listaUI = document.getElementById('listaUsuariosAPI');
    const erroUI = document.getElementById('mensagemErro');

    // Resetar estado inicial ao clicar novamente (Requisito: Interatividade)
    listaUI.innerHTML = "";
    erroUI.innerText = "";

    try {
        // 1. Requisição à API (Requisito: fetch)
        const response = await fetch('https://jsonplaceholder.typicode.com/users');

        // 2. Verificação de status (Requisito: response.ok)
        if (!response.ok) {
            // Caso o status indique erro, lançamos um erro manual
            throw new Error(`STATUS_CODE_${response.status}`);
        }

        // 3. Conversão para JSON (Requisito: .json())
        const usuarios = await response.json();

        // 4. Manipulação de Dados e Criação Dinâmica (Requisito: createElement/appendChild)
        usuarios.forEach(user => {
            // Criar o item de lista (li)
            const li = document.createElement('li');
            
            // Estilização tech via JS para manter o tema
            li.style.padding = "12px";
            li.style.borderBottom = "1px solid #333";
            li.style.marginBottom = "5px";
            li.style.background = "rgba(255,255,255,0.02)";

            // Conteúdo (Requisito: Nomes e E-mails)
            li.innerHTML = `
                <span style="color: var(--accent-color); font-weight: bold;">[ID_${user.id}]</span> 
                <strong>${user.name}</strong> - 
                <span style="color: #888;">${user.email.toLowerCase()}</span>
            `;

            // Adicionar à lista pai (Requisito: appendChild)
            listaUI.appendChild(li);
        });

    } catch (error) {
        // 5. Tratamento de Erros (Requisito: try...catch e mensagem amigável)
        console.error("LOG_SISTEMA:", error);
        erroUI.innerText = "Erro ao carregar os usuários, tente novamente mais tarde.";
    }
}