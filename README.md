# 🏥 Chatbot Clínico de Triaje con RAG y Gemini AI

Este proyecto es un simulador de chatbot clínico inteligente para el "Centro de Diálisis Margarita". Está diseñado para interactuar con pacientes, agendar citas médicas y, de manera innovadora, realizar una **Evaluación Médica (Triaje) Inteligente** utilizando técnicas avanzadas de Inteligencia Artificial como RAG (Retrieval-Augmented Generation) y modelos generativos de Google (Gemini 1.5 Flash).

## 🚀 Características Principales

*   **📅 Agendamiento de Citas:** Un flujo conversacional paso a paso para recopilar datos del paciente, validar especialidades y asignar citas verificando la disponibilidad real de los médicos en la base de datos.
*   **🤖 Triaje Inteligente (Evaluación Médica con RAG):** 
    *   **Retrieval (ClinicalBERT):** Utiliza un modelo de lenguaje especializado en textos médicos (`emilyalsentzer/Bio_ClinicalBERT`) para buscar en una base de conocimientos interna el protocolo médico más adecuado para los síntomas presentados por el paciente.
    *   **Generation (Google Gemini Flash):** Envía los síntomas del paciente, el protocolo médico sugerido y la disponibilidad en tiempo real de los médicos al modelo Gemini. La IA razona qué especialidad es necesaria, busca qué doctor está disponible en esa área y redacta una respuesta empática y profesional para asignar al paciente o derivarlo a urgencias (Código Rojo) si es necesario.
*   **🩺 Base de Datos Simulada:** Cuenta con una base de datos de prueba para gestionar especialidades como Medicina General, Cardiología, Psicología y Fisioterapia, y manejar los estados (Disponible/Ocupado) de los médicos.

## 🛠️ Tecnologías Utilizadas

*   **Python:** Lenguaje principal de programación.
*   **Google Gemini AI API (`google-genai`):** Motor de razonamiento lógico, asignación de citas y redacción empática.
*   **Transformers (Hugging Face):** Uso de `ClinicalBERT` para vectorización de textos (Embeddings) y búsqueda semántica de protocolos.
*   **PyTorch (`torch`) y Scikit-Learn:** Cálculos de similaridad del coseno (Cosine Similarity) para la base de conocimientos RAG.
*   **Google Colab / Jupyter Notebook:** Entorno de ejecución principal.

## 📝 Instrucciones de Ejecución

1. **Abrir en Google Colab o Jupyter:** 
   El núcleo de este proyecto es el archivo `chatbot_clinico_colab.ipynb`. Sube este notebook a tu cuenta de Google Colab o ejecútalo en un entorno local compatible con Jupyter.
2. **Configurar la API Key de Gemini:**
   *   Si usas **Google Colab**, guarda tu clave de API en la pestaña de Secretos (🔑) con el nombre `GEMINI_API_KEY`. El código la detectará automáticamente.
   *   Si lo ejecutas de forma local, el sistema te pedirá que introduzcas la API Key manualmente al iniciar la celda de importaciones de Gemini.
3. **Instalación de Dependencias:**
   Asegúrate de tener instaladas las siguientes librerías (el notebook debería contener una celda para instalarlas):
   ```bash
   pip install google-genai torch transformers scikit-learn numpy
   ```
4. **Ejecutar las celdas:**
   Ejecuta las celdas en orden (importación de librerías, clases de Retriever y Base de Datos, funciones del sistema) hasta llegar al *Bucle Principal*.
5. **Interactuar con el Chatbot:**
   Una vez en el simulador, elige la opción **2️⃣ Evaluación Médica (Triaje RAG AI)** e ingresa tus síntomas (por ejemplo, "Me duele mucho el pecho y el brazo izquierdo" o "Tengo algo de ansiedad y no puedo dormir bien"). ¡Observa cómo la IA hace la magia!

## 📂 Estructura de Archivos

*   `chatbot_clinico_colab.ipynb`: El cuaderno de Jupyter principal con toda la lógica del chatbot y el Triaje RAG.
*   `update_nb_api*.py`: Scripts automatizados en Python usados para parchear e inyectar actualizaciones y mejoras de código directamente en las celdas del Notebook.
*   Archivos Markdown de documentación (Informes y presentaciones sobre los algoritmos diseñados).

---
*Desarrollado como proyecto de agentes de inteligencia artificial.*
