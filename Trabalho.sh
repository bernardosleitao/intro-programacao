#!/bin/bash

# Atribui os parâmetros posicionais a variáveis com nomes mais claros

NOME_PROFESSOR="$1"
NOME_DISCIPLINA="$2"
MEDIA_APROVACAO=6.0

# Verifica se os dois parâmetros foram fornecidos
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <nome_do_professor> <nome_da_disciplina>"
    exit 1
fi



rm resultado.txt
echo "Aluno,Trabalho,Teste,Prova,Media,Status" > resultado.txt


while true; do

# Exibe os dados recebidos
echo "Nome do Professor: $NOME_PROFESSOR"
echo "Nome da Disciplina: $NOME_DISCIPLINA"

echo "Informe o nome do aluno:"
read NOME

# Pedir as 3 notas
echo "Informe a nota do Trabalho:"
read TRABALHO

echo "Informe a nota do Teste:"
read TESTE 

echo "Informe a nota da Prova:"
read PROVA

# (Opcional) Calcular e exibir a média
# É necessário usar bc para cálculos de ponto flutuante em bash
MEDIA=$(echo "scale=2; ($TRABALHO + $TESTE + $PROVA) / 3" | bc)
SITUACAO=""

if [ "$(echo "$MEDIA >= $MEDIA_APROVACAO" | bc -l)" -eq 1 ]; then
    SITUACAO="APROVADO"
else
    SITUACAO="REPROVADO"
fi

echo "$NOME,$TRABALHO,$TESTE,$PROVA,$MEDIA,$SITUACAO" >> resultado.txt

echo "Continuar Sim ou Não - Digita S ou N"
read condicao_de_parada

if [ "$condicao_de_parada" != "S" ]; then
    break # Sai do loop
fi

done

