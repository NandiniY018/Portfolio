/**
 * main.js — Premium Portfolio Interactive Logic
 * Handles: Navbar, Typing, Scroll Reveal, Skill Bars,
 *          Counters, Contact Form, Toast, Back-to-Top,
 *          Mobile Menu, Particles.
 */

'use strict';

/* ============================================================
   UTILITY HELPERS
   ============================================================ */
const $ = (selector, ctx = document) => ctx.querySelector(selector);
const $$ = (selector, ctx = document) => [...ctx.querySelectorAll(selector)];

/* ============================================================
   1. NAVBAR — Sticky + Scroll Highlight + Mobile Menu
   ============================================================ */
(function initNavbar() {
  const navbar       = $('#navbar');
  const navLinks     = $$('.nav-link[data-section]');
  const hamburger    = $('#hamburger');
  const mobileMenu   = $('#mobile-menu');
  const mobileLinks  = $$('#mobile-menu .nav-link');

  // Solid glass on scroll
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    if (scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Active section highlighting
    const sections = $$('section[id]');
    let currentSection = '';

    sections.forEach(section => {
      const sectionTop    = section.offsetTop - 100;
      const sectionHeight = section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        currentSection = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.toggle('active', link.dataset.section === currentSection);
    });

    lastScroll = scrollY;
  }, { passive: true });

  // Mobile menu toggle
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.contains('open');
      mobileMenu.classList.toggle('open', !isOpen);
      hamburger.classList.toggle('open', !isOpen);
      hamburger.setAttribute('aria-expanded', String(!isOpen));
    });

    // Close on mobile link click
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });
  }
})();

/* ============================================================
   2. TYPING ANIMATION
   ============================================================ */
(function initTyping() {
  const el = $('#typing-text');
  if (!el) return;

  const phrases = [
    'Python Full Stack Developer',
    'Django Backend Engineer',
    'React Frontend Developer',
    'MySQL Database Designer',
    'Data Science Enthusiast',
  ];

  let phraseIndex = 0;
  let charIndex   = 0;
  let isDeleting  = false;
  let isPaused    = false;

  const TYPE_SPEED   = 80;
  const DELETE_SPEED = 45;
  const PAUSE_AFTER  = 1800;
  const PAUSE_BEFORE = 300;

  function type() {
    const current = phrases[phraseIndex];

    if (!isDeleting && charIndex <= current.length) {
      el.textContent = current.substring(0, charIndex++);
      if (charIndex > current.length) {
        isPaused = true;
        setTimeout(() => { isPaused = false; isDeleting = true; setTimeout(type, PAUSE_BEFORE); }, PAUSE_AFTER);
        return;
      }
      setTimeout(type, TYPE_SPEED);
    } else if (isDeleting && charIndex >= 0) {
      el.textContent = current.substring(0, charIndex--);
      if (charIndex < 0) {
        isDeleting  = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        setTimeout(type, PAUSE_BEFORE);
        return;
      }
      setTimeout(type, DELETE_SPEED);
    }
  }

  setTimeout(type, 800);
})();

/* ============================================================
   3. SCROLL REVEAL (IntersectionObserver)
   ============================================================ */
(function initScrollReveal() {
  const revealEls = $$('.reveal, .reveal-left, .reveal-right');
  if (!revealEls.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach(el => observer.observe(el));
})();

/* ============================================================
   4. SKILL BAR ANIMATIONS
   ============================================================ */
(function initSkillBars() {
  const bars = $$('[data-skill-width]');
  if (!bars.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const width = bar.dataset.skillWidth || '0%';
        // Small delay so transition is visible
        requestAnimationFrame(() => {
          setTimeout(() => { bar.style.width = width; }, 150);
        });
        observer.unobserve(bar);
      }
    });
  }, { threshold: 0.3 });

  bars.forEach(bar => observer.observe(bar));
})();

/* ============================================================
   5. COUNTER ANIMATIONS
   ============================================================ */
