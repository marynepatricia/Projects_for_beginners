total = list()
dados = dict()
gols = list()

while True:
    dados.clear()
    dados['Jogador: '] = str(input('Digite o nome do jogador: '))
    dados['Partida: '] = int(input(f'Quantas partidas {dados["Jogador: "]} jogou? '))
    for i in range(0, dados['Partida: ']):
        gols.append(int(input(f'    Quantos gols na partida {i+1} ? ')))
    dados['Gols por partidas: '] = gols[:]
    dados['Total de Gols: '] = sum(gols)
    gols.clear()
    total.append(dados.copy())
    while True:
        resp = str(input('Deseja cadastrar mais um jogador ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('RESPOSTA INVÁLIDA! Digite S ou N.')
    if resp == 'N':
        break

print('=-'*30)
print(f'{"ANALISANDO OS RESULTADOS":^60}')
print('=-'*30)
for i in dados.keys():
    print(f'{i:^15} ', end='')
print()
print('-'*60)
for k, v in enumerate(total):
    print(f'{k:<3}', end=' ')
    for c in v.values():
        print(f'{str(c):^15}', end='')
    print()
print('-'*60)

while True:
    busca = int(input('Mostrar dados de qual jogador? (Digite 999 para parar) '))
    print('-'*60)
    if busca == 999:
        break
    if busca >= len(total):
        print(f'Número inválido. Não existe jogador com o código {busca}')
    else:
        print(f'DADOS DO JOGADOR {total[busca]["Jogador: "]}')
        for k, v in enumerate(total[busca]['Gols por partidas: ']):
            print(f'    No jogo {k} fez {v} gols.')
    print('-'*60)


