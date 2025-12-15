# RAG IA Assistant

Este proyecto es una aplicación de Asistente de IA con RAG (Retrieval-Augmented Generation) construida en Python, LangChain y Gradio, lista para desplegar en Railway o cualquier plataforma cloud.

## ¿Qué hace esta app?

- Permite chatear con una IA avanzada (Google Gemini) que puede responder preguntas usando tanto su conocimiento general como documentos que tú subas.
- Puedes cargar archivos PDF y textos, que la IA usará como contexto para darte respuestas más precisas y personalizadas.
- Incluye una interfaz web amigable (Gradio) para interactuar fácilmente.
- Soporta búsqueda semántica en los documentos cargados.
- Todo el procesamiento y almacenamiento de documentos se realiza en memoria (no se guardan en disco).

## Tecnologías principales
- **Python 3.10+**
- **LangChain** (orquestación de LLM y RAG)
- **Google Gemini** (modelo LLM y embeddings)
- **Gradio** (interfaz web tipo chat)
- **Railway** (despliegue cloud)

## ¿Cómo funciona?
1. Sube documentos PDF o texto desde la interfaz web.
2. La IA procesa y "lee" los documentos usando embeddings y vector store.
3. Haz preguntas en el chat: la IA buscará primero en tus documentos y luego usará su conocimiento general si es necesario.
4. Puedes limpiar la base de conocimiento o el historial de chat en cualquier momento.

## Despliegue rápido
1. Clona el repo y configura tu archivo `.env` con tu clave de Google Gemini.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta `python app.py` y accede a la interfaz web.
4. Para producción, despliega en Railway siguiendo el script `deploy_to_railway.sh`.

## Variables de entorno
- `GOOGLE_API_KEY`: Tu clave de API de Google Gemini (obligatoria).

## Créditos
- Proyecto creado por Waterproof82 con ❤️ y tecnología de código abierto.
