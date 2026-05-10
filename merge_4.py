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

def extract_body(html):
    m = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    return m.group(1) if m else ""

def extract_script(html):
    m = re.findall(r'<script.*?>(.*?)</script>', html, re.DOTALL)
    return "\n".join(m)

def strip_script(html):
    return re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)

def extract_css(html):
    m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    return m.group(1) if m else ""

def scope_css(css, wrapper_id):
    css = re.sub(r':root\s*\{', f'#{wrapper_id} {{', css)
    css = re.sub(r'body\s*\{', f'#{wrapper_id} {{', css)
    css = re.sub(r'\*\s*\{', f'#{wrapper_id} * {{', css)
    return css

# Extract CSS and dynamically scope it
css_about = scope_css(extract_css(about), 'about-wrapper')
css_skill = scope_css(extract_css(skill), 'skills-wrapper')
css_edu = scope_css(extract_css(education), 'edu-wrapper')
css_proj = scope_css(extract_css(projects), 'projects-wrapper')

# Rename the few specific classes that share names across different pages
# Skill.html (.logo -> .skill-logo)
css_skill = css_skill.replace('.logo{', '.skill-logo{').replace('.logo {', '.skill-logo {').replace('.logo img', '.skill-logo img')
body_skill = strip_script(extract_body(skill)).replace('class="logo"', 'class="skill-logo"')
body_skill = body_skill.replace('from-left', 'skill-from-left').replace('from-right', 'skill-from-right')
css_skill = css_skill.replace('.from-left', '.skill-from-left').replace('.from-right', '.skill-from-right')

# Edu.html conflicts
body_edu = strip_script(extract_body(education)).replace('from-left', 'edu-from-left').replace('from-right', 'edu-from-right')
css_edu = css_edu.replace('.from-left', '.edu-from-left').replace('.from-right', '.edu-from-right')

# Projects.html precise replacements
# Use regex to ONLY match exact classes, not substrings like .card-img
css_proj = re.sub(r'\.card(?=[\s:{])', '.carousel-card', css_proj)
css_proj = re.sub(r'\.content(?=[\s:{])', '.carousel-content', css_proj)
css_proj = re.sub(r'\.arrow(?=[\s:{.])', '.carousel-arrow', css_proj)
# Now safely replace in the HTML body exactly
body_proj = strip_script(extract_body(projects))
body_proj = body_proj.replace('class="card"', 'class="carousel-card"')
body_proj = body_proj.replace('class="content"', 'class="carousel-content"')
body_proj = body_proj.replace('class="arrow left"', 'class="carousel-arrow left"')
body_proj = body_proj.replace('class="arrow right"', 'class="carousel-arrow right"')
# And inside the JS script
script_proj = extract_script(projects).replace('.card', '.carousel-card')

# Other Bodies & Scripts
body_about = strip_script(extract_body(about))

script_about = extract_script(about)
script_skill = extract_script(skill)
script_edu = extract_script(education)

# Combine CSS
all_new_css = "\n/* --- ABOUT CSS --- */\n" + css_about + "\n/* --- SKILLS CSS --- */\n" + css_skill + "\n/* --- EDU CSS --- */\n" + css_edu + "\n/* --- PROJ CSS --- */\n" + css_proj

# Combine Scripts
all_new_scripts = "\n// --- ABOUT SCRIPT ---\n" + script_about + "\n// --- SKILL SCRIPT ---\n" + script_skill + "\n// --- EDU SCRIPT ---\n" + script_edu + "\n// --- PROJ SCRIPT ---\n" + script_proj

# Combine HTML wrapped in their scoped IDs
new_html = f'''
<!-- ABOUT SECTION -->
<div id="about-wrapper" style="display: block; width: 100%;">
{body_about}
</div>

<!-- SKILLS SECTION -->
<div id="skills-wrapper" style="display: block; width: 100%;">
{body_skill}
</div>

<!-- EDUCATION SECTION -->
<div id="edu-wrapper" style="display: block; width: 100%;">
{body_edu}
</div>

<!-- PROJECTS SECTION -->
<div id="projects-wrapper" style="display: block; width: 100%;">
{body_proj}
</div>
'''

# Start merge
merge = home

# Inject CSS into home
merge = merge.replace('</style>', all_new_css + '\n</style>')

# Replace Nav links
merge = merge.replace('href="about.html"', 'href="#about-wrapper"')
merge = merge.replace('href="skill.html"', 'href="#skills-wrapper"')
merge = merge.replace('href="education.html"', 'href="#edu-wrapper"')
merge = merge.replace('href="projects.html"', 'href="#projects-wrapper"')

# Inject Body before script.js
merge = merge.replace('<script src="script.js"></script>', new_html + '\n<script src="script.js"></script>')

# Inject scripts
merge = merge.replace('</body>', '<script>\n' + all_new_scripts + '\n</script>\n</body>')

with open(os.path.join(base_dir, 'merge.html'), 'w', encoding='utf-8') as f:
    f.write(merge)

print("Successfully merged About, Skill, Education, and Projects flawlessly!")
