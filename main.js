/* ============================================================
   ANJISH BHONDWE — Portfolio
   main.js
   ============================================================ */

'use strict';

/* ── NAV: shrink on scroll ── */
const nav = document.getElementById('topnav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 60);
});

/* ── MOBILE MENU ── */
const hamburger  = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');

function toggleMenu() {
  const open = mobileMenu.classList.toggle('open');
  hamburger.setAttribute('aria-expanded', open);
  // animate bars
  const bars = hamburger.querySelectorAll('span');
  if (open) {
    bars[0].style.transform = 'translateY(7px) rotate(45deg)';
    bars[1].style.opacity   = '0';
    bars[2].style.transform = 'translateY(-7px) rotate(-45deg)';
  } else {
    bars.forEach(b => { b.style.transform = ''; b.style.opacity = ''; });
  }
}

hamburger.addEventListener('click', toggleMenu);

// close on nav link click
mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  mobileMenu.classList.remove('open');
  hamburger.querySelectorAll('span').forEach(b => { b.style.transform = ''; b.style.opacity = ''; });
}));

// close on outside click
document.addEventListener('click', e => {
  if (mobileMenu.classList.contains('open') &&
      !mobileMenu.contains(e.target) &&
      !hamburger.contains(e.target)) {
    mobileMenu.classList.remove('open');
    hamburger.querySelectorAll('span').forEach(b => { b.style.transform = ''; b.style.opacity = ''; });
  }
});

/* ── SCROLL REVEAL ── */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

/* ── ACTIVE NAV LINK (highlight section in view) ── */
const sections = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav-links a, #mobile-menu a');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(a => {
        a.style.color = a.getAttribute('href') === '#' + entry.target.id
          ? 'var(--vl)' : '';
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => sectionObserver.observe(s));

/* ── ARTICLE CARDS: open links ── */
document.querySelectorAll('.article-card[data-url]').forEach(card => {
  card.addEventListener('click', () => {
    window.open(card.dataset.url, '_blank', 'noopener,noreferrer');
  });
});

/* ── CLIENT LOGOS: tooltip / label fade ── */
document.querySelectorAll('.client-logo').forEach(logo => {
  logo.addEventListener('mouseenter', () => {
    logo.querySelector('.client-label')?.style.setProperty('color', 'var(--vl)');
  });
  logo.addEventListener('mouseleave', () => {
    logo.querySelector('.client-label')?.style.setProperty('color', '');
  });
});

/* ── SMOOTH SCROLL OFFSET (account for fixed nav) ── */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = nav.offsetHeight + 16;
    window.scrollTo({ top: target.offsetTop - offset, behavior: 'smooth' });
  });
});

/* ── TYPEWRITER EFFECT on hero subtitle ── */
const subtitles = [
  'Enterprise Agile & AI Governance Leader',
  'Compliant Velocity Architect',
  'EU AI Act Delivery Specialist',
  'Interim Director · Agile CoE Builder',
];
let subIdx = 0, charIdx = 0, deleting = false;
const titleEl = document.getElementById('hero-typewriter');

if (titleEl) {
  function typeWrite() {
    const current = subtitles[subIdx];
    if (!deleting) {
      titleEl.textContent = current.slice(0, ++charIdx);
      if (charIdx === current.length) {
        deleting = true;
        setTimeout(typeWrite, 2400);
        return;
      }
    } else {
      titleEl.textContent = current.slice(0, --charIdx);
      if (charIdx === 0) {
        deleting = false;
        subIdx = (subIdx + 1) % subtitles.length;
      }
    }
    setTimeout(typeWrite, deleting ? 38 : 62);
  }
  // start after hero animation settles
  setTimeout(typeWrite, 1600);
}

/* ── COUNTER ANIMATION on hero stats ── */
function animateCounter(el, target, suffix = '') {
  const duration = 1600;
  const start    = performance.now();
  function step(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased    = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    el.textContent = Math.round(eased * target) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.querySelectorAll('[data-count]').forEach(el => {
      const target = parseInt(el.dataset.count, 10);
      const suffix = el.dataset.suffix || '';
      animateCounter(el, target, suffix);
    });
    statsObserver.unobserve(entry.target);
  });
}, { threshold: 0.5 });

const statsBlock = document.querySelector('.hero-stats');
if (statsBlock) statsObserver.observe(statsBlock);
