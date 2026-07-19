import os
import streamlit as st
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAILike

# Cargar las variables del archivo .env (para local)
load_dotenv()

# Envolvemos el agente en la función que tu app.py necesita
def crear_agente_tutor():
    return Agent(
        name="Tutor IA",
        model=OpenAILike(
            id=st.secrets.get("LM_STUDIO_MODEL", os.getenv("LM_STUDIO_MODEL")),
            base_url=st.secrets.get("LM_STUDIO_BASE_URL", os.getenv("LM_STUDIO_BASE_URL")),
            api_key=st.secrets.get("LM_STUDIO_API_KEY", os.getenv("LM_STUDIO_API_KEY", "lm-studio")),
        ),
        instructions=[
            "Responde siempre en español.",
            "Explica el tema de forma sencilla.",
            "Da un ejemplo.",
            "Adapta la explicación al nivel del estudiante.",
        ]
    )
