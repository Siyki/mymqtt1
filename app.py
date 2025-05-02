import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.set_page_config(
    page_title="MQTT Dashboard",
    page_icon="📡",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;600&display=swap');

html, body, .stApp {
    background: linear-gradient(to right, #fddb92, #d1fdff);
    color: #2b2b2b;
    font-family: 'Raleway', sans-serif;
    text-align: center;
}

h1, h2, h3, h4, h5, h6, .stTitle, .stHeader {
    color: #0077b6;
    text-align: center;
}

.stButton>button {
    background-color: #0077b6;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}

.stSidebar > div:first-child {
    background-color: #ffffff88;
    color: #2b2b2b;
    font-family: 'Raleway', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("📡 MQTT Monitor en Vivo")
st.write("🔧 Monitorizando mensajes MQTT con estilo")
st.write("🐍 Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):
    print("✅ El dato ha sido publicado\n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.success("📩 Mensaje recibido:")
    st.code(message_received, language='json')
