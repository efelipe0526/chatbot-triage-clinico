import json

filepath = "d:/INTELIGENCIA ARTIFICIAL/chatbot_clinico_colab.ipynb"
with open(filepath, "r", encoding="utf-8") as f:
    nb = json.load(f)

new_code = r"""# 2. IMPORTACIÓN DE LIBRERÍAS Y CONFIGURACIÓN DE GEMINI
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from google import genai
import time
import getpass

# --- CARGA AUTOMÁTICA O MANUAL DE LA API KEY ---
try:
    from google.colab import userdata
    # Busca el secreto llamado "GEMINI_API_KEY" en la pestaña de la llave de Colab
    gemini_api_key = userdata.get('GEMINI_API_KEY')
    print("✅ API Key cargada automáticamente desde los secretos de Google Colab.")
except Exception:
    # Si no estás en Colab o no creaste el secreto, pedirá la llave manualmente
    print("Por favor, ingresa tu API Key de Google Gemini:")
    gemini_api_key = getpass.getpass('API Key: ')

cliente_gemini = genai.Client(api_key=gemini_api_key)

# --- DETECCIÓN AUTOMÁTICA DEL MODELO CORRECTO ---
modelo_disponible = 'gemini-1.5-flash' # fallback
try:
    print("\nBuscando modelos compatibles con tu cuenta...")
    modelos = list(cliente_gemini.models.list())
    nombres = [m.name for m in modelos]
    
    if nombres:
        # Buscamos el mejor modelo disponible para tu cuenta (ej. gemini-2.0, flash-8b, etc.)
        for n in nombres:
            if 'flash' in n or 'pro' in n:
                modelo_disponible = n.replace('models/', '')
                break
        else:
            modelo_disponible = nombres[0].replace('models/', '')
            
    print(f"✅ ¡Éxito! Modelo asignado automáticamente: {modelo_disponible}")
except Exception as e:
    print("\n⚠️ Error al listar modelos (revisa si tu API key tiene restricciones). Usando modelo por defecto.")

# Variable global para el generador
global_modelo_gemini = modelo_disponible
"""

lines = new_code.split('\n')
new_source = [line + '\n' for line in lines[:-1]] + [lines[-1]]

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source_str = "".join(cell["source"])
        if "# 2. IMPORTACIÓN DE LIBRERÍAS Y CONFIGURACIÓN DE GEMINI" in source_str:
            cell["source"] = new_source
            break

with open(filepath, "w", encoding="utf-8", newline='\n') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
    f.write('\n')
