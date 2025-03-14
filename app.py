import streamlit as st
import pandas as pd
import duckdb

# Création des onglets
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# Données pour le DataFrame initial
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

# Onglet 1 - Saisie de requête SQL
with tab1:
    sql_query = st.text_area(label="Entrez votre input")

    if sql_query.strip():  # Si une requête est saisie
        try:
            result = duckdb.query(sql_query).df()
            st.write(f"Vous avez entré la query suivante : {sql_query}")
            st.dataframe(result)
        except Exception as e:
            st.error(f"Erreur lors de l'exécution de la requête : {e}")
    else:  # Si aucune requête n'est saisie, afficher le DataFrame initial
        st.warning("Veuillez entrer une requête SQL.")
        st.dataframe(df)




