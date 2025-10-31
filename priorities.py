import collections

PRIORIDADES = {
    "Vermelho": 5,  # Emergência (atendimento imediato)
    "Laranja": 4,
    "Amarelo": 3,
    "Verde": 2,
    "Azul": 1,      # Não urgente
}

class Fila:
    def __init__(self):
        self.itens = collections.deque()

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.itens.popleft()

    def is_empty(self):
        return len(self.itens) == 0

    def size(self):
        return len(self.itens)

FILAS_DE_TRIAGEM = {
    "Vermelho": Fila(),
    "Laranja": Fila(),
    "Amarelo": Fila(),
    "Verde": Fila(),
    "Azul": Fila(),
}
