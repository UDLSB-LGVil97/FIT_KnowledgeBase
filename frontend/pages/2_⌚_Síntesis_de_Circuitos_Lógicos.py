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


def Tutoriales_content():
    st.header("Tutoriales y grabaciones de clases")

    # Menú en la página
    menu_tutorial = ["Vivado", "1er Parcial", "2do Parcial", "3er Parcial"]
    choice_tutorial = st.selectbox("Elige una opción:", menu_tutorial)
    st.divider()

    if(choice_tutorial == "Vivado"):
        st.subheader("Pasos para sintetizar, implementar y cargar arquitectura digital a la tarjeta de desarrollo de FPGA")

        st.markdown(" ")
        st.markdown("**1.** Crear un proyecto nuevo. >> _Quick Start_ -> _Create Project_")
        st.image("https://i.ibb.co/BGYXwfr/Vivado-1.png", width=500)
        st.markdown(" ")
        st.markdown("**2.** Configurar el nombre del proyecto y la ubicación de guardado. Activar _Create project subdirectory_.")
        st.image("https://i.ibb.co/Ldb8Hcj/Vivado-2.png", width=500)
        st.markdown(" ")
        st.markdown("**3.** Seleccionar el tipo de proyecto y desactivar el resto de casillas. >> _RTL Project_")
        st.image("https://i.ibb.co/BC0CSjx/Vivado-3.png", width=500)
        st.markdown(" ")
        st.markdown("**4.** Agregar los archivos fuente de código VHDL (.vhd) para llevar a cabo la arquitectura digital. Activar _Copy sources into project_.")
        st.image("https://i.ibb.co/34p4qJ5/Vivado-4.png", width=500)
        st.markdown(" ")
        st.markdown("**5.** Agregar archivo de restricciones (.xdc) que le corresponde al modelo de la tarjeta de desarrollo. Activar _Copy constraints files into project_.")
        st.image("https://i.ibb.co/xhfw8FB/Vivado-5.png", width=500)
        st.markdown(" ")
        st.markdown("**6.** Seleccionar el modelo del CI del FPGA en la tarjeta de desarrollo. >> Family: _Artix-7_ -> Package: _csg324_ -> Speed: _-1_ -> Part: _xc7a100tcsg324-1_")
        st.image("https://i.ibb.co/sWsDJnw/Vivado-6.png", width=500)
        st.markdown(" ")
        st.markdown("**7.** De esta forma se llega al entorno de desarrollo. En _Design Sources_ se encuentran las jerarquías de la arquitectura con sus respectivos códigos de VHDL.")
        st.image("https://i.ibb.co/gwDMrms/Vivado-7.png", width=500)
        st.markdown(" ")
        st.markdown("**8.** Abrir el archivo de restricciones y hacer coincidir *todos* los nombres de las señales del código más alto en la jerarquía de la arquitectura contra las señales de los periféricos de la tarjeta de desarrollo.")
        st.image("https://i.ibb.co/vC9bs2f/Vivado-8.png", width=500)
        st.markdown(" ")
        st.markdown("**9.** _Flow Navigator_ -> _PROJECT MANAGER_ -> _Settings_")
        st.image("https://i.ibb.co/MPrhNBB/Vivado-9.png", width=500)
        st.markdown(" ")
        st.markdown("**10.** _Project Settings_ -> _Bitstream_ -> Activar la casilla de _bin_file_")
        st.image("https://i.ibb.co/JdKsj82/Vivado-10.png", width=500)
        st.markdown(" ")
        st.markdown("**11.** _Flow Navigator_ -> _SYNTHESIS_ -> _Run Synthesis_")
        st.image("https://i.ibb.co/wCp68tB/Vivado-11.png", width=500)
        st.markdown(" ")
        st.markdown("**12.** Dejar las opciones por defecto y usar el máximo de núcleos disponibles en la computadora en _Number of jobs_. Esperar a que se complete la síntesis.")
        st.image("https://i.ibb.co/mRvCY5b/Vivado-12.png", width=500)
        st.markdown(" ")
        st.markdown("**13.** Ya que se completó el proceso, seleccionar la opción _Open Synthesized Design_.")
        st.image("https://i.ibb.co/vQhLr2G/Vivado-13.png", width=500)
        st.markdown(" ")
        st.markdown("**14.** Pestaña _Tools_ -> _Edit Device Properties_")
        st.image("https://i.ibb.co/BGNPgFZ/Vivado-14.png", width=500)
        st.markdown(" ")
        st.markdown("**15.** _General_ -> _Bitstream Properties_ -> _Enable Bitstream Compression_: TRUE")
        st.image("https://i.ibb.co/dkdnvqH/Vivado-15.png", width=500)
        st.markdown(" ")
        st.markdown("**16.** _Configuration_ -> _Configuration Setup_ -> _Configuration Rate (MHz)_: 33")
        st.image("https://i.ibb.co/ZXBLkfb/Vivado-16.png", width=500)
        st.markdown(" ")
        st.markdown("**17.** _Configuration Modes_ -> Activar únicamente _Master SPI x4_")
        st.image("https://i.ibb.co/3fXSWry/Vivado-17.png", width=500)
        st.markdown(" ")
        st.markdown("**18.** _Flow Navigator_ -> _PROGRAM AND DEBUG_ -> _Generate Bitstream_")
        st.image("https://i.ibb.co/JrNHc2R/Vivado-18.png", width=500)
        st.markdown(" ")
        st.markdown("**19.** Guardar todos los cambios antes de generar el bitstream y activar la casilla de _Synthesized Design_.")
        st.image("https://i.ibb.co/KGDXfbz/Vivado-19.png", width=500)
        st.markdown(" ")
        st.markdown("**20.** Aceptar la alerta.")
        st.image("https://i.ibb.co/ypJxtZW/Vivado-20.png", width=500)
        st.markdown(" ")
        st.markdown("**21.** _Select an existing file_ -> Seleccionar el archivo de restricciones cargado previamente")
        st.image("https://i.ibb.co/DgQd09P/Vivado-21.png", width=500)
        st.markdown(" ")
        st.markdown("**22.** Aceptar la inicialización del proceso de _Implementation_.")
        st.image("https://i.ibb.co/DtJ7xkR/Vivado-22.png", width=500)
        st.markdown(" ")
        st.markdown("**23.** Dejar las opciones por defecto y usar el máximo de núcleos disponibles en la computadora en _Number of jobs_. Esperar a que se complete la implementación.")
        st.image("https://i.ibb.co/kMYNxTH/Vivado-23.png", width=500)
        st.markdown(" ")
        st.markdown("**24.** Ya que se completó el proceso, seleccionar la opción _Open Hardware Manager_.")
        st.image("https://i.ibb.co/kBcxNRy/Vivado-24.png", width=500)
        st.markdown(" ")
        st.markdown("**25.** Aparecerá una banda de color verde dentro del entorno de desarrollo. Es importante conectar la tarjeta de desarrollo y encenderla para proceder.")
        st.image("https://i.ibb.co/WDtykyw/Vivado-25.png", width=500)
        st.markdown(" ")
        st.markdown("**26.** Dirigirse a la sección de la banda verde -> _Open target_ -> _Open New Target..._")
        st.image("https://i.ibb.co/rGjyjkh/Vivado-26.png", width=500)
        st.markdown(" ")
        st.markdown("**27.** Dejar la opción por defecto de _Local server_.")
        st.image("https://i.ibb.co/KK5MJR1/Vivado-27.png", width=500)
        st.markdown(" ")
        st.markdown("**28.** _Hardware Targets_ -> _xilinx_tcf_ -> _JTAG Clock Frequency_: 30000000")
        st.image("https://i.ibb.co/zrV0fdk/Vivado-28.png", width=500)
        st.markdown(" ")
        st.markdown("**29.** Seleccionar la opción de _Program device_.")
        st.image("https://i.ibb.co/DQTnj4f/Vivado-29.png", width=500)
        st.markdown(" ")
        st.markdown("**30.** Dejar el _Bitstream file_ por defecto y habilitar la casilla de _Enable end of startup check_. Programar el dispositivo.")
        st.image("https://i.ibb.co/xCnCb8S/Vivado-30.png", width=500)
        st.markdown(" ")
        st.markdown("**31.** ¡Listo! Una vez hechos todos los pasos, la tarjeta de desarrollo cargará en su memoria volátil la arquitectura digital diseñada. Es importante recalcar que si la tarjeta se desconecta o apaga, se perderá el programa y será necesario sólo volver a cargarlo.")
        st.image("https://i.ibb.co/0Qn3Byp/Vivado-31.png", width=500)
    elif(choice_tutorial == "1er Parcial"):
        st.subheader("Práctica #1 - Decodificador BIN a 7SEG")
        st.video("https://www.youtube.com/watch?v=-Jr8jsJ4JBg")
        st.video("https://www.youtube.com/watch?v=pPK1Mr01Ld0")
        st.divider()
        st.subheader("Práctica #2 - Divisor de frecuencia con FF")
        st.divider()
        st.subheader("Práctica #3 - Contador BCD (1 dígito)")
    elif(choice_tutorial == "2do Parcial"):
        pass
    elif(choice_tutorial == "3er Parcial"):
        pass



def main():
    st.set_page_config(
    page_title="SCL",
    page_icon="⌚",
    layout="centered",
    initial_sidebar_state="expanded"
)

    st.title('03LIB319 - Síntesis de Circuitos Lógicos')

    # Menú en el sidebar
    menu = ["Inicio", "Tutoriales"]
    choice = st.sidebar.selectbox("Elige un tópico:", menu)

    if(choice == "Inicio"):
        Inicio_content()
    elif(choice == "Tutoriales"):
        Tutoriales_content()



if __name__ == "__main__":
    main()