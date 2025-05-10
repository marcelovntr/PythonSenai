function listarTarefas() {
    let listItems = document.querySelectorAll('ul li');
    listItems.forEach(item => { console.log(item.textContent); }); 
}

function adicionarTarefa() {
    const input = document.getElementById('nova-tarefa');
    const texto = input.value.trim();
  
    if (texto === '') {
      alert('Por favor, digite uma tarefa!');
      return;
    }

    const tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];
    tarefas.push(texto);
    localStorage.setItem('tarefas', JSON.stringify(tarefas));
  
    criarItemNaLista(texto);
    input.value = '';
  }
  

  function criarItemNaLista(texto, index = null) {
    const ul = document.querySelector('.lista-de-afazeres');
    const li = document.createElement('li');
    li.className = 'item-da-lista';
  
    const id = 'item' + (index !== null ? index : ul.children.length + 1);
  
    li.innerHTML = `
      <input type="checkbox" id="${id}">
      <label for="${id}">${texto}</label>
    `;
  
    ul.appendChild(li);
  }
  
  function carregarTarefasSalvas() {
    const tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];
    tarefas.forEach((tarefa, index) => {
      criarItemNaLista(tarefa, index + 1);
    });
  }
  
  // Executa quando a página carrega
  window.onload = carregarTarefasSalvas;