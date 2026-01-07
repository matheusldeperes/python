import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Configuração da página para ocupar a tela toda
st.set_page_config(layout="wide")

# Atualiza a página a cada 30 segundos
count = st_autorefresh(interval=30000, key="framereload")

# Lista de links (Use o link de "Publicar na Web")
links = [
    "https://app.powerbi.com/view?r=eyJrIjoiMmUxMjMzMmQtM2FhMC00NmMyLThkYzQtM2I2OTNlY2M4MjA1IiwidCI6IjgwNGM1M2Y3LTIwNWEtNDI4NS1hNjhmLWVjOTU4NzllOTYzYiJ9",
   # "https://app.powerbi.com/view?r=eyJrIjoiMTI5MDM0M2QtMGU1ZS00ODE3LWI0NGMtZTcwYWIyMDA0NGQ4IiwidCI6IjgwNGM1M2Y3LTIwNWEtNDI4NS1hNjhmLWVjOTU4NzllOTYzYiJ9"
]

# Lógica para alternar o link baseado no contador de refresh
indice = count % len(links)

# Exibindo o dashboard
st.components.v1.iframe(links[indice], height=800, scrolling=False)