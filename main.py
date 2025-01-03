import pyautogui as pg
import time

print('qual o nome do contato para mandar a mensagem?')
contact = input()
print('Qual a mensagem?')
M = input()
print('digite Y para continuar')
C = input()

if C == 'Y' or 'y':
    #aperta a tecla windows do teclado e entra no whatsapp
    pg.press('win')
    pg.write('whatsApp', interval=0.05)
    pg.press('enter')
    #pesquisa o contato
    time.sleep(2.5)
    pg.hotkey('ctrl' + 'F')
    pg.write(contact)
    #seleciona o contato
    pg.press('down')
    pg.press('enter')
    #manda a mensagem
    time.sleep(2)
    pg.click(x=1100, y=950)
    pg.write(M, interval=0.2)
    pg.press('enter')

