
import os
import pyperclip
import pyautogui
import time
from tkinter import *
from zipfile import ZipFile
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

root = Tk()
pyautogui.PAUSE = 1

#DEFINA
seu_nome_de_usuario = 'Peppão'
photoshop_abre_em_quantos_segundos = 13

download = 'C:/Users/' + seu_nome_de_usuario + '/Downloads/'
desktop = 'C:/Users/' + seu_nome_de_usuario + '/Desktop/'
quantidade_frames = 0


largura_da_sua_tela = root.winfo_screenwidth()
altura_da_sua_tela = root.winfo_screenheight()
largura_tela_do_thiago = 1366
altura_tela_do_thiago = 768

def abrir_arquivo():
  pyautogui.hotkey('ctrl','o')

def coloca_no_diretorio_certo():
  abrir_arquivo()
  pyautogui.click(x = largura_da_sua_tela * (626 / largura_tela_do_thiago), y = altura_da_sua_tela * (50 / altura_tela_do_thiago)) 
  pyautogui.write('C:/Users/')
  escreve_nome_usuario_com_utf8()
  pyautogui.write('/Desktop/itachi-gif')
  pyautogui.press('enter')

def transforma_em_png(i):
  #move para a camada
  pyautogui.moveTo(x = largura_da_sua_tela * (1234 / largura_tela_do_thiago), y = altura_da_sua_tela * (634 / altura_tela_do_thiago))
  time.sleep(1)
  pyautogui.click(button='right')
  time.sleep(1)
  #exportação rápida como png
  pyautogui.click(x = largura_da_sua_tela * (1232 / largura_tela_do_thiago), y = altura_da_sua_tela * (470 / altura_tela_do_thiago))
  time.sleep(1)
  pyautogui.write(f'{i}')
  pyautogui.press('enter')

def tira_fundo():
  time.sleep(1)
  #Tira o "cadeado" da camada, caso esteja bloqueada
  pyautogui.click(x = largura_da_sua_tela * (1327 / largura_tela_do_thiago), y = altura_da_sua_tela *(634 / altura_tela_do_thiago))
  #Seleciona a varinha mágica
  pyautogui.moveTo(x = largura_da_sua_tela * (20 / largura_tela_do_thiago), y = altura_da_sua_tela *(177 / altura_tela_do_thiago))
  pyautogui.click(button='right')
  pyautogui.click(x = largura_da_sua_tela * (113 / largura_tela_do_thiago), y = altura_da_sua_tela *(214 / altura_tela_do_thiago))
  #Seleciona e retira o fundo
  pyautogui.click(x = largura_da_sua_tela * (335 / largura_tela_do_thiago), y = altura_da_sua_tela *(244 / altura_tela_do_thiago))
  pyautogui.press('delete')
  #Salva imagem
  pyautogui.hotkey('Ctrl','Shift','s')
  pyautogui.click(x = largura_da_sua_tela * (768 / largura_tela_do_thiago), y = altura_da_sua_tela *(564 / altura_tela_do_thiago))
  pyautogui.press('enter')
  pyautogui.press('tab')
  pyautogui.press('enter')
  pyautogui.press('enter')

def seleciona_png(i):
  abrir_arquivo()
  pyautogui.click(x = largura_da_sua_tela * (690 / largura_tela_do_thiago), y = altura_da_sua_tela * (463 / altura_tela_do_thiago))
  pyautogui.write(str(i) +'.png')
  pyautogui.press('enter')
  time.sleep(1)
  pyautogui.click(x = largura_da_sua_tela * (777 / largura_tela_do_thiago), y = altura_da_sua_tela * (371 / altura_tela_do_thiago))
  
