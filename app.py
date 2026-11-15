
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AgriShift",
    page_icon="assets/AgriShift_Orbital_Leaf_Logo-removebg-preview.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hero_images = {
    "Dashboard": "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
    "Farmer Profile": "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/image_data/file/25511/s960_crops-PL-1005922__3_.png",
    "Rotation Analysis": "https://api.groenkennisnet.nl/upload_mm/e/1/7/cid5041_1756704163450_cid803991_1710932829648_20230718_DJI_0013GLB_veldmaatregelen_bionext_LR.jpg",
    "Climate Explorer": "https://leaf.imgix.net/blog/23-05-04_1.jpg?auto=format&w=auto",
    "Vegetation": "https://cdn.sanity.io/images/hvd5n54p/blog/1f19e32aee83ae6f3187b56d40a838883e9fe0e1-2200x1320.jpg",
    "Soil Health": "https://images.squarespace-cdn.com/content/v1/66f28538e3122c440d99a842/1727720443905-M4M0966X7V8UBZGHVCWF/unsplash-image-Zg0m32COaZU.jpg",
    "Data & Methodology": "https://www.zvut.cz/i/media/document_images/fotogalerie_doc/ostra/252346/PSP2_1600.png"
}

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #092B27;
    --navy-2: #123E35;
    --green: #059669;
    --emerald: #10B981;
    --lime: #BEF264;
    --yellow: #FACC15;
    --text: #183C34;
    --muted: #668178;
    --background: #F5FBF6;
}

/* =========================================
   GLOBAL
========================================= */

html, body, [data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] *,
.stMarkdown, .stMarkdown *,
button, input, textarea, select {
    font-family: 'Manrope', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 15%, rgba(16,185,129,.19), transparent 34%),
        radial-gradient(ellipse at 95% 35%, rgba(190,242,100,.16), transparent 32%),
        radial-gradient(ellipse at 50% 90%, rgba(5,150,105,.13), transparent 42%),
        #F5FBF6 !important;
    background-attachment: fixed !important;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"],
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
}

.block-container {
    padding-top: 105px !important;
    padding-bottom: 4rem !important;
    max-width: 1500px;
    animation: pageReveal .7s ease-out;
}

h1, h2, h3 {
    color: var(--navy) !important;
    font-weight: 800 !important;
    letter-spacing: -1px !important;
}

h4, h5, h6 {
    color: var(--green) !important;
    font-weight: 800 !important;
}

p, li, label {
    color: var(--text);
}

[data-testid="stCaptionContainer"] p {
    color: var(--muted) !important;
}

/* =========================================
   DESKTOP NAVIGATION
========================================= */

.st-key-agrishift_navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    z-index: 999999 !important;
    background: linear-gradient(110deg, #071F1B, #10392F, #092B27) !important;
    padding: 13px 3% !important;
    box-shadow:
        0 8px 30px rgba(4,35,27,.24),
        0 0 25px rgba(16,185,129,.20),
        0 1px 0 rgba(190,242,100,.18) !important;
    backdrop-filter: blur(18px);
}

.st-key-agrishift_navbar button {
    height: 49px !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
    font-size: 12px !important;
    color: white !important;
    transition: all .28s ease !important;
    outline: none !important;
    box-shadow: none !important;
    -webkit-tap-highlight-color: transparent !important;
}

.st-key-agrishift_navbar button p,
.st-key-agrishift_navbar button span {
    color: white !important;
}

.st-key-agrishift_navbar button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid transparent !important;
}

.st-key-agrishift_navbar button[kind="secondary"]:hover {
    background: rgba(190,242,100,.10) !important;
    border-color: rgba(190,242,100,.18) !important;
    box-shadow: 0 0 20px rgba(16,185,129,.18) !important;
    transform: translateY(-2px);
}

.st-key-agrishift_navbar button[kind="primary"] {
    background: linear-gradient(135deg, #155C45, #167B55) !important;
    border: 1px solid rgba(190,242,100,.22) !important;
    border-bottom: 3px solid #BEF264 !important;
    box-shadow:
        0 5px 18px rgba(16,185,129,.22),
        0 0 24px rgba(16,185,129,.20) !important;
}

.st-key-agrishift_navbar button:focus,
.st-key-agrishift_navbar button:focus-visible,
.st-key-agrishift_navbar button:active {
    outline: none !important;
    box-shadow: none !important;
}

/* =========================================
   MOBILE NAVIGATION - HIDDEN ON DESKTOP
========================================= */

.st-key-agrishift_mobile_nav {
    display: none !important;
}

/* =========================================
   HERO
========================================= */

.farm-hero {
    position: relative;
    overflow: hidden;
    min-height: 350px;
    padding: 58px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,.20);
    background:
        linear-gradient(
            115deg,
            rgba(4,28,23,.94) 0%,
            rgba(7,65,45,.77) 48%,
            rgba(9,43,39,.35) 100%
        ),
        var(--hero-image);
    background-size: cover;
    background-position: center;
    box-shadow:
        0 25px 60px rgba(7,43,35,.19),
        0 0 30px rgba(16,185,129,.12);
    animation: heroReveal .9s cubic-bezier(.2,.8,.2,1);
    transition: box-shadow .4s ease;
}

.farm-hero:hover {
    box-shadow:
        0 30px 75px rgba(7,43,35,.23),
        0 0 45px rgba(16,185,129,.24);
}

.farm-hero::before {
    content: "";
    position: absolute;
    width: 430px;
    height: 430px;
    right: -120px;
    top: -180px;
    border-radius: 50%;
    background: rgba(190,242,100,.22);
    filter: blur(95px);
    animation: glowFloat 8s ease-in-out infinite alternate;
    pointer-events: none;
}

.farm-hero::after {
    content: "";
    position: absolute;
    width: 420px;
    height: 260px;
    left: 25%;
    bottom: -190px;
    border-radius: 50%;
    background: rgba(16,185,129,.25);
    filter: blur(90px);
    pointer-events: none;
}

.farm-hero > * {
    position: relative;
    z-index: 2;
}

.hero-eyebrow {
    display: inline-block;
    width: fit-content;
    color: #D9F99D;
    background: rgba(190,242,100,.11);
    border: 1px solid rgba(190,242,100,.30);
    border-radius: 50px;
    padding: 9px 17px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    backdrop-filter: blur(10px);
}

