import json

filepath = "d:/INTELIGENCIA ARTIFICIAL/chatbot_clinico_colab.ipynb"
with open(filepath, "r", encoding="utf-8") as f:
    nb = json.load(f)

new_code = r"""def generar_respuesta_gemini(sintomas, protocolo, especialidades_db):
    prompt = f'''
    Eres el asistente virtual médico (Triaje AI) de una clínica. Debes asignar al paciente al médico adecuado basándote en sus síntomas y la disponibilidad.

    SÍNTOMAS DEL PACIENTE: '{sintomas}'
    PROTOCOLO SUGERIDO POR IA: '{protocolo}'
    
    BASE DE DATOS DE MÉDICOS Y DISPONIBILIDAD:
    {especialidades_db}
    
    INSTRUCCIONES:
    1. Analiza los síntomas y el protocolo para determinar qué especialidad necesita el paciente (ej. Cardiología, Medicina General, Psicología, Fisioterapia).
    2. Revisa la base de datos de médicos y busca un doctor que esté DISPONIBLE en esa especialidad.
    3. Si es Código Rojo (urgencia vital, como infarto o dolor de pecho grave), advierte al paciente con firmeza de ir a URGENCIAS inmediatamente.
    4. Si hay un médico disponible adecuado, asígnale la cita mencionando el nombre del doctor y su especialidad. Si no hay disponible en su especialidad, ofrécele Medicina General como alternativa.
    5. Redacta la respuesta final de forma empática, profesional y en máximo 2 párrafos cortos, como si fueras humano respondiendo por WhatsApp.
    '''
    try:
        # Utilizando la nueva sintaxis de google-genai con el modelo detectado (Gemini Flash)
        respuesta = cliente_gemini.models.generate_content(
            model=global_modelo_gemini,
            contents=prompt,
        )
        return respuesta.text
    except Exception as e:
        return f"[Error de redacción AI]: Revise su API Key. Detalles técnicos: {str(e)}"

def procesar_mensaje_whatsapp_rag(mensaje_paciente):
    # 1. Recuperación de Información (ClinicalBERT)
    protocolo = retriever.retrieve(mensaje_paciente)
    print(f"\n🧠 [Motor Interno - Protocolo Encontrado]: {protocolo}")
    
    # 2. Consulta a Base de Datos (Toda la disponibilidad)
    # Extraemos un resumen de la base de datos para pasárselo a Gemini
    especialidades = db.obtener_especialidades()
    resumen_db = ""
    for k, esp in especialidades.items():
        resumen_db += f"- Especialidad: {esp['nombre_esp']}\n"
        for doc in esp['doctores']:
            disp = 'Disponible' if doc['disponible'] else 'Ocupado'
            resumen_db += f"  * Dr. {doc['nombre']} ({disp})\n"
    
    # 3. Generación Aumentada (Gemini Flash razona y asigna el médico)
    print(f"✨ [Gemini AI ({global_modelo_gemini}) Analizando síntomas y asignando médico...]")
    respuesta_final = generar_respuesta_gemini(mensaje_paciente, protocolo, resumen_db)
    
    print("\n🤖 [Respuesta Final del Chatbot en WhatsApp]:")
    print(f"{respuesta_final}\n")
"""

lines = new_code.split('\n')
new_source = [line + '\n' for line in lines[:-1]] + [lines[-1]]

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source_str = "".join(cell["source"])
        if "def procesar_mensaje_whatsapp_rag" in source_str:
            cell["source"] = new_source
            break

with open(filepath, "w", encoding="utf-8", newline='\n') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("¡Notebook actualizado correctamente con el sistema de asignación avanzado con Gemini!")
