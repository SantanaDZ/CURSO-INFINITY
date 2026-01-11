// function gerarRelatorio() {
//     // Captura dos elementos do DOM
//     const nomeVal = document.getElementById('nome').value;
//     const idadeVal = Number(document.getElementById('idade').value);
//     const n1 = document.getElementById('n1').value;
//     const n2 = document.getElementById('n2').value;
//     const n3 = document.getElementById('n3').value;
//     const nExtra = document.getElementById('nExtra').value;

//     // 1. Declarar o objeto aluno
//     const aluno = {
//         nome: nomeVal,
//         idade: idadeVal,
//         notas: [Number(n1), Number(n2), Number(n3)],

//         // 2. Método para calcular a média
//         calcularMedia() {
//             const soma = this.notas.reduce((acc, nota) => acc + nota, 0);
//             return (soma / this.notas.length).toFixed(2);
//         }
//     };

//     // 3. Utilizar desestruturação para acessar nome e idade
//     const { nome, idade } = aluno;

//     // 4. Usar o spread operator CONDICIONALMENTE
//     // Só adiciona se o campo não estiver vazio
//     if (nExtra !== "") {
//         aluno.notas = [...aluno.notas, Number(nExtra)];
//     }

//     // 5. Função verificarSituacao
//     function verificarSituacao(media) {
//         return media >= 7 ? "Aprovado" : "Reprovado";
//     }

//     const mediaFinal = aluno.calcularMedia();
//     const situacao = verificarSituacao(mediaFinal);

//     // --- EXIBIÇÃO NO CONSOLE ---
//     console.clear();
//     console.log("%c--- BOLETIM ESCOLAR ---", "color: blue; font-weight: bold;");
    
//     // Nome e idade desestruturados
//     console.log(`Aluno: ${nome}`);
//     console.log(`Idade: ${idade} anos`);

//     // 6. Loop para exibir todas as notas
//     console.log("Notas:");
//     aluno.notas.forEach((nota, index) => {
//         console.log(`  Avaliação ${index + 1}: ${nota}`);
//     });

//     console.log("-----------------------");
//     console.log(`Média Final: ${mediaFinal}`);
//     console.log(`Situação: ${situacao}`);
// }


function gerarRelatorio() {
    const nomeVal = document.getElementById('nome').value;
    const idadeVal = Number(document.getElementById('idade').value);
    const n1 = document.getElementById('n1').value;
    const n2 = document.getElementById('n2').value;
    const n3 = document.getElementById('n3').value;
    const nExtra = document.getElementById('nExtra').value;

    // Validação simples
    if (!nomeVal || !n1 || !n2 || !n3) {
        alert("Por favor, preencha o nome e as 3 notas básicas.");
        return;
    }

    const aluno = {
        nome: nomeVal,
        idade: idadeVal,
        notas: [Number(n1), Number(n2), Number(n3)],
        calcularMedia() {
            const soma = this.notas.reduce((acc, nota) => acc + nota, 0);
            return (soma / this.notas.length).toFixed(2);
        }
    };

    const { nome, idade } = aluno;

    // Spread operator apenas se houver nota extra
    if (nExtra.trim() !== "") {
        aluno.notas = [...aluno.notas, Number(nExtra)];
    }

    function verificarSituacao(media) {
        return media >= 7 ? "Aprovado" : "Reprovado";
    }

    const mediaFinal = aluno.calcularMedia();
    const situacao = verificarSituacao(mediaFinal);

    // --- SAÍDA NO CONSOLE ---
    console.clear();
    console.log("BOLETIM GERADO:");
    console.log(`Aluno: ${nome} | Idade: ${idade}`);
    console.log("Notas registradas:");
    aluno.notas.forEach((n, i) => console.log(` Nota ${i+1}: ${n}`));
    console.log(`Média: ${mediaFinal} -> ${situacao}`);

    // Feedback visual já que não podemos abrir o console sozinhos
    alert("Relatório gerado com sucesso! Aperte F12 para visualizar os detalhes no Console.");
}