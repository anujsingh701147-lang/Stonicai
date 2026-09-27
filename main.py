import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
import json

# ---------------------------------------------------------
# PAGE CONFIGURATION (PITCH BLACK LANDSCAPE THEME)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Stonic AI — Multi-Dashboard",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Pitch Black CSS Styling
st.markdown("""
    <style>
    /* Global Pitch Black Styling */
    .stApp {
        background-color: #030407;
        color: #e2e8f0;
    }
    
    /* Header Card */
    .dashboard-header {
        background: #0d111a;
        border-left: 4px solid #00f3ff;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
    }
    
    /* Section Boxes */
    .glass-box {
        background: #0b0f19;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
    }

    /* Custom Terminal Box */
    .terminal-box {
        background-color: #050907;
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 8px;
        padding: 12px;
        font-family: 'Courier New', Courier, monospace;
        color: #10b981;
        font-size: 12px;
        height: 140px;
        overflow-y: auto;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER SECTION
# ---------------------------------------------------------
st.markdown("""
    <div class="dashboard-header">
        <h1 style="margin:0; font-size: 26px; color: #ffffff;">STONIC <span style="color: #00f3ff; text-shadow: 0 0 10px rgba(0,243,255,0.5);">AI LABS</span></h1>
        <p style="margin:0; font-size: 12px; color: #94a3b8; font-family: monospace;">FULL PYTHON MULTI-DASHBOARD SYSTEM ENGINE</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR CONTROLS
# ---------------------------------------------------------
st.sidebar.markdown("<h2 style='color: #00f3ff;'>⚡ Control Panel</h2>", unsafe_allow_html=True)
global_task = st.sidebar.button("🚀 Assign Global Task", use_container_width=True)
theme_color = st.sidebar.selectbox("Dashboard Accent Theme", ["Electric Cyan", "Neon Violet", "Emerald Green"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 System Status")
st.sidebar.markdown("• **Core Engine:** `Running`\n• **Connected Nodes:** `1,024`\n• **Latency:** `12ms`")

# ---------------------------------------------------------
# DASHBOARD LAYOUT (2 COLUMNS - LANDSCAPE)
# ---------------------------------------------------------
col_left, col_right = st.columns([7, 5])

# --- DASHBOARD 01: AGENT TOWN MAP (LEFT COLUMN) ---
with col_left:
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#00f3ff; font-size: 16px; margin-bottom: 10px;'>[DASHBOARD 01] Agent Town 2D Map</h3>", unsafe_allow_html=True)
    
    # 2D Interactive Office Canvas Engine using HTML5/JS embedded in Python
    task_script = "true" if global_task else "false"
    
    canvas_html = f"""
    <div style="background: #070a12; border: 1px solid rgba(0, 243, 255, 0.2); border-radius: 10px; overflow: hidden;">
        <canvas id="townCanvas" width="600" height="340" style="width:100%; height:340px;"></canvas>
    </div>
    <script>
    const canvas = document.getElementById("townCanvas");
    const ctx = canvas.getContext("2d");
    
    const LOCS = {{
        DESK_A: {{ x: 90, y: 80, name: "Alice's Desk" }},
        SERVER: {{ x: 450, y: 80, name: "Server Center" }},
        MEETING: {{ x: 450, y: 250, name: "Conference Room" }},
        BREAK: {{ x: 90, y: 250, name: "Coffee Lounge" }}
    }};

    const agents = [
        {{ name: "Alice", color: "#00f3ff", x: 90, y: 80, target: LOCS.DESK_A, speed: 1.2, thought: "Refactoring Code", walk: 0 }},
        {{ name: "Bob", color: "#ff0055", x: 220, y: 80, target: LOCS.SERVER, speed: 1.5, thought: "Checking Database", walk: 0 }},
        {{ name: "Carol", color: "#00ff88", x: 90, y: 180, target: LOCS.MEETING, speed: 1.1, thought: "Leading Meeting", walk: 0 }},
        {{ name: "Dave", color: "#fbbf24", x: 220, y: 180, target: LOCS.BREAK, speed: 1.0, thought: "Espresso Break ☕", walk: 0 }}
    ];

    if ({task_script}) {{
        agents.forEach(a => {{ a.target = LOCS.SERVER; a.thought = "⚡ Urgent Task!"; }});
    }}

    function drawRooms() {{
        ctx.fillStyle = "rgba(0, 243, 255, 0.05)"; ctx.fillRect(20, 20, 260, 140); ctx.strokeStyle = "rgba(0,243,255,0.3)"; ctx.strokeRect(20, 20, 260, 140);
        ctx.fillStyle = "rgba(255, 0, 85, 0.06)"; ctx.fillRect(320, 20, 240, 140); ctx.strokeStyle = "rgba(255,0,85,0.3)"; ctx.strokeRect(320, 20, 240, 140);
        ctx.fillStyle = "rgba(0, 255, 136, 0.05)"; ctx.fillRect(320, 180, 240, 140); ctx.strokeStyle = "rgba(0,255,136,0.3)"; ctx.strokeRect(320, 180, 240, 140);
        ctx.fillStyle = "rgba(251, 191, 36, 0.05)"; ctx.fillRect(20, 180, 260, 140); ctx.strokeStyle = "rgba(251,191,36,0.3)"; ctx.strokeRect(20, 180, 260, 140);
    }}

    function drawHuman(agent) {{
        ctx.save();
        ctx.translate(agent.x, agent.y);
        ctx.fillStyle = agent.color;
        ctx.beginPath(); ctx.arc(0, -14, 5, 0, Math.PI * 2); ctx.fill(); // Head
        ctx.fillRect(-4, -8, 8, 10); // Torso
        
        ctx.strokeStyle = agent.color; ctx.lineWidth = 2;
        const swing = agent.isMoving ? Math.sin(agent.walk) * 5 : 0;
        ctx.beginPath(); ctx.moveTo(-2, 2); ctx.lineTo(-2 + swing, 12); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(2, 2); ctx.lineTo(2 - swing, 12); ctx.stroke();
        ctx.restore();

        if(agent.thought) {{
            ctx.fillStyle = "#0d111a"; ctx.strokeStyle = agent.color; ctx.lineWidth = 1;
            ctx.fillRect(agent.x - 30, agent.y - 36, 60, 14);
            ctx.strokeRect(agent.x - 30, agent.y - 36, 60, 14);
            ctx.fillStyle = "#ffffff"; ctx.font = "8px monospace"; ctx.textAlign = "center";
            ctx.fillText(agent.thought, agent.x, agent.y - 26);
        }}
    }}

    function animate() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawRooms();
        agents.forEach(agent => {{
            const dx = agent.target.x - agent.x;
            const dy = agent.target.y - agent.y;
            const dist = Math.hypot(dx, dy);
            if (dist > 2) {{
                agent.x += (dx / dist) * agent.speed;
                agent.y += (dy / dist) * agent.speed;
                agent.isMoving = true; agent.walk += 0.2;
            }} else {{ agent.isMoving = false; }}
            drawHuman(agent);
        }});
        requestAnimationFrame(animate);
    }}
    animate();
    </script>
    """
    st.components.v1.html(canvas_html, height=350)
    
    # Status Cards Grid
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Alice", "Working", "Cyan Zone")
    a2.metric("Bob", "In Transit", "Magenta Zone")
    a3.metric("Carol", "Meeting", "Emerald Zone")
    a4.metric("Dave", "Break", "Amber Zone")
    st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD 02 & 03 (RIGHT COLUMN) ---
with col_right:
    # --- DASHBOARD 02: DEDICATED 3D GLOBE ---
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#a855f7; font-size: 16px; margin-bottom: 10px;'>[DASHBOARD 02] Global Net 3D Sphere</h3>", unsafe_allow_html=True)
    
    # Three.js Dedicated 3D Globe Render Component
    globe_html = """
    <div id="globeBox" style="width:100%; height:180px; background:#090614; border-radius:10px; overflow:hidden;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
    const box = document.getElementById("globeBox");
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, box.clientWidth / box.clientHeight, 0.1, 1000);
    camera.position.z = 3.5;
    
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(box.clientWidth, box.clientHeight);
    box.appendChild(renderer.domElement);
    
    const geometry = new THREE.SphereGeometry(1.2, 20, 20);
    const material = new THREE.MeshBasicMaterial({ color: 0xa855f7, wireframe: true });
    const globe = new THREE.Mesh(geometry, material);
    scene.add(globe);
    
    function animateGlobe() {
        requestAnimationFrame(animateGlobe);
        globe.rotation.y += 0.006;
        globe.rotation.x += 0.002;
        renderer.render(scene, camera);
    }
    animateGlobe();
    </script>
    """
    st.components.v1.html(globe_html, height=190)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- DASHBOARD 03: SYSTEM OPERATIONS & LOGS ---
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#10b981; font-size: 16px; margin-bottom: 10px;'>[DASHBOARD 03] System Operations</h3>", unsafe_allow_html=True)
    
    st.write("Core Neural Telemetry:")
    st.progress(42)
    st.write("Bandwidth Utilization:")
    st.progress(78)
    
    # Live Python Terminal Box
    curr_time = time.strftime("%H:%M:%S")
    st.markdown(f"""
        <div class="terminal-box">
            [{curr_time}] [PYTHON_CORE] Pitch Black Engine Online.<br>
            [{curr_time}] [DASHBOARD_01] Agent Town Canvas Mounted.<br>
            [{curr_time}] [DASHBOARD_02] 3D Wireframe Globe Matrix active.<br>
            [{curr_time}] [DASHBOARD_03] Telemetry stream operational.
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
