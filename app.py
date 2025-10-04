import streamlit as st
import streamlit.components.v1 as components


# -------------------------------------------------
# Layout & Styles
# -------------------------------------------------
st.set_page_config(
    page_title="Wertminderung Rechner", page_icon="altes_Teil_32x32.ico", layout="wide"
)

st.markdown(
    """
    <style>
        .stApp {background-color:#2c3e50;color:#ffb90f;}
        h1,h2,h3,h4,h5,h6,p,label,.markdown-text-container {color:#ffb90f !important;}
        .stTextInput > div > input {background-color:#ecf0f1;color:#2c3e50;font-weight:bold;}
        .stButton > button {background-color:#34495e;color:white;font-weight:bold;}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# Konstanten und Hilfsfunktionen
# -------------------------------------------------


def parse_float(value: str) -> float:
    """Parst eine Zahl mit deutschem oder englischem Dezimaltrennzeichen."""
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(value.replace(",", "."))
    except Exception:
        return 0.0


col1, col2 = st.columns([1, 1])

with col1:
    st.header("reine Wertminderung")

    anschaffungswert_input = st.text_input(
        "Anschaffungswert (€):", placeholder="z.B. 1000,00"
    )

    anschaffungswert = parse_float(anschaffungswert_input)
    prozent_liste = list(range(5, 55, 5))  # 5, 10, 15, ..., 50
    wertminderungs_prozent = st.selectbox(
        "Prozentuale Wertminderung (%):", prozent_liste
    )

    if anschaffungswert > 0:
        wertminderung = anschaffungswert * (wertminderungs_prozent / 100)
        wertminderungs_text = f"{wertminderung:,.2f}€"

        st.subheader("Ergebnis:")
        st.write(f"**Wertminderung:** {wertminderungs_text}")

        st.code(wertminderungs_text, language=None)
    else:
        st.info("Bitte geben Sie einen gültigen Anschaffungswert ein.")
