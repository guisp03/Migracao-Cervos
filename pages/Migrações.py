from pathlib import Path

import pandas as pd
import pydeck as pdk
import streamlit as st

dir_path = Path(__file__).parent.parent
deer_data = pd.read_csv(str(dir_path / "data/female_red_deer_study.csv"))

def migrations_page():
    st.set_page_config(
        page_title="Migrações dos veados",
        page_icon=":woman-running",
        initial_sidebar_state="expanded"
    )

    # pre-processing
    deer_data["timestamp"] = pd.to_datetime(deer_data["timestamp"]) 

    st.title("Migração dos veados 🏃‍♀️")
    selected_deer = st.selectbox(
        "Selecione o veado",
        pd.unique(deer_data["individual-local-identifier"])
    )

    selected_deer_data = deer_data.loc[
        deer_data["individual-local-identifier"] == selected_deer
    ]

    selected_year = st.selectbox(
        "Selecione o ano",
        pd.unique(selected_deer_data["timestamp"].dt.year)
    )

    filtered_deer_data = selected_deer_data.loc[
        selected_deer_data["timestamp"].dt.year == selected_year
    ]

    path_data = filtered_deer_data[
        ["location-long", "location-lat"]
    ].values.tolist()
    initial_lat = filtered_deer_data["location-lat"].median()
    initial_long = filtered_deer_data["location-long"].median()

    st.pydeck_chart(
        pdk.Deck(
            layers=pdk.Layer(       
                type="PathLayer",
                data=[{"path": path_data}],
                pickable=True,
                width_scale=20,
                width_min_pixels=2,
                get_color=[237, 28, 36],
                get_path="path",
                get_width=5,
            ),
            initial_view_state={
                "latitude": initial_lat,
                "longitude": initial_long,
                "zoom": 10,
                "pitch": 50,
            }
        )
    )

if __name__ == "__main__":
    migrations_page()