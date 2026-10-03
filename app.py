import streamlit as st
from sections import home, assessment, results, mood_tracker, resources, emergency

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MindCheck – Mental Health Assessment",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ═══════════════════════════════════════════════════════
   FONTS
═══════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap');

:root {
    /* Calming palette */
    --indigo:      #5e60ce;
    --indigo-lt:   #7b7fd4;
    --indigo-dk:   #4243a8;
    --teal:        #48cae4;
    --teal-dk:     #0096b7;
    --purple:      #8338ec;
    --purple-lt:   #c77dff;
    --sage:        #52b788;
    --sage-dk:     #2d6a4f;
    --amber:       #f9c74f;
    --rose:        #e63946;

    /* Neutrals */
    --white:       #ffffff;
    --surface:     rgba(255,255,255,0.82);
    --surface-2:   rgba(255,255,255,0.55);
    --border:      rgba(94,96,206,0.13);
    --text-h:      #1a1d3b;
    --text-b:      #3a3d5c;
    --text-muted:  #7a7d9a;

    /* Shadows */
    --shadow-sm:   0 2px 8px rgba(94,96,206,0.10);
    --shadow-md:   0 6px 24px rgba(94,96,206,0.14);
    --shadow-lg:   0 12px 40px rgba(94,96,206,0.18);
}

/* ═══════════════════════════════════════════════════════
   BASE
═══════════════════════════════════════════════════════ */
html, body, [class*="css"] {
    font-family: 'Inter', 'DM Sans', system-ui, sans-serif !important;
    color: var(--text-b);
}

h1,h2,h3,h4,h5 {
    color: var(--text-h) !important;
    font-weight: 700 !important;
    letter-spacing: -0.3px;
}

p, li, span, div {
    color: var(--text-b);
}

/* Force dark text for Streamlit Markdown elements in the main container */
.main .stMarkdown p,
.main .stMarkdown li,
.main .stMarkdown span {
    color: #1a202c !important;
}

/* Exclude the selected radio buttons and custom HTML cards that define their own colors */
.main .stRadio div[role="radiogroup"] label:has(input:checked) p,
.main .stRadio div[role="radiogroup"] label:has(input:checked) span {
    color: #ffffff !important;
}

/* ═══════════════════════════════════════════════════════
   BACKGROUND — soft animated gradient
═══════════════════════════════════════════════════════ */
.stApp {
    background:
        radial-gradient(ellipse at 0% 0%,   #dde4ff 0%, transparent 55%),
        radial-gradient(ellipse at 100% 0%,  #e0f7fa 0%, transparent 55%),
        radial-gradient(ellipse at 50% 100%, #f3e8ff 0%, transparent 60%),
        #f4f6ff;
    background-attachment: fixed;
}

/* ═══════════════════════════════════════════════════════
   SIDEBAR
═══════════════════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(26,29,59,0.95) 0%, rgba(45,47,107,0.95) 50%, rgba(30,58,95,0.95) 100%) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Sidebar header — MindCheck title */
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2 {
    background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 50%, #67e8f9 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    font-size: 1.9rem !important;
    font-weight: 900 !important;
    letter-spacing: -0.5px;
    margin-bottom: 0.2rem !important;
    filter: drop-shadow(0 0 12px rgba(167,139,250,0.5)) !important;
}
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #e2e8f0 !important;
    -webkit-text-fill-color: #e2e8f0 !important;
}

/* Sidebar subtext */
[data-testid="stSidebar"] em {
    color: #a0b4d0 !important;
    font-size: 0.88rem !important;
    display: inline-block;
    margin-bottom: 1.5rem !important;
    opacity: 0.8;
}

/* Sidebar divider */
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.08) !important;
    margin: 1.5rem 0 !important;
}

/* Sidebar nav radio — hide main label */
[data-testid="stSidebar"] .stRadio > label { display:none; }

/* Hide radio dots entirely */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label > div:first-child {
    display: none !important;
}

/* Nav option buttons (Pill/Card style) */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: rgba(255,255,255,0.03) !important;
    color: #d1d5db !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    padding: 0.85rem 1.2rem !important;
    border-radius: 14px !important;
    margin: 12px 0 !important;
    border: 1px solid rgba(255,255,255,0.04) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    display: flex !important;
    align-items: center !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.12) !important;
    color: #ffffff !important;
    transform: translateX(6px) scale(1.02) !important;
    border-color: rgba(255,255,255,0.25) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
}
/* Selected nav item */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-checked="true"],
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] [aria-checked="true"] ~ label {
    background: linear-gradient(90deg, rgba(94,96,206,0.6), rgba(72,202,228,0.4)) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    box-shadow: 0 4px 14px rgba(94,96,206,0.3) !important;
    transform: translateX(4px);
}

