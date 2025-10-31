class NodoArvore:
    def __init__(self, pergunta=None, cor_resultado=None):
        self.pergunta = pergunta       # Pergunta feita ao usuário
        self.cor_resultado = cor_resultado # (cor, descrição) se for um nó folha
        self.sim = None                # Próximo nó se a resposta for 's'
        self.nao = None                # Próximo nó se a resposta for 'n'

    def is_folha(self):
        return self.cor_resultado is not None

def montar_arvore():
    vermelho = NodoArvore(cor_resultado=("Vermelho", "emergência (atendimento imediato)"))
    laranja = NodoArvore(cor_resultado=("Laranja", "muito urgente"))
    amarelo = NodoArvore(cor_resultado=("Amarelo", "urgente"))
    verde = NodoArvore(cor_resultado=("Verde", "pouco urgente"))
    azul = NodoArvore(cor_resultado=("Azul", "não urgente"))

    febre = NodoArvore(pergunta="Está com febre alta (acima de 39°C) ou vômitos persistentes? (s/n)")
    febre.sim = verde      
    febre.nao = azul       

    dor_intensa = NodoArvore(pergunta="Está com dor intensa? (s/n)")
    dor_intensa.sim = amarelo  
    dor_intensa.nao = febre 

    consciente = NodoArvore(pergunta="Está consciente? (s/n)")
    consciente.nao = laranja  
    consciente.sim = dor_intensa 

    respirando = NodoArvore(pergunta="O paciente está respirando? (s/n)")
    respirando.nao = vermelho 
    respirando.sim = consciente 
    
    return respirando

def triagem(arvore_raiz):
    print("\n--- INÍCIO DA TRIAGEM ---")
    nodo_atual = arvore_raiz
    
    while not nodo_atual.is_folha():
        while True:
            try:
                resposta = input(f"{nodo_atual.pergunta}: ").lower().strip()
                if resposta in ('s', 'n'):
                    break
                else:
                    print("Resposta inválida. Use 's' para sim ou 'n' para não.")
            except EOFError: 
                resposta = 's' 
                break

        if resposta == 's':
            nodo_atual = nodo_atual.sim
        elif resposta == 'n':
            nodo_atual = nodo_atual.nao

    return nodo_atual.cor_resultado
