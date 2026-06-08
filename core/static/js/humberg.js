/* ============================================================
   HAMBURGER MENU JS — Add to base.html script block,
   OR append to your index.js file
   ============================================================ */

(function () {
  /* ─ Hamburger toggle ─ */
  const toggle = document.getElementById('navToggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      const open = navLinks.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });

    /* Close on outside click */
    document.addEventListener('click', (e) => {
      if (!toggle.contains(e.target) && !navLinks.contains(e.target)) {
        navLinks.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });

    /* Close on nav link click */
    navLinks.querySelectorAll('a:not(.nav-item > a)').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        toggle.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ─ Mobile dropdown accordion ─ */
  document.querySelectorAll('.nav-item > a').forEach(link => {
    link.addEventListener('click', (e) => {
      /* Only accordion on mobile */
      if (window.innerWidth > 768) return;
      e.preventDefault();
      const parent = link.closest('.nav-item');
      const wasOpen = parent.classList.contains('open');
      /* Close all others */
      document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) parent.classList.add('open');
    });
  });

  /* ─ Close menu on resize back to desktop ─ */
  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
      navLinks && navLinks.classList.remove('open');
      toggle && toggle.classList.remove('open');
      document.body.style.overflow = '';
      document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('open'));
    }
  });
})();