import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from unittest.mock import patch, MagicMock
import json
from api_saude import buscar_dica_saude


def test_buscar_dica_saude_sucesso():
    mock_data = {
        "products": [
            {
                "product_name": "Banana",
                "nutriments": {"energy-kcal_100g": 89}
            }
        ]
    }
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(mock_data).encode("utf-8")
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_response):
        resultado = buscar_dica_saude()

    assert resultado["status"] == "ok"
    assert resultado["nome"] == "Banana"
    assert resultado["calorias_100g"] == 89


def test_buscar_dica_saude_erro_conexao():
    with patch("urllib.request.urlopen", side_effect=Exception("Sem conexao")):
        resultado = buscar_dica_saude()

    assert resultado["status"] == "erro"
    assert "Sem conexao" in resultado["mensagem"]
