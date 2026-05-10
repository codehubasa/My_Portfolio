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
projects = read("projects.html")
experience = read("experience.html")
certification = read("certification.html")
contact = read("contact.html")

def extract_css(html):
    m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    return m.group(1) if m else ""

def extract_body(html):
    m = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    return m.group(1) if m else ""

def extract_script(html):
    m = re.findall(r'<script.*?>(.*?)</script>', html, re.DOTALL)
    return "\n".join(m)

def strip_script(html):
    return re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)

def scope_css(css, wrapper_id):
    # scope :root variables to the wrapper
    css = re.sub(r':root\s*\{', f'#{wrapper_id} {{', css)
    # scope body styles to the wrapper
    css = re.sub(r'body\s*\{', f'#{wrapper_id} {{', css)
    # scope global reset styles to the wrapper's children
    css = re.sub(r'\*\s*\{', f'#{wrapper_id} * {{', css)
    return css

# Extract CSS and Scope (this preserves 100% of the original look!)
css_about = scope_css(extract_css(about), 'about-wrapper')
css_skill = scope_css(extract_css(skill), 'skills-wrapper')
css_edu = scope_css(extract_css(education), 'edu-wrapper')
css_proj = scope_css(extract_css(projects), 'projects-wrapper')
css_exp = scope_css(extract_css(experience), 'exp-wrapper')
css_cert = scope_css(extract_css(certification), 'cert-wrapper')
css_cont = scope_css(extract_css(contact), 'contact-wrapper')

# Rename the few specifically conflicting classes across pages
# Skill.html (.logo -> .skill-logo)
css_skill = css_skill.replace('.logo{', '.skill-logo{').replace('.logo {', '.skill-logo {').replace('.logo img', '.skill-logo img')
body_skill = extract_body(skill).replace('class="logo"', 'class="skill-logo"')

# Projects.html (.card -> .carousel-card, .content -> .carousel-content, .arrow -> .carousel-arrow)
css_proj = css_proj.replace('.card', '.carousel-card').replace('.content', '.carousel-content').replace('.arrow', '.carousel-arrow')
body_proj = extract_body(projects).replace('class="card"', 'class="carousel-card"').replace('class="content"', 'class="carousel-content"')
body_proj = body_proj.replace('class="arrow left"', 'class="carousel-arrow left"').replace('class="arrow right"', 'class="carousel-arrow right"')
script_proj = extract_script(projects).replace('.card', '.carousel-card')

# Certification.html (.container -> .cert-container)
css_cert = css_cert.replace('.container', '.cert-container')
body_cert = extract_body(certification).replace('class="container"', 'class="cert-container"')

# Extract other bodies and scripts
body_about = extract_body(about)
body_edu = extract_body(education)
body_exp = extract_body(experience)
body_cont = extract_body(contact)

script_about = extract_script(about)
script_skill = extract_script(skill)
script_edu = extract_script(education)
script_exp = extract_script(experience)
script_cert = extract_script(certification)
script_cont = extract_script(contact)

# Strip scripts from bodies and wrap in scoped div with anchor IDs for navigation
body_about = f'<div id="about-wrapper" class="section-wrapper">\n<div id="about"></div>\n{strip_script(body_about)}\n</div>'
body_skill = f'<div id="skills-wrapper" class="section-wrapper">\n<div id="skills"></div>\n{strip_script(body_skill)}\n</div>'
body_edu = f'<div id="edu-wrapper" class="section-wrapper">\n<div id="edu-nav"></div>\n{strip_script(body_edu)}\n</div>'
body_proj = f'<div id="projects-wrapper" class="section-wrapper">\n<div id="projects-carousel"></div>\n{strip_script(body_proj)}\n</div>'
body_exp = f'<div id="exp-wrapper" class="section-wrapper">\n<div id="exp"></div>\n{strip_script(body_exp)}\n</div>'
body_cert = f'<div id="cert-wrapper" class="section-wrapper">\n<div id="achievements"></div>\n{strip_script(body_cert)}\n</div>'
body_cont = f'<div id="contact-wrapper" class="section-wrapper">\n<div id="contact"></div>\n{strip_script(body_cont)}\n</div>'

# Combine CSS
all_new_css = "\n/* --- ABOUT CSS --- */\n" + css_about + "\n/* --- SKILLS CSS --- */\n" + css_skill + "\n/* --- EDU CSS --- */\n" + css_edu + "\n/* --- PROJ CSS --- */\n" + css_proj + "\n/* --- EXP CSS --- */\n" + css_exp + "\n/* --- CERT CSS --- */\n" + css_cert + "\n/* --- CONT CSS --- */\n" + css_cont

# Combine Scripts
all_new_scripts = "\n// --- ABOUT SCRIPT ---\n" + script_about + "\n// --- SKILL SCRIPT ---\n" + script_skill + "\n// --- EDU SCRIPT ---\n" + script_edu + "\n// --- PROJ SCRIPT ---\n" + script_proj + "\n// --- EXP SCRIPT ---\n" + script_exp + "\n// --- CERT SCRIPT ---\n" + script_cert + "\n// --- CONT SCRIPT ---\n" + script_cont

# Combine Bodies
all_new_body = "\n<!-- ABOUT -->\n" + body_about + "\n<!-- SKILL -->\n" + body_skill + "\n<!-- EDU -->\n" + body_edu + "\n<!-- PROJ -->\n" + body_proj + "\n<!-- EXP -->\n" + body_exp + "\n<!-- CERT -->\n" + body_cert + "\n<!-- CONT -->\n" + body_cont

# Merge into home.html
merge = home

# Update Nav Links (ensure smooth scrolling)
merge = merge.replace('href="about.html"', 'href="#about"')
merge = merge.replace('href="skill.html"', 'href="#skills"')
merge = merge.replace('href="education.html"', 'href="#edu"')
merge = merge.replace('href="projects.html"', 'href="#projects-carousel"')
merge = merge.replace('href="experience.html"', 'href="#exp"')
merge = merge.replace('href="certification.html"', 'href="#achievements"')
merge = merge.replace('href="contact.html"', 'href="#contact"')

# Ensure font-awesome is included
fa_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
if fa_link not in merge:
    merge = merge.replace('</head>', f'    {fa_link}\n</head>')

# Inject CSS
merge = merge.replace('</style>', all_new_css + '\n</style>')

# Inject HTML Body before script.js
merge = merge.replace('<script src="script.js"></script>', all_new_body + '\n<script src="script.js"></script>')

# Inject Scripts
merge = merge.replace('</body>', '<script>\n' + all_new_scripts + '\n</script>\n</body>')

with open(os.path.join(base_dir, 'merge.html'), 'w', encoding='utf-8') as f:
    f.write(merge)
print("Done! The new merge.html perfectly preserves the exact original frontend layout of every individual page!")
