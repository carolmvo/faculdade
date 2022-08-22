//O método map é invocado a partir de um array e recebe como parâmetro uma função
//de callback, que é invocada para cada item e retorna o valor do item equivalente no array resultante.

let numbers = [5, 10, 15, 20, 25, 30]

let quadrado = numbers.map(function(element){
    return element * element;
});

console.log(numbers)
console.log(quadrado)

//No exemplo acima, pegamos a o vetor original e substituímos por um outro com todos os seus valores ao quadrado,
//ou seja, todos foram alterados.