const tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];

const addTask = () => {
//   event.preventDefault();

  const ul = document.querySelector(".lista-tarefas");
  const li = document.createElement("li");
  const input = document.querySelector("input").value;
  //acessar o input vindo do campo input

  li.textContent = input;

  ul.appendChild(li);

  // Recupera o que já tem no localStorage (ou array vazio se não tiver nada)
  const tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
  tarefas.push(input); // adiciona nova tarefa
  localStorage.setItem("tarefas", JSON.stringify(tarefas)); // salva de volta

  document.querySelector("input").value = "";
  loadTasks();
};

if (tarefas){
const ul = document.querySelector(".lista-tarefas");

tarefas.forEach((tarefa) => {
  const li = document.createElement("li");
  li.textContent = tarefa;
  ul.appendChild(li);
});
loadTasks();
// Conectar o formulário ao addTask
const form = document.getElementById("form-tarefa");
form.addEventListener("submit", addTask);
}
// window.onload = () => {

//     const tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];
//         const ul = document.querySelector('.lista-tarefas')

//         tarefas.forEach(tarefa => {
//         const li = document.createElement('li');
//         li.textContent = tarefa;
//         ul.appendChild(li);
//     });
//     loadTasks();
//      // Conectar o formulário ao addTask
//     const form = document.getElementById('form-tarefa');
//     form.addEventListener('submit', addTask);
// }

function logOut() {
  localStorage.clear();
  location.reload();
}

function loadTasks() {
  const tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
  const numeroTarefas = tarefas.length;

  document.getElementById("contador-tarefas").textContent = numeroTarefas;
}
