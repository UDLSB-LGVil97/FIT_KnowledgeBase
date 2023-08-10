import streamlit as st



def Inicio_content():
    st.write("# ¡Bienvenido a la Knowledge Base de la Facultad de Ingenierías y Tecnologías de la Universidad De La Salle Bajío 👋")

    st.markdown(
    """
    Este dashboard está en construcción. Fue diseñado con el
    objetivo de brindar un sitio web con la documentación
    necesaria para el desarrollo de las materias presentes.
    """
    )
    st.image("../assets/home/logo_FIT.jpg")



def main():
    st.set_page_config(
    page_title="FIT-KB",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)


    # Menú en el sidebar
    st.sidebar.info("--- Selecciona una asignatura ---")
    st.sidebar.warning(f"""
# ⚠️ ¡Importante! 
Es indispensable poseer una cuenta de GitHub para descargar los códigos provistos de cada clase.
https://github.com/LaSalleBajio-FIT""")
    Inicio_content()



if __name__ == "__main__":
    main()