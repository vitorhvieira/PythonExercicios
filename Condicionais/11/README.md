# Exercício 11

## Valor da parcela do Sucesso Compartilhado

Na Cubos Academy alguns estudantes podem fazer o Curso de Desenvolvimento de Software e só começar a pagar após finalizado o curso quando (e se) tiverem obtido renda acima de R$ 2.000,00. Nesse caso o valor da parcela a ser paga é de 18% do valor da renda mensal da pessoal.

Após 60 meses, independente de ter quitado ou não o valor total do curso (de R$ 18.000,00) a pessoa não deve nada, ou seja, o valor da parcela é zero.

**a)** Faça um programa que calcula o valor da parcela a ser paga pelo aluno. Imprima uma mensagem bonita na tela, com o valor em reais.

```javascript
const rendaMensalEmCentavos = 300000;

// Tempo decorrido de contrato. Se for maior que 60 meses, o aluno não deve mais nada.
const mesesDecorridos = 12;

/* 
Soma das parcelas já pagas pelo aluno nos meses anteriores (em centavos). 
Se for igual a 18 mil reais, o aluno não deve pagar mais nada,
pois já quitou a dívida.
*/
const totalJaPagoPeloAluno = 1000000;
```

Para o exemplo acima, o programa deve imprimir a mensagem:

```
    O valor da parcela desse mês é R$ 540 reais
```
