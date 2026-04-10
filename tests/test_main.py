import unittest
import os
import json
from src.main import load_data, save_data

class TestVidaSana(unittest.TestCase):
    def setUp(self):
        # Configurar ambiente limpo
        self.test_file = "refeicoes.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_and_save_data(self):
        # Testa load quando o arquivo não existe
        data = load_data()
        self.assertIn("refeicoes", data)
        self.assertIn("habitos", data)
        
        # Testa save e load
        data["refeicoes"].append({"data_hora": "2026-01-01 12:00", "alimento": "Maçã", "calorias": 52})
        save_data(data)
        
        loaded_data = load_data()
        self.assertEqual(len(loaded_data["refeicoes"]), 1)
        self.assertEqual(loaded_data["refeicoes"][0]["alimento"], "Maçã")

if __name__ == "__main__":
    unittest.main()
