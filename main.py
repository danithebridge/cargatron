import streamlit as st
import functions as ft

st.set_page_config(layout='wide')

pagina = st.sidebar.selectbox('Página', ('Home', 'Datos'))

if pagina == 'Home':
    ft.home()
elif pagina == 'Datos':
    ft.datos()