def seleciona_gif(i):
  if(i != 0 ):
      abrir_arquivo()
  pyautogui.click(x = largura_da_sua_tela * (690 / largura_tela_do_thiago), y = altura_da_sua_tela * (463 / altura_tela_do_thiago))
  if(i < 10):
    pyautogui.write('frame_0'+ str(i) +'_delay-0.1s.gif')
  elif(i == 71):
    pyautogui.write('frame_'+ str(i) +'_delay-0.2s.gif')
  else:
    pyautogui.write('frame_'+ str(i) +'_delay-0.1s.gif')
  pyautogui.press('enter')
  time.sleep(1)
  pyautogui.click(x = largura_da_sua_tela * (777 / largura_tela_do_thiago), y = altura_da_sua_tela * (371 / altura_tela_do_thiago))
  
  


    

def baixa_gif_em_frames():
  options = Options()
  options.add_argument('--ignore-certificate-errors')
  options.add_argument('--incognito')
  navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  espera = WebDriverWait(navegador, 2)
  navegador.maximize_window()
  navegador.get('https://ezgif.com/split')
  #Faz o upload da imagem
  input =  espera.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#upload-form > fieldset > p:nth-child(3) > input')))
  input.send_keys('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/82270e70-01a6-4570-8622-80a356bb7daa/ddmfrwz-9e09be79-b0c0-47d3-a4ad-c1e94430c4fa.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzgyMjcwZTcwLTAxYTYtNDU3MC04NjIyLTgwYTM1NmJiN2RhYVwvZGRtZnJ3ei05ZTA5YmU3OS1iMGMwLTQ3ZDMtYTRhZC1jMWU5NDQzMGM0ZmEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.81GrWtANJJSJuePKKj_NP1n8iFkcTN2LvlYWE6_pSLY')
  input.send_keys(Keys.ENTER)
  time.sleep(1)
  #Prepara os frames
  input = espera.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#tool-submit-button > input')))
  input.send_keys(Keys.ENTER)
  time.sleep(1)
  #Faz o download dos frames em zip
  input = espera.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Download')))
  input.click()
  time.sleep(5)
  
def abre_photoshop():
  pyautogui.press('win')
  pyautogui.write('photoshop')
  pyautogui.press('enter')
  time.sleep(photoshop_abre_em_quantos_segundos)

def extrair_frames(caminho):
  z = ZipFile(caminho, 'r')
  z.extractall()
  z.close()


def cria_diretorio_com_os_frames():
  os.chdir(download)
  data_modificacao = lambda f: f.stat().st_mtime
  diretorio = Path(download)
  arquivos = diretorio.glob('*.zip')
  arquivos_ordenados = sorted(arquivos, key=data_modificacao, reverse=True)
  os.mkdir('C:/Users/' + seu_nome_de_usuario + '/Desktop/itachi-gif')
  os.chdir('C:/Users/' + seu_nome_de_usuario + '/Desktop/itachi-gif')
  extrair_frames(arquivos_ordenados[0])
  atualiza_quantidade_de_frames()

def escreve_nome_usuario_com_utf8():
  for char in seu_nome_de_usuario:
    pyperclip.copy(char)
    pyautogui.hotkey('ctrl', 'v')

def excluir_gifs():
  os.chdir(f'{desktop}/itachi-gif')
  diretorio = Path(f'{desktop}/itachi-gif')
  arquivos = diretorio.glob('*.gif')
  for arquivo in arquivos:
    os.remove(arquivo)

def atualiza_quantidade_de_frames():
  pasta = 'C:/Users/' + seu_nome_de_usuario + '/Desktop/itachi-gif'
  global quantidade_frames 
  for path in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, path)):
        quantidade_frames += 1

def photoshop(quantidadeDeFrames):
  abre_photoshop()
  time.sleep(2)
  coloca_no_diretorio_certo()
  for i in range(quantidadeDeFrames):
    seleciona_gif(i)
    transforma_em_png(i)
    seleciona_png(i)
    tira_fundo()

def executa():
  baixa_gif_em_frames()
  cria_diretorio_com_os_frames()
  photoshop(quantidade_frames)
  excluir_gifs()

executa()




