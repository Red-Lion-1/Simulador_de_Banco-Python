from time import sleep
cor = {'cl':'\33[m',
       'In':'\33[7m',
       'B':'\33[34m',
       'R':'\33[31m',
       'G':'\33[32m',
       'Y':'\33[33m',
       'P':'\33[35m',
       'C':'\33[36m'}
print('=' * 20)
print(' Starting System ')
print('=' * 20)
sleep(2)
totVal = 10000
n10 = 100  #notas de 10 →R$1000
n20 = 200  #notas de 20 → R$4000
n50 = 100  #notas de 50 → R$5000
user1 = 5000  #Saldo do usuário
bLoan = 5000  #Valor máximo para empréstimo(bank loan)
while True:
    print('\33[7m  Banco CeV   \33[m')
    print(f''' Escolha sua opção:
    {cor['P']}[ 1 ] Usuário {cor['cl']}
    {cor['P']}[ 2 ] Adm {cor['cl']}
    {cor['P']}[ X ] Exit {cor['cl']}''')
    cmd = ''
    while cmd != '1' and cmd != '2' and cmd != 'X':
        cmd = str(input(f'{cor["R"]} Opção: {cor["cl"]}')).strip().upper()[0]
    print('=' * 20)
    if cmd == '1':
        print('Option 1 → OK')  # editando....
        print('=' * 20)

    if cmd == '2':
        # ------START ADM
        cpw = 1
        pw = ''
        cmd2 = ''
        while cmd2 != 'X':  # senha para acesso
            pw = str(input(f'{cor["R"]}Password: {cor["cl"]}')).strip().upper()
            if pw != 'ADM123' and cpw < 3:
                cpw += 1
                print(f'{cor["R"]}Senha inválida - {cpw}ª tentativa')
            elif pw != 'ADM123' and cpw == 3:
                print(f'{cor["R"]}Senha inválida{cor["cl"]}')
                print(f'{cor["R"]}Por razões de segurança, o sistema será desativado!{cor["cl"]}')
                cmd = 'X'
                cmd2 = 'X'
            else:
                while True:
                    print('=' * 20)
                    print(f'{cor["In"]} Administrador Banco CEV {cor["cl"]}')
                    print(f'  MENU: ')
                    print(f'{cor["P"]} [ 1 ] Quantidade Total de Dinheiro {cor["cl"]}')
                    print(f'{cor["P"]} [ 2 ] Inserir Dinheiro na Máquina {cor["cl"]}')
                    print(f'{cor["B"]} [ X ] voltar {cor["cl"]}')
                    cmd3 = ''
                    while cmd3 != '1' and cmd3 != '2' and cmd3 != 'X':
                        cmd3 = str(input(f'{cor["R"]} Opção: {cor["cl"]}')).strip().upper()[0]
                    print('=' * 20)
                    if cmd3 == '1':
                        while True:
                            print(f'{cor["In"]} Quantidade Total de Dinheiro {cor["cl"]}')
                            print(f'{cor["Y"]} Quantia: R${totVal} {cor["cl"]}')
                            print(f'{cor["Y"]} Notas de R$10: {n10} {cor["cl"]}')
                            print(f'{cor["Y"]} Notas de R$20: {n20} {cor["cl"]}')
                            print(f'{cor["Y"]} Notas de R$50: {n50} {cor["cl"]}')
                            atl1 = str(input(f'{cor["B"]}A → atualizar /B → Menu: {cor["cl"]}')).strip().upper()[0]
                            if atl1 == 'A':
                                print('Atualizando valores...')
                                sleep(1)
                                print(' ')
                            elif atl1 == 'B':
                                break
                            else:
                                print('Opção inválida! Voltando ao menu principal!')
                                sleep(1)
                                break
                    if cmd3 == '2':
                        while True:
                            print(f'{cor["In"]} Inserir Dinheiro na Máquina {cor["cl"]}')
                            print(f'{cor["Y"]} Quantia na Máquina: R${totVal} {cor["cl"]}')
                            print(f'{cor["Y"]} Quanto deseja inserir? {cor["cl"]}')
                            n10add = int(input(f'{cor["B"]}Notas de R$10: {cor["cl"]}'))
                            n10 = n10 + n10add
                            soma10 = n10add * 10
                            n20add = int(input(f'{cor["B"]}Notas de R$20: {cor["cl"]}'))
                            n20 = n20 + n20add
                            soma20 = n20add * 20
                            n50add = int(input(f'{cor["B"]}Notas de R$50: {cor["cl"]}'))
                            n50 = n50 + n50add
                            soma50 = n50add * 50
                            somanota = soma10 + soma20 + soma50
                            totVal = totVal + somanota
                            print('=-=' * 18)
                            print(f'{cor["Y"]} Resultado da operação: {cor["cl"]}')
                            print(f'{cor["Y"]} Foi adicionado à Máquina: R${somanota}{cor["cl"]}')
                            atl2 = str(input(f'{cor["B"]}A → Nova Operação /B → Menu: {cor["cl"]}')).strip().upper()[0]
                            if atl2 == 'A':
                                print('Nova Operação...')
                                sleep(1)
                                print(' ')
                            elif atl2 == 'B':
                                break
                            else:
                                print('Opção inválida! Voltando ao menu principal!')
                                sleep(1)
                                break
                    if cmd3 == 'X':
                        cmd2 = 'X'
                        break
        print('=' * 20)
        # ------END ADM
        '''cpw = 1
        pw = ''
        while True:  # senha para acesso
            pw = str(input(f'{cor["R"]}Password: {cor["cl"]}')).strip().upper()
            if pw != 'ADM123' and cpw < 3:
                cpw += 1
                print(f'{cor["R"]}Senha inválida - {cpw}ª tentativa')
            elif pw != 'ADM123' and cpw == 3:
                print(f'{cor["R"]}Senha inválida{cor["cl"]}')
                print(f'{cor["R"]}Por razões de segurança, o sistema será desativado!{cor["cl"]}')
                cmd = 'X'
                break
            else:
                #print('[Senha correta]')
                print('=' * 20)
                print(f'  MENU: ')
                print(f'{cor["P"]} [ 1 ] Quantidade Total de Dinheiro {cor["cl"]}')
                print(f'{cor["P"]} [ 2 ] Inserir Dinheiro na Máquina {cor["cl"]}')
                print(f'{cor["B"]} [ X ] voltar {cor["cl"]}')
                cmd3 = ''
                while cmd3 != '1' and cmd3 != '2' and cmd3 != 'X':
                    cmd3 = str(input(f'{cor["R"]} Opção: {cor["cl"]}')).strip().upper()[0]
                print('=' * 20)
                if cmd3 == '1':
                    print('1 - ok....')
                if cmd3 == '2':
                    print('2 - ok....')
                if cmd3 == 'X':
                    break
        print('=' * 20)'''
    if cmd == 'X':
        break
print(' Shutting down System ')
print('=' * 20)
sleep(2)
print(' Done ')
print('=' * 20)
