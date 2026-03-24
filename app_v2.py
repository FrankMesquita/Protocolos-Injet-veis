import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Protocolos Injetáveis", layout="wide")

# =========================
# ESTILO
# =========================
st.markdown(
    """
    <style>
    .main {
        background-color: #F5F7FA;
    }

    .bloco-topo {
        background: linear-gradient(135deg, #1B4F7C 0%, #2C5D8A 100%);
        padding: 34px 40px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
    }

    .topo-container {
        display: flex;
        align-items: center;
        gap: 24px;
    }

    .logo-topo {
        width: 150px;
        max-width: 150px;
        height: auto;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.08);
        padding: 6px;
    }

    .texto-topo {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .titulo-principal {
        color: white;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 10px;
        line-height: 1.2;
    }

    .subtitulo-principal {
        color: #DCEAF5;
        font-size: 20px;
        margin-bottom: 0;
    }

    .bloco-info {
        background-color: #EAF3FA;
        border-left: 6px solid #1B4F7C;
        padding: 18px 20px;
        border-radius: 12px;
        margin-top: 18px;
        margin-bottom: 28px;
        color: #2C3E50;
        font-size: 16px;
    }

    h1, h2, h3 {
        color: #1B4F7C !important;
    }

    div[data-testid="stSelectbox"] label,
    div[data-testid="stTextInput"] label,
    div[data-testid="stTextArea"] label,
    div[data-testid="stMultiSelect"] label {
        font-weight: 600;
        color: #2C3E50;
    }

    .stButton > button {
        background-color: #1B4F7C;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 22px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #163f63;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# TOPO
# =========================
topo_html = """
<div class="bloco-topo">
    <div class="topo-container">
        <img src="data:image/png;base64,{logo_b64}" class="logo-topo">
        <div class="texto-topo">
            <div class="titulo-principal">Formulário de Criação de Protocolos</div>
            <div class="subtitulo-principal">Hospital Vascular de Londrina + CKO Services</div>
        </div>
    </div>
</div>
"""

# Carrega a logo e converte para base64
import base64

logo_path = "assets/logo_hospital.png"
logo_b64 = ""

if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        logo_b64 = base64.b64encode(image_file.read()).decode("utf-8")

st.markdown(topo_html.format(logo_b64=logo_b64), unsafe_allow_html=True)

st.markdown(
    """
    <div class="bloco-info">
    <strong>Passo importante:</strong> Criação/validação dos protocolos com os respectivos ativos para avanço na criação dos pacotes, precificação, estruturação de materiais comerciais entre outros.
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================
# DADOS BASE
# =========================
protocolos = {
    "Lipedema": ["Celular", "Consolidação", "Performance"],
    "Linfedema": ["Celular", "Consolidação", "Performance"],
    "Pós-operatório": [],
    "Neuropatia diabética": [],
    "Desinflamação": [],
}

ativos_lista = [
    "Ácido Alfa-Lipoico 600mg/30ml - EV",
    "Coenzima Q10 100mg - IM",
    "Complexo B (sem B1) - EV",
    "Cúrcuma 200mg/2ml - EV",
    "Glutationa 600mg/5ml - EV",
    "HMB 50mg/2ml - EV",
    "L-Arginina 1250mg - EV",
    "L-Metionina 100mg/2ml - EV",
    "L-Taurina 200mg/2ml - EV",
    "Magnésio 400mg/1ml - EV",
    "N-Acetilcisteína 300mg/2ml - EV",
    "NADH 50mg pó liofilizado - IM",
    "Resveratrol - IM",
    "SAMe 200mg/2ml - EV",
    "Selênio 800mcg/2ml - EV",
    "Vitamina C 444mg/2ml - EV",
    "Vitamina D 600.000UI - IM",
    "5-OH-Triptofano 10mg/2ml - EV",
    "Soro fisiológico 0,9% 100ml",
    "Soro fisiológico 0,9% 500ml",
    "Procaína 2% 2ml",
]

# =========================
# SELEÇÃO DO PROTOCOLO
# =========================
st.header("1. Seleção do Protocolo")

protocolo = st.selectbox("Selecione o protocolo:", list(protocolos.keys()))

nivel = ""
if protocolos[protocolo]:
    nivel = st.selectbox("Nível do protocolo:", protocolos[protocolo])

duracao = ""
frequencia = ""
estrutura = ""

if protocolo == "Lipedema":
    duracao = "24 semanas (12 semanas injetáveis)"
    frequencia = "Semanal (8 semanas + pausa + 4 semanas)"
    estrutura = "Inclui injetáveis + nutrição + fisioterapia + drenagem + acompanhamento"
elif protocolo == "Linfedema":
    duracao = "24 semanas (ajustável)"
    frequencia = "Semanal"
    estrutura = "Maior foco em drenagem e fisioterapia"
elif protocolo == "Pós-operatório":
    duracao = "Aplicação única pós cirurgia"
    frequencia = "Imediato pós-operatório"
    estrutura = "Aplicado durante internação"
elif protocolo == "Neuropatia diabética":
    duracao = "A definir"
    frequencia = "Semanal"
    estrutura = "Baseado em ativos neuroprotetores"
elif protocolo == "Desinflamação":
    duracao = "4 a 8 semanas"
    frequencia = "Semanal"
    estrutura = "Foco em detox e anti-inflamatório"

# =========================
# ESTRUTURA DO PROTOCOLO
# =========================
st.header("2. Estrutura do Protocolo")

nome_protocolo = st.text_input("Nome do protocolo:", value=protocolo)
objetivo = st.text_area("Objetivo clínico:")
duracao_edit = st.text_input("Duração:", value=duracao)
frequencia_edit = st.text_input("Frequência:", value=frequencia)
estrutura_edit = st.text_area("Estrutura do tratamento:", value=estrutura)

# =========================
# ATIVOS
# =========================
st.header("3. Ativos do Protocolo")

ativos_selecionados = st.multiselect("Selecione os ativos:", ativos_lista)

# =========================
# COMPONENTES ADICIONAIS
# =========================
st.header("4. Componentes adicionais")

nutri = st.checkbox("Nutricionista")
drenagem = st.checkbox("Drenagem")
fisioterapia = st.checkbox("Fisioterapia")
personal = st.checkbox("Personal Trainer")
caneta = st.checkbox("Caneta emagrecedora")

# =========================
# SALVAR
# =========================
st.header("5. Salvar Protocolo")

if st.button("Salvar protocolo"):
    adicionais = []

    if nutri:
        adicionais.append("Nutricionista")
    if drenagem:
        adicionais.append("Drenagem")
    if fisioterapia:
        adicionais.append("Fisioterapia")
    if personal:
        adicionais.append("Personal Trainer")
    if caneta:
        adicionais.append("Caneta emagrecedora")

    dados = {
        "Protocolo": nome_protocolo,
        "Tipo de protocolo": protocolo,
        "Nível": nivel,
        "Objetivo clínico": objetivo,
        "Duração": duracao_edit,
        "Frequência": frequencia_edit,
        "Estrutura do tratamento": estrutura_edit,
        "Ativos selecionados": ", ".join(ativos_selecionados),
        "Adicionais": ", ".join(adicionais),
    }

    df_novo = pd.DataFrame([dados])
    caminho_arquivo = "respostas/protocolos.xlsx"

    if os.path.exists(caminho_arquivo):
        df_existente = pd.read_excel(caminho_arquivo)
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        df_final = df_novo

    df_final.to_excel(caminho_arquivo, index=False)

    st.success("Protocolo salvo com sucesso no Excel!")

    st.markdown("## Resumo do Protocolo")
    st.write("**Protocolo:**", nome_protocolo)
    st.write("**Tipo de protocolo:**", protocolo)

    if nivel:
        st.write("**Nível:**", nivel)

    st.write("**Objetivo:**", objetivo)
    st.write("**Duração:**", duracao_edit)
    st.write("**Frequência:**", frequencia_edit)
    st.write("**Estrutura:**", estrutura_edit)
    st.write("**Ativos:**", ", ".join(ativos_selecionados))
    st.write("**Adicionais:**", ", ".join(adicionais))