import defs, getpass, os

os.system('color 1f')

def Name():
    
    while True:
        
        name = input('\nNome Completo: ')
        
        if name == '':
            
            defs.Clear()
            print('\nErro! Campo Vazio!\n')
            defs.Pause()
            defs.Clear
            continue
        
        temp = ''.join(name.split(' '))
        
        for i in temp:
            
            if i.isdigit():
                
                defs.Clear()
                print('\nDigite um nome válido!\n')
                defs.Pause()
                break
            
        else:
            
            return name.strip(' ')
        
def Password():
    
    while True:
        
        password = getpass.getpass('\nSenha: ')
        
        if password == '':
            
            defs.Clear()
            print('\nErro! Campo Vazio!\n')
            defs.Pause()
            defs.Clear
            continue
        
        return password.strip(' ')
    
def Email():
    
    while True:
        
        email = input('\nE-mail: ')
        
        if email == '':
            
            defs.Clear()
            print('\nErro! Campo Vazio!\n')
            defs.Pause()
            defs.Clear
            continue
        
        elif '@' and '.com' in email:
            
            return email.strip(' ')
        
        else:
            
            defs.Clear()
            print('\nE-mail Inválido! Deve conter "@" e ".com"\n')
            defs.Pause()
            defs.Clear()
        
def Date():
    
    while True:
        
        date = input('\nNascimento (dd/mm/aaaa): ')
        
        if date == '':
            
            defs.Clear()
            print('\nErro! Campo Vazio!\n')
            defs.Pause()
            defs.Clear
            continue
        
        temp = ''.join(date.split('/'))
        
        if not temp.isnumeric():
            
            defs.Clear()
            print('\nDigite uma data válida!\n')
            defs.Pause()
            defs.Clear()
            continue
        
        if date.count('/') == 2 and date != '//':
            
            Day, Month, Year = date.split('/')
            
            if 1 <= int(Day) <= 31 and 1 <= int(Month) <= 12 and 1900 <= int(Year) <= 3000:
                
                return date.split(' ')
            
            else:
                
                defs.Clear()
                print('\nDia/Mês/Ano Inválido(s)!\n')
                defs.Pause()
                defs.Clear()
        
        else:
            
            defs.Clear()
            print('\nDigite a data no padrão dd/mm/aaaa!\n')
            defs.Pause()
            defs.Clear()
            
def Login():
    
    while True:
        
        login = input('\nLogin: ')
        
        if login == '':
            
            defs.Clear()
            print('\nErro! Campo Vazio!\n')
            defs.Pause()
            defs.Clear
            continue
        
        return login.strip(' ')
    
def Telephone():
    
    while True:
        
        telephone = input('\nTelefone (Apenas Números): ')
        
        if telephone == '':
            
            defs.Clear()
            print('\nErro! Campo Vazio!\n')
            defs.Pause()
            defs.Clear
            continue
        
        elif not telephone.isnumeric():
            
            defs.Clear()
            print('\nInsira apenas números!\n')
            defs.Pause()
            defs.Clear
            continue
        
        else:
            
            if 9 <= len(telephone) <= 11:
                
                return telephone
            
            else:
                
                defs.Clear()
                print('\nO telefone deve ter entre 9 a 11 caracteres!\n')
                defs.Pause()
                defs.Clear
                
def Address():
    
    while True:
        
        data = {
            
            'Road': input('\nRua: '),
            'Number': input('\nNúmero: '),
            'Complement': input('\nComplemento: '),
            'Neighborhood': input('\nBairro: '),
            'CEP': input('\nCEP: '),
            'City': input('\nCidade: '),
            'Reference': input('\nReferência: '),
            
        }
        
        return data