'''
This file consists of creating the system menu.

'''

import defs, os

os.system('color 1f')

defs.Clear()

while True:
    
    choice = defs.main()
    
    if choice == '1':
        
        defs.Clear()
        defs.Register()
    
    elif choice == '2':
        
        defs.Clear()
        defs.ShowsData()
        
    elif choice == '3':
        
        defs.Clear()
        defs.CustomerRegistrations()
    
    elif choice == '4':
        
        defs.Clear()
        defs.Report()
    
    elif choice == '5':
        
        defs.Clear()
        print('\nSaindo...\n')
        defs.Pause()
        defs.Clear()
        break
    
    else:
        
        defs.Clear()
        print('\nOpção Inválida!!!\n')
        print('Favor inserir a opção correta!\n')
        defs.Pause()
        defs.Clear()