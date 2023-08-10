import streamlit as st



def Inicio_content():
    st.markdown(
    """
    # Instalación de software
    """  
    )

    st.markdown(
    """
    ## Vivado
    [Vivado](https://www.xilinx.com/support/download.html)
    """  
    )
    st.image("https://cdn.imperix.com/doc/wp-content/uploads/2021/08/vivado_design_suite_ml_edition.png")

    st.markdown(
    """
    ## Git
    [Git](https://git-scm.com/)
    """  
    )
    st.image("https://blog.coffeedevs.com/content/images/size/w1000/2016/07/Git-rename-branch.jpg")


def suma_content():
    st.header("Suma de Dos Números en C")
    code = """
    #include <stdio.h>
    
    int main() {
        int a, b, suma;
        printf("Introduce dos números: ");
        scanf("%d %d", &a, &b);
        suma = a + b;
        printf("La suma de %d y %d es %d\\n", a, b, suma);
        return 0;
    }
    """
    st.code(code, language='c', line_numbers=True)



def main():
    st.set_page_config(
    page_title="SCL",
    page_icon="⌚",
    layout="centered",
    initial_sidebar_state="expanded"
)

    st.title('03LIB319 - Síntesis de Circuitos Lógicos')

    # Menú en el sidebar
    menu = ["Inicio", "Contenido"]
    choice = st.sidebar.selectbox("Elige un tópico:", menu)

    if(choice == "Inicio"):
        Inicio_content()
    elif(choice == "Contenido"):
        pass
        #suma_content()



if __name__ == "__main__":
    main()