# Manchester

Esta é uma implementação em Python do Protocolo Manchester, 
um método utilizado em serviços de urgência e emergência para 
classificar pacientes de acordo com a gravidade do seu estado e 
determinar a prioridade de atendimento.


# Estrutura de Dados e Prioridade


O sistema é construído sobre duas estruturas principais:

*) PRIORIDADES (Dicionário): Define a ordem hierárquica das cores de triagem, onde um valor mais alto representa uma urgência maior.

*) Vermelho (5): Emergência (atendimento imediato).

*) Laranja (4): Muito urgente.

*) Amarelo (3): Urgente.

*) Verde (2): Pouco urgente.

*) Azul (1): Não urgente.


# Algoritmo de Triagem (Árvore de Decisão)


O núcleo do sistema é a classe NodoArvore e a função montar_arvore(), que juntas criam uma Árvore Binária de Decisão para guiar a triagem:

*) NodoArvore: Representa um nó da árvore. Pode ser um nó de pergunta (pergunta preenchida) 
com dois ramos (sim e nao) ou um nó folha (cor_resultado preenchido) que representa o resultado 
final da triagem (uma cor e sua descrição).

*) montar_arvore(): Constrói a estrutura da árvore com perguntas sequenciais, simulando o fluxo de decisão do Protocolo de Manchester. 
A árvore começa com a avaliação das condições mais críticas (ex: "O paciente está respirando?"), levando a classificações de maior prioridade.

A função triagem(arvore_raiz) percorre essa árvore interativamente, fazendo perguntas ao usuário (input) 
e navegando para o nó sim ou nao com base na resposta, até atingir um nó folha que define a cor final.


# Funcionalidades do Sistema

O programa principal (main) oferece um menu com três funções principais para gerenciar o fluxo de pacientes:

1) cadastrar_paciente(arvore_raiz):

*) Solicita o nome do paciente.

*) Executa a função triagem() para determinar a cor de prioridade.

*) Adiciona o nome do paciente à fila correspondente dentro do dicionário FILAS_DE_TRIAGEM.

2) chamar_paciente():

*) Busca o paciente mais prioritário a ser atendido.

*) Usa o dicionário PRIORIDADES para iterar pelas filas em ordem decrescente de prioridade (Vermelho $\rightarrow$ Azul).

*) Remove o primeiro paciente (dequeue) da primeira fila não vazia encontrada.

3) mostrar_status():

Exibe o tamanho atual de cada fila de triagem, ordenando as cores pela prioridade (do Vermelho ao Azul).
