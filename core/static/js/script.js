document.addEventListener("DOMContentLoaded", function () {
  // Atualiza ano no rodapé
  const anoAtual = new Date().getFullYear();
  const spanAno = document.getElementById("ano");
  if (spanAno) {
    spanAno.textContent = anoAtual;
  }

  // Alterna entre login e cadastro
  
});
const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("container");

signUpButton.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});
