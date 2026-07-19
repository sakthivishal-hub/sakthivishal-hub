from datetime import datetime

svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="350">
    <rect width="1200" height="350" fill="#0d1117"/>
    <text x="40" y="60" fill="#58a6ff"
          font-size="32"
          font-family="Consolas">
        🤖 AI ENGINEER DASHBOARD
    </text>

    <text x="40" y="110"
          fill="white"
          font-size="22"
          font-family="Consolas">
        Name : Sakthivishal Thilagaraj
    </text>

    <text x="40" y="150"
          fill="#8b949e"
          font-size="18"
          font-family="Consolas">
        AI & Data Science Engineer
    </text>

    <text x="40" y="210"
          fill="#3fb950"
          font-size="18"
          font-family="Consolas">
        Last Updated :
        {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}
    </text>
</svg>
"""

with open("assets/dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("dashboard.svg generated")
