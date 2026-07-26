# Explicación Detallada de los Módulos de Código

Este documento explica, bloque por bloque, el funcionamiento del Jupyter Notebook (`chatbot_clinico_colab.ipynb`) tras la última actualización arquitectónica que integra **RAG con Google Gemini Flash**.

---

## Módulo 1: Instalación de Dependencias
Instala los paquetes necesarios en el entorno de Google Colab:
*   `google-genai`: El SDK oficial y más reciente de Google para conectarse con Gemini.
*   `transformers` y `torch`: Herramientas de Machine Learning para utilizar el modelo ClinicalBERT (desarrollado por Hugging Face y PyTorch).
*   `scikit-learn`: Utilizado específicamente para calcular la similitud del coseno (Cosine Similarity).

---

## Módulo 2: Importación y Configuración Inteligente de Gemini
Este módulo se encarga de inicializar el "cerebro" generativo.
1.  **Carga de API Key:** Usa `google.colab.userdata` para buscar la clave secreta `GEMINI_API_KEY` de forma segura. Si el código corre localmente, usa un prompt interactivo (`getpass`).
2.  **Detección Automática de Modelo:** Realiza una petición a la API de Google para listar los modelos que tu cuenta tiene permitidos usar. 
3.  **Selección:** Busca específicamente la cadena "flash" o "pro". La última actualización garantiza que el modelo usado sea **Gemini 1.5 Flash** (o superior), el cual es ultrarrápido e ideal para el triaje en tiempo real.

---

## Módulo 3: Base de Datos de la Clínica (`DatabaseMock`)
Como no hay un motor SQL conectado, se usa una clase de Python que actúa como una base de datos en memoria (Mock).
*   Almacena un diccionario estructurado (`self.medicos`).
*   Organiza la información por especialidades (Medicina General, Cardiología, Psicología, Fisioterapia).
*   Para cada especialidad, guarda una lista de médicos y su variable booleana `disponible` (True/False).
*   La función `obtener_especialidades()` es clave en la nueva versión porque permite extraer **toda la clínica** para entregársela al modelo de IA.

---

## Módulo 4: Motor de Búsqueda RAG - Retriever (`ClinicalRetriever`)
Este módulo representa la parte **"Retrieval"** de la arquitectura RAG.
1.  **ClinicalBERT:** Carga un modelo pre-entrenado con millones de textos médicos (`emilyalsentzer/Bio_ClinicalBERT`).
2.  **Base de Conocimientos Interna:** Una lista de protocolos (ej. Infarto = Código Rojo; Resfriado = Código Verde; Ansiedad = Código Amarillo).
3.  **Embeddings (Vectorización):** Convierte el texto de los protocolos a vectores matemáticos multidimensionales.
4.  **Búsqueda Semántica:** Cuando el paciente escribe sus síntomas, este módulo convierte esos síntomas en un vector y busca matemáticamente cuál de los protocolos se parece más (usando *Cosine Similarity*). Retorna el protocolo oficial al sistema principal.

---

## Módulo 5: Triaje Inteligente y Generación RAG (¡Última Actualización!)
Este es el núcleo de la magia. Combina los datos obtenidos con el poder de razonamiento de Gemini.
Se divide en dos funciones:

### `procesar_mensaje_whatsapp_rag(mensaje_paciente)`
*   **Paso 1 (Recuperación):** Llama al `ClinicalRetriever` y obtiene el protocolo médico (Ej: "Protocolo Ansiedad").
*   **Paso 2 (Contexto Global):** Llama a la Base de Datos y arma una cadena de texto gigante con el resumen de *todas* las especialidades y la disponibilidad de todos los doctores.
*   **Paso 3 (Invocación):** Pasa los síntomas, el protocolo y la base de datos a Gemini.

### `generar_respuesta_gemini(sintomas, protocolo, especialidades_db)`
Este es el motor de razonamiento lógico (**Augmented Generation**).
Usa un **Prompt de Ingeniería** muy específico donde se le exige a Gemini Flash que haga lo siguiente:
1.  Razonar los síntomas contra el protocolo para descubrir **qué especialidad se necesita**.
2.  Leer el string de la base de datos para ver **quién está libre en esa especialidad específica**.
3.  Si hay una urgencia grave (Código Rojo dictado por el protocolo), ignorar la base de datos y mandar al paciente a Urgencias.
4.  Si hay disponibilidad, redactar un texto humano de 2 párrafos indicando que la cita ha sido pre-asignada con el doctor disponible correcto (Ej: "Te asignaremos con la Dra. Ruiz de Psicología").

---

## Módulo 6: El Simulador (Bucle Principal y CLI)
Es la interfaz de usuario en la consola de comandos.
*   **Menú Infinito (`while True`):** Mantiene el programa corriendo ofreciendo las 5 opciones principales.
*   **Opción 1 (`agendar_cita_flujo`):** Es el método tradicional (sin IA). Pregunta paso a paso con `input()` todos los datos (nombre, hora, especialidad). Si la hora está ocupada, tiene un algoritmo rudimentario para sugerir 3 horarios alternativos.
*   **Opción 2 (Evaluación Médica):** Intercepta la solicitud, pide los síntomas por texto libre, y dispara todo el flujo del **Módulo 5** (RAG), permitiendo que la IA evalúe y responda sin tener que pasar por el aburrido menú manual.
