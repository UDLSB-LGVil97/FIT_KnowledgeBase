import streamlit as st



def Inicio_content():
    st.markdown(
    """
    # Instalación de software
    """  
    )
    st.divider()

    st.markdown(
    """
    ## Visual Studio Code
    [Visual Studio Code](https://code.visualstudio.com/)
    """  
    )
    st.image("https://code.visualstudio.com/opengraphimg/opengraph-home.png")
    st.divider()

    st.markdown(
    """
    ### Complementos
    """  
    )
    tab1, tab2, tab3, tab4 = st.tabs(["Material Icon Theme", "Code Runner", "C/C++ Extension Pack", "Compilador"])
    with tab1:
        st.markdown("[Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)")
        st.image("https://i.ibb.co/rK90HRc/extension-icons.png", width=500)
    with tab2:
        st.markdown("[Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)")
        st.image("https://i.ibb.co/T0n6pF0/extension-runner.png", width=500)
    with tab3:
        st.markdown("[C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack)")
        st.image("https://i.ibb.co/ScWkYR9/extension-c.png", width=500)
    with tab4:
        st.markdown("[TDM-GCC](https://jmeubank.github.io/tdm-gcc/)")
        st.image("https://i.ibb.co/xCm3tXr/complement-tdmgcc.png", width=500)
        st.write("Windows 10/11")
        st.video("https://www.youtube.com/watch?v=uPGs8eJ98aE")
    st.divider()

    st.markdown(
    """
    ## Git
    [Git](https://git-scm.com/)
    """  
    )
    st.image("https://blog.coffeedevs.com/content/images/size/w1000/2016/07/Git-rename-branch.jpg")
    st.divider()

    st.markdown(
    """
    ## PSoC Creator
    [PSoC Creator v4.4](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.psoccreator)
    [.NET Framework 3.5](https://dotnet.microsoft.com/es-es/download/dotnet-framework/net35-sp1)
    """  
    )
    st.image("https://i.ytimg.com/vi/eacL0myDFws/hqdefault.jpg")
    st.divider()

    st.markdown(
    """
    ## Arduino IDE
    [Arduino IDE](https://www.arduino.cc/en/software)
    """  
    )
    st.image("https://docs.arduino.cc/static/36ffc036e2c2e9fcdec541c603989a81/c6720/local-sketchbook.png")
    st.divider()

    st.markdown(
    """
    ## Hercules SETUP utility
    [Hercules SETUP utility](https://www.hw-group.com/software/hercules-setup-utility)
    """  
    )
    st.image("https://www.hw-group.com/files/styles/large/public/swapplication/5462-hercules-setup-utility/serial1.png?itok=4_EL1BA-")


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
    page_title="MPU",
    page_icon="📟",
    layout="centered",
    initial_sidebar_state="expanded"
)

    st.title('05LIE531 - Diseño con Microprocesadores')


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