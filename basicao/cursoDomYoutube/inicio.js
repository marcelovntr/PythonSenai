// getElementByid
document.getElementById("main-heading").style.color = "red";
const titulo = document.getElementById("main-heading");
console.log(titulo);
console.log(`imprimindo variável: ${titulo}`); // <h1 id="main-heading">Filme Favorito</h1> (titulo)
console.log("imprimindo textContent: ", titulo.textContent);

//getElementByClassName

document.getElementsByClassName("list-item")[0].style.color = "blue";
const itemLista = document.getElementsByClassName("list-item");
console.log(itemLista); //HTMLCollection { 0: li.list-item, 1: li.list-item, 2: li.list-item, 3: li.list-item, 4: li.list-item, length: 5 }
console.log(`imprimindo variável: ${itemLista}`); // [object HTMLCollection]
console.log("imprimindo textContent: ", itemLista.textContent); // undefined
for (let itenzinho of itemLista) {
  console.log(itenzinho.textContent);
} // aaaaa, wwww, yyyyy, zzzzz, xxxxx

//getElementByTagName
const listinha = document.getElementsByTagName("li");
console.log(listinha); //HTMLCollection { 0: li.list-item, 1: li.list-item, 2: li.list-item, 3: li.list-item, 4: li.list-item, length: 5 }
console.log(`imprimindo variável: ${listinha}`); // [object HTMLCollection]
console.log("imprimindo textContent: ", listinha.textContent); // undefined
for (let itenzinho of listinha) {
  console.log(itenzinho.textContent);
  itenzinho.style.color = "green";
  itenzinho.style.textDecoration = "line-through";
} // aaaaa, wwww, yyyyy, zzzzz, xxxxx

//querySelector
const primeiroItemAchado = document.querySelector("div");
console.log(primeiroItemAchado); // <div class="container">
console.log(`imprimindo variável: ${primeiroItemAchado}`); // [object HTMLDivElement]
console.log("imprimindo textContent: ", primeiroItemAchado.textContent); /*  Filme Favorito       
aaaaa
wwwww
yyyyy
zzzzz
xxxxx*/

//querySelectorAll
const todosOsItens = document.querySelectorAll("li");
console.log(todosOsItens); //NodeList(5) [ li.list-item, li.list-item, li.list-item, li.list-item, li.list-item ]
console.log(`imprimindo variável: ${todosOsItens}`); // imprimindo variável: [object NodeList]
console.log("imprimindo textContent: ", todosOsItens.textContent); //imprimindo textContent:  undefined