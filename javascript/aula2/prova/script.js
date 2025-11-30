let idade = Number(prompt("Digite sua idade: "));
const status = prompt(
  "Digite seu status (registrado / não registrado):").toLowerCase();
console.log(status);

let maioridade = false;

if (idade >= 18) {
  maioridade = true;
}

switch (status) {
  case "registrado":
    console.log("Bem-vindo !");
    break;

  case "nao registrado":
  case "não registrado":
    console.log("Por favor, complete seu cadastro");
    break;
  default:
    console.log("Status desconhecido");
}

if (maioridade && status == "registrado") {
  console.log("Acesso completo.");
} else if (maioridade == false || status !== "registrado") {
  console.log("Acesso limitado.");
}
