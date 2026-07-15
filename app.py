import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

st.set_page_config(
    page_title="SOC Log Analysis Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ THEME ------------------

dark_mode = st.sidebar.toggle(
    "🌙 Dark Mode",
    value=True
)

if dark_mode:
    bg = "#0B1120"
    card = "#111827"
    text = "#FFFFFF"
    border = "#00FF99"
else:
    bg = "#F5F5F5"
    card = "#FFFFFF"
    text = "#000000"
    border = "#2563EB"

st.markdown(f"""
<style>

.stApp {{
    background-color:{bg};
}}

[data-testid="stSidebar"] {{
    background-color:{card};
}}

div[data-testid="metric-container"] {{
    background-color:{card};
    border:2px solid {border};
    padding:20px;
    border-radius:20px;
}}

h1,h2,h3,h4,h5 {{
    color:{border};
}}

</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------

st.markdown("""
<div style="
background:#111827;
padding:25px;
border-radius:25px;
text-align:center;
border:2px solid #00FF99;
">

<h1 style="color:#00FF99;">
🛡️ SOC LOG ANALYSIS DASHBOARD
</h1>

<h3 style="color:white;">
Real-Time Authentication Monitoring & Threat Investigation
</h3>

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🛡️ SOC Dashboard")
st.sidebar.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

uploaded_file = st.sidebar.file_uploader(
    "Upload Authentication Dataset",
    type=["csv"]
)
page = st.sidebar.selectbox(
    "Navigation",
    [
        "🏠 Home",
        "📂 Dataset",
        "📊 Dashboard",
        "📈 Visualizations",
        "🚨 Threat Investigation",
        "🔐 Security Analytics",
        "📑 Incident Report"
    ]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    df["Date"] = df["timestamp"].dt.date
    df["Hour"] = df["timestamp"].dt.hour
    df["Month"] = df["timestamp"].dt.month

    total_logs = len(df)
    successful = len(df[df["success"] == True])
    failed = len(df[df["success"] == False])
    suspicious = len(
        df[df["suspicious_activity"] == True]
    )
    blocked = len(df[df["blocked"] == True])

    # ---------------- HOME ----------------

    if page == "🏠 Home":

        st.info(
            "👈 Please select a module from the sidebar to begin analysis."
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "📄 Total Logs",
            total_logs
        )

        c2.metric(
            "❌ Failed Logins",
            failed
        )

        c3.metric(
            "🚨 Suspicious",
            suspicious
        )

        c4.metric(
            "🚫 Blocked",
            blocked
        )

        st.markdown("## 🛡️ SOC Features & Capabilities")
        a,b,c = st.columns(3)
        d, e, f = st.columns(3)

        with a:
            st.success("""
📂 Dataset Analysis

• Upload Logs
• Missing Values
• Dataset Information
• Log Inspection
""")

        with b:
            st.success("""
📊 Dashboard Monitoring

• Total Events
• Failed Logins
• Suspicious Events
• Blocked Accounts
""")

        with c:
            st.success("""
📈 Security Visualizations

• Threat Levels
• Top Users
• Top IPs
• Login Trends
""")

        with d:
            st.success("""
🚨 Threat Investigation

• Brute Force Detection
• Failed Logins
• Suspicious Accounts
• Blocked Users
""")

        with e:
            st.success("""
🔐 Security Analytics

• MFA Monitoring
• Admin Users
• Privilege Levels
• Security Metrics
""")

        with f:
            st.success("""
📑 Incident Reporting

• Generate Reports
• Download Reports
• Recommendations
• Incident Summary
""")

    elif page == "📂 Dataset":

        st.header("📂 Dataset Information")

        st.subheader("First 5 Rows")
        st.dataframe(df.head())

        st.subheader("Last 5 Rows")
        st.dataframe(df.tail())

        st.write(
            "Rows:",
            df.shape[0]
        )

        st.write(
            "Columns:",
            df.shape[1]
        )

        st.subheader("Column Names")
        st.write(df.columns.tolist())

        st.subheader("Missing Values")
        st.dataframe(
            df.isnull().sum()
        )

        st.subheader("Data Types")
        st.dataframe(
            df.dtypes
        )

    elif page == "📊 Dashboard":

        st.header("📊 Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Logs",
            total_logs
        )

        c2.metric(
            "Success",
            successful
        )

        c3.metric(
            "Failed",
            failed
        )

        c4.metric(
            "Suspicious",
            suspicious
        )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            fig = px.pie(
                df,
                names="login_method",
                title="Login Methods"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col2:

            fig = px.bar(
                df["threat_level"]
                .value_counts(),
                title="Threat Levels"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    elif page == "📈 Visualizations":

        st.header("📈 Security Visualizations")

        fig = px.bar(
            df["username"]
            .value_counts()
            .head(10),
            title="Top Users"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        fig = px.bar(
            df["ip_address"]
            .value_counts()
            .head(10),
            title="Top IP Addresses"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        fig = px.histogram(
            df,
            x="failed_attempts",
            title="Failed Attempts"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif page == "🚨 Threat Investigation":

        st.header("🚨 Threat Investigation")

        st.subheader(
            "Suspicious Activities"
        )

        st.dataframe(
            df[
                df[
                    "suspicious_activity"
                ] == True
            ]
        )

        st.subheader(
            "Blocked Accounts"
        )

        st.dataframe(
            df[
                df["blocked"] == True
            ]
        )

        st.subheader(
            "Brute Force Detection"
        )

        brute = df[
            df[
                "failed_attempts"
            ] > 5
        ]

        st.dataframe(brute)

    elif page == "🔐 Security Analytics":

        st.header(
            "🔐 Security Analytics"
        )

        st.subheader(
            "Admin Accounts"
        )

        admin = df[
            df["role"]
            .astype(str)
            .str.contains(
                "admin",
                case=False,
                na=False
            )
        ]

        st.dataframe(admin)

        st.subheader(
            "High Privilege Accounts"
        )

        high = df.sort_values(
            by="privilege_level",
            ascending=False
        )

        st.dataframe(
            high[
                [
                    "username",
                    "role",
                    "privilege_level"
                ]
            ].head(20)
        )

        fig = px.pie(
            df,
            names="mfa_enabled",
            title="MFA Enabled"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif page == "📑 Incident Report":

        st.header(
            "📑 Incident Report"
        )

        report = f"""
SOC INCIDENT REPORT

Total Events : {total_logs}

Successful Logins : {successful}

Failed Logins : {failed}

Suspicious Activities : {suspicious}

Blocked Accounts : {blocked}

Recommendations

1. Enable MFA
2. Investigate suspicious accounts
3. Monitor privileged users
4. Block malicious IPs
5. Review login failures
"""

        st.text(report)

        st.download_button(
            "Download Report",
            report,
            file_name="SOC_Report.txt"
        )

else:
    st.info(
        "📂 Upload a CSV file to begin analysis."
    )

st.markdown("---")

st.markdown("""
<center>
Developed by Dhiman Sharma<br>
SOC Log Analysis & Incident Investigation Project
</center>
""", unsafe_allow_html=True)