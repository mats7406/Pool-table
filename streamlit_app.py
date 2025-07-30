import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Biljardbord i ditt rum", layout="centered")

st.title("🎱 Lägg till ett biljardbord i ditt rum")
st.write("Ladda upp ett foto av ditt rum och välj ett biljardbord nedan!")

# Ladda upp bild
uploaded_image = st.file_uploader("📷 Ladda upp bild på ditt rum", type=["jpg", "jpeg", "png"])

# Välj biljardbord
bord_val = st.selectbox("🎯 Välj biljardbord", ["Inget", "Bord 1", "Bord 2"])

if uploaded_image and bord_val != "Inget":
    room = Image.open(uploaded_image).convert("RGBA")

    if bord_val == "Bord 1":
        table = Image.open("static/table1.png").convert("RGBA")
    else:
        table = Image.open("static/table2.png").convert("RGBA")

    table = table.resize((int(room.width * 0.8), int(room.height * 0.4)))
    room.paste(table, (int(room.width * 0.1), int(room.height * 0.5)), table)
    st.image(room, caption="Resultat", use_column_width=True)
else:
    if uploaded_image:
        st.image(uploaded_image, caption="Din bild", use_column_width=True)