// =============================================
// KAJOL SHAH — Advocate Website
// Main JavaScript
// =============================================

// --- Custom Cursor ---
const cur  = document.getElementById('cur');
const ring = document.getElementById('ring');

document.addEventListener('mousemove', e => {
  cur.style.left  = e.clientX + 'px';
  cur.style.top   = e.clientY + 'px';
  ring.style.left = e.clientX + 'px';
  ring.style.top  = e.clientY + 'px';
});

document.querySelectorAll('a, button, .card').forEach(el => {
  el.addEventListener('mouseenter', () => {
    ring.style.width   = '56px';
    ring.style.height  = '56px';
    ring.style.opacity = '1';
  });
  el.addEventListener('mouseleave', () => {
    ring.style.width   = '36px';
    ring.style.height  = '36px';
    ring.style.opacity = '.5';
  });
});

// --- Tabs ---
function switchTab(id, btn) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('on'));
  document.querySelectorAll('.tab').forEach(b => b.classList.remove('on'));
  document.getElementById('panel-' + id).classList.add('on');
  btn.classList.add('on');
  // Re-observe reveal elements in the newly shown panel
  setTimeout(() => {
    document.querySelectorAll('#panel-' + id + ' .r:not(.v)').forEach(el => obs.observe(el));
  }, 10);
}

// --- Mobile Menu ---
function toggleMenu() {
  document.getElementById('mobMenu').classList.toggle('open');
}

// --- Scroll Reveal ---
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('v');
      obs.unobserve(e.target);
    }
  });
}, { threshold: .08 });

document.querySelectorAll('.r').forEach(el => obs.observe(el));
