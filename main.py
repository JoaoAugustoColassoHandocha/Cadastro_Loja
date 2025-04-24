'''
This file consists of creating the system menu.

'''

import defs

defs.Color()

defs.Clear()

while True:
    
    choice = defs.main()
    
    if choice == 'C' or 'c':
        
        defs.Clear()
        defs.Register()
    
    elif choice == 'D' or 'd':
        
        defs.Clear()
        defs.ShowsData()
        
    elif choice == 'B' or 'b':
        
        defs.Clear()
        defs.CustomerRegistrations()
    
    elif choice == 'R' or 'r':
        
        defs.Clear()
        defs.Report()
    
    elif choice == 'S' or 's':
        
        defs.Clear()
        print('\nSaindo...')
        defs.Pause()
        defs.Clear()
        break
    
    else:
        
        defs.Clear()
        print('\nOpção Inválida!!!\n')
        print('Favor inserir a opção correta!\n')
        defs.Pause()
        defs.Clear()