/* ═══════════════════════════════════════════════════════
   MAIN CONTENT AREA
═══════════════════════════════════════════════════════ */
.main .block-container {
    padding-top: 1.8rem !important;
    padding-bottom: 3rem !important;
    max-width: 1100px;
}

/* Page headings */
.main h2 {
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    background: linear-gradient(90deg, var(--indigo-dk), #48cae4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem !important;
    letter-spacing: -0.5px;
}
.main h3 {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: var(--indigo-dk) !important;
    margin-bottom: 0.8rem !important;
}

/* ═══════════════════════════════════════════════════════
   DISCLAIMER BANNER
═══════════════════════════════════════════════════════ */
.disclaimer-box {
    background: linear-gradient(90deg, #fef9ec, #fffae8);
    border-left: 5px solid var(--amber);
    border-radius: 12px;
    padding: 0.85rem 1.3rem;
    margin-bottom: 1.2rem;
    font-size: 0.875rem;
    color: #7a5c00;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(249,199,79,0.15);
}

/* ═══════════════════════════════════════════════════════
   BUTTONS (PREMIUM STARTUP DESIGN)
═══════════════════════════════════════════════════════ */
.stButton > button {
    border-radius: 50px !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 1.6rem !important;
    min-height: 52px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    border: none !important;
    letter-spacing: 0.3px;
    line-height: 1.2 !important;
}
/* Primary buttons */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #48cae4, #5e60ce) !important;
    color: white !important;
    box-shadow: 0 6px 20px rgba(94,96,206,0.35) !important;
    border: 2px solid transparent !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 12px 28px rgba(94,96,206,0.55) !important;
    background: linear-gradient(135deg, #5e60ce, #48cae4) !important;
}
/* Secondary buttons */
.stButton > button[kind="secondary"] {
    background: #ffffff !important;
    color: var(--indigo) !important;
    border: 2px solid rgba(94,96,206,0.3) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
}
.stButton > button[kind="secondary"]:hover {
    background: rgba(94,96,206,0.04) !important;
    border-color: var(--indigo) !important;
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 8px 20px rgba(94,96,206,0.2) !important;
}

/* ═══════════════════════════════════════════════════════
   TABS
═══════════════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.6) !important;
    border-radius: 12px !important;
    padding: 4px !important;
    gap: 4px !important;
    border: 1px solid var(--border) !important;
    backdrop-filter: blur(8px);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 9px !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    color: var(--text-muted) !important;
    padding: 0.45rem 1rem !important;
    transition: all 0.2s !important;
    background: transparent !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--indigo), var(--indigo-dk)) !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 3px 10px rgba(94,96,206,0.30) !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding-top: 1.2rem !important;
}

/* ═══════════════════════════════════════════════════════
   METRICS
═══════════════════════════════════════════════════════ */
[data-testid="stMetric"] {
    background: var(--surface) !important;
    border-radius: 14px !important;
    padding: 1rem 1.1rem !important;
    box-shadow: var(--shadow-sm) !important;
    border: 1px solid var(--border) !important;
    backdrop-filter: blur(8px);
    transition: box-shadow 0.2s ease;
}
[data-testid="stMetric"]:hover {
    box-shadow: var(--shadow-md) !important;
}
[data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    color: var(--text-muted) !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}
[data-testid="stMetricValue"] {
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: var(--indigo-dk) !important;
    margin-top: 4px;
}

/* ═══════════════════════════════════════════════════════
   EXPANDER (PREMIUM CARD UI)
═══════════════════════════════════════════════════════ */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.75) !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.9) !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06) !important;
    backdrop-filter: blur(10px);
    overflow: hidden;
    margin-bottom: 0.8rem !important;
    transition: all 0.3s ease !important;
}
[data-testid="stExpander"]:hover {
    box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stExpander"] > details > summary {
    padding: 1.1rem 1.3rem !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    color: var(--indigo-dk) !important;
    background: transparent !important;
}
[data-testid="stExpander"] > details > summary:hover {
    color: var(--indigo) !important;
    background: rgba(94,96,206,0.04) !important;
}

