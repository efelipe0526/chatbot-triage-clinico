import json

filepath = "d:/INTELIGENCIA ARTIFICIAL/chatbot_clinico_colab.ipynb"
with open(filepath, "r", encoding="utf-8") as f:
    nb = json.load(f)

new_code = r"""import time

citas_agendadas = {}

def agendar_cita_flujo():
    print("\n👤 Por favor, ingresa tu nombre completo:")
    nombre = input("> ")
    
    print("\n🪪 Digite su número de cedula:")
    cedula = input("> ")
    
    print("\n📞 Ingrese su número de teléfono:")
    telefono = input("> ")
    
    print("\n🩺 Selecciona una especialidad:")
    print("1️⃣ 🩺 Medicina General")
    print("2️⃣ ❤️ Cardiología")
    print("3️⃣ 🧠 Psicología")
    print("4️⃣ 🦴 Fisioterapia")
    esp_opcion = input("\nResponde con el número: ")
    
    especialidades = db.obtener_especialidades()
    if esp_opcion not in especialidades:
        print("\n❌ Opción inválida, volviendo al menú principal...")
        time.sleep(2)
        return
        
    esp_nombre = especialidades[esp_opcion]["nombre_esp"]
    doctores = especialidades[esp_opcion]["doctores"]
    
    print("\n👨‍⚕️ Ingrese el número del médico:")
    for idx, doc in enumerate(doctores):
        disp = "(Disponible)" if doc['disponible'] else "(Ocupado)"
        print(f"{idx+1}. {doc['nombre']} {disp}")
    
    doc_opcion = input("> ")
    try:
        doc_idx = int(doc_opcion) - 1
        medico_seleccionado = doctores[doc_idx]
        if not medico_seleccionado["disponible"]:
            print("\n❌ El médico seleccionado está ocupado. Volviendo al menú principal...")
            time.sleep(2)
            return
        medico_nombre = medico_seleccionado["nombre"]
    except:
        print("\n❌ Selección inválida. Volviendo al menú principal...")
        time.sleep(2)
        return

    print("\n📆 ¿Qué fecha prefieres para tu cita? (Ej: mañana, 25/03/2026)")
    fecha = input("> ")
    
    while True:
        print("\n🕐 ¿A qué hora te gustaría? (Ej: 3pm, 14:30)")
        hora = input("> ")
        
        # Validar si el horario ya está ocupado
        if medico_nombre in citas_agendadas and fecha in citas_agendadas[medico_nombre] and hora in citas_agendadas[medico_nombre][fecha]:
            print(f"\n😔 ¡Ups! Lo sentimos mucho, {nombre}.")
            print(f"El/La {medico_nombre} ya tiene una cita programada a las {hora} para el día {fecha}.")
            
            # Sugerir alternativas
            horas_ocupadas = citas_agendadas[medico_nombre][fecha]
            horas_comunes = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "8am", "9am", "10am", "11am", "2pm", "3pm", "4pm", "5pm"]
            horas_disponibles = [h for h in horas_comunes if h not in horas_ocupadas and h != hora]
            
            if horas_disponibles:
                print("\n✨ ¡Pero no te preocupes! Tenemos estos otros horarios disponibles ese mismo día:")
                sugerencias = horas_disponibles[:3]
                for idx, h_sug in enumerate(sugerencias):
                    print(f"  {idx+1}️⃣ {h_sug}")
                print(f"  {len(sugerencias)+1}️⃣ Prefiero escribir otra hora diferente")
                
                opcion_hora = input(f"\nElige una opción (1-{len(sugerencias)+1}): ")
                try:
                    opcion_idx = int(opcion_hora) - 1
                    if 0 <= opcion_idx < len(sugerencias):
                        hora = sugerencias[opcion_idx]
                        print(f"\n✅ ¡Excelente elección! Hemos actualizado tu hora a las {hora}.")
                        break
                except:
                    pass
                print("\n🔄 Entendido. Por favor, ingresa una nueva hora.")
            else:
                print("\n📅 Lamentablemente no tenemos más horarios sugeridos disponibles. Por favor intenta con otra fecha u hora.")
        else:
            break
            
    print("\n📝 Por favor, describe brevemente el motivo de tu consulta:")
    motivo = input("> ")
    
    print("\n📋 *Confirma tus datos: *")
    print(f"👤 Nombre: {nombre}")
    print(f"🪪 Cédula: {cedula}")
    print(f"🩺 Especialidad: {esp_nombre}")
    print(f"👨‍⚕️ Médico: {medico_nombre}")
    print(f"📆 Fecha: {fecha}")
    print(f"🕐 Hora: {hora}")
    print(f"📝 Motivo: {motivo}")
    
    confirmar = input("\n¿Confirmar? (sí/no): ").lower()
    if confirmar in ['si', 'sí', 's']:
        print(f"\n✅ *¡Cita agendada exitosamente!* Te esperamos el {fecha} a las {hora}.")
        
        # Guardar la cita agendada
        if medico_nombre not in citas_agendadas:
            citas_agendadas[medico_nombre] = {}
        if fecha not in citas_agendadas[medico_nombre]:
            citas_agendadas[medico_nombre][fecha] = []
        citas_agendadas[medico_nombre][fecha].append(hora)
    else:
        print("\n❌ Cita cancelada.")
    time.sleep(3)

# ----------------- BUCLE PRINCIPAL -----------------
while True:
    print("\n" + "="*50)
    print("✨ *Bienvenido al Centro de Diálisis Margarita* ✨")
    print("Tu salud es nuestra prioridad. 🏥")
    print("\n¿En qué puedo ayudarte hoy?")
    print("*Opciones disponibles:*")
    print("1️⃣ 📅 Agendar Cita Completa")
    print("2️⃣ 🤖 Evaluación Médica (Triaje RAG AI)")
    print("3️⃣ ❓ Preguntas Frecuentes")
    print("4️⃣ 📞 Contacto")
    print("5️⃣ ❌ Salir del Simulador")
    
    opcion = input("\nResponde con el número de la opción: ")
    
    if opcion == '1':
        agendar_cita_flujo()
    elif opcion == '2':
        sintomas = input("\n👤 [Tú]: Por favor, describe tus síntomas médicos: ")
        print("\n⏳ Evaluando... (RAG Activo)")
        procesar_mensaje_whatsapp_rag(sintomas)
        time.sleep(3)
    elif opcion == '3':
        print("\n🤖 [Chatbot]: Nuestro horario de atención es de 8am a 6pm. Para más dudas, contacta a soporte.")
        time.sleep(2)
    elif opcion == '4':
        print("\n🤖 [Chatbot]: Puedes llamarnos al 01-8000-CLINICA o escribirnos a contacto@margarita.com")
        time.sleep(2)
    elif opcion == '5':
        print("\n🤖 [Chatbot]: Gracias por usar el sistema. ¡Cuídate mucho! 👋")
        break
    else:
        print("\n🤖 [Chatbot]: ⚠️ Opción no válida.")
        time.sleep(1)
"""

lines = new_code.split('\n')
new_source = [line + '\n' for line in lines[:-1]] + [lines[-1]]

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source_str = "".join(cell["source"])
        if "def agendar_cita_flujo():" in source_str:
            cell["source"] = new_source
            break

with open(filepath, "w", encoding="utf-8", newline='\n') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
    f.write('\n')
