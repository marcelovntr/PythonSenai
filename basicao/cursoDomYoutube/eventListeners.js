const botao2 = document.querySelector('.btn-2');

//forma 1:****************************

function alertando() {
    alert('alertaaaaaaa');
}

botao2.addEventListener('click', alertando); //alertando() executa sempre q carregar pág

//forma 2:****************************
// botao2.addEventListener('click', function() {
//     alert('alertaaaaaaa');
// });

//MOUSEOVER

const newBoxThree = document.querySelector('.box-3');

newBoxThree.addEventListener('mouseover', function() {
    newBoxThree.style.backgroundColor = 'pink';
    newBoxThree.style.transform = 'scale(1.2)';
});
newBoxThree.addEventListener('mouseout', function() {
    newBoxThree.style.backgroundColor =' #575151';
    newBoxThree.style.transform = 'scale(1)';
});