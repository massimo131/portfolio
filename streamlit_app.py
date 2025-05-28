import streamlit as st
from PIL import Image

st.set_page_config(page_title="Nimesh Wankhede | Data Science Portfolio", layout="wide")

# Sidebar navigation
st.sidebar.title("📂 Menu")
page = st.sidebar.radio("Navigate", ["Home", "About", "Experience", "Projects", "Contact"])

# ---- HOME ----
if page == "Home":
    st.title("👋 Hi, I'm Nimesh Wankhede")
    st.subheader("Data Scientist | AI/ML Developer")
    st.markdown("""
    Welcome to my portfolio! I’m a Master’s graduate in Data Science from the University of the Pacific, 
    passionate about building AI driven systems for real world impact. I have hands-on experience machine learning pipelines, intelligent agents and full-stack web apps based on Python.
    """)

# ---- ABOUT ----
elif page == "About":
    st.header("📘 About Me")
    st.markdown("""
    I specialize in data engineering, machine learning and backend development. I’ve interned at **Zof AI**, where I created AI agents for automated software testing 
    and log analysis, and at **V4U Technologies**, where I built marketing analytics solutions using predictive modeling and segmentation.

    My work includes optimizing system reliability, parsing and classifying large-scale logs. I have also built full-stack solutions like **MealMind**, a geolocation-based food recommendation engine.
    
    I enjoy solving challenges at the intersection of **AI**, **data infrastructure**, and **automation**.
    """)

# ---- EXPERIENCE ----
elif page == "Experience":
    st.header("💼 Professional Experience")

    st.subheader("ML Intern – Zof AI (May 2025 – Present)")
    st.write("""
    - Created AI agents that autonomously generate, execute and validate software test cases.
    - Integrated reinforcement learning and predictive modeling to enable agents to adapt strategies over time.
    - Parsed and analyzed 20K+ structured and unstructured log files using NLP techniques to identify system anomalies and optimize performance.
    """)

    st.subheader("Data Analyst Intern – V4U Technologies (Apr 2022 – Oct 2022)")
    st.write("""
    - Tracked marketing KPIs and conducted A/B testing, improving conversion rates by 15%.
    - Used decision trees to predict churn and performed customer segmentation using K-Means and RFM with over 85% accuracy.
    - Developed interactive Tableau dashboards for ROI analysis and campaign monitoring.
    """)

    st.subheader("Programmer – Beyond Alliance (Oct 2021 – Apr 2022)")
    st.write("""
    - Refactored automation code to enhance maintainability and reduce errors by 40%.
    - Delivered production-grade automation with zero known failures.
    """)

# ---- PROJECTS ----
elif page == "Projects":
    st.header("🛠️ Featured Projects")

    st.subheader("🚗 Lane Keeping with CARLA Simulator")
    st.write("""
    Designed a TimeDistributed CNN-GRU model for lane-following in a simulated self-driving environment. Used over 1.2M frames across 4 development stages to improve generalization and control accuracy.
    """)

    st.subheader("🍽️ MealMind – API-driven Food App")
    st.write("""
    Full-stack project using FastAPI, Jinja2, and Geopy. Integrated APIs to suggest meals and restaurants based on user location. Features delivery estimates, recipes, and responsive UI.
    """)

    st.subheader("✈️ Airline Passenger Satisfaction Model")
    st.write("""
    Constructed a predictive pipeline using SelectKBest and Random Forests, achieving 94% accuracy on 100K+ records. Used for customer experience analytics in airline services.
    """)

# ---- CONTACT ----
elif page == "Contact":
    st.header("📬 Contact")
    st.markdown("""
    - 📧 Email: [nimeshw8@gmail.com](mailto:nimeshw8@gmail.com)  
    - 💼 LinkedIn: [linkedin.com/in/nimesh13](https://www.linkedin.com/in/nimesh13/)  
    - 🐱 GitHub: [github.com/massimo131](https://github.com/massimo131)  
    """)
    st.write("Let’s connect! I’m actively looking for data-focused roles in AI/ML, software testing, or data engineering.")
