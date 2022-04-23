# kernel_panik

**Número da Lista**: StackTraceError<br>
**Conteúdo da Disciplina**: Final<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0033620  |  João Henrique C. Paulino |
| 18/0052845  |  Gabriela da Gama Pivetta |

## Sobre 
![panikito](img/panik.jpeg)

Kernel panic, a versão Linux da tela azul da morte do Windows.
Ambos são provenientes de erros do kernel de sistemas
operacionais e são lançados quando o S.O. está sofrendo.
O processo é tão traumático que os programadores buscam 
ao máximo evitar esta situação, o que leva a implementação
de técnicas extremamente sofisticadas para evitar isso.

Uma versão humana do Kernel panic é o [burnout](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/sindrome-de-burnout#:~:text=S%C3%ADndrome%20de%20Burnout%20ou%20S%C3%ADndrome,justamente%20o%20excesso%20de%20trabalho.)
,que força o desligamento e reinicialização em modo de "segurança" do seu corpo, e pode vir acompanhado
de outros problemas psicológicos.

Este problema típico da sociedade do desempenho, descrito por
Byung-Chul Han em seu livro "Sociedade do cansaço", ainda não
possui solução definitiva. Entretanto, o repositório atual
busca ajudar você jovem estudante da FGA a selecionar 
a ordem de resolução das atividades mais importantes, para
o caso de você ter que escolher "tomar o dano" de não fazer
uma atividade em troca da sua saúde mental.

O princípio geral do repositório pode ser descrito da seguinte forma:

- O sistema possui a grade curricular do seu curso.
- O sistema sabe quantas matérias serão trancadas caso você reprove na matéria X.
- Você insere as atividades que deverão ser feitas referentes as matérias.
- O sistema calcula a ordem das matérias a serem feitas.
- O sistema retorna a lista com a prioridade de atividades a serem feitas.

## Screenshots
![loading](img/loading.jpeg)

## Instalação 
**Linguagem**: Python3<br>
**Framework**: Flask<br>

 - Instalacao dos pacotes necessarios
```
  $ sudo apt install virtualenv
  $ virtualen env
  $ source env/bin/activate
  $ pip3 install -r requirements.txt

```
 - Execucao do projeto
```
  $ cd src
  $ python3 app.py
```

## Uso 
Acessar a pagina inicial da aplicacao( localhost:5000 ) usando o seu navegado de preferencia, selecionar seu curso e inserir as atividades.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.
