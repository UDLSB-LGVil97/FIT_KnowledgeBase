import streamlit as st

st.set_page_config(
    page_title="FIT-KnowledgeBase",
    page_icon="🏠",
)

st.write("# ¡Bienvenido a la Knowledge Basede la Facultad de Ingenierías y Tecnologías de la Universidad De La Salle Bajío 👋")

st.sidebar.header("🏠 Home")
st.sidebar.success("--- Selecciona una asignatura ---")

st.markdown(
    """
    Este dashboard está en construcción. Fue diseñado con el
    objetivo de brindar un sitio web con la documentación
    necesaria para el desarrollo de las materias presentes.
"""
)