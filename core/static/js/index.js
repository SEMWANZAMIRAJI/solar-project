// ================================================================
//   TESTECH — index.js
//   Used by: index.html (home page)
// ================================================================

// ── CUSTOM CURSOR ──
const cursor = document.getElementById('cursor');
const ring   = document.getElementById('cursorRing');

if (cursor && ring) {
  document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top  = e.clientY + 'px';
    ring.style.left   = e.clientX + 'px';
    ring.style.top    = e.clientY + 'px';
  });

  document.querySelectorAll('a, button').forEach(item => {
    item.addEventListener('mouseenter', () => {
      cursor.style.width  = '18px';
      cursor.style.height = '18px';
      ring.style.width    = '55px';
      ring.style.height   = '55px';
    });
    item.addEventListener('mouseleave', () => {
      cursor.style.width  = '10px';
      cursor.style.height = '10px';
      ring.style.width    = '38px';
      ring.style.height   = '38px';
    });
  });
}

// ── SCROLL REVEAL ──
const revealEls = document.querySelectorAll('.reveal');
if (revealEls.length) {
  const revealObs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.12 });
  revealEls.forEach(el => revealObs.observe(el));
}

// ── FORM SUBMIT BUTTON ──
const submitBtn = document.querySelector('.premium-submit-btn');
if (submitBtn) {
  submitBtn.addEventListener('click', function () {
    const span = this.querySelector('span');
    if (span) {
      span.textContent = '✓ Sent!';
      setTimeout(() => { span.textContent = 'Send Message'; }, 2000);
    }
  });
}

// ── HAMBURGER MENU ──
document.addEventListener('DOMContentLoaded', () => {
  const hamburger     = document.getElementById('hamburger');
  const mobileOverlay = document.getElementById('mobileNavOverlay');

  if (!hamburger || !mobileOverlay) return;

  // Toggle open/close
  hamburger.addEventListener('click', function () {
    const isOpen = hamburger.classList.toggle('open');
    mobileOverlay.classList.toggle('open', isOpen);
    hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  // Accordion dropdowns inside mobile menu
  document.querySelectorAll('.mobile-dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      const parentLi = this.closest('li');
      const wasOpen  = parentLi.classList.contains('open');
      // close all siblings first
      document.querySelectorAll('.mobile-nav-links > li').forEach(li => {
        if (li !== parentLi) li.classList.remove('open');
      });
      parentLi.classList.toggle('open', !wasOpen);
    });
  });

  // Close menu when a normal link is clicked
  mobileOverlay.querySelectorAll('a:not(.mobile-dropdown-toggle)').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('open');
      mobileOverlay.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });

  // Close on resize back to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth > 900) {
      hamburger.classList.remove('open');
      mobileOverlay.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  });
});