.hero-title {
    font-size: clamp(42px, 5.5vw, 70px);
    font-weight: 800;
    letter-spacing: -2px;
    line-height: 1.2;
    margin: 20px 0;
    padding: 5px 3px 10px;
    display: block;
    width: fit-content;
    max-width: 100%;
    background: linear-gradient(100deg, #FFFFFF 5%, #D9F99D 48%, #6EE7B7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: titleReveal 1s ease-out;
}

.hero-description {
    color: #E2F5EB;
    font-size: 16px;
    line-height: 1.9;
    max-width: 680px;
}

/* =========================================
   INTRO AND SCENARIO
========================================= */

.intro-section {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #FFFFFF, #F0FBF3);
    border: 1px solid #D5EBDD;
    border-radius: 22px;
    padding: 32px;
    margin-top: 23px;
    margin-bottom: 25px;
    box-shadow:
        0 12px 35px rgba(9,43,39,.055),
        0 0 22px rgba(16,185,129,.09);
    transition: transform .3s ease, box-shadow .3s ease;
}

.intro-section:hover {
    transform: translateY(-3px);
    box-shadow:
        0 18px 42px rgba(9,43,39,.09),
        0 0 30px rgba(16,185,129,.19);
}

.intro-section p {
    line-height: 1.9;
}

.scenario {
    background: linear-gradient(120deg, #E4F9E9, #F4FCE8);
    border-left: 5px solid #10B981;
    border-radius: 14px;
    padding: 22px 25px;
    margin-top: 18px;
    box-shadow:
        inset 0 0 30px rgba(16,185,129,.045),
        0 0 23px rgba(16,185,129,.12);
}

.scenario p {
    color: #24543E !important;
    margin-bottom: 0;
    line-height: 1.9;
}

/* =========================================
   METRIC CARDS
========================================= */

[data-testid="stMetric"] {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #092B27 0%, #10513D 55%, #167653 100%) !important;
    border: 1px solid rgba(190,242,100,.23) !important;
    border-radius: 20px !important;
    padding: 25px !important;
    box-shadow:
        0 10px 28px rgba(9,43,39,.13),
        0 0 22px rgba(16,185,129,.13);
    animation: fadeUp .65s ease both;
    transition: transform .3s ease, box-shadow .3s ease;
}

[data-testid="stMetric"]::before {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    right: -70px;
    top: -80px;
    border-radius: 50%;
    background: rgba(190,242,100,.15);
    filter: blur(35px);
    pointer-events: none;
}

[data-testid="stMetric"]::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 3px;
    left: 0;
    bottom: 0;
    background: linear-gradient(90deg, #10B981, #BEF264, #6EE7B7);
    opacity: .7;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-7px) scale(1.015);
    box-shadow:
        0 20px 40px rgba(9,43,39,.20),
        0 0 32px rgba(16,185,129,.28);
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] *,
[data-testid="stMetricLabel"] p {
    color: #C7F9DA !important;
    -webkit-text-fill-color: #C7F9DA !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] *,
[data-testid="stMetricValue"] div,
[data-testid="stMetricValue"] span {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    font-weight: 800 !important;
    font-size: 28px !important;
    opacity: 1 !important;
    overflow: visible !important;
    text-overflow: clip !important;
    white-space: nowrap !important;
}

[data-testid="stMetricDelta"],
[data-testid="stMetricDelta"] * {
    color: #D9F99D !important;
    -webkit-text-fill-color: #D9F99D !important;
}

/* =========================================
   CHARTS AND DATAFRAMES
========================================= */

[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,.94);
    border: 1px solid #DCEDE2;
    border-radius: 21px;
    padding: 16px;
    box-shadow:
        0 10px 30px rgba(9,43,39,.055),
        0 0 20px rgba(16,185,129,.10);
    animation: fadeUp .7s ease both;
    transition: transform .3s ease, box-shadow .3s ease;
}

[data-testid="stPlotlyChart"]:hover {
    transform: translateY(-3px);
    box-shadow:
        0 18px 38px rgba(9,43,39,.10),
        0 0 32px rgba(16,185,129,.23);
}

[data-testid="stDataFrame"] {
    background: white !important;
    border: 1px solid #DCEDE2;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(16,185,129,.07);
}

/* =========================================
   BUTTONS
========================================= */

.stButton > button,
[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #059669, #10B981) !important;
    color: white !important;
    border: 1px solid rgba(16,185,129,.25) !important;
    border-radius: 12px !important;
    font-weight: 800 !important;
    box-shadow:
        0 6px 17px rgba(5,150,105,.17),
        0 0 15px rgba(16,185,129,.13);
    transition: all .25s ease !important;
}

.stButton > button:hover,
[data-testid="stFormSubmitButton"] button:hover {
    background: linear-gradient(135deg, #047857, #065F46) !important;
    color: white !important;
    transform: translateY(-2px);
    box-shadow:
        0 11px 25px rgba(5,150,105,.27),
        0 0 28px rgba(16,185,129,.25);
}

.stButton > button p,
.stButton > button span {
    color: white !important;
}

/* =========================================
   SLIDERS
========================================= */

[data-testid="stSlider"] {
    accent-color: #10B981 !important;
}

[data-testid="stSlider"] [role="slider"] {
    background: #10B981 !important;
    border-color: #10B981 !important;
    box-shadow: 0 0 0 4px rgba(16,185,129,.16) !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
    background-color: #10B981 !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] div[role="presentation"] {
    background-color: #10B981 !important;
}

/* =========================================
   EXPANDERS AND FORMS
========================================= */

[data-testid="stExpander"] {
    background: linear-gradient(135deg, #FFFFFF, #F5FCF7) !important;
    border: 1px solid #D9EDE0 !important;
    border-radius: 16px !important;
    box-shadow:
        0 7px 22px rgba(9,43,39,.045),
        0 0 20px rgba(16,185,129,.09);
    transition: box-shadow .3s ease, transform .3s ease;
}

[data-testid="stExpander"]:hover {
    transform: translateY(-2px);
    box-shadow:
        0 10px 25px rgba(9,43,39,.07),
        0 0 28px rgba(16,185,129,.18);
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary * {
    color: var(--navy) !important;
}

[data-testid="stForm"] {
    background: rgba(255,255,255,.86);
    border: 1px solid #DCEDE2;
    border-radius: 21px;
    padding: 27px;
    box-shadow:
        0 10px 30px rgba(9,43,39,.05),
        0 0 23px rgba(16,185,129,.10);
    transition: box-shadow .3s ease;
}

[data-testid="stForm"]:hover {
    box-shadow:
        0 14px 35px rgba(9,43,39,.08),
        0 0 30px rgba(16,185,129,.18);
}

/* =========================================
   INPUTS AND SELECTS
========================================= */

[data-baseweb="select"] > div {
    background: #F0FAF3 !important;
    border: 1px solid #B8DCC6 !important;
    border-radius: 11px !important;
    color: var(--navy) !important;
}

[data-baseweb="select"] *,
[data-baseweb="select"] input {
    color: var(--navy) !important;
    -webkit-text-fill-color: var(--navy) !important;
}

[data-baseweb="select"] svg {
    fill: #059669 !important;
    color: #059669 !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"] {
    background: white !important;
}

[role="option"] {
    color: var(--navy) !important;
}

[data-testid="stDateInput"] input {
    background: #F0FAF3 !important;
    color: var(--navy) !important;
    -webkit-text-fill-color: var(--navy) !important;
    border: 1px solid #B8DCC6 !important;
    border-radius: 11px !important;
}

[data-testid="stDateInput"] button,
[data-testid="stDateInput"] svg {
    color: #059669 !important;
    fill: #059669 !important;
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background: white !important;
    color: var(--navy) !important;
    border-radius: 10px !important;
}

[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] label * {
    color: var(--text) !important;
}

[data-testid="stCheckbox"] input {
    accent-color: #10B981 !important;
}

/* =========================================
   ALERTS
========================================= */

[data-testid="stAlert"] {
    background: linear-gradient(135deg, #E9F9EE, #F5FCEB) !important;
    border: 1px solid #B8E8C7 !important;
    border-radius: 14px !important;
    box-shadow: 0 0 20px rgba(16,185,129,.10);
}

[data-testid="stAlert"] *,
[data-testid="stAlert"] p {
    color: #24543E !important;
    -webkit-text-fill-color: #24543E !important;
}

/* =========================================
   INFORMATION CARDS
========================================= */

.info-card {
    background: linear-gradient(135deg, white, #F0FAF3);
    border: 1px solid #D5EBDD;
    border-radius: 17px;
    padding: 24px;
    margin-bottom: 14px;
    box-shadow:
        0 7px 22px rgba(9,43,39,.045),
        0 0 20px rgba(16,185,129,.09);
    transition: all .3s ease;
}

.info-card:hover {
    transform: translateY(-5px);
    border-color: #86D6A5;
    box-shadow:
        0 15px 32px rgba(9,43,39,.09),
        0 0 32px rgba(16,185,129,.20);
}

.info-card h4 {
    margin-top: 0;
}

.info-card p {
    color: var(--text);
    line-height: 1.8;
}

/* =========================================
   WATER HIGHLIGHT
========================================= */

.water-highlight {
    background: linear-gradient(125deg, #E2F8E9, #F3FCE8);
    border: 1px solid #B8E8C7;
    border-radius: 18px;
    padding: 23px 27px;
    margin: 15px 0;
    box-shadow:
        0 7px 23px rgba(16,185,129,.07),
        0 0 27px rgba(16,185,129,.15);
}

.water-highlight strong {
    display: block;
    color: #174B36 !important;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 9px;
}

.water-highlight p {
    color: #24543E !important;
    line-height: 1.8;
}

/* =========================================
   GENERAL ELEMENTS
========================================= */

.intro-section,
.info-card,
[data-testid="stForm"],
[data-testid="stExpander"],
[data-testid="stPlotlyChart"] {
    will-change: box-shadow;
}

hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, #B9DCC6, transparent) !important;
    margin: 30px 0 !important;
}

/* =========================================
   ANIMATIONS
========================================= */

@keyframes pageReveal {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes heroReveal {
    from { opacity: 0; transform: translateY(20px) scale(.985); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

@keyframes titleReveal {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes glowFloat {
    from { transform: translate(0, 0) scale(1); }
    to { transform: translate(-35px, 35px) scale(1.12); }
}

/* =========================================
   TABLET NAVIGATION
========================================= */

@media (max-width: 850px) {

    /* Hide desktop buttons */
    .st-key-agrishift_navbar {
        display: none !important;
    }

    /* Show mobile dropdown */
    .st-key-agrishift_mobile_nav {
        display: block !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        z-index: 999999 !important;
        background: linear-gradient(110deg, #071F1B, #10392F, #092B27) !important;
        padding: 10px 20px 5px 20px !important;
        box-shadow: 0 6px 25px rgba(4,35,27,.3) !important;
    }

    .st-key-agrishift_mobile_nav [data-baseweb="select"] > div {
    background: linear-gradient(
        135deg,
        #123E35,
        #08734F,
        #10513D
    ) !important;

    border: 1px solid rgba(190,242,100,.65) !important;
    border-radius: 13px !important;
    min-height: 46px !important;

    box-shadow:
        0 0 8px rgba(16,185,129,.45),
        0 0 18px rgba(16,185,129,.30),
        0 0 30px rgba(190,242,100,.12),
        inset 0 0 12px rgba(190,242,100,.08) !important;

    transition: all .3s ease !important;
}

    .st-key-agrishift_mobile_nav label,
    .st-key-agrishift_mobile_nav label p,
    .st-key-agrishift_mobile_nav [data-testid="stWidgetLabel"],
    .st-key-agrishift_mobile_nav [data-testid="stWidgetLabel"] p {
    color: #D9F99D !important;
    -webkit-text-fill-color: #D9F99D !important;
    font-weight: 800 !important;
    font-size: 13px !important;
}

    .st-key-agrishift_mobile_nav [data-baseweb="select"] *,
    .st-key-agrishift_mobile_nav [data-baseweb="select"] input {
        color: white !important;
        -webkit-text-fill-color: white !important;
    }

    .st-key-agrishift_mobile_nav [data-baseweb="select"] svg {
        fill: #D9F99D !important;
        color: #D9F99D !important;
    }

    .block-container {
        padding-top: 115px !important;
        padding-left: 28px !important;
        padding-right: 28px !important;
    }

    .farm-hero {
        padding: 35px;
        min-height: 270px;
        background-position: center;
    }

    .hero-title {
        font-size: 48px;
        letter-spacing: -2px;
    }
}

/* =========================================
   MOBILE PHONES
========================================= */

@media (max-width: 550px) {

    .block-container {
        padding-top: 110px !important;
        padding-left: 14px !important;
        padding-right: 14px !important;
        padding-bottom: 2rem !important;
    }

    /* Hero */
    .farm-hero {
        padding: 25px 21px;
        min-height: 225px;
        border-radius: 18px;
        background-position: center;
    }

    .hero-eyebrow {
        font-size: 9px;
        letter-spacing: 1.5px;
        padding: 7px 11px;
    }

    .hero-title {
        font-size: clamp(34px, 9vw, 42px);
        letter-spacing: -1.5px;
        margin: 17px 0 12px;
    }

    .hero-description {
        font-size: 13px;
        line-height: 1.7;
    }

    /* Headings */
    h1 {
        font-size: 27px !important;
        letter-spacing: -.7px !important;
    }

    h2 {
        font-size: 23px !important;
        letter-spacing: -.5px !important;
    }

    h3 {
        font-size: 19px !important;
        letter-spacing: -.4px !important;
    }

    h4 {
        font-size: 16px !important;
    }

    /* Intro and scenario */
    .intro-section {
        padding: 20px 17px;
        margin-top: 16px;
        margin-bottom: 18px;
        border-radius: 17px;
    }

    .intro-section p,
    .scenario p {
        font-size: 13px;
        line-height: 1.75;
    }

    .scenario {
        padding: 16px;
        border-radius: 12px;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        padding: 15px !important;
        border-radius: 14px !important;
        min-width: 0 !important;
    }

    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] *,
    [data-testid="stMetricValue"] div,
    [data-testid="stMetricValue"] span {
        font-size: clamp(17px, 4.5vw, 23px) !important;
        white-space: normal !important;
        overflow-wrap: anywhere !important;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] p {
        font-size: 11px !important;
        line-height: 1.4 !important;
    }

    [data-testid="stMetricDelta"] {
        font-size: 10px !important;
    }

    /* Charts */
    [data-testid="stPlotlyChart"] {
        padding: 5px !important;
        border-radius: 14px !important;
        overflow: hidden !important;
    }

    [data-testid="stPlotlyChart"] > div {
        width: 100% !important;
        min-width: 0 !important;
    }

    /* Information cards */
    .info-card {
        padding: 17px;
        border-radius: 14px;
        margin-bottom: 12px;
    }

    .info-card p {
        font-size: 13px;
        line-height: 1.7;
    }

    .water-highlight {
        padding: 17px;
        border-radius: 14px;
    }

    .water-highlight strong {
        font-size: 16px;
    }

    .water-highlight p {
        font-size: 13px;
    }

    /* Forms */
    [data-testid="stForm"] {
        padding: 16px !important;
        border-radius: 15px;
    }

    /* Buttons and inputs */
    .stButton > button,
    [data-testid="stFormSubmitButton"] button {
        min-height: 43px !important;
        font-size: 13px !important;
    }

    [data-baseweb="select"] > div {
        min-height: 42px !important;
    }

    /* Tables */
    [data-testid="stDataFrame"] {
        max-width: 100% !important;
        overflow-x: auto !important;
    }

    /* Dividers */
    hr {
        margin: 21px 0 !important;
    }

    /* Disable hover movement on touch screens */
    .intro-section:hover,
    .info-card:hover,
    [data-testid="stMetric"]:hover,
    [data-testid="stPlotlyChart"]:hover,
    [data-testid="stExpander"]:hover {
        transform: none !important;
    }
}

/* =========================================
   ACCESSIBILITY
========================================= */

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation: none !important;
        transition: none !important;
    }
}

</style>
""", unsafe_allow_html=True)



# CUSTOM NAVBAR

nav_sections = [
    "Dashboard",
    "Farmer Profile",
    "Rotation Analysis",
    "Climate Explorer",
    "Vegetation",
    "Soil Health",
    "Data & Methodology"
]

if "agrishift_navigation" not in st.session_state:
    st.session_state.agrishift_navigation = "Dashboard"

if "mobile_navigation" not in st.session_state:
    st.session_state.mobile_navigation = (
        st.session_state.agrishift_navigation
    )


# Desktop navigation callback
def set_desktop_navigation(nav_section):
    st.session_state.agrishift_navigation = nav_section
    st.session_state.mobile_navigation = nav_section


# Mobile navigation callback
def set_mobile_navigation():
    st.session_state.agrishift_navigation = (
        st.session_state.mobile_navigation
    )


# Desktop navigation
with st.container(key="agrishift_navbar"):

    nav_cols = st.columns(len(nav_sections), gap="small")

    for col, nav_section in zip(nav_cols, nav_sections):

        with col:
            st.button(
                nav_section,
                key=f"nav_{nav_section}",
                use_container_width=True,
                type=(
                    "primary"
                    if st.session_state.agrishift_navigation == nav_section
                    else "secondary"
                ),
                on_click=set_desktop_navigation,
                args=(nav_section,)
            )


# Mobile navigation
with st.container(key="agrishift_mobile_nav"):

    st.selectbox(
        "Navigate to",
        nav_sections,
        key="mobile_navigation",
        on_change=set_mobile_navigation
    )


section = st.session_state.agrishift_navigation


st.markdown(
    f"""
    <div class="farm-hero" style="--hero-image: url('{hero_images[section]}');">
        <div class="hero-eyebrow">NASA Earth Observations</div>
        <div class="hero-title">AgriShift</div>
        <div class="hero-description">
            Helping farmers make better crop decisions using climate,
            vegetation, soil moisture, and crop rotation data.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if section == "Dashboard":
    st.markdown(
        """
        <div class="intro-section">
            <h3>Making farming decisions easier</h3>
            <p>
                AgriShift brings together climate and agricultural data to help
                farmers understand changing conditions, explore vegetation
                patterns, monitor soil moisture, and compare different crop
                rotations. It helps turn complex data into information that
                farmers can use when planning their fields.
            </p>
            <div class="scenario">
                <p>
                    <strong>Meet Rashid.</strong> He is a third-generation farmer
                    in Punjab. Every year, he faces challenges from rising
                    temperatures, unpredictable rainfall, and periods of drought.
                    Using AgriShift, Rashid can explore past climate patterns,
                    monitor vegetation and soil moisture, and compare crop
                    rotations to find options that may better suit the conditions
                    on his farm.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


@st.cache_data
def load_climate():
    data = pd.read_csv(
        "data/monthly_climate_full.csv",
        index_col=0,
        parse_dates=True
    )
    data.index = pd.to_datetime(data.index)
    return data.sort_index()


@st.cache_data
def load_ndvi():
    data = pd.read_csv("data/ndvi_raw.csv")
    data.columns = data.columns.str.strip()

    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["NDVI"] = pd.to_numeric(
        data["MOD13Q1_061__250m_16_days_NDVI"],
        errors="coerce"
    )

    quality_column = "MOD13Q1_061__250m_16_days_VI_Quality_MODLAND"

    data["MODLAND_Quality"] = (
        data[quality_column].astype(str).str.strip()
    )

    data = data.dropna(subset=["Date", "NDVI"])
    data = data.sort_values("Date")

    return data


@st.cache_data

def load_rotation_scores():
    data = pd.read_csv("data/rotation_evidence.csv")

    # Clean column names
    data.columns = data.columns.str.strip()

    # Standardise the rotation column
    data = data.rename(columns={data.columns[0]: "Rotation"})
    data["Rotation"] = data["Rotation"].str.replace(
        r"^[A-Z]:\s*", "", regex=True
    )

    # Calculate continuous scores (0–100)

    # Lower irrigation requirement = better water score
    data["Water"] = (
        100 * (1 - data["irrigation_mm"] / 1000)
    ).clip(0, 100)

    # Fewer heat-stress months = better risk score
    data["Risk"] = (
        100 * (1 - data["heat_months"] / 12)
    ).clip(0, 100)

    # Soil indicator is assumed to be on a 0–5 scale
    data["Soil"] = (
        data["soil"] / 5 * 100
    ).clip(0, 100)

    # Income indicator is assumed to be on a 0–5 scale
    data["Income"] = (
        data["income"] / 5 * 100
    ).clip(0, 100)

    # Equal-weight overall score for reference
    data["Overall"] = data[
        ["Water", "Risk", "Soil", "Income"]
    ].mean(axis=1)

    return data[
        ["Rotation", "Water", "Risk", "Soil", "Income", "Overall"]
    ]



def style_chart(fig, title=None):
    fig.update_layout(
        font=dict(
            family="Manrope",
            color="#163C32",
            size=13
        ),
        title=dict(
            text=title,
            font=dict(color="#142B45", size=20)
        ) if title else None,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="rgba(255,255,255,0)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.35,
            xanchor="center",
            x=0.5,
            font=dict(
                family="Manrope",
                color="#142B45",
                size=12
            ),
            title=dict(
                font=dict(color="#142B45", size=12)
            )
        ),
        xaxis=dict(
            tickfont=dict(color="#142B45", size=11),
            title_font=dict(color="#142B45", size=12),
            gridcolor="#E2E8E3",
            zerolinecolor="#AAB8B0",
            linecolor="#AAB8B0"
        ),
        yaxis=dict(
            tickfont=dict(color="#142B45", size=11),
            title_font=dict(color="#142B45", size=12),
            gridcolor="#E2E8E3",
            zerolinecolor="#AAB8B0",
            linecolor="#AAB8B0"
        ),
        margin=dict(l=25, r=25, t=65, b=100)
    )

    fig.update_annotations(
        font=dict(
            family="Manrope",
            color="#142B45",
            size=12
        )
    )

    return fig


def format_stat(value):
    if pd.isna(value):
        return "N/A"

    if value == 0:
        return "0.00"

    if abs(value) < 0.01:
        return f"{value:.6f}".rstrip("0").rstrip(".")

    return f"{value:.2f}"


climate = load_climate()


if section == "Dashboard":

    st.markdown("## Climate Overview")
    st.markdown(
        "A look at historical weather patterns in Lahore, Punjab."
    )

    total_rain = climate["PRECTOTCORR"].sum()
    avg_temp = climate["T2M"].mean()
    avg_max = climate["T2M_MAX"].mean()
    avg_min = climate["T2M_MIN"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Rainfall", f"{total_rain:,.0f} mm")
    col2.metric("Average Temperature", f"{avg_temp:.1f} °C")
    col3.metric("Average Maximum", f"{avg_max:.1f} °C")
    col4.metric("Average Minimum", f"{avg_min:.1f} °C")

    st.markdown("---")
    st.markdown("### Average Monthly Rainfall")

    monthly_rain = (
        climate.groupby(climate.index.month)["PRECTOTCORR"]
        .mean()
        .reset_index()
    )

    monthly_rain.columns = ["Month", "Rainfall"]

    month_names = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    monthly_rain["Month"] = month_names

    fig = px.bar(
        monthly_rain,
        x="Month",
        y="Rainfall",
        color="Rainfall",
        color_continuous_scale=[
            "#D9F99D",
            "#86EFAC",
            "#10B981",
            "#047857",
            "#092B27"
        ],
        labels={
            "Rainfall": "Average Rainfall (mm)",
            "Month": "Month"
        }
    )

    fig = style_chart(fig, "Average Monthly Rainfall")
    fig.update_layout(coloraxis_showscale=False)

    fig.update_traces(
        marker_line_width=0,
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Rainfall: %{y:.1f} mm<extra></extra>"
        )
    )

    st.markdown("""
        This chart displays average rainfall for each month across the available climate record.
        It helps identify seasonal rainfall patterns and months when crops may depend more heavily on irrigation.
    """)

    st.markdown("""
        This chart displays the selected climate variable across your chosen date range.
        It helps reveal long-term trends and short-term fluctuations, although regional estimates may differ from conditions at a specific farm.
    """)

    st.plotly_chart(fig, use_container_width=True)


elif section == "Farmer Profile":

    st.markdown("## Your Farm Profile")
    st.write(
        "Tell AgriShift about your farm. These details will help "
        "personalize crop rotation recommendations."
    )

    if "farm_constraints" not in st.session_state:
        st.session_state.farm_constraints = {}

    with st.form("farm_constraints_form"):

        st.markdown("### Farm Information")

        col1, col2 = st.columns(2)

        with col1:
            land_size = st.number_input(
                "Farm size (acres)",
                min_value=0.1,
                value=5.0,
                step=0.5
            )

            water = st.selectbox(
                "Water availability",
                ["Low", "Moderate", "High"]
            )

            soil_type = st.selectbox(
                "Soil type",
                [
                    "Unknown",
                    "Sandy",
                    "Clay",
                    "Loamy",
                    "Silt",
                    "Other"
                ]
            )

        with col2:
            budget = st.number_input(
                "Available farming budget per acre (PKR)",
                min_value=0,
                value=50000,
                step=5000
            )

            season = st.selectbox(
                "Growing season",
                [
                    "Kharif",
                    "Rabi",
                    "Both seasons"
                ]
            )

            machinery = st.selectbox(
                "Machinery availability",
                [
                    "None",
                    "Limited",
                    "Available"
                ]
            )

        st.markdown("### Crop Preferences")

        preferred_crops = st.multiselect(
            "Crops you prefer to grow",
            [
                "Wheat",
                "Rice",
                "Mung bean",
                "Maize",
                "Cotton",
                "Sugarcane"
            ]
        )

        excluded_crops = st.multiselect(
            "Crops you want to avoid",
            [
                "Wheat",
                "Rice",
                "Mung bean",
                "Maize",
                "Cotton",
                "Sugarcane"
            ]
        )

        st.markdown("### Your Farming Goals")

        risk_preference = st.select_slider(
            "Risk preference",
            options=[
                "Very cautious",
                "Cautious",
                "Balanced",
                "Flexible",
                "High risk tolerance"
            ],
            value="Balanced"
        )

        submitted = st.form_submit_button(
            "Save Farm Profile",
            use_container_width=True
        )

    if submitted:

        st.session_state.farm_constraints = {
            "land_size": land_size,
            "water": water,
            "soil_type": soil_type,
            "budget": budget,
            "season": season,
            "machinery": machinery,
            "preferred_crops": preferred_crops,
            "excluded_crops": excluded_crops,
            "risk_preference": risk_preference
        }

        st.success("Your farm profile has been saved!")

    if st.session_state.farm_constraints:

        st.markdown("---")
        st.markdown("### Your Saved Farm Profile")

        profile = st.session_state.farm_constraints

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Farm Size",
            f"{profile['land_size']} acres"
        )

        col2.metric(
            "Water Availability",
            profile["water"]
        )

        col3.metric(
            "Budget",
            f"PKR {profile['budget']:,.0f}"
        )

        st.write("**Soil:**", profile["soil_type"])
        st.write("**Season:**", profile["season"])
        st.write("**Machinery:**", profile["machinery"])

        st.write(
            "**Preferred crops:**",
            ", ".join(profile["preferred_crops"])
            if profile["preferred_crops"]
            else "No preferences"
        )

        st.write(
            "**Crops to avoid:**",
            ", ".join(profile["excluded_crops"])
            if profile["excluded_crops"]
            else "None"
        )

        st.write("**Risk preference:**", profile["risk_preference"])

        if st.button("Reset Farm Profile"):
            st.session_state.farm_constraints = {}
            st.rerun()

elif section == "Rotation Analysis":

    st.markdown("## Crop Rotation Recommendations")
    st.write(
        "Choose what matters most to your farm. AgriShift will rank "
        "the crop rotations based on your choices and saved farm profile."
    )

    farm_profile = st.session_state.get("farm_constraints", {})

    if farm_profile:
        st.info(
            f"Using your farm profile: "
            f"{farm_profile.get('water', 'Moderate')} water availability, "
            f"{farm_profile.get('risk_preference', 'Balanced')} risk preference."
        )
    else:
        st.info(
            "No farm profile saved. Recommendations use your priority sliders."
        )

    st.markdown("### Your Farming Priorities")

    water = st.slider("Saving Water", 0, 100, 30)
    soil = st.slider("Improving Soil", 0, 100, 30)
    income = st.slider("Making a Profit", 0, 100, 20)
    risk = st.slider("Reducing Risk", 0, 100, 20)

    total_weight = water + soil + income + risk

    if total_weight == 0:
        st.warning("Please select at least one farming priority.")

    else:

        water_multiplier = {
            "Low": 1.5,
            "Moderate": 1.0,
            "High": 0.7
        }

        risk_multiplier = {
            "Very cautious": 1.5,
            "Cautious": 1.25,
            "Balanced": 1.0,
            "Flexible": 0.85,
            "High risk tolerance": 0.7
        }

        adjusted_water = water * water_multiplier.get(
            farm_profile.get("water", "Moderate"), 1.0
        )

        adjusted_risk = risk * risk_multiplier.get(
            farm_profile.get("risk_preference", "Balanced"), 1.0
        )

        adjusted_total = adjusted_water + soil + income + adjusted_risk

        weights = {
            "Water": adjusted_water / adjusted_total,
            "Soil": soil / adjusted_total,
            "Income": income / adjusted_total,
            "Risk": adjusted_risk / adjusted_total
        }

        st.markdown("### How Your Priorities Are Weighted")

        priority_data = pd.DataFrame({
            "Priority": [
                "Saving Water",
                "Improving Soil",
                "Making a Profit",
                "Reducing Risk"
            ],
            "Weight": [
                weights["Water"],
                weights["Soil"],
                weights["Income"],
                weights["Risk"]
            ]
        })

        priority_fig = px.bar(
            priority_data,
            x="Priority",
            y="Weight",
            color="Weight",
            color_continuous_scale=[
                "#D8EEDC",
                "#52B788",
                "#23865B"
            ]
        )

        priority_fig = style_chart(priority_fig)
        priority_fig.update_layout(
            showlegend=False,
            coloraxis_showscale=False,
            yaxis=dict(
                tickformat=".0%",
                gridcolor="#E2E8E3",
                tickfont=dict(color="#142B45"),
                title_font=dict(color="#142B45")
            )
        )

        st.markdown("""
            This chart shows how your farming priorities are weighted after adjustments for water availability and risk preference.
            These percentages determine how strongly water conservation, soil improvement, profitability, and risk reduction influence the final rotation rankings.
        """)

        st.plotly_chart(priority_fig, use_container_width=True)

        rotation_scores = load_rotation_scores()

        rotation_scores["Recommendation Score"] = (
            rotation_scores["Water"] * weights["Water"]
            + rotation_scores["Soil"] * weights["Soil"]
            + rotation_scores["Income"] * weights["Income"]
            + rotation_scores["Risk"] * weights["Risk"]
        )

        crop_matches = {
            "Wheat-Rice (current)": {"Wheat", "Rice"},
            "Wheat-Mung bean": {"Wheat", "Mung bean"},
            "Wheat-Maize": {"Wheat", "Maize"}
        }

        preferred_crops = set(
            farm_profile.get("preferred_crops", [])
        )

        excluded_crops = set(
            farm_profile.get("excluded_crops", [])
        )

        rotation_scores["Crops"] = rotation_scores["Rotation"].map(
            crop_matches
        )

        rotation_scores["Crops"] = rotation_scores["Crops"].apply(
            lambda crops: crops if isinstance(crops, set) else set()
        )

        if excluded_crops:
            rotation_scores = rotation_scores[
                rotation_scores["Crops"].apply(
                    lambda crops: not bool(crops & excluded_crops)
                )
            ]

        if rotation_scores.empty:
            st.warning(
                "All available rotations contain crops you excluded. "
                "Please remove some excluded crops from your farm profile."
            )

        else:

            if preferred_crops:
                rotation_scores["Preference Bonus"] = (
                    rotation_scores["Crops"].apply(
                        lambda crops: len(crops & preferred_crops) * 4
                    )
                )
            else:
                rotation_scores["Preference Bonus"] = 0

            ranked = rotation_scores.sort_values(
                "Recommendation Score",
                ascending=False
            ).reset_index(drop=True)

            st.markdown("### Recommended Crop Rotations")

            best_rotation = ranked.iloc[0]

            st.success(
                f"Best match for your priorities: {best_rotation['Rotation']}"
            )

            st.metric(
                "Suitability Score",
                f"{best_rotation['Recommendation Score']:.1f}/100"
            )

            st.markdown("### Crop Rotation Rankings")

            ranking_fig = px.bar(
                ranked,
                x="Rotation",
                y="Recommendation Score",
                color="Recommendation Score",
                color_continuous_scale=[
                    "#D8EEDC",
                    "#52B788",
                    "#23865B"
                ],
                text="Recommendation Score"
            )

            ranking_fig.update_traces(
                texttemplate="%{text:.1f}",
                textposition="outside",
                textfont=dict(color="#142B45")
            )

            ranking_fig = style_chart(ranking_fig)
            ranking_fig.update_layout(
                coloraxis_showscale=False,
                yaxis=dict(
                    range=[0, 110],
                    gridcolor="#E2E8E3",
                    title="Suitability Score",
                    tickfont=dict(color="#142B45"),
                    title_font=dict(color="#142B45")
                ),
                xaxis_title="Crop Rotation"
            )

            st.markdown("""
                This chart ranks crop rotations according to their suitability scores under your selected farming priorities and saved farm profile.
                Higher scores indicate a stronger match to the model's assumptions, not guaranteed yields or profits.
            """)

            st.plotly_chart(ranking_fig, use_container_width=True)

            st.markdown("---")
            st.markdown("## Water Requirements")

            st.write(
                "Compare the minimum water required by each crop rotation "
                "in dry, normal, and wet years."
            )

            water_data = pd.DataFrame({
                "Rotation": [
                    "Wheat-Rice (current)",
                    "Wheat-Mung bean",
                    "Wheat-Maize"
                ],
                "Dry years": [984, 188, 353],
                "Normal years": [855, 173, 217],
                "Wet years": [588, 124, 124]
            })

            water_long = water_data.melt(
                id_vars=["Rotation"],
                var_name="Year Type",
                value_name="Minimum Water Required"
            )

            water_fig = px.bar(
                water_long,
                x="Rotation",
                y="Minimum Water Required",
                color="Year Type",
                barmode="group",
                color_discrete_map={
                    "Dry years": "#142B45",
                    "Normal years": "#23865B",
                    "Wet years": "#F4BE36"
                },
                labels={
                    "Minimum Water Required": "Minimum Water Required (mm)"
                },
                text="Minimum Water Required"
            )

            water_fig.update_traces(
                textposition="outside",
                texttemplate="%{text:,} mm",
                textfont=dict(color="#142B45")
            )

            water_fig = style_chart(
                water_fig,
                "Minimum Water Required by Crop Rotation"
            )

            water_fig.update_layout(
                yaxis_title="Minimum Water Required (mm)",
                xaxis_title="Crop Rotation",
                legend_title="Year Type",
                yaxis=dict(
                    tickfont=dict(color="#142B45"),
                    title_font=dict(color="#142B45"),
                    gridcolor="#E2E8E3"
                ),
                xaxis=dict(
                    tickfont=dict(color="#142B45"),
                    title_font=dict(color="#142B45")
                )
            )

            st.markdown("""
                This chart compares the minimum water requirements of each crop rotation across dry, normal, and wet years.
                It helps illustrate how alternative rotations compare with Wheat-Rice, although actual irrigation needs vary with local soil, rainfall, and farming conditions.
            """)

            st.plotly_chart(water_fig, use_container_width=True)

            st.markdown("### How Much Water Can Be Saved?")

            baseline = water_data[
                water_data["Rotation"] == "Wheat-Rice (current)"
            ].iloc[0]

            savings_rows = []

            for _, row in water_data.iterrows():
                if row["Rotation"] == "Wheat-Rice (current)":
                    continue

                savings_rows.append({
                    "Crop Rotation": row["Rotation"],
                    "Dry Years": (
                        (baseline["Dry years"] - row["Dry years"])
                        / baseline["Dry years"] * 100
                    ),
                    "Normal Years": (
                        (baseline["Normal years"] - row["Normal years"])
                        / baseline["Normal years"] * 100
                    ),
                    "Wet Years": (
                        (baseline["Wet years"] - row["Wet years"])
                        / baseline["Wet years"] * 100
                    )
                })

            savings_data = pd.DataFrame(savings_rows)

            savings_long = savings_data.melt(
                id_vars=["Crop Rotation"],
                var_name="Year Type",
                value_name="Water Saved (%)"
            )

            savings_fig = px.bar(
                savings_long,
                x="Crop Rotation",
                y="Water Saved (%)",
                color="Year Type",
                barmode="group",
                color_discrete_map={
                    "Dry Years": "#142B45",
                    "Normal Years": "#23865B",
                    "Wet Years": "#F4BE36"
                },
                text="Water Saved (%)"
            )

            savings_fig.update_traces(
                texttemplate="%{text:.1f}%",
                textposition="outside",
                textfont=dict(color="#142B45")
            )

            savings_fig = style_chart(
                savings_fig,
                "Water Saved Compared with Wheat-Rice"
            )

            savings_fig.update_layout(
                yaxis=dict(
                    title="Water Saved (%)",
                    range=[0, 110],
                    gridcolor="#E2E8E3",
                    tickfont=dict(color="#142B45"),
                    title_font=dict(color="#142B45")
                ),
                xaxis=dict(
                    title="Crop Rotation",
                    tickfont=dict(color="#142B45"),
                    title_font=dict(color="#142B45")
                )
            )

            st.markdown("""
                This chart shows the estimated percentage reduction in minimum water requirements compared with Wheat-Rice, the baseline rotation.
                Positive percentages indicate lower water requirements in the project's dataset, not guaranteed real-world irrigation savings.
            """)

            st.plotly_chart(
                savings_fig,
                use_container_width=True
            )

            st.markdown("### Water Comparison Table")

            display_savings = savings_data.copy()

            display_savings.columns = [
                "Crop Rotation",
                "Water Saved in Dry Years",
                "Water Saved in Normal Years",
                "Water Saved in Wet Years"
            ]

            styled_table = (
                display_savings.style
                .format({
                    "Water Saved in Dry Years": "{:.1f}%",
                    "Water Saved in Normal Years": "{:.1f}%",
                    "Water Saved in Wet Years": "{:.1f}%"
                })
                .set_table_styles([
                    {
                        "selector": "th",
                        "props": [
                            ("background-color", "#23865B"),
                            ("color", "white"),
                            ("font-weight", "bold"),
                            ("border", "1px solid #B8D9C2"),
                            ("padding", "12px")
                        ]
                    },
                    {
                        "selector": "td",
                        "props": [
                            ("color", "#142B45"),
                            ("border", "1px solid #C9E3D0"),
                            ("padding", "12px")
                        ]
                    },
                    {
                        "selector": "table",
                        "props": [
                            ("background-color", "#EDF6EF"),
                            ("border-collapse", "collapse"),
                            ("border-radius", "10px")
                        ]
                    }
                ])
                .apply(
                    lambda row: [
                        "background-color: #EDF6EF"
                        if row.name % 2 == 0
                        else "background-color: #DCEFE1"
                        for _ in row
                    ],
                    axis=1
                )
            )

            st.dataframe(
                styled_table,
                use_container_width=True,
                hide_index=True
            )

            st.markdown("""
            <div class="water-highlight">
                <strong>What does this mean?</strong>
                <p>
                    Wheat-Rice is used as the comparison because it represents
                    the current rotation in this dataset. The percentages show
                    how much less minimum water the alternative rotations need
                    compared with Wheat-Rice under each type of year.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.caption(
                "Water requirements are taken from the project's dry, normal, "
                "and wet year comparison dataset. These values are not a direct "
                "measurement of total farm irrigation use."
            )

            st.markdown("---")
            st.markdown("### Why These Rotations May Work")

            rotation_explanations = {
                "Wheat-Rice (current)": {
                    "Water": "Rice usually needs a large amount of irrigation water.",
                    "Soil": "Growing the same types of crops repeatedly can limit crop diversity.",
                    "Income": "Rice can provide good returns depending on market prices and yields.",
                    "Risk": "Both crops can be affected by heat and water shortages."
                },
                "Wheat-Mung bean": {
                    "Water": "Mung bean generally needs less irrigation than rice.",
                    "Soil": "Mung bean can add nitrogen to the soil through natural processes.",
                    "Income": "Mung bean offers another crop to sell, although returns can vary.",
                    "Risk": "Growing different crops can reduce dependence on one crop."
                },
                "Wheat-Maize": {
                    "Water": "Maize may use less water than rice under suitable conditions.",
                    "Soil": "Different crops can use soil nutrients in different ways.",
                    "Income": "Maize gives farmers another possible source of income.",
                    "Risk": "Heat and water shortages can still affect maize yields."
                }
            }

            for _, row in ranked.iterrows():
                with st.container(border=True):
                    st.markdown(f"#### {row['Rotation']}")
                    st.write(
                        f"**Suitability score:** "
                        f"{row['Recommendation Score']:.1f}/100"
                    )

                    explanation = rotation_explanations.get(
                        row["Rotation"], {}
                    )

                    factors = {
                        "Water": row["Water"],
                        "Soil": row["Soil"],
                        "Income": row["Income"],
                        "Risk": row["Risk"]
                    }

                    strongest = max(factors, key=factors.get)
                    weakest = min(factors, key=factors.get)

                    st.write(
                        f"**Strongest area:** {strongest} "
                        f"({factors[strongest]:.1f}/100)"
                    )

                    st.write(
                        f"**Area to consider:** {weakest} "
                        f"({factors[weakest]:.1f}/100)"
                    )

                    for factor in ["Water", "Soil", "Income", "Risk"]:
                        st.write(
                            f"**{factor}:** "
                            f"{explanation.get(factor, 'No explanation available.')}"
                        )

            st.caption(
                "These are general farming considerations, not guaranteed "
                "results for every farm. Suitability scores come from the "
                "project's crop rotation scoring dataset."
            )


elif section == "Climate Explorer":

    st.markdown("## Climate Explorer")
    st.write(
        "Explore how rainfall, temperature, and other climate conditions "
        "have changed over time."
    )

    climate_options = {
        "Rainfall": "PRECTOTCORR",
        "Average Temperature": "T2M",
        "Maximum Temperature": "T2M_MAX",
        "Minimum Temperature": "T2M_MIN",
        "Root-Zone Soil Moisture": "GWETROOT",
        "Surface Soil Moisture": "GWETTOP",
        "Evapotranspiration": "EVPTRNS"
    }

    selected_variable = st.selectbox(
        "Choose what you want to explore",
        list(climate_options.keys())
    )

    variable = climate_options[selected_variable]

    climate_filtered = climate.copy()

    start_date = climate.index.min().date()
    end_date = climate.index.max().date()

    date_range = st.date_input(
        "Choose a date range",
        value=(start_date, end_date),
        min_value=start_date,
        max_value=end_date
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        climate_filtered = climate_filtered.loc[
            str(date_range[0]):str(date_range[1])
        ]

    if climate_filtered.empty:
        st.warning("There is no data for this date range.")

    else:
        fig = px.line(
            climate_filtered,
            x=climate_filtered.index,
            y=variable,
            title=f"{selected_variable} Over Time",
            labels={
                variable: selected_variable,
                "x": "Date"
            }
        )

        fig.update_traces(
            line=dict(color="#16A36A", width=3),
            hovertemplate="%{x|%b %Y}<br>%{y:.3f}<extra></extra>"
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title=selected_variable
        )

        fig = style_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Climate Statistics")

        col1, col2, col3 = st.columns(3)

        positive_values = climate_filtered.loc[
            climate_filtered[variable] > 0,
            variable
        ]

        lowest_nonzero = (
            positive_values.min()
            if not positive_values.empty
            else 0
        )

        col1.metric(
            "Average",
            format_stat(climate_filtered[variable].mean())
        )

        col2.metric(
            "Highest",
            format_stat(climate_filtered[variable].max())
        )

        col3.metric(
            "Lowest non-zero",
            format_stat(lowest_nonzero),
            help=(
                "The smallest value above zero. "
                "This is used so small positive values are not hidden "
                "by actual zero observations."
            )
        )


elif section == "Vegetation":

    st.markdown("## Vegetation Monitoring")
    st.write(
        "Explore changes in vegetation over time using NASA satellite data."
    )

    try:
        ndvi = load_ndvi()

        if ndvi.empty:
            st.warning("No valid vegetation observations were found.")

        else:
            st.markdown("### Observation Settings")

            quality_filter = st.checkbox(
                "Show only high-quality observations",
                value=True,
                help="Uses the MODLAND quality flag 0b00."
            )

            if quality_filter:
                ndvi_filtered = ndvi[
                    ndvi["MODLAND_Quality"] == "0b00"
                ].copy()
            else:
                ndvi_filtered = ndvi.copy()

            if ndvi_filtered.empty:
                st.warning(
                    "No observations match this quality setting. "
                    "Try including all observations."
                )

            else:
                min_date = ndvi_filtered["Date"].min().date()
                max_date = ndvi_filtered["Date"].max().date()

                date_range = st.date_input(
                    "Choose an observation period",
                    value=(min_date, max_date),
                    min_value=min_date,
                    max_value=max_date,
                    key="ndvi_date_range"
                )

                if isinstance(date_range, tuple) and len(date_range) == 2:
                    ndvi_filtered = ndvi_filtered[
                        (ndvi_filtered["Date"] >= pd.Timestamp(date_range[0]))
                        & (ndvi_filtered["Date"] <= pd.Timestamp(date_range[1]))
                    ]

                if ndvi_filtered.empty:
                    st.warning("There is no data for this date range.")

                else:
                    latest_ndvi = ndvi_filtered.iloc[-1]["NDVI"]
                    average_ndvi = ndvi_filtered["NDVI"].mean()
                    highest_ndvi = ndvi_filtered["NDVI"].max()

                    col1, col2, col3, col4 = st.columns(4)

                    col1.metric("Latest NDVI", f"{latest_ndvi:.3f}")
                    col2.metric("Average NDVI", f"{average_ndvi:.3f}")
                    col3.metric("Highest NDVI", f"{highest_ndvi:.3f}")
                    col4.metric(
                        "Observations",
                        f"{len(ndvi_filtered):,}"
                    )

                    st.markdown("---")
                    st.markdown("### Vegetation Changes Over Time")

                    trend_fig = px.line(
                        ndvi_filtered,
                        x="Date",
                        y="NDVI",
                        labels={
                            "Date": "Observation Date",
                            "NDVI": "Vegetation Index (NDVI)"
                        }
                    )

                    trend_fig.update_traces(
                        line=dict(color="#23865B", width=2.5),
                        mode="lines+markers",
                        marker=dict(size=4),
                        hovertemplate=(
                            "<b>%{x|%d %b %Y}</b><br>"
                            "NDVI: %{y:.3f}<extra></extra>"
                        )
                    )

                    trend_fig = style_chart(
                        trend_fig,
                        "Vegetation Index Over Time"
                    )

                    trend_fig.update_layout(
                        yaxis=dict(
                            range=[0, 1],
                            gridcolor="#E2E8E3",
                            title="NDVI",
                            tickfont=dict(color="#142B45"),
                            title_font=dict(color="#142B45")
                        )
                    )

                    st.markdown("""
                        This chart tracks satellite-derived NDVI observations over the selected period.
                        Rising or falling NDVI can indicate changes in vegetation greenness, but NDVI alone does not prove crop health or yield.
                    """)

                    st.plotly_chart(
                        trend_fig,
                        use_container_width=True
                    )

                    st.markdown("### Vegetation Throughout the Year")

                    ndvi_filtered["Month"] = (
                        ndvi_filtered["Date"].dt.month
                    )

                    month_names = [
                        "Jan", "Feb", "Mar", "Apr",
                        "May", "Jun", "Jul", "Aug",
                        "Sep", "Oct", "Nov", "Dec"
                    ]

                    seasonal = (
                        ndvi_filtered.groupby("Month")["NDVI"]
                        .mean()
                        .reindex(range(1, 13))
                        .reset_index()
                    )

                    seasonal["Month Name"] = [
                        month_names[int(month) - 1]
                        for month in seasonal["Month"]
                    ]

                    seasonal_fig = px.bar(
                        seasonal,
                        x="Month Name",
                        y="NDVI",
                        color="NDVI",
                        color_continuous_scale=[
                            "#D9F99D",
                            "#86EFAC",
                            "#22C55E",
                            "#059669",
                            "#102A43"
                        ],
                        labels={
                            "Month Name": "Month",
                            "NDVI": "Average NDVI"
                        }
                    )

                    seasonal_fig = style_chart(
                        seasonal_fig,
                        "Average Vegetation Index by Month"
                    )

                    seasonal_fig.update_layout(
                        coloraxis_showscale=False,
                        yaxis=dict(
                            range=[0, 1],
                            gridcolor="#E2E8E3",
                            tickfont=dict(color="#142B45"),
                            title_font=dict(color="#142B45")
                        )
                    )

                    st.markdown("""
                        This chart averages NDVI by calendar month across the selected observations.
                        It helps identify recurring seasonal vegetation patterns, although crop calendars and the number of observations per month can affect the averages.
                    """)

                    st.plotly_chart(
                        seasonal_fig,
                        use_container_width=True
                    )

                    st.markdown("### Comparing Different Years")

                    ndvi_filtered["Year"] = (
                        ndvi_filtered["Date"].dt.year
                    )

                    yearly = (
                        ndvi_filtered.groupby("Year")["NDVI"]
                        .agg(["mean", "min", "max", "count"])
                        .reset_index()
                    )

                    yearly.columns = [
                        "Year",
                        "Average NDVI",
                        "Lowest NDVI",
                        "Highest NDVI",
                        "Observations"
                    ]

                    yearly_fig = px.line(
                        yearly,
                        x="Year",
                        y="Average NDVI",
                        markers=True,
                        labels={
                            "Average NDVI": "Annual Average NDVI",
                            "Year": "Year"
                        }
                    )

                    yearly_fig.update_traces(
                        line=dict(color="#23865B", width=3),
                        marker=dict(size=8)
                    )

                    yearly_fig = style_chart(
                        yearly_fig,
                        "Average Vegetation Index by Year"
                    )

                    yearly_fig.update_layout(
                        yaxis=dict(
                            range=[0, 1],
                            gridcolor="#E2E8E3",
                            tickfont=dict(color="#142B45"),
                            title_font=dict(color="#142B45")
                        )
                    )

                    st.markdown("""
                        This chart compares annual average NDVI across years.
                        It helps identify broad changes in vegetation greenness, but differences may also reflect crop type, growth stage, or observation quality.
                    """)

                    st.plotly_chart(
                        yearly_fig,
                        use_container_width=True
                    )

                    st.dataframe(
                        yearly.style.format({
                            "Average NDVI": "{:.3f}",
                            "Lowest NDVI": "{:.3f}",
                            "Highest NDVI": "{:.3f}"
                        }),
                        use_container_width=True,
                        hide_index=True
                    )

                    st.markdown("### What Does NDVI Tell Us?")

                    st.write(
                        "NDVI is a measurement made using satellite images. "
                        "It looks at how plants reflect different types of "
                        "light. It helps us understand how much green "
                        "vegetation is present in an area."
                    )

                    ndvi_ranges = pd.DataFrame({
                        "NDVI Range": [
                            "Below 0",
                            "0.0 – 0.2",
                            "0.2 – 0.4",
                            "0.4 – 0.6",
                            "0.6 – 1.0"
                        ],
                        "What It Can Indicate": [
                            "Water, snow, or surfaces without vegetation",
                            "Bare soil or very little vegetation",
                            "Small amounts of vegetation",
                            "Moderate amounts of vegetation",
                            "Dense green vegetation"
                        ]
                    })

                    st.dataframe(
                        ndvi_ranges,
                        use_container_width=True,
                        hide_index=True
                    )

                    st.caption(
                        "These ranges are general guides, not exact crop "
                        "health scores. NDVI can vary with crop type, soil, "
                        "plant growth stage, and satellite image quality."
                    )

                    st.caption(
                        "Source: MODIS MOD13Q1 Collection 6.1, "
                        "250 m resolution and 16-day observation interval."
                    )

    except FileNotFoundError:
        st.error(
            "Could not find data/ndvi_raw.csv. "
            "Make sure the file is inside your data folder."
        )

    except Exception as error:
        st.error(f"Could not load the vegetation data: {error}")

elif section == "Soil Health":

    st.markdown("## Soil Moisture Monitoring")

    st.write(
        "See how much moisture is present near the soil surface "
        "and deeper in the soil where plant roots grow."
    )

    soil_columns = ["GWETROOT", "GWETTOP"]

    if not all(column in climate.columns for column in soil_columns):
        st.error(
            "The climate dataset must contain GWETROOT and GWETTOP."
        )

    else:
        soil_data = climate[
            soil_columns + ["PRECTOTCORR"]
        ].copy()

        soil_data = soil_data.dropna(subset=soil_columns)

        if soil_data.empty:
            st.warning("No soil moisture data was found.")

        else:
            latest_root = soil_data["GWETROOT"].iloc[-1]
            latest_surface = soil_data["GWETTOP"].iloc[-1]

            average_root = soil_data["GWETROOT"].mean()
            average_surface = soil_data["GWETTOP"].mean()

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Latest Root-Zone Moisture",
                f"{latest_root:.3f}"
            )

            col2.metric(
                "Latest Surface Moisture",
                f"{latest_surface:.3f}"
            )

            col3.metric(
                "Average Root-Zone Moisture",
                f"{average_root:.3f}"
            )

            col4.metric(
                "Average Surface Moisture",
                f"{average_surface:.3f}"
            )

            st.markdown("---")
            st.markdown("### Soil Moisture Over Time")

            soil_view = soil_data.reset_index()
            soil_view = soil_view.rename(
                columns={soil_view.columns[0]: "Date"}
            )

            soil_long = soil_view.melt(
                id_vars=["Date"],
                value_vars=["GWETROOT", "GWETTOP"],
                var_name="Moisture Type",
                value_name="Moisture"
            )

            soil_long["Moisture Type"] = soil_long[
                "Moisture Type"
            ].map({
                "GWETROOT": "Root-Zone Moisture",
                "GWETTOP": "Surface Moisture"
            })

            soil_fig = px.line(
                soil_long,
                x="Date",
                y="Moisture",
                color="Moisture Type",
                color_discrete_map={
                    "Root-Zone Moisture": "#23865B",
                    "Surface Moisture": "#F4BE36"
                },
                labels={
                    "Date": "Date",
                    "Moisture": "Soil Moisture Indicator"
                }
            )

            soil_fig = style_chart(
                soil_fig,
                "Root-Zone and Surface Soil Moisture"
            )

            soil_fig.update_layout(
                legend_title_text="Moisture Type"
            )

            st.markdown("""
                This chart compares NASA root-zone and surface moisture indicators over time.
                It shows how moisture near the surface differs from deeper root-zone moisture, but these are modeled indicators—not direct measurements of every field.
            """)

            st.plotly_chart(
                soil_fig,
                use_container_width=True
            )

            st.markdown("### Soil Moisture Throughout the Year")

            soil_data["Month"] = soil_data.index.month

            monthly_soil = (
                soil_data.groupby("Month")[soil_columns]
                .mean()
                .reset_index()
            )

            monthly_soil = monthly_soil.melt(
                id_vars=["Month"],
                value_vars=soil_columns,
                var_name="Moisture Type",
                value_name="Average Moisture"
            )

            monthly_soil["Moisture Type"] = monthly_soil[
                "Moisture Type"
            ].map({
                "GWETROOT": "Root-Zone Moisture",
                "GWETTOP": "Surface Moisture"
            })

            monthly_soil["Month"] = monthly_soil["Month"].map({
                1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
                5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
                9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
            })

            seasonal_soil_fig = px.line(
                monthly_soil,
                x="Month",
                y="Average Moisture",
                color="Moisture Type",
                markers=True,
                color_discrete_map={
                    "Root-Zone Moisture": "#23865B",
                    "Surface Moisture": "#F4BE36"
                }
            )

            seasonal_soil_fig = style_chart(
                seasonal_soil_fig,
                "Average Monthly Soil Moisture"
            )

            st.markdown("""
                This chart shows average root-zone and surface moisture by month.
                It helps identify seasonal moisture patterns and potentially drier or wetter periods, without establishing exact irrigation requirements.
            """)

            st.plotly_chart(
                seasonal_soil_fig,
                use_container_width=True
            )

            st.markdown("### Rainfall and Soil Moisture")

            rainfall_soil = soil_data.dropna(
                subset=["PRECTOTCORR", "GWETROOT", "GWETTOP"]
            ).reset_index()

            rainfall_soil = rainfall_soil.rename(
                columns={rainfall_soil.columns[0]: "Date"}
            )

            rainfall_fig = px.scatter(
                rainfall_soil,
                x="PRECTOTCORR",
                y="GWETROOT",
                color="GWETTOP",
                color_continuous_scale=[
                    "#D8EEDC",
                    "#52B788",
                    "#23865B",
                    "#142B45"
                ],
                hover_data=["Date"],
                labels={
                    "PRECTOTCORR": "Rainfall (mm)",
                    "GWETROOT": "Root-Zone Moisture",
                    "GWETTOP": "Surface Moisture"
                }
            )

            rainfall_fig = style_chart(
                rainfall_fig,
                "Rainfall and Root-Zone Soil Moisture"
            )

            st.markdown("""
                Each point compares rainfall with root-zone moisture for an observation date, while color represents surface moisture.
                Patterns can suggest associations, but they do not establish that rainfall alone caused changes in soil moisture.
            """)

            st.plotly_chart(
                rainfall_fig,
                use_container_width=True
            )

            st.markdown("### Comparing Soil Moisture by Year")

            annual_soil = (
                soil_data.groupby(soil_data.index.year)[soil_columns]
                .mean()
                .rename_axis("Year")
                .reset_index()
            )

            annual_soil = annual_soil.melt(
                id_vars=["Year"],
                value_vars=soil_columns,
                var_name="Moisture Type",
                value_name="Average Moisture"
            )

            annual_soil["Moisture Type"] = annual_soil[
                "Moisture Type"
            ].map({
                "GWETROOT": "Root-Zone Moisture",
                "GWETTOP": "Surface Moisture"
            })

            annual_fig = px.bar(
                annual_soil,
                x="Year",
                y="Average Moisture",
                color="Moisture Type",
                barmode="group",
                color_discrete_map={
                    "Root-Zone Moisture": "#23865B",
                    "Surface Moisture": "#F4BE36"
                }
            )

            annual_fig = style_chart(
                annual_fig,
                "Average Soil Moisture by Year"
            )

            st.markdown("""
                This chart compares average surface and root-zone moisture by year.
                It helps show year-to-year variability, but annual averages can hide important within-season dry periods.
            """)

            st.plotly_chart(
                annual_fig,
                use_container_width=True
            )

            st.markdown("### Understanding the Measurements")

            with st.container(border=True):
                st.markdown("#### Root-Zone Moisture")
                st.write(
                    "GWETROOT measures moisture in the deeper soil "
                    "layers where plant roots grow. It helps us understand "
                    "how much water may be available to crops."
                )

            with st.container(border=True):
                st.markdown("#### Surface Moisture")
                st.write(
                    "GWETTOP measures moisture closer to the soil surface. "
                    "It can change quickly after rainfall or when water "
                    "evaporates in hot weather."
                )

            st.info(
                "These measurements show soil moisture. They do not "
                "directly measure soil fertility, nutrients, salinity, "
                "or organic matter."
            )

            st.caption(
                "Values are shown using the original NASA dataset scale. "
                "They should not be treated as a complete soil-health score."
            )


elif section == "Data & Methodology":

    st.markdown("## Data, Methodology & About AgriShift")

    st.markdown("""
    <div class="intro-section">
        <h3>About AgriShift</h3>
        <p>
            AgriShift is an agricultural decision-support platform designed
            to help farmers explore climate trends, vegetation conditions,
            soil moisture patterns, and alternative crop rotations.
            By combining NASA Earth observations with agricultural
            analysis, it translates complex datasets into accessible
            visualizations and comparative insights.
        </p>
        <p>
            Our goal is to help farmers better understand environmental
            conditions, explore water-efficient alternatives, and make
            more informed decisions about agricultural planning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Data Sources & Methodology")

    st.markdown("""
    ### Where the Data Comes From

    - NASA POWER monthly climate data
    - NASA MODIS MOD13Q1 Collection 6.1 vegetation observations
    - Crop rotation scoring datasets
    - NASA soil moisture measurements

    ### Study Area

    Lahore, Punjab, Pakistan.

    ### Climate Data

    Monthly observations include:

    - **Rainfall:** Precipitation received over time.
    - **Average temperature:** Mean air temperature.
    - **Maximum temperature:** Maximum temperature observations.
    - **Minimum temperature:** Minimum temperature observations.
    - **Root-zone moisture:** Moisture in deeper soil layers.
    - **Surface moisture:** Moisture closer to the soil surface.
    - **Evapotranspiration:** Water transferred through evaporation
      and plant transpiration.

    ### Vegetation Data

    Vegetation is monitored using NASA MODIS NDVI observations.

    The data has a 250 m spatial resolution and a 16-day observation
    interval. A quality flag is used to identify observations
    marked as good quality.

    ### Crop Rotation Recommendations

    Crop rotations are ranked using four factors:

    - Water conservation
    - Soil health
    - Profitability
    - Risk reduction

    Farmers can change the importance of each factor. AgriShift
    calculates a suitability score for each rotation based on
    the selected priorities.

    ### Water Requirements

    The water comparison uses the minimum water required for each
    rotation in dry, normal, and wet years. Water savings are
    calculated against the Wheat-Rice rotation.

    """)

    st.markdown("---")

    st.markdown("## Limitations, Risks & Uncertainty")

    st.markdown("""
    <div class="info-card">
        <h4>Climate Data Limitations</h4>
        <p>
            NASA climate datasets provide valuable environmental
            information, but their measurements and estimates do not
            necessarily represent conditions at an individual farm.
            Local rainfall, temperature, and soil conditions can
            differ from broader datasets.
        </p>
    </div>

    <div class="info-card">
        <h4>Vegetation Monitoring Limitations</h4>
        <p>
            NDVI indicates vegetation greenness and activity, not
            guaranteed crop health or yield. Soil background, crop
            type, growth stage, clouds, and satellite resolution
            can influence observations.
        </p>
    </div>

    <div class="info-card">
        <h4>Crop Rotation Scoring Limitations</h4>
        <p>
            Rotation rankings depend on the scoring dataset and the
            weights selected by the user. A high suitability score
            indicates a better match within this model, not a
            guaranteed successful harvest or financial return.
        </p>
    </div>

    <div class="info-card">
        <h4>Local Farming Conditions</h4>
        <p>
            Actual results can differ because of soil composition,
            irrigation access, groundwater availability, seed
            varieties, fertilizer use, pests, labour, machinery,
            weather conditions, and changing market prices.
            These factors can cause a recommended rotation to
            perform differently across farms.
        </p>
    </div>

    <div class="info-card">
        <h4>Water Requirement Estimates</h4>
        <p>
            Water requirement comparisons are based on the project's
            supplied datasets and assumptions. They should not be
            interpreted as precise irrigation prescriptions or
            measurements of actual water consumed by every farm.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.warning(
        "AgriShift is an exploratory decision-support tool. "
        "Its recommendations should be evaluated alongside local "
        "agricultural knowledge, field conditions, and professional advice."
    )

    st.markdown("---")

    
    st.markdown("## Project Documents & Demonstration")

    st.write(
        "Explore AgriShift's objectives, analytical features, "
        "and application demonstration."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>Project Presentation</h4>
            <p>
                An overview of AgriShift, its objectives, data sources,
                analytical features, and potential impact.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.info("PowerPoint presentation — Coming soon")

    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>Application Demonstration</h4>
            <p>
                A walkthrough of the application's interface,
                navigation, and analytical tools.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.info("YouTube demonstration — Coming soon")

    st.markdown("""
    <div class="info-card" style="text-align: center; margin-top: 1rem;">
        <h4>Explore AgriShift</h4>
        <p>
            Navigate through the application to explore climate data,
            vegetation patterns, soil conditions, and crop rotation analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("---")
    st.markdown("---")
    st.markdown("## Meet the Team")

    team_cols = st.columns(3)

    team_members = [
        "Abdul Rehman Amjad",
        "Naad e Ali",
        "Ayan Arshad"
    ]

    for col, member in zip(team_cols, team_members):
        with col:
            st.markdown(f"""
            <div class="info-card" style="text-align: center;">
                <h4>{member}</h4>
            </div>
            """, unsafe_allow_html=True)

    st.caption(
        "AgriShift is a research and decision-support project. "
        "Its results support exploration and planning rather than "
        "providing guaranteed agricultural outcomes."
    )