/* ═══════════════════════════════════════════════════════
   SELECT / INPUT FIELDS
═══════════════════════════════════════════════════════ */
[data-testid="stSelectbox"] > div > div,
[data-testid="stTextArea"] textarea,
[data-testid="stTextInput"] input {
    border-radius: 10px !important;
    border: 1.5px solid rgba(94,96,206,0.2) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stSelectbox"] > div > div:focus-within,
[data-testid="stTextArea"] textarea:focus,
[data-testid="stTextInput"] input:focus {
    border-color: var(--indigo) !important;
    box-shadow: 0 0 0 3px rgba(94,96,206,0.15) !important;
}

/* ═══════════════════════════════════════════════════════
   SLIDER
═══════════════════════════════════════════════════════ */
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: var(--indigo) !important;
    border: 2px solid white !important;
    box-shadow: 0 2px 8px rgba(94,96,206,0.40) !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] div:nth-child(5) {
    background: linear-gradient(90deg, var(--indigo), var(--teal)) !important;
}

/* ═══════════════════════════════════════════════════════
   PROGRESS BAR
═══════════════════════════════════════════════════════ */
.stProgress > div > div {
    border-radius: 10px !important;
    background: linear-gradient(90deg, var(--indigo), var(--teal)) !important;
}
.stProgress > div {
    border-radius: 10px !important;
    background: rgba(94,96,206,0.12) !important;
}

/* ═══════════════════════════════════════════════════════
   ALERTS / INFO / WARNING / SUCCESS
═══════════════════════════════════════════════════════ */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    border: none !important;
    font-size: 0.9rem !important;
    padding: 0.9rem 1.1rem !important;
}

/* ═══════════════════════════════════════════════════════
   RADIO BUTTONS (horizontal - used in Assessments)
═══════════════════════════════════════════════════════ */
.main .stRadio div[role="radiogroup"] {
    gap: 14px !important;
    flex-wrap: wrap;
    margin-top: 0.5rem !important;
}

/* Hide native radio dots */
.main .stRadio div[role="radiogroup"] label > div:first-child {
    display: none !important;
}

