//ESTILOS BÁSICO INLINE
const titulo = document.getElementById("main-heading");
//ou
const titulao = document.querySelector("#main-heading");
console.log(titulao);
//<h1 id="main-heading" style="color: pink;">Filme Favorito</h1>
titulao.style.color = "pink";

const itemLista = document.querySelectorAll(".list-item");
console.log(itemLista);
//NodeList(5) [li.list-item, li.list-item, li.list-item, li.list-item, li.list-item]
//0: li.list-item
itemLista[2].style.color = "blue";
console.log('tentando aumentar fonte');
//FOR MAIS SIMPLES
for (let itenzinho of itemLista) {
   itenzinho.style.fontSize = "32px";
}
//SEGUNDO FOR
for(i = 0; i < itemLista.length; i++) {
    if(i % 2 == 0) {
        itemLista[i].style.backgroundColor = "lightYellow";
    }
}
//FOREACH
itemLista.forEach((coisinha) => {
    coisinha.style.textDecoration = "underline";
})
console.log(itemLista);

//CREATING ELEMENTS
//nesse caso primeiro seleciona a lista que receberá um novo item
const unorderedList = document.querySelector("ul");
//depois o item
const listItem1 = document.createElement("li");
//usar o método .append()
unorderedList.append(listItem1)
//modificar o texto
const primeiroItemAchado = document.querySelector(".list-item");

console.log(primeiroItemAchado.innerText); //só os textos
console.log(primeiroItemAchado.textContent);//mostra algo mais
console.log(primeiroItemAchado.innerHTML);//tudo dentro do elemento, incluindo outro elemento

listItem1.innerText = "funciona praga";

/***************************************************************** */

//MODIFICANDO ATRIBUTOS E CLASSES
//atributos podem ser: alt, src, placeholder...
console.log('abaixo tentando mexer em atributos')

listItem1.setAttribute('class', 'list-item');
//recebe o estilo da class/ID passado
//MAS... precisa ter um CSS externo para o novo elemento criado "herdar" as características
listItem1.removeAttribute('class');


console.log(titulao.getAttribute('id'))
const imagenzinha = document.getElementById('minhaImagem');
console.log(imagenzinha.getAttribute('alt')); 
//ou:
let altText = minhaImagem.getAttribute('alt');
console.log(altText);
//ou ainda:
console.log(minhaImagem.getAttribute('src'));

imagenzinha.setAttribute('alt', 'imagem fictícia');
console.log(imagenzinha.getAttribute('alt'));//imagem fictícia
imagenzinha.removeAttribute('alt')
console.log(imagenzinha.getAttribute('alt')); //null

listItem1.classList.add('list-item');
listItem1.classList.remove('list-item');
console.log(listItem1.classList.contains('list-item'));

// listItem1.classList.toggle('active');

listItem1.setAttribute('class', 'list-item'); //recebe a classe mas ñ o CSS pq não tenho um CSS



















