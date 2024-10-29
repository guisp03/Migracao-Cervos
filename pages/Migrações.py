from pathlib import Path

import pandas as pd
import streamlit as st

dir_path = Path(__file__).parent.parent
deer_data = pd.read_csv(str(dir_path / "data/female_red_deer_study.csv"))

def migrations_page():
    st.set_page_config(
        page_title="Migrações dos veados",
        page_icon=":woman-running",
        initial_sidebar_state="expanded"
    )

    st.title("Migração dos veados 🏃‍♀️")
    selected_deer = st.selectbox(
        "Selecione o veado",
        pd.unique(deer_data["individual-local-identifier"])
    )

if __name__ == "__main__":
    migrations_page()