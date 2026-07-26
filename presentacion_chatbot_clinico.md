# Estructura de la Presentación Oral (Cumpliendo Rúbrica de Sobresaliente)
**Duración:** 10 - 15 minutos
**Proyecto:** Asistente Virtual Clínico (Chatbot) Basado en LLMs y RAG para Triaje Médico

---

## Diapositiva 1: Título y Presentación del Contexto
*   **Contenido:** 
    *   Título: Inteligencia Artificial en Urgencias Médicas: Un Chatbot Ético de Triaje.
*   **Guion Sugerido (Sobresaliente):** "Buenos días. Para este proyecto de IA Avanzada, he elegido un problema complejo que nos afecta a todos: la saturación de los sistemas de urgencias médicas. Les presentaré el diseño de un Chatbot clínico basado en Deep Learning que no solo busca eficiencia, sino que está diseñado desde sus cimientos para ser seguro, ético y equitativo."

---

## Diapositiva 2: Identificación Profunda del Problema
*   **Contenido:**
    *   Saturación hospitalaria vs. Necesidad de triaje inmediato.
    *   El peligro de la auto-medicación y la "cibercondría".
*   **Guion Sugerido:** "El problema no es solo que la gente espere, es que durante esa espera su condición puede agravarse. Un chatbot puede hacer un triaje en segundos. Sin embargo, justificar el uso de IA aquí es delicado: un error de la máquina puede costar vidas. Por eso, una solución genérica como ChatGPT no sirve para este contexto crítico."

---

## Diapositiva 3: Revisión Bibliográfica y Conexiones al Diseño
*   **Contenido:**
    *   Revisión de NLP Clínico (ClinicalBERT, Med-PaLM).
    *   El mayor peligro ético/técnico detectado: **Las Alucinaciones**.
*   **Guion Sugerido:** "Mi revisión bibliográfica exhaustiva reveló que aunque los Modelos de Lenguaje Grande (LLMs) son brillantes entendiendo texto, tienen un fallo crítico: 'alucinan' información. Conectando este hallazgo con mi diseño, tomé la decisión de descartar un modelo generativo puro e implementar una arquitectura que fuerce a la IA a decir siempre la verdad médica."

---

## Diapositiva 4: Diseño del Algoritmo: RAG y Asignación Inteligente
*   **Contenido:**
    *   Diseño Innovador: **RAG (Retrieval-Augmented Generation)** potenciado con razonamiento.
    *   Fase 1 (Retriever): Encuentra el protocolo médico oficial usando embeddings (ClinicalBERT).
    *   Fase 2 (Generador y Asignador): El modelo lee el protocolo y la disponibilidad completa de la clínica para deducir la especialidad y asignar al doctor idóneo.
*   **Guion Sugerido:** "Aquí está mi diseño innovador: una arquitectura RAG de doble vía. Primero, el modelo de recuperación (ClinicalBERT) busca un protocolo médico oficial según los síntomas. Luego, la magia generativa: le pasamos a la IA ese protocolo junto con la disponibilidad en tiempo real de toda la clínica. La IA razona qué especialidad se requiere, verifica quién está libre y asigna la cita automáticamente, o deriva a urgencias si es un código rojo."

---

## Diapositiva 5: Implementación Robusta y Eficiente (Gemini Flash)
*   **Contenido:**
    *   Implementación en Python (HuggingFace Transformers, PyTorch) sobre Google Colab.
    *   **Motor Generativo:** Uso estratégico de **Google Gemini 1.5 Flash** para ultra-baja latencia en el triaje.
    *   **Accesibilidad:** Diseño preparado para integrarse con WhatsApp Business.
*   **Guion Sugerido:** "En cuanto a la implementación técnica, utilicé Python en Google Colab. La decisión de diseño más crítica en esta fase fue seleccionar 'Google Gemini 1.5 Flash' como motor generativo. En emergencias, la latencia es vital. La variante 'Flash' asegura que el paciente reciba su triaje y asignación de doctor en milisegundos a través de WhatsApp. Además, su amplia ventana de contexto permite inyectar toda la base de datos del hospital en tiempo real."

---

## Diapositiva 6: Pruebas Exhaustivas y Equidad (Fairness)
*   **Contenido:**
    *   Auditoría de Equidad: Evaluación de sesgos lingüísticos.
    *   Paridad Demográfica frente a dialectos y niveles de educación.
*   **Guion Sugerido:** "Para obtener una evaluación 'Sobresaliente' en las pruebas, fui más allá de la precisión básica. Desarrollé una auditoría de equidad. Probé si el chatbot reconocía los síntomas de un infarto cuando se expresan en lenguaje médico formal, y cuando se expresan con modismos coloquiales. Si la IA solo entiende a pacientes con alta educación, es una IA discriminatoria. Mis pruebas de paridad garantizan la equidad lingüística."

---

## Diapositiva 7: Evaluación Crítica y Propuestas de Mejora
*   **Contenido:**
    *   Reflexión: La IA como herramienta, no como médico.
    *   Mejora Futura: Aprendizaje Federado para proteger la privacidad.
*   **Guion Sugerido:** "Evaluando críticamente mi algoritmo, reconozco sus limitaciones: carece del tacto humano y depende enteramente de la base de datos de protocolos. Como mejora futura, propongo implementar Aprendizaje Federado, permitiendo que la IA aprenda de datos hospitalarios mejorando su comprensión de dialectos locales, sin que la información privada de los pacientes salga de los servidores del hospital."
