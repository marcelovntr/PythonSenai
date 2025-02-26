console.log('O lucro foi de', 999);

let lucro = 666;
console.log("Lucramos", lucro.toFixed(2));

let numero = 666.75;

console.log("Arredondado para baixo:", Math.floor(numero)); // 666
console.log("Arredondado para cima:", Math.ceil(numero));   // 667

/*STRINGS*/

let email = 'meupau@deoculos.com';
let nome = "feião mazanza";
let cpf = "99955533388";

// Interpolação de strings (similar ao f-string do Python)
console.log(`dados pessoais: email - ${email}, nome - ${nome}, cpf - ${cpf}`);


let email_user = 'bengalamajor@itau.com.us'.toUpperCase();
console.log(email_user);

email_user = email_user.toLowerCase();
console.log(email_user);

let arrouba = email_user.indexOf('@');
//ou findIndex()
console.log(arrouba); 
//find() é apenas apra arrays!!!!!!!!!!!!!!!!!!!!

console.log(email_user[17]); // 't' (equivalente a email_user[17] em Python)

// 2. Último caractere (equivalente a email_user[-1])
console.log(email_user[email_user.length - 1]); // 's' (não existe índice negativo direto em JS)

// 3. Slice até o índice 8 (equivalente a email_user[:8] em Python)
console.log(email_user.slice(0, 8)); // "bengalam"

// 4. Slice do índice 0 até o 8 (excluindo o 9, como Python faz com email_user[0:9])
console.log(email_user.slice(0, 9)); // "bengalama"

// 5. Slice do início até o final (equivalente a email_user[0:])
console.log(email_user.slice(0)); // "bengalamajor@itau.com.us" (copia a string inteira)

// Substituir parte da string (equivalente a replace() do Python)
let novo_email = email_user.replace("itau.com.us", "gmail.com");
console.log(novo_email); // "bengalamajor@gmail.com"

// Primeira letra maiúscula (equivalente a capitalize() do Python)
let nomeCapitalizado = nome.charAt(0).toUpperCase() + nome.slice(1);
console.log(nomeCapitalizado); // "Feião mazanza"

// Todas as iniciais maiúsculas (equivalente a title() do Python)
let nomeTitleCase = nome
  .split(" ") // Divide a string em um array de palavras
  .map(palavra => palavra.charAt(0).toUpperCase() + palavra.slice(1)) // Capitaliza cada palavra
  .join(" "); // Junta de volta em uma string
console.log(nomeTitleCase); // "Feião Mazanza"