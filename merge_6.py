import os
import re

base_dir = r"c:\Users\amitb\OneDrive\Desktop\Portfolio"

def read(f):
    with open(os.path.join(base_dir, f), 'r', encoding='utf-8') as file:
        return file.read()

# Read all files
home = read("home.html")
about = read("about.html")
skill = read("skill.html")
education = read("education.html")
projects = read("projects.html")
experience = read("experience.html")
certification = read("certification.html")

def extract_body(html):
    m = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    return m.group(1) if m else ""

def extract_script(html):
    m = re.findall(r'<script.*?>(.*?)</script>', html, re.DOTALL)
    return "\n".join(m)

def strip_script(html):
    return re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)

# Extract bodies
about_body = strip_script(extract_body(about))
skill_body = strip_script(extract_body(skill))
edu_body = strip_script(extract_body(education))
proj_body = strip_script(extract_body(projects))
exp_body = strip_script(extract_body(experience))
cert_body = strip_script(extract_body(certification))

# Extract scripts
skill_script = extract_script(skill)
edu_script = extract_script(education)
proj_script = extract_script(projects)
cert_script = extract_script(certification)
exp_script = extract_script(experience)

# Fix conflicts in skill
skill_body = skill_body.replace('class="logo"', 'class="skill-logo"')
skill_body = skill_body.replace('from-left', 'skill-from-left').replace('from-right', 'skill-from-right')

# Fix conflicts in edu
edu_body = edu_body.replace('from-left', 'edu-from-left').replace('from-right', 'edu-from-right')

# Fix conflicts in proj
proj_body = proj_body.replace('class="card"', 'class="proj-card"')
proj_body = proj_body.replace('class="content"', 'class="proj-content"')
proj_body = proj_body.replace('class="btn"', 'class="proj-btn"')
proj_body = proj_body.replace('class="arrow left"', 'class="proj-arrow left"')
proj_body = proj_body.replace('class="arrow right"', 'class="proj-arrow right"')
proj_script = proj_script.replace('.card', '.proj-card')

# Fix conflicts in cert
cert_body = cert_body.replace('class="container"', 'class="cert-container"')

