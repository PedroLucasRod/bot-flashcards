import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('flashcards_constitucional.xlsx')
vendas_sheet = workbook['Flashcards']

tag_adicionada = False

for linha in vendas_sheet.iter_rows(min_row=1):
    #Front
    pyautogui.click(526,418, duration=0.5)
    pyautogui.write(linha[0].value)
    #Back
    pyautogui.click(515,484, duration=0.5)
    pyautogui.write(linha[1].value)
    #Tag
    if not tag_adicionada:
        pyautogui.click(522,544, duration=0.5)
        pyautogui.write(linha[2].value)
        tag_adicionada = True
    #Add
    pyautogui.click(287,600, duration=1.0)