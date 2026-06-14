import streamlit as st

from parser import extract_text
from skill_extractor import extract_skills
from ats_score import calculate_ats

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------
# CUSTOM CSS
# -----------------------

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

/* Global Font */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0b1120,
        #111827,
        #1e293b
    );
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: #0a0f1c;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color:#e2e8f0 !important;
}

/* Main Heading */
.main-title{
    text-align:center;
    font-size:58px;
    font-weight:700;
    color:#ffffff;
    letter-spacing:1px;
}

/* Subtitle */
.sub-title{
    text-align:center;
    font-size:18px;
    font-weight:400;
    color:#94a3b8;
    margin-bottom:35px;
}

/* Section Headings */
h1,h2,h3,h4{
    color:#f8fafc !important;
    font-weight:600 !important;
}

/* Normal Text */
p, div, label, span{
    color:#cbd5e1;
}

/* Glass Card */
.card{
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(16px);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:22px;
    padding:25px;
    margin-bottom:20px;
}

/* Skill Tags */
.skill-tag{
    display:inline-block;
    margin:6px;
    padding:10px 18px;
    border-radius:30px;
    background:linear-gradient(
        135deg,
        #06b6d4,
        #2563eb
    );
    color:white !important;
    font-weight:600;
    font-size:14px;
}

/* Upload Box */
[data-testid="stFileUploader"]{
    background: rgba(255,255,255,0.05);
    border-radius:15px;
    padding:15px;
}

/* Metrics */
[data-testid="metric-container"]{
    background: rgba(255,255,255,0.05);
    border-radius:15px;
    padding:12px;
}

/* Metric Label */
[data-testid="metric-container"] label{
    color:#94a3b8 !important;
}

/* Metric Value */
[data-testid="metric-container"] div{
    color:white !important;
    font-weight:700 !important;
}

/* Text Area */
textarea{
    background:#0f172a !important;
    color:#f8fafc !important;
    border-radius:12px !important;
}

/* Buttons */
.stButton button,
.stDownloadButton button{
    background:linear-gradient(
        135deg,
        #06b6d4,
        #2563eb
    );
    color:white;
    border:none;
    border-radius:12px;
    font-weight:600;
    transition:0.3s;
}

.stButton button:hover,
.stDownloadButton button:hover{
    transform:translateY(-2px);
}

/* Info Box */
[data-testid="stAlert"]{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# SIDEBAR
# -----------------------

st.sidebar.markdown("""
# 📄 Resume Analyzer

### Features

🚀 Skill Extraction

📊 ATS Score

📄 Resume Preview

💡 Smart Suggestions

📥 Report Download

---

### Version

Premium UI v1.0
""")

# -----------------------
# HEADER
# -----------------------

st.markdown("""
<div class="main-title">
📄 Resume Analyzer
</div>

<div class="sub-title">
Analyze Your Resume Like A Professional Recruiter
</div>
""", unsafe_allow_html=True)

# -----------------------
# FILE UPLOAD
# -----------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# -----------------------
# PROCESS FILE
# -----------------------

if uploaded_file:

    resume_text = extract_text(
        uploaded_file
    )

    skills = extract_skills(
        resume_text
    )

    score = calculate_ats(
        resume_text,
        skills
    )

    # -----------------------
    # ATS SCORE
    # -----------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.subheader("📊 ATS Score")

        st.metric(
            "Resume Score",
            f"{score}%"
        )

        st.progress(score / 100)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.subheader("📈 Rating")

        if score >= 80:
            st.success(
                "Excellent Resume 🚀"
            )

        elif score >= 60:
            st.warning(
                "Good Resume 👍"
            )

        else:
            st.error(
                "Needs Improvement ⚠️"
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    # -----------------------
    # SKILLS
    # -----------------------

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🚀 Skills Detected")

    if skills:

        skills_html = ""

        for skill in skills:

            skills_html += f"""
            <span class="skill-tag">
            {skill}
            </span>
            """

        st.markdown(
            skills_html,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "No Skills Found"
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------
    # RESUME PREVIEW
    # -----------------------

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("📄 Resume Preview")

    st.text_area(
        "",
        resume_text[:3000],
        height=300
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------
    # SUGGESTIONS
    # -----------------------

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("💡 Suggestions")

    if score < 60:

        st.write(
            "• Add more technical skills"
        )

        st.write(
            "• Add projects section"
        )

        st.write(
            "• Include measurable achievements"
        )

    elif score < 80:

        st.write(
            "• Add more relevant keywords"
        )

        st.write(
            "• Improve project descriptions"
        )

    else:

        st.write(
            "• Resume is ATS Friendly"
        )

        st.write(
            "• Well Structured Resume"
        )

        st.write(
            "• Good Job!"
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------
    # DOWNLOAD REPORT
    # -----------------------

    report = f"""
Resume Analyzer Report

ATS Score: {score}

Skills:
{', '.join(skills)}

Resume Length:
{len(resume_text)} characters
"""

    st.download_button(
        "📥 Download Report",
        report,
        file_name="resume_report.txt"
    )

else:

    st.info(
        "Upload a Resume PDF to start analysis."
    )