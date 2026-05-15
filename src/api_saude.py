import urllib.request
import json


def buscar_dica_saude():
    url = "https://world.openfoodfacts.org/cgi/search.pl?search_terms=fruta&search_simple=1&action=process&json=1&page_size=5"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "MaisSaude/1.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))
            produtos = data.get("products", [])
            if produtos:
                produto = produtos[0]
                nome = produto.get("product_name", "Produto desconhecido")
                nutrientes = produto.get("nutriments", {})
                energia = nutrientes.get("energy-kcal_100g", "N/A")
                return {"nome": nome, "calorias_100g": energia, "status": "ok"}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
    return {"status": "erro", "mensagem": "Nenhum produto encontrado"}


def exibir_dica_saude():
    print("\n--- Dica de Alimento Saudavel (Open Food Facts) ---")
    resultado = buscar_dica_saude()
    if resultado["status"] == "ok":
        print(f"Alimento: {resultado['nome']}")
        print(f"Calorias por 100g: {resultado['calorias_100g']} kcal")
    else:
        print(f"Nao foi possivel buscar a dica: {resultado.get('mensagem')}")
