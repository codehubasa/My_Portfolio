import os
import re

base_dir = r"c:\Users\amitb\OneDrive\Desktop\Portfolio"

def read(f):
    with open(os.path.join(base_dir, f), 'r', encoding='utf-8') as file:
        return file.read()

# Base file is home.html
home = read("home.html")
about = read("about.html")

# Extract Body from about
about_body_match = re.search(r'<body>(.*?)</body>', about, re.DOTALL)
about_body = about_body_match.group(1) if about_body_match else ""

# Hardcoded scoped CSS for about.html to guarantee 0 conflicts with home.html
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

@keyframes slideInRightAbout {
  from { opacity: 0; transform: translateX(100px); }
  to { opacity: 1; transform: translateX(0); }
}

#about-wrapper .about-right h1, 
#about-wrapper .about-right p, 
#about-wrapper .about-right .final-note { 
    opacity: 0; 
    animation: slideInRightAbout 0.8s ease-out forwards; 
}
#about-wrapper .about-right h1 { animation-delay: 0.2s; }
#about-wrapper .about-right p:nth-of-type(1) { animation-delay: 0.4s; }
#about-wrapper .about-right p:nth-of-type(2) { animation-delay: 0.6s; }
#about-wrapper .about-right p:nth-of-type(3) { animation-delay: 0.8s; }
#about-wrapper .about-right p:nth-of-type(4) { animation-delay: 1.0s; }
#about-wrapper .about-right p:nth-of-type(5) { animation-delay: 1.2s; }
#about-wrapper .about-right .final-note { animation-delay: 1.4s; color: #333; font-weight: 600; }
#about-wrapper .final-line { text-align: center; font-size: 20px; font-weight: 600; padding: 40px 20px 80px; color: #333; }
"""

# Inject CSS into home
merge = home.replace('</style>', scoped_css + '\n</style>')

# Replace Nav link for about
merge = merge.replace('href="about.html"', 'href="#about-wrapper"')

# Inject Body
# In home.html, we insert it right before `<script src="script.js"></script>`
about_html = f'\n<!-- ABOUT SECTION -->\n<div id="about-wrapper">\n{about_body}\n</div>\n'
merge = merge.replace('<script src="script.js"></script>', about_html + '\n<script src="script.js"></script>')

with open(os.path.join(base_dir, 'merge.html'), 'w', encoding='utf-8') as f:
    f.write(merge)

print("Successfully created merge.html with ONLY about.html perfectly inserted!")
