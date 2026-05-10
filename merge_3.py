import os
import re

base_dir = r"c:\Users\amitb\OneDrive\Desktop\Portfolio"

def read(f):
    with open(os.path.join(base_dir, f), 'r', encoding='utf-8') as file:
        return file.read()

# Base file is home.html
home = read("home.html")
about = read("about.html")
skill = read("skill.html")
education = read("education.html")

def extract_body(html):
    m = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    return m.group(1) if m else ""

def extract_script(html):
    m = re.findall(r'<script.*?>(.*?)</script>', html, re.DOTALL)
    return "\n".join(m)

def strip_script(html):
    return re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)

about_body = strip_script(extract_body(about))
skill_body = strip_script(extract_body(skill))
edu_body = strip_script(extract_body(education))

skill_script = extract_script(skill)
edu_script = extract_script(education)

# Fix conflicts in skill
skill_body = skill_body.replace('class="logo"', 'class="skill-logo"')
skill_body = skill_body.replace('from-left', 'skill-from-left').replace('from-right', 'skill-from-right')

# Fix conflicts in edu
edu_body = edu_body.replace('from-left', 'edu-from-left').replace('from-right', 'edu-from-right')

scoped_css = """
/* ======= ABOUT.HTML CSS (SCOPED) ======= */
#about-wrapper {
    background: #f4f4f4;
    font-family: 'Poppins', sans-serif;
    width: 100%;
    overflow-x: hidden;
    color: #444;
}
#about-wrapper .main { display: flex; flex-direction: column; gap: 60px; }
#about-wrapper .about { display: flex; align-items: center; justify-content: center; padding: 80px 100px; gap: 80px; }
#about-wrapper .about-left img { width: 320px; height: auto; }
#about-wrapper .about-right { max-width: 600px; margin-left: 70px; }
#about-wrapper .about-title { font-size: 40px; font-weight: 700; margin-bottom: 30px; display: flex; align-items: center; gap: 10px; color: #000; }
#about-wrapper .about-title span { color: #facc15; }
#about-wrapper .about-text { color: #444; line-height: 1.7; margin-bottom: 20px; }
#about-wrapper .highlight { font-weight: 600; margin-top: 25px; margin-bottom: 10px; color: #000; }

@keyframes slideInRightAbout { from { opacity: 0; transform: translateX(100px); } to { opacity: 1; transform: translateX(0); } }

#about-wrapper .about-right h1, #about-wrapper .about-right p, #about-wrapper .about-right .final-note { opacity: 0; animation: slideInRightAbout 0.8s ease-out forwards; }
#about-wrapper .about-right h1 { animation-delay: 0.2s; }
#about-wrapper .about-right p:nth-of-type(1) { animation-delay: 0.4s; }
#about-wrapper .about-right p:nth-of-type(2) { animation-delay: 0.6s; }
#about-wrapper .about-right p:nth-of-type(3) { animation-delay: 0.8s; }
#about-wrapper .about-right p:nth-of-type(4) { animation-delay: 1.0s; }
#about-wrapper .about-right p:nth-of-type(5) { animation-delay: 1.2s; }
#about-wrapper .about-right .final-note { animation-delay: 1.4s; color: #333; font-weight: 600; }
#about-wrapper .final-line { text-align: center; font-size: 20px; font-weight: 600; padding: 40px 20px 80px; color: #333; }

/* ======= SKILLS.HTML CSS (SCOPED) ======= */
#skills-wrapper { background:linear-gradient(135deg,#f5f5f5,#eaeaea); font-family:'Sora',sans-serif; width: 100%; display: block; overflow-x: hidden; }
#skills-wrapper .skills{ padding:70px 100px; }
#skills-wrapper .skills-title{ text-align:center; font-size:42px; font-weight:700; margin-bottom:60px; color: #000; }
#skills-wrapper .skills-title span{ color:#eab308; }
#skills-wrapper .skills-container{ max-width:1000px; margin:auto; display:grid; grid-template-columns:1fr 1fr; gap:30px 40px; }
#skills-wrapper .skill-card{ background:#1b1b2f; color:white; padding:18px 20px; border-radius:18px; box-shadow:0 10px 25px rgba(0,0,0,0.15); opacity:0; transition:all 0.6s ease; }
#skills-wrapper .skill-from-left{ transform:translateX(-60px); }
#skills-wrapper .skill-from-right{ transform:translateX(60px); }
#skills-wrapper .show{ opacity:1; transform:translateX(0); }
#skills-wrapper .skill-top{ display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
#skills-wrapper .skill-left{ display:flex; align-items:center; gap:12px; }
#skills-wrapper .skill-logo{ width:24px; }
#skills-wrapper .skill-logo img{ width:100%; }
#skills-wrapper .skill-name{ font-size:17px; font-weight:600; }
#skills-wrapper .skill-percent{ font-size:15px; font-weight:600; }
#skills-wrapper .bar{ width:100%; height:10px; background:#d1d5db; border-radius:10px; overflow:hidden; }
#skills-wrapper .bar-fill{ height:100%; width:0; background:#facc15; border-radius:10px; transition:width 1s ease; }

/* ======= EDUCATION.HTML CSS (SCOPED) ======= */
#edu-wrapper { background:#000; font-family:'Outfit',sans-serif; width: 100%; display: block; overflow-x: hidden; }
#edu-wrapper .edu-section{ padding:70px 100px; background: radial-gradient(circle at 20% 30%, rgba(65,105,225,0.25), transparent 40%), radial-gradient(circle at 80% 70%, rgba(0,0,0,0.8), transparent 50%), linear-gradient(135deg,#000000,#020c2b,#0a1f5c); opacity:0; transform:translateY(60px); transition:all 0.8s ease; }
#edu-wrapper .edu-section.show{ opacity:1; transform:translateY(0); }
#edu-wrapper .edu-title{ text-align:center; font-size:48px; font-weight:800; color:white; margin-bottom:60px; }
#edu-wrapper .edu-title span{ color:#facc15; }
#edu-wrapper .edu-container{ max-width:1100px; margin:auto; display:grid; grid-template-columns:1fr 1fr; gap:45px; }
#edu-wrapper .column-title{ font-size:34px; font-weight:800; color:white; margin-bottom:25px; }
#edu-wrapper .edu-card{ background:rgba(30,30,30,0.95); padding:25px 28px; border-radius:8px; margin-bottom:20px; box-shadow: 0 12px 30px rgba(0,0,0,0.6), 0 0 15px rgba(65,105,225,0.15); opacity:0; transition:all 0.7s ease; }
#edu-wrapper .edu-from-left{ transform:translateX(-80px); }
#edu-wrapper .edu-from-right{ transform:translateX(80px); }
#edu-wrapper .edu-card.show{ opacity:1; transform:translateX(0); }
#edu-wrapper .edu-card h3{ color:#ffd966; font-size:22px; font-weight:700; margin-bottom:8px; }
#edu-wrapper .year{ color:#facc15; font-size:16px; font-weight:600; margin-bottom:6px; }
#edu-wrapper .degree{ font-weight:600; color:white; margin-bottom:5px; }
#edu-wrapper .edu-card p{ color:#ddd; font-size:14px; }
"""

# Inject CSS into home
merge = home.replace('</style>', scoped_css + '\n</style>')

# Replace Nav links
merge = merge.replace('href="about.html"', 'href="#about-wrapper"')
merge = merge.replace('href="skill.html"', 'href="#skills-wrapper"')
merge = merge.replace('href="education.html"', 'href="#edu-wrapper"')

# Build full body block
new_html = f'''
<!-- ABOUT SECTION -->
<div id="about-wrapper">
{about_body}
</div>

<!-- SKILLS SECTION -->
<div id="skills-wrapper">
{skill_body}
</div>

<!-- EDUCATION SECTION -->
<div id="edu-wrapper">
{edu_body}
</div>
'''

new_scripts = f'''
// SKILL SCRIPTS
{skill_script}

// EDU SCRIPTS
{edu_script}
'''

# Inject Body
merge = merge.replace('<script src="script.js"></script>', new_html + '\n<script src="script.js"></script>')

# Inject scripts
merge = merge.replace('</body>', '<script>\n' + new_scripts + '\n</script>\n</body>')

with open(os.path.join(base_dir, 'merge.html'), 'w', encoding='utf-8') as f:
    f.write(merge)

print("Successfully created merge.html with About, Skills, and Education perfectly inserted!")