(function initCounters() {
  const counters = $$('[data-counter]');
  if (!counters.length) return;

  const easeOut = (t) => 1 - Math.pow(1 - t, 3);

  function animateCounter(el) {
    const target   = parseInt(el.dataset.counter, 10);
    const suffix   = el.dataset.suffix || '';
    const duration = 1800;
    const start    = performance.now();

    function frame(now) {
      const elapsed  = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const value    = Math.floor(easeOut(progress) * target);
      el.textContent = value + suffix;
      if (progress < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
})();

/* ============================================================
   6. CONTACT FORM — Validation + AJAX Submit
   ============================================================ */
(function initContactForm() {
  const form    = $('#contact-form');
  if (!form) return;

  const inputs  = form.querySelectorAll('[data-field]');
  const btn     = $('#contact-submit');
  const btnText = btn ? btn.querySelector('.btn-text') : null;
  const btnIcon = btn ? btn.querySelector('.btn-icon') : null;

  // Real-time validation on blur
  inputs.forEach(input => {
    input.addEventListener('blur', () => validateField(input));
    input.addEventListener('input', () => {
      if (input.classList.contains('error')) validateField(input);
    });
  });

  function validateField(input) {
    const field = input.dataset.field;
    const value = input.value.trim();
    let error   = '';

    switch (field) {
      case 'name':
        if (!value || value.length < 2) error = 'Please enter your full name (min 2 characters).';
        break;
      case 'email':
        if (!value || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) error = 'Please enter a valid email address.';
        break;
      case 'subject':
        if (!value || value.length < 3) error = 'Please enter a subject (min 3 characters).';
        break;
      case 'message':
        if (!value || value.length < 10) error = 'Please enter your message (min 10 characters).';
        break;
    }

    const errEl = form.querySelector(`[data-error="${field}"]`);
    if (error) {
      input.classList.add('error');
      if (errEl) { errEl.textContent = error; errEl.classList.add('visible'); }
    } else {
      input.classList.remove('error');
      if (errEl) { errEl.textContent = ''; errEl.classList.remove('visible'); }
    }

    return !error;
  }

  function validateAll() {
    let valid = true;
    inputs.forEach(input => { if (!validateField(input)) valid = false; });
    return valid;
  }

  function setLoading(loading) {
    if (!btn) return;
    btn.disabled = loading;
    if (btnText) btnText.textContent = loading ? 'Sending...' : 'Send Message';
    if (btnIcon) btnIcon.className = loading
      ? 'btn-icon fas fa-circle-notch fa-spin'
      : 'btn-icon fas fa-paper-plane';
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!validateAll()) return;

    setLoading(true);

    const payload = {};
    inputs.forEach(input => { payload[input.dataset.field] = input.value.trim(); });

    try {
      const response = await fetch('/contact/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (data.success) {
        showToast('success', 'Message Sent!', data.message || "I'll get back to you soon.");
        form.reset();
        inputs.forEach(i => i.classList.remove('error'));
      } else if (data.errors) {
        Object.entries(data.errors).forEach(([field, msg]) => {
          const input = form.querySelector(`[data-field="${field}"]`);
          const errEl = form.querySelector(`[data-error="${field}"]`);
          if (input) input.classList.add('error');
          if (errEl) { errEl.textContent = msg; errEl.classList.add('visible'); }
        });
        showToast('error', 'Validation Error', 'Please fix the highlighted fields.');
      } else {
        showToast('error', 'Error', data.error || 'Something went wrong. Please try again.');
      }
    } catch (networkError) {
      showToast('error', 'Network Error', 'Could not reach the server. Please try again later.');
    } finally {
      setLoading(false);
    }
  });
})();

/* ============================================================
   7. TOAST NOTIFICATIONS
   ============================================================ */
function showToast(type, title, message, duration = 5000) {
  let container = $('#toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    document.body.appendChild(container);
  }

  const icon = type === 'success' ? '✓' : '✕';
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <div class="toast-icon">${icon}</div>
    <div>
      <div class="toast-title">${title}</div>
      <div class="toast-message">${message}</div>
    </div>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add('toast-hide');
    setTimeout(() => toast.remove(), 400);
  }, duration);
}

