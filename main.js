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
}, { threshold: 0, rootMargin: '0px 0px 40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// Article content must always be visible (long pages fail ratio-based thresholds on mobile)
document.querySelectorAll('.article-body').forEach(el => el.classList.add('visible'));

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

/* ── CLIENT CARDS: optional focus state ── */
document.querySelectorAll('.client-card').forEach(card => {
  card.setAttribute('tabindex', '0');
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
  'Enterprise Agile & Delivery Enablement',
  'Multi-country Agile rollout',
  'EU AI Act & delivery readiness',
  'Agile CoE builder · Interim lead',
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

/* ── CONTACT FORM (mailto) ── */
const contactForm = document.getElementById('portfolio-contact-form');
contactForm?.addEventListener('submit', e => {
  e.preventDefault();
  const name = document.getElementById('cf-name')?.value?.trim() || '';
  const from = document.getElementById('cf-email')?.value?.trim() || '';
  const company = document.getElementById('cf-company')?.value?.trim() || '';
  const inquiry = document.getElementById('cf-type')?.value || '';
  const message = document.getElementById('cf-message')?.value?.trim() || '';
  const subject = encodeURIComponent(`Portfolio inquiry: ${inquiry}`);
  const body = encodeURIComponent(
    `Name: ${name}\nEmail: ${from}\nOrganisation: ${company}\nInquiry: ${inquiry}\n\n${message}`
  );
  window.location.href = `mailto:freelanceanjish@gmail.com?subject=${subject}&body=${body}`;
});
