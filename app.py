import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.set_page_config(
    page_title="Control MQTT",
    page_icon="🔌",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

html, body, .stApp {
    background: linear-gradient(to bottom right, #fdfbfb, #ebedee);
    color: #333;
    font-family: 'Quicksand', sans-serif;
    text-align: center;
}

h1, h2, h3, h4, h5, h6, .stTitle, .stHeader {
    color: #ff5722;
    text-align: center;
}

.stButton>button {
    background-color: #ff5722;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 0.5em 1em;
    margin: 0.3em;
    border: none;
}

.stSlider > div {
    color: #333;
}

.stSidebar > div:first-child {
    background-color: #ffe0d1;
    color: #333;
    font-family: 'Quicksand', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Control de Dispositivos vía MQTT")
st.subheader("Pulsa los botones para enviar comandos 🛰️")

st.write("🔍 Versión de Python:", platform.python_version())

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

broker = "157.230.214.127"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

col1, col2 = st.columns(2)

with col1:
    if st.button('🔛 Encender (ON)'):
        act1 = "ON"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s", message)

with col2:
    if st.button('🔴 Apagar (OFF)'):
        act1 = "OFF"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("cmqtt_s", message)

st.markdown("---")

st.subheader("⚙️ Control Analógico")
values = st.slider('Selecciona un valor para enviar:', 0.0, 100.0)
st.write('🔢 Valor seleccionado:', values)

if st.button('📤 Enviar valor analógico'):
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_a", message)
