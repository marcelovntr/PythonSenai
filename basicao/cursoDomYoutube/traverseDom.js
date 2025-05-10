//UPWARDS***********************
let ul = document.querySelector('ul');
console.log(ul);

console.log(ul.parentElement)
console.log(ul.parentNode)

console.log(ul.parentElement.parentElement)
console.log(ul.parentNode.parentNode)

const htmlzao = document.documentElement;
console.log(htmlzao.parentElement);
console.log(htmlzao.parentNode);

//DOWNWARDS**********************

let ulzinha = document.querySelector('ul');
console.log(ulzinha.childNodes); // NodeList(11) [text, li.list-item...
console.log(ulzinha.children); // HTMLCollection(5) [li.list-item...

console.log(ulzinha.firstChild); // #text
console.log(ulzinha.lastChild); // #text

// ul.firstChild.style.backgroundColor = "pink"; //Uncaught TypeError: Cannot set properties of undefined

ul.childNodes[1].style.backgroundColor = "pink";//precisa do índice

console.log(ulzinha.firstElementChild); // <li class="list-item">aaaaa</li>
console.log(ulzinha.lastElementChild); // <li class="list-item">xxxxx</li>

//SIBLING NODE TRAVERSAL**********
console.log(ulzinha) //the whole element
console.log(ulzinha.previousSibling); // #text
console.log(ulzinha.nextSibling); // #text

console.log(ulzinha.previousElementSibling); // <h1 id="main-heading">Filme Favorito</h1>
console.log(ulzinha.nextElementSibling) // <img src="https://cdn-icons-png.flaticon...

