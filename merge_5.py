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

# Extract CSS and dynamically scope it to each specific wrapper. 
# This guarantees 100% original frontend layout.
css_about = scope_css(extract_css(about), 'about-wrapper')
css_skill = scope_css(extract_css(skill), 'skills-wrapper')
css_edu = scope_css(extract_css(education), 'edu-wrapper')
css_proj = scope_css(extract_css(projects), 'projects-wrapper')
css_exp = scope_css(extract_css(experience), 'exp-wrapper')

# Rename the few specific classes that share names across different pages
# Skill.html (.logo -> .skill-logo)
css_skill = css_skill.replace('.logo{', '.skill-logo{').replace('.logo {', '.skill-logo {').replace('.logo img', '.skill-logo img')
body_skill = strip_script(extract_body(skill)).replace('class="logo"', 'class="skill-logo"')
body_skill = body_skill.replace('from-left', 'skill-from-left').replace('from-right', 'skill-from-right')
css_skill = css_skill.replace('.from-left', '.skill-from-left').replace('.from-right', '.skill-from-right')

# Edu.html conflicts
body_edu = strip_script(extract_body(education)).replace('from-left', 'edu-from-left').replace('from-right', 'edu-from-right')
css_edu = css_edu.replace('.from-left', '.edu-from-left').replace('.from-right', '.edu-from-right')

# Projects.html (.card -> .carousel-card, .content -> .carousel-content, .arrow -> .carousel-arrow)
css_proj = css_proj.replace('.card', '.carousel-card').replace('.content', '.carousel-content').replace('.arrow', '.carousel-arrow')
body_proj = strip_script(extract_body(projects)).replace('class="card"', 'class="carousel-card"').replace('class="content"', 'class="carousel-content"')
body_proj = body_proj.replace('class="arrow left"', 'class="carousel-arrow left"').replace('class="arrow right"', 'class="carousel-arrow right"')
script_proj = extract_script(projects).replace('.card', '.carousel-card')

# Other Bodies & Scripts
body_about = strip_script(extract_body(about))
body_exp = strip_script(extract_body(experience))

script_about = extract_script(about)
script_skill = extract_script(skill)
script_edu = extract_script(education)
script_exp = extract_script(experience)

# Combine CSS
all_new_css = "\n/* --- ABOUT CSS --- */\n" + css_about + "\n/* --- SKILLS CSS --- */\n" + css_skill + "\n/* --- EDU CSS --- */\n" + css_edu + "\n/* --- PROJ CSS --- */\n" + css_proj + "\n/* --- EXP CSS --- */\n" + css_exp

# Combine Scripts
all_new_scripts = "\n// --- ABOUT SCRIPT ---\n" + script_about + "\n// --- SKILL SCRIPT ---\n" + script_skill + "\n// --- EDU SCRIPT ---\n" + script_edu + "\n// --- PROJ SCRIPT ---\n" + script_proj + "\n// --- EXP SCRIPT ---\n" + script_exp

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

<!-- EXPERIENCE SECTION -->
<div id="exp-wrapper" style="display: block; width: 100%;">
{body_exp}
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
merge = merge.replace('href="experience.html"', 'href="#exp-wrapper"')

# Inject Body before script.js
merge = merge.replace('<script src="script.js"></script>', new_html + '\n<script src="script.js"></script>')

# Inject scripts
merge = merge.replace('</body>', '<script>\n' + all_new_scripts + '\n</script>\n</body>')

with open(os.path.join(base_dir, 'merge.html'), 'w', encoding='utf-8') as f:
    f.write(merge)

print("Successfully merged About, Skill, Education, Projects, and Experience flawlessly!")
