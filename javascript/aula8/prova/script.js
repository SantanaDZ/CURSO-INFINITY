// Em JavaScript, objetos literais são uma maneira simples de criar objetos, agrupando propriedades e métodos. Eles são criados usando chaves {}, dentro das quais você define as propriedades e métodos que o objeto deve ter.

// Por exemplo, podemos criar um objeto chamado aluno, que vai conter as seguintes propriedades e métodos:

// nome: uma string com o nome do aluno.

// notas: um array com as notas do aluno.

// calcularMedia(): um método que vai calcular a média das notas do aluno.

// Aqui está o código que implementa isso:

// Criando o objeto aluno
const aluno = {
    nome: "Maria",
    notas: [8, 7.5, 9, 6.5],

    // Método para calcular a média das notas
    calcularMedia: function() {
        const soma = this.notas.reduce((acc, nota) => acc + nota, 0);
        return soma / this.notas.length;
    }
};

// Usando a desestruturação para acessar a propriedade "nome"
const { nome } = aluno;
console.log(`Nome do aluno: ${nome}`);  // Saída: Nome do aluno: Maria

// Usando o spread operator para adicionar uma nova nota
aluno.notas = [...aluno.notas, 10];  // Adiciona a nota 10 ao final do array
console.log(`Notas após adicionar uma nova: ${aluno.notas}`); // Saída: Notas após adicionar uma nova: 8,7.5,9,6.5,10

// Calculando a média das notas
console.log(`Média das notas: ${aluno.calcularMedia()}`);  // Saída: Média das notas: 8.0



// O que acontece no código?

// Objeto aluno:

// O objeto tem duas propriedades: nome, que é uma string, e notas, que é um array de números.

// Tem também um método calcularMedia(), que usa o reduce() para somar as notas e depois calcula a média.

// Desestruturação:

// A desestruturação é usada para pegar diretamente a propriedade nome do objeto e armazená-la em uma variável com o mesmo nome. No código, isso é feito com const { nome } = aluno;.

// Spread Operator:

// O spread operator ...aluno.notas cria uma cópia do array de notas e adiciona uma nova nota (10) ao final. Isso é feito de maneira imutável, ou seja, o array original não é modificado diretamente.

// O que você verá ao executar o código?

// Nome do aluno será exibido no console com a desestruturação.

// Notas: o spread operator adiciona uma nova nota (10) ao array de notas.

// Média: o método calcularMedia() vai calcular e exibir a média das notas.