# Scoped CSS for all sections
scoped_css = """
/* ======= ABOUT.HTML CSS (SCOPED) ======= */
#about-wrapper { background: #f4f4f4; font-family: 'Poppins', sans-serif; width: 100%; overflow-x: hidden; color: #444; display:block; }
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

/* ======= PROJECTS.HTML CSS (SCOPED) ======= */
#projects-wrapper { background: #f5f5f5; overflow-x: hidden; font-family: 'Poppins', sans-serif; width:100%; display:block;}
#projects-wrapper .projects { padding: 80px 0; text-align: center; }
#projects-wrapper .title-wrapper { display: flex; align-items: center; justify-content: center; gap: 20px; margin-bottom: 15px; }
#projects-wrapper .brain-logo { width: 65px; height: 65px; fill: #333; }
#projects-wrapper .projects-title { font-size: 54px; font-weight: 800; color: #f4b400; line-height: 1; }
#projects-wrapper .projects-title span { color: #000000; }
#projects-wrapper .projects-desc { max-width: 950px; margin: auto; font-size: 18px; color: #555; line-height: 1.7; margin-bottom: 60px; }
#projects-wrapper .carousel { width: 1050px; margin: auto; position: relative; }
#projects-wrapper .carousel-container { overflow: hidden; width: 100%; padding: 40px 10px; }
#projects-wrapper .track { display: flex; gap: 30px; transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); }
#projects-wrapper .proj-card { width: 320px; height: 540px; background: #fff; border-radius: 35px; overflow: hidden; flex-shrink: 0; display: flex; flex-direction: column; position: relative; border: 2px solid #e2e8f0; box-shadow: 0 0 25px rgba(0, 0, 0, 0.1); animation: popIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) backwards; transition: transform 0.5s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.5s ease, border-color 0.5s ease; }
#projects-wrapper .proj-card:nth-child(1) { animation-delay: 0.1s; }
#projects-wrapper .proj-card:nth-child(2) { animation-delay: 0.2s; }
#projects-wrapper .proj-card:nth-child(3) { animation-delay: 0.3s; }
#projects-wrapper .proj-card:nth-child(4) { animation-delay: 0.4s; }
#projects-wrapper .proj-card:nth-child(5) { animation-delay: 0.5s; }
#projects-wrapper .proj-card:hover { transform: translateY(-10px) scale(1); box-shadow: 0 0 35px rgba(244, 180, 0, 0.25); border-color: #facc15; }
#projects-wrapper .card-img { width: 100%; height: 50%; overflow: hidden; background: #eee; }
#projects-wrapper .card-img img { width: 100%; height: 100%; object-fit: cover; display: block; }
#projects-wrapper .proj-content { width: 100%; height: 50%; padding: 25px; display: flex; flex-direction: column; justify-content: space-between; text-align: center; }
#projects-wrapper .proj-card h3 { font-size: 19px; margin-bottom: 8px; color: #1a1a1a; font-weight: 700; }
#projects-wrapper .proj-card p { font-size: 13.5px; color: #666; line-height: 1.5; }
#projects-wrapper .btn-group { display: flex; flex-direction: column; align-items: center; gap: 10px; margin-top: auto; }
#projects-wrapper .proj-btn { background: #facc15; color: #ffffff; padding: 10px 18px; border-radius: 12px; text-decoration: none; font-size: 11.5px; font-weight: 800; width: 140px; text-transform: uppercase; letter-spacing: 0.5px; transition: all 0.3s ease; display: inline-block; border: 2px solid #facc15; }
#projects-wrapper .proj-btn:hover { background: #000; color: #fff; border-color: #000; transform: translateY(-2px); }
#projects-wrapper .proj-arrow { position: absolute; top: 50%; transform: translateY(-50%); font-size: 45px; color: #333; cursor: pointer; z-index: 1000; user-select: none; transition: color 0.3s ease, scale 0.2s ease; }
#projects-wrapper .proj-arrow:hover { color: #f4b400; scale: 1.2; }
#projects-wrapper .left { left: -70px; }
#projects-wrapper .right { right: -70px; }

/* ======= EXPERIENCE.HTML CSS (SCOPED) ======= */
#exp-wrapper { --primary-yellow: #ffc107; --text-dark: #333333; --text-gray: #666666; --bg-white: #ffffff; --shadow: 0 10px 30px rgba(0, 0, 0, 0.05); font-family: 'Poppins', sans-serif; background-color: #f5f5f5; margin: 0; padding: 60px 0; overflow-x: hidden; width: 100%; display: block; }
#exp-wrapper .experience-section { max-width: 1150px; margin: 0 auto; padding: 0 25px; }
@keyframes slideFromLeftExp { from { opacity: 0; transform: translateX(-100px); } to { opacity: 1; transform: translateX(0); } }
@keyframes slideFromRightExp { from { opacity: 0; transform: translateX(100px); } to { opacity: 1; transform: translateX(0); } }
#exp-wrapper .header-container { text-align: center; margin-bottom: 50px; }
#exp-wrapper .header-main { display: flex; justify-content: center; align-items: center; gap: 15px; font-size: 2.5rem; font-weight: 800; color: var(--text-dark); margin-bottom: 10px; }
#exp-wrapper .header-main span { color: var(--primary-yellow); }
#exp-wrapper .header-subtext { color: var(--text-gray); font-size: 1rem; white-space: nowrap; margin: 0 auto; }
#exp-wrapper .experience-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
#exp-wrapper .experience-card { background: var(--bg-white); border-radius: 15px; padding: 38px 35px; box-shadow: var(--shadow); display: flex; flex-direction: column; gap: 40px; }
#exp-wrapper .card-left { animation: slideFromLeftExp 1s ease-out forwards; }
#exp-wrapper .card-right { animation: slideFromRightExp 1s ease-out forwards; }
#exp-wrapper .timeline-item { display: flex; gap: 18px; position: relative; }
#exp-wrapper .timeline-left { display: flex; flex-direction: column; align-items: center; position: relative; }
#exp-wrapper .icon-circle { width: 42px; height: 42px; border: 2px dashed var(--primary-yellow); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: white; z-index: 2; color: var(--primary-yellow); font-size: 1.05rem; }
#exp-wrapper .timeline-line { position: absolute; top: 42px; bottom: -40px; width: 2px; border-left: 2px dashed var(--primary-yellow); z-index: 1; }
#exp-wrapper .timeline-item:last-child .timeline-line { display: none; }
#exp-wrapper .timeline-content { padding-top: 4px; }
#exp-wrapper .date-badge { background-color: var(--primary-yellow); color: #ffffff; padding: 4px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 10px; letter-spacing: 0.5px; }
#exp-wrapper .job-title { font-size: 1.05rem; font-weight: 700; color: var(--text-dark); margin-bottom: 6px; text-transform: uppercase; }
#exp-wrapper .job-desc { font-size: 0.9rem; color: var(--text-gray); line-height: 1.5; margin: 0; }
@media (max-width: 1100px) { #exp-wrapper .header-subtext { white-space: normal; max-width: 90%; } }
@media (max-width: 900px) { #exp-wrapper .experience-grid { grid-template-columns: 1fr; } #exp-wrapper .card-left, #exp-wrapper .card-right { animation: slideFromLeftExp 1s ease-out forwards; } }

/* ======= CERTIFICATION.HTML CSS (SCOPED) ======= */
#cert-wrapper { --primary-yellow: #ffc107; --text-dark: #1a1a1a; --bg-light: #f5f5f5; --three-d-shadow: 0 10px 25px rgba(0, 0, 0, 0.15), 0 2px 10px rgba(0, 0, 0, 0.1); font-family: 'Poppins', sans-serif; background-color: var(--bg-light); margin: 0; padding: 50px 0; overflow-x: hidden; width: 100%; display: block; }
#cert-wrapper .cert-container { max-width: 950px; margin: 0 auto; padding: 0 20px; }
@keyframes slideUpFadeCert { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
#cert-wrapper .header-container { text-align: center; margin-bottom: 60px; animation: slideUpFadeCert 0.8s ease-out forwards; }
#cert-wrapper .header-main { display: flex; justify-content: center; align-items: center; gap: 15px; font-size: 2.5rem; font-weight: 800; color: var(--text-dark); }
#cert-wrapper .header-main i { font-size: 2.8rem; color: #000; }
#cert-wrapper .header-main span { color: var(--primary-yellow); }
#cert-wrapper .cert-grid { display: grid; grid-template-columns: repeat(3, 1fr); row-gap: 60px; column-gap: 30px; }
#cert-wrapper .cert-card { background: #fff; border-radius: 10px; overflow: hidden; box-shadow: var(--three-d-shadow); position: relative; aspect-ratio: 1.5 / 1; border: 1px solid rgba(0, 0, 0, 0.1); opacity: 0; animation: slideUpFadeCert 0.7s ease-out forwards; transition: transform 0.3s ease, box-shadow 0.3s ease; }
#cert-wrapper .cert-card:hover { transform: translateY(-8px); box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25); }
#cert-wrapper .cert-img { width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; z-index: 1; }
#cert-wrapper .cert-overlay { position: relative; z-index: 2; height: 100%; display: flex; justify-content: center; align-items: flex-end; background: linear-gradient(transparent 40%, rgba(0, 0, 0, 0.25)); padding-bottom: 40px; }
#cert-wrapper .read-more-btn { background-color: var(--primary-yellow); color: var(--text-dark); border: none; padding: 9px 22px; border-radius: 6px; font-weight: 700; font-size: 0.85rem; cursor: pointer; text-decoration: none; box-shadow: 0 4px 0px #d4a004; transition: all 0.2s ease; text-transform: capitalize; }
#cert-wrapper .read-more-btn:hover { background-color: #ffca2c; transform: translateY(-2px); box-shadow: 0 6px 0px #d4a004; }
@media (max-width: 900px) { #cert-wrapper .cert-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px) { #cert-wrapper .cert-grid { grid-template-columns: 1fr; } }
"""

