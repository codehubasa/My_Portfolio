// ================= LOGO CLICK =================
const logo = document.getElementById("logoText");
if (logo) {
  logo.addEventListener("click", () => {
    logo.classList.toggle("active");
  });
}


// ================= TYPING =================
const roles = ["Web Developer", "AI/ML Enthusiast", "Full Stack Developer"];
let i = 0, j = 0, current = "", isDeleting = false;

function type() {
  const roleEl = document.getElementById("role");
  if (!roleEl) return;

  current = roles[i];
  j = isDeleting ? j - 1 : j + 1;
  roleEl.textContent = current.substring(0, j);

  if (!isDeleting && j === current.length) {
    isDeleting = true;
    setTimeout(type, 1200);
    return;
  }
  if (isDeleting && j === 0) {
    isDeleting = false;
    i = (i + 1) % roles.length;
  }
  setTimeout(type, isDeleting ? 40 : 80);
}
if (document.getElementById("role")) {
  type();
}


// ================= IMAGE UPLOAD =================
const container = document.getElementById("profileImageContainer");
const input = document.getElementById("photoUpload");
const img = document.getElementById("profileImage");

if (container && input) {
  container.addEventListener("click", () => input.click());
}

if (input && img) {
  input.addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (file) {
      img.src = URL.createObjectURL(file);
    }
  });
}


// ================= 🌙 THEME TOGGLE (WORKING) =================
const toggle = document.getElementById("themeToggle");
const icon = document.getElementById("themeIcon");

if (localStorage.getItem('theme') === 'dark') {
  document.body.classList.add('dark-mode');
  if (icon) icon.innerHTML = '&#9728;';
}

if (toggle) {
  toggle.addEventListener("click", () => {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    if (icon) icon.innerHTML = isDark ? '&#9728;' : '&#9789;';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
}

// ================= CANVAS =================
const canvas = document.getElementById("canvas");
if (canvas) {
  const ctx = canvas.getContext("2d");
  
  function getParticleColor() {
    const isDark = document.body.classList.contains('dark-mode');
    return isDark ? "255, 255, 255" : "15, 23, 42"; // White for dark mode, Deep Slate for light mode
  }

  let particleColor = getParticleColor();

  function setCanvasSize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', setCanvasSize);
  setCanvasSize();

  // Update color when theme changes
  const observer = new MutationObserver(() => {
    particleColor = getParticleColor();
  });
  observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });

  let particles = [];
  for (let i = 0; i < 100; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      dx: (Math.random() - 0.5) * 0.5,
      dy: (Math.random() - 0.5) * 0.5
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const isDark = document.body.classList.contains('dark-mode');
    
    particles.forEach((p, i) => {
      p.x += p.dx; p.y += p.dy;
      if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.dy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${particleColor}, ${isDark ? 0.4 : 1.0})`; 
      ctx.fill();

      for (let j = i + 1; j < particles.length; j++) {
        let p2 = particles[j];
        let d = Math.sqrt((p.x - p2.x) ** 2 + (p.y - p2.y) ** 2);
        if (d < 120) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = `rgba(${particleColor}, ${isDark ? 0.1 : 0.5})`; 
          ctx.stroke();
        }
      }
    });
    requestAnimationFrame(draw);
  }
  draw();
}