/* ============================================================
   8. BACK TO TOP BUTTON
   ============================================================ */
(function initBackToTop() {
  const btn = $('#back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();

/* ============================================================
   9. SMOOTH SCROLLING for Anchor Links
   ============================================================ */
(function initSmoothScroll() {
  document.addEventListener('click', (e) => {
    const anchor = e.target.closest('a[href^="#"]');
    if (!anchor) return;
    const id = anchor.getAttribute('href');
    if (id === '#') {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }
    const target = document.querySelector(id);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
})();

/* ============================================================
   10. HERO PARTICLES (Canvas)
   ============================================================ */
(function initParticles() {
  const canvas = $('#particles-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let particles = [];
  let animId;

  function resize() {
    canvas.width  = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }

  class Particle {
    constructor() { this.reset(); }

    reset() {
      this.x     = Math.random() * canvas.width;
      this.y     = canvas.height + 10;
      this.size  = Math.random() * 2.5 + 0.5;
      this.speedY = -(Math.random() * 0.8 + 0.3);
      this.speedX = (Math.random() - 0.5) * 0.5;
      this.life  = 0;
      this.maxLife = Math.random() * 200 + 100;
      const hues = [240, 260, 190]; // indigo, violet, cyan
      this.hue   = hues[Math.floor(Math.random() * hues.length)];
    }

    update() {
      this.x   += this.speedX;
      this.y   += this.speedY;
      this.life++;
      if (this.y < -10 || this.life > this.maxLife) this.reset();
    }

    draw() {
      const alpha = Math.min(this.life / 30, 1) * (1 - this.life / this.maxLife);
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = `hsla(${this.hue}, 80%, 70%, ${alpha * 0.7})`;
      ctx.fill();
    }
  }

  function init() {
    resize();
    particles = Array.from({ length: 60 }, () => {
      const p = new Particle();
      p.y = Math.random() * canvas.height; // scatter initially
      return p;
    });
    animate();
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    animId = requestAnimationFrame(animate);
  }

  const resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(canvas);

  // Lazy: only animate when visible
  const io = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      if (!animId) animate();
    } else {
      cancelAnimationFrame(animId);
      animId = null;
    }
  });
  io.observe(canvas);

  init();
})();

/* ============================================================
   11. HERO ENTRANCE ANIMATION (staggered)
   ============================================================ */
(function initHeroEntrance() {
  const heroEls = $$('.hero-animate');
  heroEls.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(25px)';
    el.style.transition = `opacity 0.7s ease, transform 0.7s ease`;
    setTimeout(() => {
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    }, 200 + i * 120);
  });
})();

/* ============================================================
   12. RIPPLE EFFECT on buttons
   ============================================================ */
(function initRipple() {
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.ripple');
    if (!btn) return;
    const rect   = btn.getBoundingClientRect();
    const x      = e.clientX - rect.left;
    const y      = e.clientY - rect.top;
    const circle = document.createElement('span');
    circle.style.cssText = `
      position:absolute;
      border-radius:50%;
      transform:scale(0);
      animation:ripple-anim 0.55s linear;
      background:rgba(255,255,255,0.2);
      width:100px;height:100px;
      left:${x - 50}px;top:${y - 50}px;
      pointer-events:none;
    `;
    // Inject ripple animation if missing
    if (!document.getElementById('ripple-style')) {
      const style = document.createElement('style');
      style.id = 'ripple-style';
      style.textContent = '@keyframes ripple-anim{to{transform:scale(4);opacity:0}}';
      document.head.appendChild(style);
    }
    btn.style.position = 'relative';
    btn.style.overflow = 'hidden';
    btn.appendChild(circle);
    circle.addEventListener('animationend', () => circle.remove());
  });
})();