# Inject CSS into home
merge = home.replace('</style>', scoped_css + '\n</style>')

# Replace Nav links
merge = merge.replace('href="about.html"', 'href="#about-wrapper"')
merge = merge.replace('href="skill.html"', 'href="#skills-wrapper"')
merge = merge.replace('href="education.html"', 'href="#edu-wrapper"')
merge = merge.replace('href="projects.html"', 'href="#projects-wrapper"')
merge = merge.replace('href="experience.html"', 'href="#exp-wrapper"')
merge = merge.replace('href="certification.html"', 'href="#cert-wrapper"')

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

<!-- PROJECTS SECTION -->
<div id="projects-wrapper">
{proj_body}
</div>

<!-- EXPERIENCE SECTION -->
<div id="exp-wrapper">
{exp_body}
</div>

<!-- CERTIFICATION SECTION -->
<div id="cert-wrapper">
{cert_body}
</div>
'''

new_scripts = f'''
// SKILL SCRIPTS
{skill_script}

// EDU SCRIPTS
{edu_script}

// PROJ SCRIPTS
{proj_script}

// EXP SCRIPTS
{exp_script}

// CERT SCRIPTS
{cert_script}
'''

# Inject Body
merge = merge.replace('<script src="script.js"></script>', new_html + '\n<script src="script.js"></script>')

# Inject scripts
merge = merge.replace('</body>', '<script>\n' + new_scripts + '\n</script>\n</body>')

with open(os.path.join(base_dir, 'merge.html'), 'w', encoding='utf-8') as f:
    f.write(merge)

print("Successfully merged 6 pages perfectly!")
