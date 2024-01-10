import pyautogui
import time
import pandas as pd
import pandas



pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('google')
time.sleep(0.2)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=703, y=373)
time.sleep(1)
pyautogui.write('usuario@gmail.com')
pyautogui.press('tab')
pyautogui.write('senhafoda123')
pyautogui.press('enter')
time.sleep(1)


tabela = pd.read_csv("D:\Jornada Python\Python Power Up\produtos.csv")
print(tabela)
for linha in tabela.index:

    pyautogui.click(x=767, y=260)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')


    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)