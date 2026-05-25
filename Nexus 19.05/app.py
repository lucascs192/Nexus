import streamlit as st
from datetime import datetime
import base64
import os

st.set_page_config(
    page_title="NEXUS SYSTEM",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── LOGO EM BASE64 ─────────────────────────────────────────────────────────
def get_logo_base64():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for nome in ["logo.jpg", "logo.png", "logo.jpeg", "logo.webp"]:
        caminho = os.path.join(script_dir, nome)
        if os.path.exists(caminho):
            with open(caminho, "rb") as f:
                ext = nome.split(".")[-1].replace("jpg", "jpeg")
                return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode()}"
    return ""

logo_data = get_logo_base64()

# ─── SAUDAÇÃO POR HORÁRIO ────────────────────────────────────────────────────
def saudacao():
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return "Bom dia"
    elif 12 <= hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

MSG_BOAS_VINDAS = (
    f"{saudacao()}! 👋 Seja bem-vindo ao **NEXUS**, seu assistente de suporte técnico.\n\n"
    "Espero que você esteja bem! Estou aqui para te ajudar com qualquer problema de TI "
    "que você esteja enfrentando — hardware, rede, acesso ou qualquer outra necessidade.\n\n"
    "Para começar, por favor me informe seu **nome completo** e **setor** em que trabalha:"
)

# ─── CSS ─────────────────────────────────────────────────────────────────────
LOGO_HTML = f'<img src="{logo_data}" class="nexus-logo-img">' if logo_data else '<div class="nexus-logo-fallback">⬡</div>'

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

