import json
import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo_json():
    root = tk.Tk()
    root.withdraw() 
    arquivo = filedialog.askopenfilename(title="Arquivo JSON", filetypes=[("JSON files", "*.json")])
    return arquivo

def calcular_faturamento():
    arquivo_json = selecionar_arquivo_json()

    if not arquivo_json:
        print("Nenhum arquivo selecionado.")
        return

    with open(arquivo_json, 'r') as file:
        faturamento_data = json.load(file)

    faturamento = [dia['valor'] for dia in faturamento_data if dia['valor'] > 0]
    faturamento_validos = [f for f in faturamento if f > 0]

    if not faturamento_validos:
        print("Não há dados válidos de faturamento.")
        return

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    media_mensal = sum(faturamento_validos) / len(faturamento_validos)
    dias_acima_da_media = len([f for f in faturamento_validos if f > media_mensal])

    print(f"Menor faturamento: R$ {menor_faturamento}")
    print(f"Maior faturamento: R$ {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

calcular_faturamento()
