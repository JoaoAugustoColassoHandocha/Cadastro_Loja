import valida, datetime, os, getpass

def Clear():
    
    return os.system('cls')

def Color():
    
    return os.system('color 1f')

def Pause():
    
    return os.system('pause')

Color()

date = datetime.datetime.now()
Day = date.day
Month = date.month
Year = date.year

def main():
    
    print('\n' + '=' * 10 + 'MENU' + '=' * 10)
    print('\n[C] - Cadastrar Cliente')
    print('[D] - Dados do Cliente')
    print('[B] - Banco de Clientes')
    print('[R] - Gerar Relatório')
    print('[S] - Sair\n')
    print('=' * 24)
    
    op = input('\nInsira a opção: ')
    
    return op

def Register():
    
    name = valida.Name()
    login = valida.Login()
    
    ReadLogins = open('logins.txt', 'r')
    
    for line in ReadLogins.readlines():
        
        values = line.split('-')
        
        if login == values[1].split(':')[1].split():
            
            Clear()
            print('\nLogin já existente!\n')
            Pause()
            Clear()
            return
        
    ReadLogins.close()
    
    password = valida.Password()
    email = valida.Email()
    date = valida.Date()
    telephone = valida.Telephone()
    address = valida.Address()
    
    Clear()
    print('\nCliente cadastrado com sucesso!\n')
    Pause()
    Clear()
    
    logins = open('logins.txt', 'a')
    logins.write(f'Nome: {name} - Login: {login} - Senha: {password} - Email: {email} - Data de Nascimento: {date} - Telefone: {telephone} - Endereço: {address}\n')
    
    logins.close()
    return

def ShowsData():
     
    Clear()
     
    print('\n' + '=' * 5 + 'Logue para acessar seus dados!' + '=' * 5 + '\n')
     
    userlogin = input('Login: ')
    userpassword = getpass.getpass('Senha: ')
    
    valida = False
    
    logins = open ('logins.txt', 'r')
    
    for line in logins.readlines():
        
        values = line.split('-')
        
        if userlogin == values[1].split(':')[1].strip() and userpassword in values [2].split(':')[1].strip():
            
            Clear()
            print('\nAcesso Permitido!\n')
            print('Dados do usuário: ' + '\n')
            
            for travel in range(len(values)):
                
                if values[travel].split(':')[0] == 'Endereco':
                    
                    dictAddress = eval(values[travel].split('Endereco: ')[1])
                    
                    for key in dictAddress:
                        
                        print(f'{key}: {dictAddress[key]}')
                    
                    Pause()
                    Clear()
                        
                else:
                    
                    print(values[travel])
                    
                    Pause()
                    Clear()
                    
            valida = True
            logins.close()
            break
    
    if not valida:
        
        Clear()
        print('\nErro! Login ou senha inválidos!')
        Pause()
        Clear()
        
def CustomerRegistrations():
    
    Clear()
    
    print('\n' + '=' * 10 + 'Clientes Cadastrados' + '=' * 10 + '\n')
    logins = open('logins.txt', 'r')
    
    for line in logins.readlines():
        
        l = line.split('-')
        
        print(f'{l[0]} | {l[1]}')
        
        Pause()
        Clear()
        
    return

def Report():
    
    countClient = 0
    namess = []
    
    logins = open('logins.txt', 'r')
    
    for lines in logins.readlines():
        
        l = lines.split('-')
        namess.append(l[0])
        countClient += 1
        
    Clear()
    
    file = open('data.txt', 'w+')
    file.write('Relatório de Clientes\n\n')
    file.write(f'A loja possui {countClient} cliente(s)\n')
    
    for i in range(len(namess)):
        
        file.write(str(f'{i + 1}.{namess[i].split(':')[1]}\n'))
        
    file.write(f'{Day}/{Month}/{Year}.')
    
    print('\nRelatório gerado com sucesso!')
    
    Pause()
    Clear()
    file.close()
    return