/* Pill design for options */
.main .stRadio div[role="radiogroup"] label {
    background: #ffffff !important;
    border: 2px solid rgba(94,96,206,0.18) !important;
    border-radius: 30px !important;
    padding: 0.7rem 1.6rem !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: #2c3e50 !important;
    cursor: pointer !important;
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* Hover state */
.main .stRadio div[role="radiogroup"] label:hover {
    background: rgba(94,96,206,0.06) !important;
    border-color: rgba(94,96,206,0.6) !important;
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 6px 16px rgba(94,96,206,0.15) !important;
    color: var(--indigo-dk) !important;
}

/* Active (Selected) State - Using :has selector for guaranteed compatibility */
.main .stRadio div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(135deg, #5e60ce, #48cae4) !important;
    color: #ffffff !important;
    border-color: transparent !important;
    font-weight: 700 !important;
    box-shadow: 0 6px 20px rgba(94,96,206,0.4) !important;
    transform: translateY(-2px) !important;
}
[data-testid="stWidgetLabel"] {
    font-weight: 600 !important;
    color: var(--text-h) !important;
    font-size: 0.9rem !important;
}

/* ═══════════════════════════════════════════════════════
   DIVIDER
═══════════════════════════════════════════════════════ */
hr {
    border: none !important;
    border-top: 1px solid rgba(94,96,206,0.12) !important;
    margin: 1.2rem 0 !important;
}

/* ═══════════════════════════════════════════════════════
   DOWNLOAD BUTTON
═══════════════════════════════════════════════════════ */
[data-testid="stDownloadButton"] button {
    border-radius: 12px !important;
    font-weight: 600 !important;
    background: rgba(72,202,228,0.12) !important;
    color: var(--teal-dk) !important;
    border: 1.5px solid rgba(72,202,228,0.30) !important;
    transition: all 0.2s ease !important;
}
[data-testid="stDownloadButton"] button:hover {
    background: rgba(72,202,228,0.22) !important;
    transform: translateY(-1px) !important;
}

/* ═══════════════════════════════════════════════════════
   LINE CHART CONTAINER
═══════════════════════════════════════════════════════ */
[data-testid="stArrowVegaLiteChart"] {
    border-radius: 14px !important;
    overflow: hidden !important;
    box-shadow: var(--shadow-sm) !important;
}

/* ═══════════════════════════════════════════════════════
   SIDEBAR SIZING
═══════════════════════════════════════════════════════ */
/* Prevent horizontal scrolling app-wide */
.stApp {
    overflow-x: hidden !important;
}

/* Normal desktop sidebar */
[data-testid="stSidebar"] {
    min-width: 260px !important;
    max-width: 300px !important;
}
[data-testid="stSidebar"] > div {
    width: 100% !important;
    min-width: 100% !important;
}


/* ═══════════════════════════════════════════════════════
   SIDEBAR NAVIGATION MENU STYLING (MATCH SKETCH)
═══════════════════════════════════════════════════════ */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 12px !important;
    display: flex !important;
    flex-direction: column !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label > div:first-child {
    display: none !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: transparent !important;
    border: 2px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 0.8rem 1.2rem !important;
    margin: 0 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    transition: all 0.25s ease !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p {
    color: rgba(255,255,255,0.7) !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    margin: 0 !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.05) !important;
    border-color: rgba(255,255,255,0.3) !important;
    transform: translateY(-2px) !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover p {
    color: #ffffff !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(135deg, #5e60ce, #48cae4) !important;
    border-color: transparent !important;
    box-shadow: 0 4px 15px rgba(94,96,206,0.4) !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) p {
    color: #ffffff !important;
    font-weight: 800 !important;
}

/* ═══════════════════════════════════════════════════════
   SECTION SEPARATOR UTILITY
═══════════════════════════════════════════════════════ */
.section-gap { margin-top: 2rem; margin-bottom: 0.5rem; }

/* ═══════════════════════════════════════════════════════
   HIDE STREAMLIT BRANDING (keep header/toggle visible)
═══════════════════════════════════════════════════════ */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
/* Keep header visible so the sidebar toggle button works */
/* Only hide the Deploy button */
[data-testid="stToolbar"] { visibility: hidden; }

/* Ensure sidebar is always shown and visible */
[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    transform: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state defaults ─────────────────────────────────────────────────────
defaults = {
    "page": "🏠 Home",
    "phq9_answers": {},
    "gad7_answers": {},
    "assessment_done": False,
    "assessment_step": "phq9",   # "phq9" | "gad7"
    "phq9_score": 0,
    "gad7_score": 0,
    "crisis_flag": False,
    "mood_log": [],
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

if "sidebar_hidden" not in st.session_state:
    st.session_state["sidebar_hidden"] = False

# ── Sidebar Navigation ─────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🧠 MindCheck")
    st.markdown("*Your personal mental wellness companion*")
    
    nav = st.radio(
        "Navigate",
        ["🏠 Home", "📋 Assessment", "📊 Results", "📅 Mood Tracker", "📚 Resources", "🆘 Emergency Help"],
        index=["🏠 Home", "📋 Assessment", "📊 Results", "📅 Mood Tracker", "📚 Resources", "🆘 Emergency Help"].index(
            st.session_state["page"]
        ),
        label_visibility="collapsed",
    )
    
    if nav != st.session_state["page"]:
        st.session_state["page"] = nav
        st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""<div style='color:#a8d8ea; font-size:0.75rem; line-height:1.6; opacity: 0.8;'>
🔒 Your data stays in this session<br>
💙 Built with care for your wellbeing<br>
📞 Emergency: <b>iCall: 9152987821</b>
</div>""", unsafe_allow_html=True)

# ── Disclaimer (shown on every page) ──────────────────────────────────────────
st.markdown("""
<div class='disclaimer-box'>
⚠️ <b>Disclaimer:</b> This tool is for educational and informational purposes only.
It is <b>not a medical diagnosis</b>. If you are in crisis or need immediate help,
please contact a licensed mental health professional or emergency services.
</div>
""", unsafe_allow_html=True)

# ── Auto emergency banner (shown when scores are critically high) ──────────────
# Not shown on the Emergency Help page itself to avoid duplication
if st.session_state.get("page") != "🆘 Emergency Help":
    emergency.show_emergency_banner()

# ── Route to sections ──────────────────────────────────────────────────────────
page = st.session_state["page"]

if page == "🏠 Home":
    home.render()
elif page == "📋 Assessment":
    assessment.render()
elif page == "📊 Results":
    results.render()
elif page == "📅 Mood Tracker":
    mood_tracker.render()
elif page == "📚 Resources":
    resources.render()
elif page == "🆘 Emergency Help":
    emergency.render()
