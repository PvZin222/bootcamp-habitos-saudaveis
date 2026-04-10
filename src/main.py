import json
import os
from datetime import datetime

DATA_FILE = "refeicoes.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"refeicoes": [], "habitos": []}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def registrar_refeicao(data):
    print("\n--- Registrar Refeição ---")
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M")
    alimento = input("Alimento ingerido: ")
    try:
        calorias = int(input("Quantidade de calorias (kcal): "))
    except ValueError:
        print("Calorias devem ser um número inteiro. Tente novamente.")
        return

    data["refeicoes"].append({
        "data_hora": data_hora,
        "alimento": alimento,
        "calorias": calorias
    })
    save_data(data)
    print("Sucesso: Refeição registrada!")

def listar_refeicoes(data):
    print("\n--- Histórico de Refeições ---")
    if not data["refeicoes"]:
        print("Nenhuma refeição registrada.")
        return
    for idx, ref in enumerate(data["refeicoes"], 1):
        print(f"[{idx}] {ref['data_hora']} | {ref['alimento']} | {ref['calorias']} kcal")

def registrar_habito(data):
    print("\n--- Registrar Hábito Diário ---")
    data_hora = datetime.now().strftime("%Y-%m-%d")
    print("1 - Bebeu mais de 2L de água?")
    print("2 - Praticou exercícios físicos?")
    print("3 - Dormiu pelo menos 7 horas?")
    escolha = input("Selecione o hábito (1/2/3): ")
    
    habitos_map = {
        "1": "Bebeu 2L+ de água",
        "2": "Praticou exercício",
        "3": "Dormiu 7h+"
    }
    
    if escolha in habitos_map:
        data["habitos"].append({
            "data": data_hora,
            "habito": habitos_map[escolha]
        })
        save_data(data)
        print("Sucesso: Hábito registrado!")
    else:
        print("Opção inválida.")

def main():
    data = load_data()
    while True:
        print("\n===============================")
        print(" MAIS SAÚDE")
        print("===============================")
        print("1. Registrar Refeição")
        print("2. Listar Refeições")
        print("3. Registrar Hábito Saudável")
        print("4. Sair")
        print("===============================")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            registrar_refeicao(data)
        elif escolha == '2':
            listar_refeicoes(data)
        elif escolha == '3':
            registrar_habito(data)
        elif escolha == '4':
            print("Saindo do programa. Mantenha os hábitos!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
