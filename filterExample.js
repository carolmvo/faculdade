//O método filter() é um recurso que permite fazer a filtragem de elementos com apenas poucas linhas de comandos.

let numbers = [2, 5, 6, 8, 10, 12, 15, 16, 18, 20, 22, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 45, 46, 48]

function divCinco (value){
    if (value % 5 == 0) 
    return value;
}
var resultado = numbers.filter(divCinco);
console.log(resultado);