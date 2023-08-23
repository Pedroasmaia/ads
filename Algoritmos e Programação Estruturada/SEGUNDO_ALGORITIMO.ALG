Algoritmo "segundo_algoritimo"
// Disciplina   : [Algortimos e Programação Estruturada]
// Professor   : Wesley Viana
// Descrição   : Verifica a maioridade do Usuário
// Autor(a)    : Pedro Augusto Souza Maia
// Data atual  : 19/08/2023
Var
// Seção de Declarações das variáveis 
a,b,resultado: inteiro
contador: inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite o potenciado: ")
leia(a)
escreva("Digite o potenciador: ")
leia(b)

contador <- 1
resultado <- 1

enquanto contador <=b faca
         resultado <- resultado * a
         contador <- contador + 1
fimenquanto

escreva("O resultado de ", a,"elevado a ",b," é: ", resultado)


Fimalgoritmo