import streamlit as st
import random
import time
import os
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="TruthShield X - AI Fraud Detector", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

# --- Advanced Cyber Theme ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0a0a0a 0%, #001414 50%, #0a0a0a 100%);
        color: #00f0ff;
        overflow-x: hidden;
    }
    .stTextInput > div > div > input, 
    .stTextArea > div > textarea,
    .stSelectbox > div > div > select {
        background: rgba(0,0,0,0.6);
        border: 1px solid rgba(0,240,255,0.4);
        color: #00f0ff;
        border-radius: 8px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #00f0ff 0%, #0099cc 100%);
        color: #0a0a0a;
        border: none;
        font-weight: 700;
        box-shadow: 0 0 20px rgba(0,240,255,0.4);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(0,240,255,0.7);
    }
    h1, h2, h3 {
        text-shadow: 0 0 15px #00f0ff;
    }
    div[data-testid="stSidebar"] {
        background: rgba(10,10,10,0.9) !important;
        border-right: 1px solid rgba(0,240,255,0.2);
    }
    .cyber-card {
        background: rgba(0,0,0,0.6);
        border:1px solid rgba(0,240,255,0.3);
        border-radius:10px;
        padding:20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Save 3D HTML content ---
cyber_html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body, html { 
            margin: 0; 
            padding: 0; 
            width: 100%; 
            height: 100%; 
            overflow: hidden;
            background: transparent;
        }
        canvas { display: block; }
    </style>
</head>
<body>
    <canvas id="cyber-canvas"></canvas>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 300, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('cyber-canvas'), alpha: true, antialias: true });
        
        renderer.setSize(window.innerWidth, 300);
        renderer.setPixelRatio(window.devicePixelRatio);
        
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 700;
        const posArray = new Float32Array(particlesCount * 3);
        
        for (let i = 0; i < particlesCount * 3; i++) {
            posArray[i] = (Math.random() - 0.5) * 10;
        }
        
        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        
        const material = new THREE.PointsMaterial({
            size: 0.02,
            color: 0x00f0ff,
            transparent: true,
            opacity: 0.8
        });
        
        const particlesMesh = new THREE.Points(particlesGeometry, material);
        scene.add(particlesMesh);
        
        const shieldGeometry = new THREE.TorusGeometry(0.6, 0.15, 16, 100);
        const shieldMaterial = new THREE.MeshBasicMaterial({ color: 0x00f0ff, transparent: true, opacity: 0.3, wireframe: true });
        const shield = new THREE.Mesh(shieldGeometry, shieldMaterial);
        shield.position.z = -2;
        scene.add(shield);
        
        const shield2Geometry = new THREE.TorusGeometry(0.5, 0.08, 12, 80);
        const shield2Material = new THREE.MeshBasicMaterial({ color: 0x00cccc, transparent: true, opacity: 0.5, wireframe: true });
        const shield2 = new THREE.Mesh(shield2Geometry, shield2Material);
        shield2.position.z = -2;
        shield2.rotation.x = Math.PI / 3;
        scene.add(shield2);
        
        camera.position.z = 3;
        
        let mouseX = 0, mouseY = 0;
        
        document.addEventListener('mousemove', (e) => {
            mouseX = (e.clientX / window.innerWidth) * 2 - 1;
            mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
        });
        
        function animate() {
            requestAnimationFrame(animate);
            
            particlesMesh.rotation.x += 0.0005;
            particlesMesh.rotation.y += 0.0008;
            
            shield.rotation.x += 0.005;
            shield.rotation.y += 0.008;
            
            shield2.rotation.x -= 0.008;
            shield2.rotation.y += 0.005;
            
            particlesMesh.rotation.x += mouseY * 0.001;
            particlesMesh.rotation.y += mouseX * 0.001;
            
            renderer.render(scene, camera);
        }
        
        animate();
        
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / 300;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, 300);
        });
    </script>
</body>
</html>
"""

# --- Display 3D background ---
st.components.v1.html(cyber_html_content, height=300)

# --- Animated Cyber Header ---
st.markdown("""
    <div style="
        border: 2px solid #00f0ff;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 30px;
        background: rgba(0,240,255,0.05);
        box-shadow: 0 0 30px rgba(0,240,255,0.2);
        text-align: center;
        position: relative;
        z-index: 1;
    ">
        <h1 style="font-size: 3.5em; margin: 0;">🛡️ TruthShield X</h1>
        <p style="font-size: 1.2em; color: #a0ecff; margin: 10px 0 0;">AI-Powered Fraud Detection • Cyber Security Platform</p>
    </div>
