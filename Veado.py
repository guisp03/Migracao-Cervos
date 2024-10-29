from pathlib import Path

import streamlit as st

dir_path = Path(__file__).parent

def deer_page():
    st.set_page_config(
        page_title="Análise das migrações do veado-vermelho",
        page_icon=":deer", 
        initial_sidebar_state="collapsed"
    )

    st.title("Veado-vermelho 🦌")
    st.image(str(dir_path / "images/female_red_deer.jpg"))
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas in nulla justo. Mauris mattis bibendum eros. Duis elementum purus nec ex sodales vehicula. Aenean accumsan arcu vitae sapien interdum lobortis. Donec urna lacus, interdum eget interdum vitae, elementum et tellus. Nulla suscipit efficitur eros vel consectetur. Sed a blandit ligula, porta molestie dolor. Vivamus quis eros vel purus mollis cursus. Suspendisse potenti. Mauris interdum mattis magna id elementum. Nulla dapibus eros dictum dolor faucibus vehicula. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus ac ligula dolor.")
    st.write("Sed finibus tincidunt eleifend. Vestibulum fermentum quis nunc sed imperdiet. Nullam hendrerit neque felis, vitae egestas ante euismod sit amet. Morbi euismod mollis augue, vitae scelerisque orci efficitur quis. Nullam eget massa vel nisl rutrum molestie eu vel dui. Integer accumsan eros odio, a ultricies arcu venenatis ut. Nullam feugiat dapibus porta. Proin eget posuere magna. Maecenas id nibh ornare, fringilla leo sit amet, varius magna. Praesent convallis, elit sit amet blandit tempus, magna ligula rutrum sem, id consequat orci orci at ante. Aenean eget ex aliquet, hendrerit mi vel, lobortis ex. Sed vel dui eu metus suscipit ullamcorper.")

if __name__ == "__main__":
   deer_page()