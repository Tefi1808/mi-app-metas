import streamlit as st

st.title("Mi App de Metas 🎯")
st.write("Bienvenido a tu primera app con Streamlit en GitHub!")

meta = st.text_input("Escribe tu meta de hoy:")
if meta:
    st.success(f"Tu meta de hoy es: {meta}")
