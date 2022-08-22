//Usado para encontrar um valor cumulativo ou concatenado com base em elementos de todo o vetor
const ages = [
    {filho: "José", idade: 32},
    {filho: "Antonio", idade: 29},
    {filho: "Maria", idade: 40},
    {filho: "Rafael", idade: 25}
]

const totalIdade = ages.reduce((prevVal, elem) => prevVal + elem.idade, 0)
console.log(totalIdade)

//No exemplo acima, o reduce faz com que a soma de todos os termos (idades) presentes no array sejam calculadas de forma
//mais fácil, com um código menor.