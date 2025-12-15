import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Cargar variables de entorno (.env)
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("--------------------------------------------------")
if not api_key:
    print("❌ ERROR: No se encontró GOOGLE_API_KEY en el archivo .env")
    exit()
else:
    print(f"🔑 Usando API Key: ...{api_key[-5:]} (Últimos 5 caracteres)")
print("--------------------------------------------------")

# 2. Configurar la librería
genai.configure(api_key=api_key)

print("📡 Conectando con Google para listar modelos disponibles...")

try:
    # 3. Pedir la lista a Google
    modelos = list(genai.list_models())
    
    cantidad = 0
    print("\n✅ MODELOS DISPONIBLES PARA TI:")
    for m in modelos:
        # Filtramos solo los que sirven para generar texto/chat
        if 'generateContent' in m.supported_generation_methods:
            print(f"   • {m.name}")
            cantidad += 1
            
    if cantidad == 0:
        print("\n⚠️  ATENCIÓN: La conexión funciona, pero la lista está VACÍA.")
        print("   Esto significa que tu API Key es válida, pero el PROYECTO")
        print("   tiene la 'Generative Language API' deshabilitada o restringida.")
    else:
        print(f"\nTotal encontrados: {cantidad}")

except Exception as e:
    print(f"\n💥 ERROR DE CONEXIÓN:\n{e}")
    print("\nPosibles causas:")
    print("1. Tu API Key es incorrecta o fue borrada.")
    print("2. Tienes restricciones de IP/Android que bloquean este script.")
    print("3. No tienes internet.")