html {{ background: #020408 !important; }}
body {{ background: #020408 !important; color: #C8E6F5; }}

.stApp,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stMainBlockContainer"],
[data-testid="stMain"],
.main,
.block-container,
[data-testid="stVerticalBlock"],
[data-testid="stBottom"],
[data-testid="stBottomBlockContainer"],
[data-testid="stChatInputContainer"],
.stChatFloatingInputContainer,
.stChatInputContainer,
div[class*="chatInput"],
div[class*="ChatInput"] {{
    background: #020408 !important;
    background-color: #020408 !important;
}}

[data-testid="stBottom"],
[data-testid="stBottomBlockContainer"] {{
    border-top: 1px solid rgba(0,212,255,0.08) !important;
}}

header, [data-testid="stHeader"], #MainMenu,
footer, [data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="manage-app-button"] {{
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}}

/* ── Grid animado ── */
[data-testid="stAppViewContainer"]::before {{
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,212,255,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,212,255,0.04) 1px, transparent 1px);
    background-size: 50px 50px;
    animation: gridScroll 20s linear infinite;
    z-index: 0;
    pointer-events: none;
}}
@keyframes gridScroll {{
    0%   {{ transform: translate(0,0); }}
    100% {{ transform: translate(50px,50px); }}
}}

[data-testid="stAppViewContainer"]::after {{
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 60% 40% at 50% 0%, rgba(0,114,255,0.1) 0%, transparent 70%),
        radial-gradient(ellipse 35% 25% at 85% 85%, rgba(0,212,255,0.06) 0%, transparent 60%);
    z-index: 0;
    pointer-events: none;
}}

.main .block-container,
[data-testid="stMainBlockContainer"] {{
    position: relative;
    z-index: 1;
    padding: 0 2rem 6rem !important;
    max-width: 860px !important;
    margin: 0 auto !important;
}}

/* ── Logo ── */
.nexus-header {{
    text-align: center;
    padding: 2rem 0 0.5rem;
    position: relative;
    z-index: 2;
}}

.nexus-logo-img {{
    width: 155px;
    height: auto;
    display: block;
    margin: 0 auto 0.6rem;
    filter: drop-shadow(0 0 16px rgba(0,180,255,0.5)) drop-shadow(0 0 38px rgba(0,90,255,0.25));
    animation: logoFloat 5s ease-in-out infinite;
}}

@keyframes logoFloat {{
    0%,100% {{
        transform: translateY(0px) scale(1);
        filter: drop-shadow(0 0 16px rgba(0,180,255,0.5)) drop-shadow(0 0 38px rgba(0,90,255,0.25));
    }}
    50% {{
        transform: translateY(-11px) scale(1.02);
        filter: drop-shadow(0 0 26px rgba(0,212,255,0.75)) drop-shadow(0 0 52px rgba(0,114,255,0.35));
    }}
}}

.nexus-logo-fallback {{
    width: 80px; height: 80px;
    margin: 0 auto 0.8rem;
    border: 2px solid #00D4FF;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Orbitron', monospace;
    font-size: 1.6rem; color: #00D4FF;
    box-shadow: 0 0 20px rgba(0,212,255,0.3);
    animation: logoFloat 5s ease-in-out infinite;
}}

.nexus-subtitle {{
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.66rem;
    letter-spacing: 0.22em;
    color: #00D4FF;
    opacity: 0.6;
    text-transform: uppercase;
}}

.nexus-divider {{
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, #00D4FF 35%, #0072FF 65%, transparent 100%);
    margin: 1.1rem 0 0.7rem;
    opacity: 0.3;
}}

.status-bar {{
    display: flex; gap: 1.4rem;
    justify-content: center;
    margin-bottom: 1.1rem;
    flex-wrap: wrap;
}}

.status-item {{
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    color: rgba(0,212,255,0.5);
    letter-spacing: 0.12em;
    display: flex; align-items: center; gap: 0.3rem;
}}

.status-dot {{
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00FF88;
    box-shadow: 0 0 7px #00FF88;
    animation: blink 2.2s ease-in-out infinite;
    flex-shrink: 0;
}}

@keyframes blink {{
    0%,100% {{ opacity: 1; }}
    50%      {{ opacity: 0.2; }}
}}

/* ── Mensagens ── */
[data-testid="stChatMessage"] {{
    background: rgba(2,4,8,0.88) !important;
    border: 1px solid rgba(0,212,255,0.12) !important;
    border-radius: 4px !important;
    padding: 1rem 1.25rem !important;
    margin-bottom: 0.6rem !important;
    backdrop-filter: blur(6px);
    position: relative; z-index: 2;
}}

[data-testid="stChatMessage"]:nth-child(odd)  {{ border-left: 3px solid #00D4FF !important; }}
[data-testid="stChatMessage"]:nth-child(even) {{
    border-left: 3px solid #0072FF !important;
    background: rgba(0,8,20,0.88) !important;
}}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] td,
[data-testid="stChatMessage"] th {{
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.05rem !important;
    line-height: 1.65 !important;
    color: #C8E6F5 !important;
}}

[data-testid="stChatMessage"] strong {{ color: #00D4FF !important; }}

[data-testid="stChatMessage"] table {{
    width: 100%;
    border-collapse: collapse;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.8rem !important;
}}
[data-testid="stChatMessage"] th,
[data-testid="stChatMessage"] td {{
    border: 1px solid rgba(0,212,255,0.14) !important;
    padding: 0.38rem 0.7rem !important;
}}
[data-testid="stChatMessage"] th {{
    background: rgba(0,212,255,0.06) !important;
    color: #00D4FF !important;
}}

/* ── Input de chat ── */
[data-testid="stChatInput"],
div[data-testid="stChatInput"] > div {{
    background: rgba(2,4,8,0.96) !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 5px !important;
}}

[data-testid="stChatInput"]:focus-within {{
    border-color: rgba(0,212,255,0.55) !important;
    box-shadow: 0 0 16px rgba(0,212,255,0.1) !important;
}}

[data-testid="stChatInput"] textarea {{
    background: transparent !important;
    color: #0a0a0a !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.88rem !important;
    caret-color: #00D4FF;
}}

[data-testid="stChatInput"] textarea::placeholder {{
    color: rgba(0,0,0,0.4) !important;
}}

[data-testid="stChatInput"] button {{
    background: transparent !important;
    border: none !important;
    color: #00D4FF !important;
}}

/* ── Botões ── */
.stButton > button {{
    background: rgba(2,4,8,0.9) !important;
    color: #00D4FF !important;
    border: 1px solid rgba(0,212,255,0.3) !important;
    border-radius: 3px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.77rem !important;
    letter-spacing: 0.08em !important;
    padding: 0.62rem 0.85rem !important;
    width: 100% !important;
    transition: all 0.16s ease !important;
    text-transform: uppercase !important;
}}

.stButton > button:hover {{
    background: rgba(0,212,255,0.07) !important;
    border-color: #00D4FF !important;
    color: #FFFFFF !important;
    box-shadow: 0 0 16px rgba(0,212,255,0.16) !important;
    transform: translateY(-1px) !important;
}}

.stButton > button:active {{
    transform: translateY(0) !important;
    box-shadow: none !important;
}}

[data-testid="stHorizontalBlock"] {{
    gap: 0.6rem !important;
    background: transparent !important;
}}

.protocol-box {{
    border: 1px solid rgba(0,255,136,0.45);
    padding: 0.9rem 1.3rem;
    margin: 0.5rem 0;
    background: rgba(0,255,136,0.03);
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
}}
.protocol-label {{
    font-size: 0.57rem; letter-spacing: 0.2em;
    color: rgba(0,255,136,0.5); text-transform: uppercase;
    margin-bottom: 0.2rem;
}}
.protocol-number {{
    font-size: 1.45rem; color: #00FF88; font-weight: 700;
    text-shadow: 0 0 16px rgba(0,255,136,0.4);
    letter-spacing: 0.15em;
}}

::-webkit-scrollbar {{ width: 3px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{ background: rgba(0,212,255,0.16); border-radius: 2px; }}
::-webkit-scrollbar-thumb:hover {{ background: rgba(0,212,255,0.35); }}
</style>

<div class="nexus-header">
    {LOGO_HTML}
    <div class="nexus-subtitle">Sistema Inteligente de Suporte Técnico · v2.4.1</div>
</div>
<div class="nexus-divider"></div>
<div class="status-bar">
    <div class="status-item"><span class="status-dot"></span>SISTEMA ONLINE</div>
    <div class="status-item"><span class="status-dot"></span>TI DISPONÍVEL</div>
    <div class="status-item"><span class="status-dot"></span>CONEXÃO SEGURA</div>
</div>
""", unsafe_allow_html=True)

# ─── SESSION STATE ───────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages  = []
    st.session_state.step      = "identificacao"
    st.session_state.usuario   = ""

# ─── HISTÓRICO ───────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# ─── FLUXO ───────────────────────────────────────────────────────────────────

if st.session_state.step == "identificacao":
    with st.chat_message("assistant"):
        st.markdown(MSG_BOAS_VINDAS)

    if entrada := st.chat_input("Ex: João Silva · Financeiro"):
        st.session_state.messages.append({"role": "user", "content": entrada})
        st.session_state.usuario = entrada
        primeiro_nome = entrada.split()[0].capitalize()
        st.session_state.messages.append({
            "role": "assistant",
            "content": (
                f"Perfeito, **{primeiro_nome}**! Identidade registrada com sucesso. ✅\n\n"
                "Agora selecione a **categoria** do seu chamado:"
            )
        })
        st.session_state.step = "menu"
        st.rerun()

elif st.session_state.step == "menu":
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💻  Hardware / Computador"):
            st.session_state.categoria = "Hardware / Computador"
            st.session_state.messages.append({"role": "user", "content": "💻 Hardware / Computador"})
            st.session_state.step = "urgencia"
            st.rerun()
        if st.button("🔑  Acesso / Senhas"):
            st.session_state.categoria = "Acesso / Senhas"
            st.session_state.messages.append({"role": "user", "content": "🔑 Acesso / Senhas"})
            st.session_state.step = "urgencia"
            st.rerun()
    with col2:
        if st.button("🌐  Rede / Internet"):
            st.session_state.categoria = "Rede / Internet"
            st.session_state.messages.append({"role": "user", "content": "🌐 Rede / Internet"})
            st.session_state.step = "urgencia"
            st.rerun()
        if st.button("➕  Outro Problema"):
            st.session_state.categoria = "Outro"
            st.session_state.messages.append({"role": "user", "content": "➕ Outro Problema"})
            st.session_state.step = "descrever"
            st.rerun()

elif st.session_state.step == "urgencia":
    with st.chat_message("assistant"):
        st.markdown(
            f"Categoria registrada: **{st.session_state.categoria}**\n\n"
            "Qual o **nível de urgência** desse problema?"
        )
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🟢  Baixa"):
            st.session_state.urgencia = "Baixa"
            st.session_state.messages.append({"role": "user", "content": "🟢 Urgência Baixa"})
            st.session_state.step = "descrever"
            st.rerun()
    with col2:
        if st.button("🟡  Média"):
            st.session_state.urgencia = "Média"
            st.session_state.messages.append({"role": "user", "content": "🟡 Urgência Média"})
            st.session_state.step = "descrever"
            st.rerun()
    with col3:
        if st.button("🔴  Alta"):
            st.session_state.urgencia = "Alta"
            st.session_state.messages.append({"role": "user", "content": "🔴 Urgência Alta"})
            st.session_state.step = "descrever"
            st.rerun()

elif st.session_state.step == "descrever":
    with st.chat_message("assistant"):
        st.markdown("Entendido! Agora me descreva o problema com o **máximo de detalhes** possível:")

    if detalhe := st.chat_input("Descreva o que está acontecendo..."):
        st.session_state.messages.append({"role": "user", "content": detalhe})
        st.session_state.descricao = detalhe
        st.session_state.step = "finalizar"
        st.rerun()

elif st.session_state.step == "finalizar":
    protocolo     = f"NX-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    urgencia      = getattr(st.session_state, "urgencia",  "Padrão")
    categoria     = getattr(st.session_state, "categoria", "Geral")
    primeiro_nome = st.session_state.usuario.split()[0].capitalize()

    with st.chat_message("assistant"):
        st.markdown(f"""
Tudo certo, **{primeiro_nome}**! Seu chamado foi registrado com sucesso. 🎯

<div class="protocol-box">
    <div class="protocol-label">Protocolo de Atendimento</div>
    <div class="protocol-number">{protocolo}</div>
</div>

| Campo | Valor |
|---|---|
| **Usuário** | {st.session_state.usuario} |
| **Categoria** | {categoria} |
| **Urgência** | {urgencia} |
| **Descrição** | {getattr(st.session_state, 'descricao', '—')} |
| **Status** | 🟡 Aguardando atribuição |

O setor de TI foi **notificado automaticamente** e entrará em contato em breve.
Guarde seu protocolo para acompanhamento. Qualquer dúvida, estamos à disposição! 🤝
""", unsafe_allow_html=True)

    if st.button("⟳  Abrir Novo Chamado"):
        for k in ["messages", "step", "usuario", "categoria", "urgencia", "descricao"]:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()