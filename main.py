from priorities import PRIORIDADES, FILAS_DE_TRIAGEM
from tree import montar_arvore, triagem

def cadastrar_paciente(arvore_raiz):
    nome = input("Nome do paciente: ")
    cor, descricao = triagem(arvore_raiz)
    
    FILAS_DE_TRIAGEM[cor].enqueue(nome)
    
    print("-" * 30)
    print(f"Cor atribuída: {cor} - {descricao}")
    print(f"Paciente {nome} adicionado à fila {cor.lower()}.")
    print("-" * 30)

def chamar_paciente():
    cores_ordenadas = sorted(PRIORIDADES, key=PRIORIDADES.get, reverse=True)
    
    paciente_chamado = None
    cor_fila = None

    for cor in cores_ordenadas:
        fila = FILAS_DE_TRIAGEM[cor]
        if not fila.is_empty():
            paciente_chamado = fila.dequeue()
            cor_fila = cor
            break # Encontrado o paciente mais urgente, para a busca

    if paciente_chamado:
        tamanho_restante = FILAS_DE_TRIAGEM[cor_fila].size()
        print("\n" + "=" * 40)
        print(f"Chamando paciente da fila **{cor_fila}** ({tamanho_restante} restantes):")
        print(f"**Paciente:** {paciente_chamado}")
        print("=" * 40 + "\n")
    else:
        print("\n*** Todas as filas estão vazias. Sem pacientes para chamar. ***\n")

def mostrar_status():
    print("\n=== STATUS DAS FILAS DE TRIAGEM ===")
    cores_ordenadas = sorted(PRIORIDADES, key=PRIORIDADES.get, reverse=True)
    
    for cor in cores_ordenadas:
        tamanho = FILAS_DE_TRIAGEM[cor].size()
        print(f"* Fila **{cor}**: {tamanho} paciente(s)")
    print("===================================\n")

def main():
    arvore_manchester = montar_arvore()
    
    while True:
        print("=== SISTEMA DE TRIAGEM MANCHESTER ===")
        print("1 - Cadastrar paciente")
        print("2 - Chamar paciente")
        print("3 - Mostrar status das filas")
        print("0 - Sair")
        
        try:
            escolha = input("Escolha: ").strip()
            
            if escolha == '1':
                cadastrar_paciente(arvore_manchester)
            elif escolha == '2':
                chamar_paciente()
            elif escolha == '3':
                mostrar_status()
            elif escolha == '0':
                print("Encerrando o sistema de triagem...")
                break
            else:
                print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 0.\n")
                
        except Exception as e:
            print(f"\nOcorreu um erro: {e}")
            
if __name__ == "__main__":
    main()
