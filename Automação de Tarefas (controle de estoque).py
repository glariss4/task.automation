# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui 
import time

# pyautogui.click > clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> combinação de teclas
# abrir o chrome

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
 
# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
pyautogui.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=433, y=397)
pyautogui.write("gl.lariss4@gmail.com")

pyautogui.press("tab") # passar para o campo de senha
pyautogui.write("automatizando_tarefas")

pyautogui.press("tab") #passei p/ botão de login
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados de produtos
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)


for linha in tabela.index:

    # Passo 4: Cadastrar um produto
    pyautogui.click(x=412, y=282)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    #preencher os campos 

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    #apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

# dar scroll de tudo pra cima
    pyautogui.scroll(50000)
# Passo 5: Repetir o cadastro para todos os produtos