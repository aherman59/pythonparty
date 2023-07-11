import streamlit as st
import pandas as pd
import plotly.express as px


########################################################################
# UTILS
########################################################################
def departements():
    df = chargement_donnees()
    return df["code_dep"].to_list()


@st.cache_data
def chargement_donnees():
    return pd.read_csv("resultat_departement.csv")


def graph(dep):
    df = chargement_donnees()
    df_dep = df[df.code_dep == dep]
    return px.bar(
        df_dep,
        x="code_dep",
        y=["nombre_logement", "nombre_maison", "nombre_appt"],
        barmode="group",
    )


########################################################################
# APPS
########################################################################

st.title("Ma super application !")

st.subheader("Mon super sous-titre")

departements = departements()
dep = st.selectbox("Choix du département", departements)

st.write(f"Département choisi : {dep}")

st.plotly_chart(graph(dep), use_container_width=True)