""", unsafe_allow_html=True)

# --- Navigation ---
st.sidebar.markdown("# TruthShield X")
page = st.sidebar.radio("Navigation", ["🏠 Home", "🔍 Scanner", "📊 Analytics", "⚙️ Settings"])

# --- Fake AI Analysis Function ---
def analyze_content(content, scan_type):
    """Mock AI analysis for demonstration"""
    risk_score = random.randint(0, 100)
    is_fraud = risk_score > 50
    confidence = random.uniform(0.75, 0.99)
    
    explanations = {
        "message": "AI detected suspicious patterns common in message scams.",
        "email": "Content exhibits characteristics of phishing emails.",
        "url": "URL analysis indicates potential malicious content.",
        "image": "Media analysis suggests potential deepfake characteristics.",
        "job": "Job posting contains red flags for employment scams.",
        "investment": "Investment opportunity shows signs of fraudulent schemes.",
        "romance": "Conversation patterns align with romance scam tactics.",
        "payment": "Payment request exhibits suspicious behavior."
    }
    
    indicators = [
        "Unusual urgency in language",
        "Request for personal/financial information",
        "Too-good-to-be-true promises",
        "Unverified sender/source",
        "Poor grammar or spelling"
    ]
    
    recommendations = [
        "Do not click any links or download attachments",
        "Report to relevant authorities/platform",
        "Block sender/caller if applicable",
        "Monitor financial accounts for suspicious activity",
        "Educate yourself on common scam tactics"
    ]
    
    num_ind = random.randint(2, 4)
    num_rec = random.randint(2, 4)
    
    return {
        "score": risk_score,
        "is_fraud": is_fraud,
        "confidence": confidence,
        "explanation": explanations.get(scan_type, "AI analysis complete."),
        "indicators": random.sample(indicators, num_ind),
        "recommendations": random.sample(recommendations, num_rec)
    }

# --- HOME PAGE ---
if page == "🏠 Home":
    st.header("Welcome to the Future of Fraud Detection")
    st.markdown("<p style='color: #a0ecff; font-size:1.1em;'>Protect yourself with AI-powered threat detection across multiple vectors.</p>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        st.metric(label="🚀 Scans Today", value="328")
    with col2:
        st.metric(label="⚠️ Threats Blocked", value="47")
    with col3:
        st.metric(label="✅ Safe Checks", value="281")
    with col4:
        st.metric(label="📈 Accuracy", value="98.5%")
    
    st.divider()
    
    colL, colR = st.columns([1.5, 1])
    with colL:
        st.subheader("Key Features")
        features = [
            "📱 Message Scam Detection", "📧 Email Phishing Detection",
            "🔗 URL Analysis", "🖼️ Deepfake Detection",
            "📋 Fake Job Scam Detection", "💰 Investment Fraud Detection",
            "❤️ Romance Scam Detection", "💳 Payment Fraud Detection"
        ]
        for feat in features:
            st.markdown(f"- {feat}")
        st.info("Go to the Scanner page to start detecting fraud!")
        
    with colR:
        st.subheader("System Status")
        st.markdown("""
            <div class="cyber-card">
                <p>🛡️ Shield Module: <span style='color: #22ff22;'>Online</span></p>
                <p>⚡ AI Engine: <span style='color: #22ff22;'>Active</span></p>
                <p>🔒 Connection: <span style='color: #22ff22;'>Secure</span></p>
                <p>📶 Network: <span style='color: #22ff22;'>Optimal</span></p>
            </div>
        """, unsafe_allow_html=True)

# --- SCANNER PAGE ---
elif page == "🔍 Scanner":
    st.header("🔍 Threat Scanner")
    
    # Module selection with icons
    scan_modules = {
        "📱 Message Scam": "message",
        "📧 Email Phishing": "email",
        "🔗 URL Analysis": "url",
        "🖼️ Deepfake Detection": "image",
        "📋 Fake Job Scam": "job",
        "💰 Investment Fraud": "investment",
        "❤️ Romance Scam": "romance",
        "💳 Payment Fraud": "payment"
    }
    
    selected_module = st.selectbox("Select detection module:", list(scan_modules.keys()))
    selected_type = scan_modules[selected_module]
    
    input_data = None
    
    # --- Input based on module type ---
    if selected_type == "image":
        st.subheader("Upload Image for Deepfake Detection")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            input_data = uploaded_file.name  # Just using filename for mock analysis
    else:
        st.subheader("Enter Content")
        input_data = st.text_area("Enter content for analysis:", height=160, placeholder="Paste your message, email, URL, etc. here...")
    
    col1, col2 = st.columns([1,2])
    with col1:
        scan_button = st.button("🚀 Start Analysis")
    
    if scan_button:
        if (selected_type == "image" and input_data) or (selected_type != "image" and input_data):
            with st.spinner("Initializing AI scan..."):
                time.sleep(1.5)
                
                result = analyze_content(input_data, selected_type)
                
                st.divider()
                st.subheader("Analysis Complete")
                
                colR1, colR2 = st.columns([1,1])
                with colR1:
                    st.metric("Risk Score", f"{result['score']}%")
                    st.metric("Confidence", f"{round(result['confidence']*100)}%")
                    
                    if result['is_fraud']:
                        st.error("⚠️ FRAUD DETECTED!")
                    else:
                        st.success("✅ CONTENT SAFE")
                
                with colR2:
                    st.subheader("AI Explanation")
                    st.write(result['explanation'])
                
                st.subheader("🚩 Red Flags Identified")
                for ind in result['indicators']:
                    st.write(f"• {ind}")
                
                st.subheader("📋 Recommendations")
                for rec in result['recommendations']:
                    st.write(f"→ {rec}")
        else:
            if selected_type == "image":
                st.warning("Please upload an image first!")
            else:
                st.warning("Please enter some content to analyze!")

# --- ANALYTICS PAGE ---
elif page == "📊 Analytics":
    st.header("📊 Analytics Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Scans", "1,120", "+12%")
    with col2:
        st.metric("Fraud Cases", "260", "-3%")
    with col3:
        st.metric("Avg. Response Time", "1.2s", "-0.2s")
    with col4:
        st.metric("Active Users", "450", "+8%")
        
    st.divider()
    st.subheader("Recent Scan History")
    
    history = [
        {"type": "📧 Email Phishing", "date": "Today, 14:23", "status": "Fraud", "risk": 87},
        {"type": "📱 Message Scam", "date": "Today, 11:15", "status": "Safe", "risk": 12},
        {"type": "🖼️ Deepfake", "date": "Yesterday, 19:42", "status": "Fraud", "risk": 74},
        {"type": "💳 Payment", "date": "Yesterday, 16:05", "status": "Safe", "risk": 23},
        {"type": "🔗 URL Analysis", "date": "2 days ago", "status": "Safe", "risk": 31}
    ]
    
    for scan in history:
        if scan['status'] == "Fraud":
            st.error(f"⚠️ {scan['type']} | {scan['date']} | Risk: {scan['risk']}%")
        else:
            st.success(f"✅ {scan['type']} | {scan['date']} | Risk: {scan['risk']}%")

# --- SETTINGS PAGE ---
elif page == "⚙️ Settings":
    st.header("⚙️ Settings")
    
    st.subheader("API Configuration")
    api_key_input = st.text_input("Anthropic Claude API Key (optional)", type="password")
    
    if st.button("💾 Save Configuration"):
        st.success("Settings saved!")
        
    st.divider()
    st.subheader("Theme & Display")
    dark_mode = st.checkbox("Cyber Dark Theme", value=True)
    
    st.divider()
    st.subheader("User Preferences")
    auto_save = st.checkbox("Auto-save scan history", value=True)
    email_alerts = st.checkbox("Email notifications for high-risk scans")
    
    st.divider()
    st.info("TruthShield X v1.0 • Built with Streamlit, Three.js & Python")

# --- Sidebar Footer ---
st.sidebar.divider()
st.sidebar.markdown("""
    <div style="text-align: center; color: #a0ecff;">
        <p>TruthShield X</p>
        <p>© 2026 Cyber Security Platform</p>
    </div>
""", unsafe_allow_html=True)
