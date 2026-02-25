import streamlit as st
from utils.gemini_helper import analyze_image
from utils.prompts import material_prompt, documentation_prompt, bridge_prompt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Spacer
from reportlab.platypus import Preformatted
from reportlab.platypus import Image as RLImage
from reportlab.lib.units import inch
import tempfile

st.set_page_config(page_title="Civil Engineering Insight Studio", layout="wide")

st.title("🏗️ Civil Engineering Insight Studio")
st.markdown("AI-powered analysis of civil engineering structures")

scenario = st.selectbox(
    "Select Scenario",
    [
        "Material Identification",
        "Project Documentation",
        "Bridge Structural Analysis"
    ]
)

uploaded_file = st.file_uploader("Upload Construction Image", type=["jpg", "jpeg", "png"])

if uploaded_file:

    image_bytes = uploaded_file.read()
    st.image(image_bytes, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Image"):

        with st.spinner("Analyzing with Gemini Vision..."):

            if scenario == "Material Identification":
                prompt = material_prompt()
            elif scenario == "Project Documentation":
                prompt = documentation_prompt()
            else:
                prompt = bridge_prompt()

            result = analyze_image(image_bytes, prompt)

        st.subheader("🔍 AI Analysis Result")
        st.text_area("Output", result, height=300)

        # Generate PDF Report
        if st.button("Download PDF Report"):

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            doc = SimpleDocTemplate(temp_file.name)
            styles = getSampleStyleSheet()
            elements = []

            elements.append(Paragraph("Civil Engineering Insight Report", styles["Heading1"]))
            elements.append(Spacer(1, 12))
            elements.append(Preformatted(result, styles["Normal"]))

            doc.build(elements)

            with open(temp_file.name, "rb") as f:
                st.download_button(
                    label="Download Report",
                    data=f,
                    file_name="civil_engineering_report.pdf",
                    mime="application/pdf"
                )
