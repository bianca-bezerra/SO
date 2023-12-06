
from termcolor import *


def getRecursosTotais(qtd_recursos):
    recursos_totais = []
    for i in range(qtd_recursos):
        recursos_totais.append(int(input("Digite a " + colored("quantidade",
                               'red') + " do recurso " + colored(str(i + 1), 'blue') + ": ")))
    return recursos_totais


def getRecursosAlocados(qtd_recursos):
    recursos_alocados = []
    for i in range(qtd_recursos):
        recursos_alocados.append(int(input("Digite a " + colored("quantidade de alocados",
                                 'red') + " do recurso " + colored(str(i + 1), 'blue') + ": ")))
    return recursos_alocados


def getRecursosDisponiveis(recursos_alocados, recursos_totais):
    recursos_disponiveis = []
    for i in range((len(recursos_totais))):
        recursos_disponiveis.append(recursos_totais[i] - recursos_alocados[i])
    return recursos_disponiveis


def getMatrizRecursosNecessarios(qtd_processos, qtd_recursos):
    recursos_necessarios = []
    for i in range(qtd_processos):
        linha = []
        for j in range(qtd_recursos):
            linha.append(int(input("Digite a " + colored("quantidade necessária ", 'red') + "do recurso " +
                         colored(str(j + 1), 'green') + " para o processo " + colored(str(i + 1), 'blue') + ": ")))
        recursos_necessarios.append(linha)
    return recursos_necessarios


def getMatrizRecursosAlocados(qtd_processos, qtd_recursos):
    recursos_alocados_processos = []
    for i in range(qtd_processos):
        linha = []
        for j in range(qtd_recursos):
            linha.append(int(input("Digite a " + colored("quantidade alocada ", 'red') + "do recurso " +
                         colored(str(j + 1), 'green') + " para o processo " + colored(str(i + 1), 'blue') + ": ")))
        recursos_alocados_processos.append(linha)
    return recursos_alocados_processos


def algoritmo_banqueiro(qtd_recursos, qtd_processos, recursos_disponiveis, recursos_necessarios_matriz, recursos_alocados_matriz):

    processos_concluidos = [False] * qtd_processos
    sequencia_execucao = []

    while True:
        processo_executado = False

        for i in range(qtd_processos):
            if not processos_concluidos[i]:
                # Se a quantidade necessária menos a quantidade que o processo ja tem alocado for menor ou igual ao disponível, ele executa
                if all(recursos_disponiveis[j] >= recursos_necessarios_matriz[i][j] - recursos_alocados_matriz[i][j] for j in range(qtd_recursos)):

                    diferenca1 = []
                    for j in range(qtd_recursos):
                        diff = recursos_necessarios_matriz[i][j] - \
                            recursos_alocados_matriz[i][j]
                        if (diff < 0):
                            diferenca1.append(0)
                        else:
                            diferenca1.append(diff)

                    print("\n==============================================")
                    print(f">> Processo {i + 1} está " +
                          colored("sendo executado", 'green') + "\n")
                    print("\nMatriz Recursos " + colored("Alocados", 'yellow') +
                          colored(" antes", 'magenta') + " da execução:")
                    for linha in recursos_alocados_matriz:
                        print(linha)
                    print()
                    print("Recursos " + colored("alocados", 'yellow') +
                          " antes no P" + str([i+1]) + ":", recursos_alocados_matriz[i])
                    print("Recursos " + colored("necessários", 'cyan') +
                          " antes no P" + str([i+1]) + ":", recursos_necessarios_matriz[i])
                    print("Recursos " + colored("que faltam", 'red') +
                          " no P" + str([i+1]) + ":", diferenca1)
                    print("Recursos " + colored("disponíveis", 'green') +
                          " antes:", str(recursos_disponiveis) + "\n")

                    for j in range(qtd_recursos):
                        recursos_disponiveis[j] += recursos_alocados_matriz[i][j]
                        recursos_alocados_matriz[i][j] = 0

                    processos_concluidos[i] = True
                    sequencia_execucao.append(i + 1)
                    processo_executado = True

                    # print("Recursos alocados depois:", recursos_alocados_matriz[i])
                    print("Recursos disponíveis depois:",
                          str(recursos_disponiveis))
                    # print("============================================")

                # Se não o processo da vez não for concluido
                if (processos_concluidos[i] == False):
                    diferenca2 = []
                    for j in range(qtd_recursos):
                        diff = recursos_necessarios_matriz[i][j] - \
                            recursos_alocados_matriz[i][j]
                        if (diff < 0):
                            diferenca2.append(0)
                        else:
                            diferenca2.append(diff)
                    print("============================================")
                    print(f">> Processo {i + 1} " +
                          colored("não", 'red') + " executado\n")
                    print("Recursos " + colored("alocados", 'yellow') +
                          " no P" + str([i+1]) + ":", recursos_alocados_matriz[i])
                    print("Recursos " + colored("necessários", 'cyan') +
                          " no P" + str([i+1]) + ":", recursos_necessarios_matriz[i])
                    print("Recursos " + colored("que faltam", 'red') +
                          " no P" + str([i+1]) + ":", diferenca2)
                    print("Recursos " + colored("disponíveis", 'green') +
                          " :", str(recursos_disponiveis))
                    print(
                        "Não há recursos suficiente para executar esse processo!" + "\n")

                else:
                    print("\nMatriz Recursos " + colored("Alocados",
                          'yellow') + colored(" atual:", 'magenta'))
                    for linha in recursos_alocados_matriz:
                        print(linha)
                    print()

        if not processo_executado:
            break

    if all(processos_concluidos):
        print("\nO sistema está em um estado " + colored("seguro", 'green'))
        print("Sequência segura de execução: ", sequencia_execucao)
    else:
        print("\nO sistema está em um estado " + colored("inseguro", 'red'))


def main():

    try:
        qtd_recursos = int(input("Digite a " + colored("quantidade",
                           'red') + " de " + colored("recursos: ", 'green')))
        qtd_processos = int(input("Digite a " + colored("quantidade",
                            'red') + " de " + colored("processos: ", 'green')))
        print()
        recursos_totais = getRecursosTotais(qtd_recursos)
        print()
        recursos_alocados = getRecursosAlocados(qtd_recursos)
        print()
        recursos_disponiveis = getRecursosDisponiveis(
            recursos_alocados, recursos_totais)
        recursos_necessarios_matriz = getMatrizRecursosNecessarios(
            qtd_processos, qtd_recursos)
        print()
        recursos_alocados_matriz = getMatrizRecursosAlocados(
            qtd_processos, qtd_recursos)
        algoritmo_banqueiro(qtd_recursos, qtd_processos, recursos_disponiveis,
                            recursos_necessarios_matriz, recursos_alocados_matriz)
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro.")


main()
