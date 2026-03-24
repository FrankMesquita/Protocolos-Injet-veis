import os
from io import BytesIO

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Protocolos Injetáveis", layout="wide")

# =========================================================
# ESTILO
# =========================================================
st.markdown(
    """
    <style>
    .main {
        background-color: #F5F7FA;
    }

    .topo-box {
        background: linear-gradient(135deg, #1B4F7C 0%, #2C5D8A 100%);
        padding: 28px 34px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
    }

    .topo-titulo {
        color: white;
        font-size: 42px;
        font-weight: 700;
        line-height: 1.15;
        margin-bottom: 12px;
    }

    .topo-subtitulo {
        color: #DCEAF5;
        font-size: 19px;
        margin-bottom: 0;
    }

    .bloco-info {
        background-color: #EAF3FA;
        border-left: 6px solid #1B4F7C;
        padding: 18px 20px;
        border-radius: 12px;
        margin-top: 8px;
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
    div[data-testid="stMultiSelect"] label,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stRadio"] label {
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
        background-color: #163F63;
        color: white;
    }

    .stDownloadButton > button {
        background-color: #2C5D8A;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 22px;
        font-weight: 600;
    }

    .stDownloadButton > button:hover {
        background-color: #1B4F7C;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# TOPO
# =========================================================
col_topo_texto, col_topo_logo1, col_topo_logo2 = st.columns([6, 1.5, 1.5])

with col_topo_texto:
    st.markdown(
        """
        <div class="topo-box">
            <div class="topo-titulo">Formulário de Criação de Protocolos</div>
            <div class="topo-subtitulo">Hospital Vascular de Londrina + CKO Services</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_topo_logo1:
    if os.path.exists("assets/logo_hospital.png"):
        st.image("assets/logo_hospital.png", width=180)

with col_topo_logo2:
    if os.path.exists("assets/logo_cko.png"):
        st.image("assets/logo_cko.png", width=150)

st.markdown(
    """
    <div class="bloco-info">
    <strong>Passo importante:</strong> Criação/validação dos protocolos com os respectivos ativos para avanço na criação dos pacotes, precificação, estruturação de materiais comerciais entre outros.
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# BASE
# =========================================================
PROTOCOLS = {
    "Lipedema": ["Celular", "Consolidação", "Performance"],
    "Linfedema": ["Celular", "Consolidação", "Performance"],
    "Pós-operatório": [],
    "Neuropatia diabética": [],
    "Desinflamação": [],
}

TOTAL_PROTOCOLS_BASE = 9

ATIVOS_LISTA = [
    "Ácido Alfa-Lipoico",
    "Coenzima Q10",
    "Complexo B (sem B1)",
    "Cúrcuma",
    "Glutationa",
    "HMB",
    "L-Arginina",
    "L-Metionina",
    "L-Taurina",
    "Magnésio",
    "N-Acetilcisteína",
    "NADH",
    "Resveratrol",
    "SAMe",
    "Selênio",
    "Vitamina C",
    "Vitamina D",
    "5-OH-Triptofano",
    "Soro fisiológico 0,9% 100ml",
    "Soro fisiológico 0,9% 250ml",
    "Soro fisiológico 0,9% 500ml",
    "Procaína 2% 2ml",
]

TIPOS_SORO = [
    "SF 0,9% 100ml",
    "SF 0,9% 250ml",
    "SF 0,9% 500ml",
    "Outro",
]

# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def montar_nome_base(protocolo_escolhido: str, nivel_escolhido: str) -> str:
    if protocolo_escolhido in ["Lipedema", "Linfedema"] and nivel_escolhido:
        return f"Protocolo {protocolo_escolhido} {nivel_escolhido}"
    return f"Protocolo {protocolo_escolhido}"


def valores_padrao_protocolo(protocolo_escolhido: str) -> tuple[str, str, str]:
    duracao = ""
    frequencia = ""
    estrutura = ""

    if protocolo_escolhido == "Lipedema":
        duracao = "24 semanas (12 semanas injetáveis)"
        frequencia = "Semanal (8 semanas + pausa + 4 semanas)"
        estrutura = "Inclui injetáveis + acompanhamento escalonado conforme nível."
    elif protocolo_escolhido == "Linfedema":
        duracao = "24 semanas (ajustável)"
        frequencia = "Semanal"
        estrutura = "Inclui injetáveis + foco em drenagem e fisioterapia conforme nível."
    elif protocolo_escolhido == "Pós-operatório":
        duracao = "Aplicação única pós-cirurgia"
        frequencia = "Imediato pós-operatório"
        estrutura = "Aplicado durante internação."
    elif protocolo_escolhido == "Neuropatia diabética":
        duracao = "A definir"
        frequencia = "Semanal"
        estrutura = "Baseado em ativos neuroprotetores."
    elif protocolo_escolhido == "Desinflamação":
        duracao = "4 a 8 semanas"
        frequencia = "Semanal"
        estrutura = "Foco em detox e anti-inflamatório."

    return duracao, frequencia, estrutura


def criar_excel_em_memoria(
    df_protocolos: pd.DataFrame,
    df_ativos: pd.DataFrame,
    df_soros: pd.DataFrame,
) -> bytes:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_protocolos.to_excel(writer, sheet_name="Protocolos", index=False)
        df_ativos.to_excel(writer, sheet_name="Ativos", index=False)
        df_soros.to_excel(writer, sheet_name="Soros_EV", index=False)
    output.seek(0)
    return output.getvalue()


def carregar_aba_excel(caminho: str, aba: str) -> pd.DataFrame:
    if not os.path.exists(caminho):
        return pd.DataFrame()

    try:
        return pd.read_excel(caminho, sheet_name=aba)
    except Exception:
        return pd.DataFrame()


# =========================================================
# 1. SELEÇÃO DO PROTOCOLO
# =========================================================
st.header("1. Seleção do Protocolo")

protocolo = st.selectbox("Selecione o protocolo:", list(PROTOCOLS.keys()))

nivel = ""
if PROTOCOLS[protocolo]:
    nivel = st.selectbox("Nível do protocolo:", PROTOCOLS[protocolo])

nome_base = montar_nome_base(protocolo, nivel)
duracao_padrao, frequencia_padrao, estrutura_padrao = valores_padrao_protocolo(protocolo)

# =========================================================
# 2. ESTRUTURA DO PROTOCOLO
# =========================================================
st.header("2. Estrutura do Protocolo")

nome_protocolo = st.text_input("Nome do protocolo:", value=nome_base)

objetivo_clinico = st.text_area(
    "Objetivo clínico:",
    placeholder="Descreva o propósito terapêutico do protocolo."
)

estrategia_protocolo = st.text_area(
    "Estratégia do protocolo:",
    placeholder="Ex.: protocolo base, intermediário, intensivo, econômico, premium."
)

duracao_edit = st.text_input("Duração:", value=duracao_padrao)

frequencia_edit = st.text_input(
    "Frequência:",
    value=frequencia_padrao,
    placeholder="Ex.: semanal, quinzenal, semanal com pausa."
)

estrutura_edit = st.text_area(
    "Estrutura do tratamento:",
    value=estrutura_padrao,
    placeholder="Resumo da lógica do protocolo."
)

# =========================================================
# 3. INJETÁVEIS
# =========================================================
st.header("3. Injetáveis do Protocolo")

st.caption(
    "Selecione os injetáveis do protocolo. Para cada ativo selecionado, será possível ajustar dose, unidade, via, volume e observações específicas."
)

ativos_selecionados = st.multiselect("Selecione os injetáveis:", ATIVOS_LISTA)

st.info(
    "Glossário técnico:\n"
    "- Dose numérica: valor quantitativo do ativo.\n"
    "- Unidade: mg, mcg, UI, ml, ampola ou frasco.\n"
    "- Via: EV (endovenoso), IM (intramuscular), EV/IM ou outra.\n"
    "- Volume (ml): volume físico da aplicação ou apresentação.\n"
    "- Observação específica: ajuste técnico, exceção clínica, diluição ou detalhe relevante daquele ativo."
)

observacoes_gerais_injetaveis = st.text_area(
    "Observações gerais dos injetáveis:",
    placeholder="Ex.: combinação especial, substituição de ativo, lógica escalonada, ajustes conforme resposta clínica."
)

ativos_detalhados: list[dict] = []
ativos_ev_nomes: list[str] = []
ativos_im_nomes: list[str] = []

if ativos_selecionados:
    st.subheader("Detalhamento técnico dos injetáveis selecionados")

    for ativo in ativos_selecionados:
        st.markdown(f"### {ativo}")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            dose_valor = st.number_input(
                f"Dose - {ativo}",
                min_value=0.0,
                step=0.1,
                key=f"dose_{ativo}",
            )

        with col2:
            unidade = st.selectbox(
                f"Unidade - {ativo}",
                ["mg", "mcg", "UI", "ml", "ampola", "frasco", "outro"],
                key=f"unidade_{ativo}",
            )

        with col3:
            via = st.selectbox(
                f"Via - {ativo}",
                ["EV", "IM", "EV/IM", "Outra"],
                key=f"via_{ativo}",
            )

        with col4:
            volume_ml = st.number_input(
                f"Volume (ml) - {ativo}",
                min_value=0.0,
                step=0.1,
                key=f"volume_{ativo}",
            )

        observacao_ativo = st.text_area(
            f"Observação específica daquele ativo - {ativo}",
            placeholder="Ex.: diluição diferenciada, dose fora do padrão, uso opcional, aplicar apenas em perfis específicos.",
            key=f"obs_{ativo}",
        )

        if via in ["EV", "EV/IM"]:
            ativos_ev_nomes.append(ativo)
        if via in ["IM", "EV/IM"]:
            ativos_im_nomes.append(ativo)

        ativos_detalhados.append(
            {
                "Ativo": ativo,
                "Dose": dose_valor,
                "Unidade": unidade,
                "Via": via,
                "Volume_ml": volume_ml,
                "Observacao": observacao_ativo,
            }
        )

# =========================================================
# 3.1 ESTRUTURA EV / SOROS
# =========================================================
soros_ev_rows: list[dict] = []

if ativos_ev_nomes:
    st.subheader("3.1 Estrutura EV (Soros)")
    st.caption("Preencha essa seção quando houver ativos endovenosos no protocolo.")

    quantidade_soros = st.number_input(
        "Quantidade de soros EV necessários",
        min_value=0,
        step=1,
        value=1,
        key="quantidade_soros",
    )

    for i in range(int(quantidade_soros)):
        st.markdown(f"### Soro EV {i + 1}")

        col_soro1, col_soro2 = st.columns(2)

        with col_soro1:
            tipo_soro = st.selectbox(
                f"Tipo de soro - EV {i + 1}",
                TIPOS_SORO,
                key=f"tipo_soro_{i}",
            )

        with col_soro2:
            volume_total_soro = st.number_input(
                f"Volume total do soro (ml) - EV {i + 1}",
                min_value=0.0,
                step=1.0,
                key=f"volume_soro_{i}",
            )

        ativos_no_soro = st.multiselect(
            f"Ativos que compõem o soro EV {i + 1}",
            ativos_ev_nomes,
            key=f"ativos_soro_{i}",
        )

        observacao_soro = st.text_area(
            f"Observação do soro EV {i + 1}",
            placeholder="Ex.: ativos compatíveis no mesmo soro, velocidade, observações operacionais.",
            key=f"obs_soro_{i}",
        )

        soros_ev_rows.append(
            {
                "Soro_EV": f"Soro EV {i + 1}",
                "Tipo_soro": tipo_soro,
                "Volume_total_ml": volume_total_soro,
                "Ativos_no_soro": ", ".join(ativos_no_soro),
                "Observacao_soro": observacao_soro,
            }
        )

# =========================================================
# 3.2 OBSERVAÇÕES POR VIA
# =========================================================
if ativos_ev_nomes or ativos_im_nomes:
    st.subheader("3.2 Observações por via")

    if ativos_ev_nomes:
        observacao_ev = st.text_area(
            "Observações dos ativos EV",
            placeholder="Ex.: quais ativos correm no mesmo soro, ordem, particularidades da via endovenosa.",
        )
    else:
        observacao_ev = ""

    if ativos_im_nomes:
        observacao_im = st.text_area(
            "Observações dos ativos IM",
            placeholder="Ex.: divisão de aplicações, local, volume por ponto, particularidades da via intramuscular.",
        )
    else:
        observacao_im = ""
else:
    observacao_ev = ""
    observacao_im = ""

# =========================================================
# 4. COMPONENTES ADICIONAIS
# =========================================================
st.header("4. Componentes adicionais")

st.caption(
    "Os componentes adicionais podem variar conforme o nível do protocolo, gravidade clínica, estratégia terapêutica e condição financeira da paciente."
)

tem_nutri = st.radio("Consulta com Nutri?", ["Não", "Sim"], horizontal=True)
qtd_nutri = 0
if tem_nutri == "Sim":
    qtd_nutri = st.number_input("Quantidade de consultas com Nutri", min_value=1, step=1)

tem_fisioterapia = st.radio("Sessões de Fisioterapia?", ["Não", "Sim"], horizontal=True)
qtd_fisioterapia = 0
if tem_fisioterapia == "Sim":
    qtd_fisioterapia = st.number_input("Quantidade de sessões de Fisioterapia", min_value=1, step=1)

tem_drenagem = st.radio("Sessões de Drenagem?", ["Não", "Sim"], horizontal=True)
qtd_drenagem = 0
if tem_drenagem == "Sim":
    qtd_drenagem = st.number_input("Quantidade de drenagens", min_value=1, step=1)

tem_personal = st.radio("Sessões com Personal Trainer?", ["Não", "Sim"], horizontal=True)
qtd_personal = 0
freq_personal = ""
if tem_personal == "Sim":
    qtd_personal = st.number_input("Quantidade de sessões mensais com Personal Trainer", min_value=1, step=1)
    freq_personal = st.selectbox("Frequência do Personal Trainer", ["Semanal", "Quinzenal"])

tem_emagrecimento = st.radio("Com ou sem protocolo de emagrecimento?", ["Não", "Sim"], horizontal=True)
tipo_protocolo_emagrecimento = ""
dose_emagrecimento = ""
progressao_emagrecimento = ""
duracao_emagrecimento = ""
obs_emagrecimento = ""

if tem_emagrecimento == "Sim":
    tipo_protocolo_emagrecimento = st.selectbox(
        "Escolha o protocolo de emagrecimento",
        [
            "Ozempic® (Semaglutida)",
            "Mounjaro® (Tirzepatida)",
            "Wegovy® (Semaglutida)",
            "Retatrutida (Retatrutide)",
        ],
    )

    dose_emagrecimento = st.text_input(
        "Dose inicial do protocolo de emagrecimento",
        placeholder="Ex.: 0,25 mg"
    )

    progressao_emagrecimento = st.text_input(
        "Progressão do protocolo de emagrecimento",
        placeholder="Ex.: aumentar a cada 4 semanas"
    )

    duracao_emagrecimento = st.text_input(
        "Duração do protocolo de emagrecimento",
        placeholder="Ex.: 12 semanas"
    )

    obs_emagrecimento = st.text_area(
        "Observação do protocolo de emagrecimento",
        placeholder="Ex.: estratégia por fase, quantidade de canetas, observação clínica."
    )

observacoes_clinicas_gerais = st.text_area(
    "Observações clínicas gerais",
    placeholder="Ex.: indicação por perfil de paciente, restrições, observações por fase."
)

observacoes_operacionais = st.text_area(
    "Observações operacionais / comerciais",
    placeholder="Ex.: protocolo econômico, versão premium, estratégia de venda, diferenciais."
)

# =========================================================
# 5. SALVAR
# =========================================================
st.header("5. Salvar Protocolo")

if st.button("Salvar protocolo"):
    if len(ativos_selecionados) == 0:
        st.error("É obrigatório selecionar ao menos um injetável para salvar o protocolo.")
        st.stop()

    # validação de consistência dos ativos
    erros_ativos = []
    for item in ativos_detalhados:
        if item["Dose"] <= 0:
            erros_ativos.append(f"O ativo '{item['Ativo']}' precisa ter dose maior que zero.")
        if not str(item["Unidade"]).strip():
            erros_ativos.append(f"O ativo '{item['Ativo']}' precisa ter unidade.")
        if not str(item["Via"]).strip():
            erros_ativos.append(f"O ativo '{item['Ativo']}' precisa ter via.")

    if erros_ativos:
        for erro in erros_ativos:
            st.error(erro)
        st.stop()

    adicionais_lista = []

    if tem_nutri == "Sim":
        adicionais_lista.append(f"Nutri ({qtd_nutri})")
    if tem_fisioterapia == "Sim":
        adicionais_lista.append(f"Fisioterapia ({qtd_fisioterapia})")
    if tem_drenagem == "Sim":
        adicionais_lista.append(f"Drenagem ({qtd_drenagem})")
    if tem_personal == "Sim":
        adicionais_lista.append(f"Personal Trainer ({qtd_personal} - {freq_personal})")
    if tem_emagrecimento == "Sim":
        adicionais_lista.append(f"Protocolo de emagrecimento: {tipo_protocolo_emagrecimento}")

    dados_protocolo = {
        "Protocolo": nome_protocolo,
        "Tipo de protocolo": protocolo,
        "Nível": nivel,
        "Objetivo clínico": objetivo_clinico,
        "Estratégia do protocolo": estrategia_protocolo,
        "Duração": duracao_edit,
        "Frequência": frequencia_edit,
        "Estrutura do tratamento": estrutura_edit,
        "Injetáveis selecionados": ", ".join(ativos_selecionados),
        "Observações gerais dos injetáveis": observacoes_gerais_injetaveis,
        "Observações EV": observacao_ev,
        "Observações IM": observacao_im,
        "Consulta com Nutri": tem_nutri,
        "Qtd Nutri": qtd_nutri,
        "Sessões de Fisioterapia": tem_fisioterapia,
        "Qtd Fisioterapia": qtd_fisioterapia,
        "Sessões de Drenagem": tem_drenagem,
        "Qtd Drenagem": qtd_drenagem,
        "Personal Trainer": tem_personal,
        "Qtd Personal Trainer": qtd_personal,
        "Frequência Personal Trainer": freq_personal,
        "Protocolo de emagrecimento": tem_emagrecimento,
        "Tipo protocolo emagrecimento": tipo_protocolo_emagrecimento,
        "Dose inicial emagrecimento": dose_emagrecimento,
        "Progressão emagrecimento": progressao_emagrecimento,
        "Duração emagrecimento": duracao_emagrecimento,
        "Obs protocolo emagrecimento": obs_emagrecimento,
        "Observações clínicas gerais": observacoes_clinicas_gerais,
        "Observações operacionais/comerciais": observacoes_operacionais,
        "Adicionais resumidos": ", ".join(adicionais_lista),
    }

    df_novo_protocolo = pd.DataFrame([dados_protocolo])

    caminho_arquivo = "protocolos.xlsx"

    df_protocolos_existente = carregar_aba_excel(caminho_arquivo, "Protocolos")
    df_ativos_existente = carregar_aba_excel(caminho_arquivo, "Ativos")
    df_soros_existente = carregar_aba_excel(caminho_arquivo, "Soros_EV")

    df_protocolos_final = pd.concat([df_protocolos_existente, df_novo_protocolo], ignore_index=True)

    ativos_rows = []
    for item in ativos_detalhados:
        ativos_rows.append(
            {
                "Protocolo": nome_protocolo,
                "Tipo de protocolo": protocolo,
                "Nível": nivel,
                "Ativo": item["Ativo"],
                "Dose": item["Dose"],
                "Unidade": item["Unidade"],
                "Via": item["Via"],
                "Volume_ml": item["Volume_ml"],
                "Observacao_especifica": item["Observacao"],
            }
        )

    df_ativos_novo = pd.DataFrame(ativos_rows)
    df_ativos_final = pd.concat([df_ativos_existente, df_ativos_novo], ignore_index=True)

    soros_rows_final = []
    for linha in soros_ev_rows:
        soros_rows_final.append(
            {
                "Protocolo": nome_protocolo,
                "Tipo de protocolo": protocolo,
                "Nível": nivel,
                "Soro_EV": linha["Soro_EV"],
                "Tipo_soro": linha["Tipo_soro"],
                "Volume_total_ml": linha["Volume_total_ml"],
                "Ativos_no_soro": linha["Ativos_no_soro"],
                "Observacao_soro": linha["Observacao_soro"],
            }
        )

    df_soros_novo = pd.DataFrame(soros_rows_final)
    df_soros_final = pd.concat([df_soros_existente, df_soros_novo], ignore_index=True)

    with pd.ExcelWriter(caminho_arquivo, engine="openpyxl", mode="w") as writer:
        df_protocolos_final.to_excel(writer, sheet_name="Protocolos", index=False)
        df_ativos_final.to_excel(writer, sheet_name="Ativos", index=False)
        df_soros_final.to_excel(writer, sheet_name="Soros_EV", index=False)

    excel_bytes = criar_excel_em_memoria(df_protocolos_final, df_ativos_final, df_soros_final)

    st.success("Protocolo salvo com sucesso!")

    faltantes = max(TOTAL_PROTOCOLS_BASE - len(df_protocolos_final), 0)
    if faltantes > 0:
        st.info(
            f"Protocolo criado com sucesso. Ainda faltam {faltantes} protocolos-base para completar a estrutura inicial do projeto."
        )
    else:
        st.success("Todos os protocolos-base iniciais já foram cadastrados.")

    st.download_button(
        label="Baixar Excel atualizado",
        data=excel_bytes,
        file_name="protocolos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    st.markdown("## Resumo do Protocolo")
    st.write("**Protocolo:**", nome_protocolo)
    st.write("**Tipo de protocolo:**", protocolo)
    if nivel:
        st.write("**Nível:**", nivel)
    st.write("**Objetivo clínico:**", objetivo_clinico)
    st.write("**Estratégia do protocolo:**", estrategia_protocolo)
    st.write("**Duração:**", duracao_edit)
    st.write("**Frequência:**", frequencia_edit)
    st.write("**Estrutura do tratamento:**", estrutura_edit)
    st.write("**Injetáveis:**", ", ".join(ativos_selecionados))
    st.write("**Observações gerais dos injetáveis:**", observacoes_gerais_injetaveis)
    st.write("**Observações EV:**", observacao_ev)
    st.write("**Observações IM:**", observacao_im)
    st.write("**Adicionais resumidos:**", ", ".join(adicionais_lista))
    st.write("**Observações clínicas gerais:**", observacoes_clinicas_gerais)
    st.write("**Observações operacionais/comerciais:**", observacoes_operacionais)
