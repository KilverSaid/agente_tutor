import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai.like import OpenAILike

# Cargar las variables del archivo .env
load_dotenv()

agente = Agent(
    name="Tutor IA",
    model=OpenAILike(
        id=os.getenv("LM_STUDIO_MODEL"),
        base_url=os.getenv("LM_STUDIO_BASE_URL"),
        api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
    ),
    instructions=[
        "Responde siempre en español.",
        "Explica el tema de forma sencilla.",
        "Da un ejemplo.",
        "Adapta la explicación al nivel del estudiante.",
        "Finaliza con una pregunta de evaluación."
    ],
    markdown=True,
)

def crear_agente_tutor():
    return agente