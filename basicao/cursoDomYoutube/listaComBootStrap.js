const bekigraundi = document.querySelector('body')
bekigraundi.style.backgroundColor = 'lightGrey';

//VETORES || ARRAYS

let frutas = [];
console.log(frutas); 
/*Array []
    length: 0
    <prototype>: Array []*/
frutas.push('banana');
frutas.push('maca');
frutas.push('laranja');
frutas.push('uva');
console.log(frutas);
frutas.pop();
console.log(frutas);
frutas.unshift('badalo')//<-- insere no inicio
console.log(frutas);
frutas.shift(); //<-- remove do inicio
console.log(frutas);
console.log(frutas.indexOf('banana'));
console.log(frutas.includes('banana'));
console.log(frutas.join('')); // <--- transforma em string, tudo junto
console.log(frutas.join(', '));// <--- transforma em string. separando com vírgula
console.log(frutas.reverse());
console.log(frutas.sort());
console.log(frutas[2]);
frutas[3] = 'xerereca'
console.log(frutas);

//OBJETOS
let pessoa = {
    nome: 'Geraldo',
    idade: 33,
    email: 'bengalamajor@itau.com.us',
    telefone: '99955533388',
    senha: '123456',
    deAcordoTermos: true,
    "quero-comprar": false, //<-----caracteres especiais
    criadoEm: new Date(),
    andar: function() {
        console.log('andando');
    }
}

pessoa.beleza = true;
console.log(pessoa.beleza);

console.log(pessoa);
console.log(pessoa['senha']);
console.log(pessoa.email);
console.log(pessoa['quero-comprar']); //<-----caracteres especiais
console.log(pessoa.criadoEm);
console.log(pessoa.criadoEm.getFullYear());
console.log(pessoa.criadoEm.getMonth());
console.log(pessoa.andar());


//UM POUCO DE FUNÇÕES

function xablau() {
    console.log('Bin Laden');
}
xablau('Bin Laden');

let contagem = 0;
console.log(frutas.forEach((fruta)=>{
    console.log(`número de frutas: ${contagem}`);
    console.log(fruta);
    contagem ++
}));
console.log(`contagem final: ${contagem}`);

frutas.forEach(function(valor, indice) {
    console.log(`indice: ${indice}, valor: ${valor}`);
});


let novoArray = frutas.map(function(valor, indice) {
    console.log(indice, valor);
    return valor + ' - ' + 'tá vendo';
});
console.log(novoArray);

//REPASSANDO CAPTURA DE ELEMENTOS

let bla = document.querySelector('.container form button')
console.log(bla);

// bla.innerHTML = "<span>testando</span>"
// bla.innerText = "<span>testando</span>"
bla.textContent = "<span>testando</span>"
let itemLista = document.querySelector('li');
console.log(itemLista);
let itensLista = document.querySelectorAll('li');
console.log(itensLista);

////////////////////////////////////////////////////////////////////

//AGORA SIM, EVENTOS e LocalStorage:
let elementoInput = document.querySelector('input');
let elementoButton = document.querySelector('button');
let listaDeElementos = document.querySelector('ul');

//puxa já convertendo, mas pode puxar e depois converter
let tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];

elementoButton.addEventListener('click', function() {
    console.log('clicou');
    console.log(elementoInput.value)
    let valorInput = elementoInput.value;
    if (valorInput === '') return; // evita adicionar vazio

    tarefas.push(valorInput);
    console.log(tarefas);
    elementoInput.value = '';

    //parte de criar novo item no html:
    let novoItem = document.createElement('li');
    novoItem.classList.add('list-group-item');
// novoItem.setAttribute('class', 'list-group-item');
    novoItem.innerText = valorInput;
    listaDeElementos.appendChild(novoItem);
    
    //const tarefasConvertidas = JSON.stringify(tarefas);
    localStorage.setItem('tarefas', JSON.stringify(tarefas));
});
//ou apenas if(tarefas){}
if (tarefas.length > 0){
    tarefas.forEach(tarefa => {

    let novoItem = document.createElement('li');
    novoItem.classList.add('list-group-item');
// novoItem.setAttribute('class', 'list-group-item');
    novoItem.innerText = tarefa; //aqui não mais o input
    listaDeElementos.appendChild(novoItem);

})
}

//versão melhorada
/*
let tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];
    // Função para renderizar a lista
        function renderizarTarefas() {
            listaDeElementos.innerHTML = ''; // limpa a lista atual --> retirar para manter os elementos "fixos"
            tarefas.forEach(tarefa => {
                let novoItem = document.createElement('li');
                novoItem.innerText = tarefa;
                novoItem.setAttribute('class', 'list-group-item');
                listaDeElementos.appendChild(novoItem);
            });
        }

        // Chama a função para mostrar as tarefas salvas
        renderizarTarefas();

        // Evento de clique no botão
        elementoButton.addEventListener('click', function () {
            let valorInput = elementoInput.value.trim();
            if (valorInput === '') return; // evita adicionar vazio

            tarefas.push(valorInput);
            localStorage.setItem('tarefas', JSON.stringify(tarefas));
            elementoInput.value = '';

            renderizarTarefas(); // atualiza a lista
        });
*/

