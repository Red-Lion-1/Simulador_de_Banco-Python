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
totVal = 20000  #10000
n10 = 100  #notas de 10 →R$1000
n20 = 250  #notas de 20 → R$5000
n50 = 280  #notas de 50 → R$14000
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
        # ------START USER
        while True:
            print('=' * 20)
            print(f'{cor["In"]} Cliente Banco CEV {cor["cl"]}')
            print(f'  MENU: ')
            print(f'{cor["P"]} [ 1 ] Saldo {cor["cl"]}')
            print(f'{cor["P"]} [ 2 ] Saque {cor["cl"]}')
            print(f'{cor["P"]} [ 3 ] Empréstimo {cor["cl"]}')
            print(f'{cor["B"]} [ X ] voltar {cor["cl"]}')
            cmd4 = ''
            while cmd4 != '1' and cmd4 != '2' and cmd4 != '3' and cmd4 != 'X':
                cmd4 = str(input(f'{cor["R"]} Opção: {cor["cl"]}')).strip().upper()[0]
            print('=' * 20)
            if cmd4 == '1':
                while True:
                    sleep(2)
                    print(f'{cor["In"]}   Saldo   {cor["cl"]}')
                    print(f'{cor["Y"]} Você possui: R${user1} {cor["cl"]}')
                    if user1 < 0:
                        print(f'{cor["R"]}Seu saldo está negativo! {cor["cl"]}')
                        print(f'{cor["R"]}Entre em contato com a gente para negociar sua divida! {cor["cl"]}')
                    print(' ')
                    back1 = str(input(f'{cor["B"]}A→ atualizar/B→ voltar {cor["cl"]}')).strip().upper()[0]
                    if back1 == 'A':
                        print('Atualizando saldo...')
                        sleep(1)
                        print(' ')
                    elif back1 == 'B':
                        break
                    else:
                        print('Opção inválida! Voltando ao menu principal!')
                        sleep(1)
                        break
            if cmd4 == '2':
                while True:
                    if totVal <= 10000:
                        print(f'{cor["Y"]}Maquina indisponível para Saque {cor["cl"]}')
                        sleep(1)
                        print('=-=' * 16)
                        break
                    elif user1 <= 0:
                        print(f'{cor["Y"]}Você não possui saldo para saque {cor["cl"]}')
                        sleep(1)
                        print('=-=' * 16)
                        break
                    else:
                        print(f'{cor["In"]}   Saque   {cor["cl"]}')
                        print(f'{cor["Y"]}Notas disponiveis: 50, 20 e 10 {cor["cl"]}')
                        print(f'{cor["Y"]}Quanto quer sacar? {cor["cl"]}')
                        saq = int(input(f'{cor["R"]}Valor: {cor["cl"]}'))
                        if saq > totVal or user1 < saq or saq < 9:
                            print(f'{cor["G"]}Limite de saque: R${user1} {cor["cl"]}')
                        else:
                            u = saq // 1 % 10
                            d = saq // 10 % 10
                            c = saq // 100 % 10
                            m = saq // 1000 % 10
                            if u != 0:
                                print(f'{cor["R"]}Valor inválido!{cor["cl"]}')
                                print(f'{cor["Y"]}Notas disponiveis para saque: 50, 20 e 10 {cor["cl"]}')
                                sleep(1)
                                print('=-=' * 16)
                                break
                            n50Mfim = 0
                            n50Cfim = 0
                            n20Dfim = 0
                            v20fim = 0
                            difD = 0
                            difV = 0
                            if m >= 1:
                                mtot = (m * 1000) / 50
                                if n50 >= mtot:
                                    n50Mfim = mtot  # notas que serão entregues
                                else:
                                    print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                    break
                            # print(f'[debug] n50Mfim {n50Mfim}')
                            if c >= 1:
                                ctot = (c * 100) / 50
                                if (n50 - mtot) >= ctot:
                                    n50Cfim = ctot  # notas que serão entregues
                                else:
                                    print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                    break
                            # print(f'[debug] n50Cfim {n50Cfim}')
                            if d >= 1 and d % 2 == 0:
                                dtot = (d * 10) / 20
                                if n20 >= dtot:
                                    n20Dfim = dtot  # notas que serão entregues
                                else:
                                    print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                    break
                            elif d >= 1 and d % 2 == 1:
                                calcD = d - 1
                                dtot = (calcD * 10) / 20
                                difD = 1
                                if n20 >= dtot:
                                    n20Dfim = dtot  # notas que serão entregues
                                else:
                                    print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                    break
                            else:
                                print(f'{cor["R"]}Operação indisponivel! Tente outro valor!{cor["cl"]}')
                                break
                            # print(f'[debug] n20Dfim {n20Dfim}')
                            totFim = (n50Mfim * 50) + (n50Cfim * 50) + (n20Dfim * 20) + difD
                            totFalt = saq - totFim
                            # print(f'[debug] falt {totFalt}  fim {totFim}')
                            if totFalt % 20 == 0:
                                v20 = totFalt / 20
                                if (n20 - dtot) >= v20:
                                    v20fim = v20
                                else:
                                    print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                    break
                            if totFalt % 20 == 1:
                                tfCalc = totFalt - 10
                                difV = 1
                                v20 = tfCalc / 20
                                if (n20 - dtot) >= v20:
                                    v20fim = v20
                                else:
                                    print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                    break
                            cedula50 = n50Mfim + n50Cfim
                            cedula20 = n20Dfim + v20fim
                            cedula10 = difD + difV
                            # print(f'[debug] n50={n50}  n20={n20} n10={n10}')
                            sleep(1)
                            user1 = user1 - saq
                            totVal = totVal - saq
                            n50 = n50 - cedula50
                            n20 = n20 - cedula20
                            n10 = n10 - cedula10
                            # print(f'[debug] n50={n50}  n20={n20} n10={n10}')
                            # print(f'[debug] user1={user1}  banco={totVal}')
                            print(f'{cor["G"]}Contando...{cor["cl"]}')
                            sleep(1)
                            print(f'{cor["G"]}{int(cedula50)}x Notas de R$50{cor["cl"]}')
                            print(f'{cor["G"]}{int(cedula20)}x Notas de R$20{cor["cl"]}')
                            print(f'{cor["G"]}{int(cedula10)}x Notas de R$10{cor["cl"]}')
                            print(f'{cor["G"]}Total: R${saq} {cor["cl"]}')
                            sleep(1)
                        back2 = str(input(f'{cor["B"]}A→ Novo saque/B→ voltar {cor["cl"]}')).strip().upper()[0]
                        if back2 == 'A':
                            if totVal <= 10000:
                                sleep(2)
                                print('=-=' * 16)
                                print(f'{cor["Y"]}Maquina indisponível para Saque {cor["cl"]}')
                                print('Voltando ao menu principal!')
                                sleep(2)
                                print(' ')
                                break
                            else:
                                print('Atualizando...')
                                sleep(2)
                                print(' ')
                        elif back2 == 'B':
                            break
                        else:
                            print('Opção inválida! Voltando ao menu principal!')
                            sleep(1)
                            break
            if cmd4 == '3':
                while True:
                    if bLoan <= 0:
                        print(f'{cor["R"]}Você alcançou o limite de empréstimo {cor["cl"]}')
                        sleep(1)
                        print('=-=' * 16)
                        break
                    elif user1 > 1:
                        print(f'{cor["R"]}Para fazer um empréstimo, sua conta precisa estar vazia! {cor["cl"]}')
                        sleep(1)
                        print('=-=' * 16)
                        break
                    else:
                        print(f'{cor["In"]}   Empréstimo   {cor["cl"]}')
                        print(f'{cor["Y"]}Notas disponiveis: 50, 20 e 10 {cor["cl"]}')
                        print(f'{cor["Y"]}Você tem R${bLoan} disponível para empréstimo {cor["cl"]}')
                        emp = str(input(f'{cor["Y"]}Deseja fazer um empréstimo? [S/N]: {cor["cl"]}')).strip().upper()[0]
                        if emp == 'S':
                            print(f'{cor["Y"]}Quanto quer sacar? {cor["cl"]}')
                            saq = int(input(f'{cor["R"]}Valor: {cor["cl"]}'))
                            if saq > totVal or bLoan < saq or saq < 9:
                                print(f'{cor["G"]}Limite de empréstimo: R${bLoan} {cor["cl"]}')
                            else:
                                u = saq // 1 % 10
                                d = saq // 10 % 10
                                c = saq // 100 % 10
                                m = saq // 1000 % 10
                                if u != 0:
                                    print(f'{cor["R"]}Valor inválido!{cor["cl"]}')
                                    print(f'{cor["Y"]}Notas disponiveis para saque: 50, 20 e 10 {cor["cl"]}')
                                    sleep(1)
                                    print('=-=' * 16)
                                    break
                                n50Mfim = 0
                                n50Cfim = 0
                                n20Dfim = 0
                                v20fim = 0
                                difD = 0
                                difV = 0
                                if m >= 1:
                                    mtot = (m * 1000) / 50
                                    if n50 >= mtot:
                                        n50Mfim = mtot  # notas que serão entregues
                                    else:
                                        print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                        break
                                # print(f'[debug] n50Mfim {n50Mfim}')
                                if c >= 1:
                                    ctot = (c * 100) / 50
                                    if (n50 - mtot) >= ctot:
                                        n50Cfim = ctot  # notas que serão entregues
                                    else:
                                        print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                        break
                                # print(f'[debug] n50Cfim {n50Cfim}')
                                if d >= 1 and d % 2 == 0:
                                    dtot = (d * 10) / 20
                                    if n20 >= dtot:
                                        n20Dfim = dtot  # notas que serão entregues
                                    else:
                                        print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                        break
                                elif d >= 1 and d % 2 == 1:
                                    calcD = d - 1
                                    dtot = (calcD * 10) / 20
                                    difD = 1
                                    if n20 >= dtot:
                                        n20Dfim = dtot  # notas que serão entregues
                                    else:
                                        print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                        break
                                else:
                                    print(f'{cor["R"]}Operação indisponivel! Tente outro valor!{cor["cl"]}')
                                    break
                                # print(f'[debug] n20Dfim {n20Dfim}')
                                totFim = (n50Mfim * 50) + (n50Cfim * 50) + (n20Dfim * 20) + difD
                                totFalt = saq - totFim
                                # print(f'[debug] falt {totFalt}  fim {totFim}')
                                if totFalt % 20 == 0:
                                    v20 = totFalt / 20
                                    if (n20 - dtot) >= v20:
                                        v20fim = v20
                                    else:
                                        print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                        break
                                if totFalt % 20 == 1:
                                    tfCalc = totFalt - 10
                                    difV = 1
                                    v20 = tfCalc / 20
                                    if (n20 - dtot) >= v20:
                                        v20fim = v20
                                    else:
                                        print(f'{cor["R"]}Operação indisponivel! Tente um valor menor!{cor["cl"]}')
                                        break
                                cedula50 = n50Mfim + n50Cfim
                                cedula20 = n20Dfim + v20fim
                                cedula10 = difD + difV
                                # print(f'[debug] n50={n50}  n20={n20} n10={n10}')
                                sleep(1)
                                bLoan = bLoan - saq
                                user1 = user1 - saq
                                totVal = totVal - saq
                                n50 = n50 - cedula50
                                n20 = n20 - cedula20
                                n10 = n10 - cedula10
                                # print(f'[debug] n50={n50}  n20={n20} n10={n10}')
                                # print(f'[debug] user1={user1}  banco={totVal}')
                                print(f'{cor["G"]}Contando...{cor["cl"]}')
                                sleep(1)
                                print(f'{cor["G"]}{int(cedula50)}x Notas de R$50{cor["cl"]}')
                                print(f'{cor["G"]}{int(cedula20)}x Notas de R$20{cor["cl"]}')
                                print(f'{cor["G"]}{int(cedula10)}x Notas de R$10{cor["cl"]}')
                                print(f'{cor["G"]}Total: R${saq} {cor["cl"]}')
                                sleep(1)
                            back2 = str(input(f'{cor["B"]}A→ Novo empréstimo/B→ voltar {cor["cl"]}')).strip().upper()[0]
                            if back2 == 'A':
                                if totVal <= 10000:
                                    sleep(2)
                                    print('=-=' * 16)
                                    print(f'{cor["Y"]}Maquina indisponível para Saque {cor["cl"]}')
                                    print('Voltando ao menu principal!')
                                    sleep(2)
                                    print(' ')
                                    break
                                else:
                                    print('Atualizando...')
                                    sleep(2)
                                    print(' ')
                            elif back2 == 'B':
                                break
                            else:
                                print('Opção inválida! Voltando ao menu principal!')
                                sleep(1)
                                break
                        elif emp == 'N':
                            print(f'{cor["R"]}Cancelando empréstimo... {cor["cl"]}')
                            sleep(1)
                            print('=-=' * 16)
                            break
                        else:
                            print(f'{cor["R"]}Opção inválida! Cancelando empréstimo... {cor["cl"]}')
                            sleep(1)
                            print('=-=' * 16)
                            break
            if cmd4 == 'X':
                break
        # ------END USER
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
