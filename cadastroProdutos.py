import pyautogui
import pandas as pd
import time

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'leo@gmail.com'
senha = '123456@leo'

tabela = pd.read_csv('produtos.csv')

pyautogui.PAUSE = 0.3


#Abre o site
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=1259, y=616)
pyautogui.write(link)
pyautogui.press('enter')

#faz login
pyautogui.click(x=1110, y=394)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('enter')

time.sleep(1)

for linha in tabela.index:
    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']         
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo'] 
    obs = tabela.loc[linha, 'obs']
  
    #cadastra produto  -  
    pyautogui.click(x=1118, y=282)

    pyautogui.write(codigo)
    pyautogui.press('tab')   

    pyautogui.write(marca)
    pyautogui.press('tab')

    pyautogui.write(tipo)
    pyautogui.press('tab')

    pyautogui.write(str(int(categoria)))
    pyautogui.press('tab')

    pyautogui.write(str(int(preco)))
    pyautogui.press('tab')

    pyautogui.write(str(int(custo)))
    pyautogui.press('tab')


    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab')
    pyautogui.press('enter')

    break
 
#time.sleep(4)
#print(pyautogui.position()) 

