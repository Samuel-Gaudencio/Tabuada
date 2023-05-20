def tabuada() -> None:
    print('========== Tabuada ==========')
    num: int = int(input("De qual numero você deseja saber a tabuada? "))
    operacao = [n * num for n in range(1, 11)]
    print(f'========== Tabuada de {num} ==========')
    print(f'{num} X 1 = {operacao[0]}')
    print(f'{num} X 2 = {operacao[1]}')
    print(f'{num} X 3 = {operacao[2]}')
    print(f'{num} X 4 = {operacao[3]}')
    print(f'{num} X 5 = {operacao[4]}')
    print(f'{num} X 6 = {operacao[5]}')
    print(f'{num} X 7 = {operacao[6]}')
    print(f'{num} X 8 = {operacao[7]}')
    print(f'{num} X 9 = {operacao[8]}')
    print(f'{num} X 10 = {operacao[9]}')


tabuada()

