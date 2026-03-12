/**
 * interactions.js
 * Overlay interactivity: popover, hovercard, toast, cmd+k
 */

document.addEventListener('DOMContentLoaded', () => {

  // ── POPOVER ──────────────────────────────────────────
  // Any button with data-popover="id" toggles that popover
  document.querySelectorAll('[data-popover]').forEach(trigger => {
    const targetId = trigger.dataset.popover;
    const popover = document.getElementById(targetId);
    if (!popover) return;

    trigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isHidden = popover.classList.contains('popover-hidden');
      // Close all open popovers first
      document.querySelectorAll('.popover-content:not(.popover-hidden)').forEach(p => {
        p.classList.add('popover-hidden');
      });
      if (isHidden) {
        popover.classList.remove('popover-hidden');
      }
    });
  });

  // Click outside closes all popovers
  document.addEventListener('click', () => {
    document.querySelectorAll('.popover-content:not(.popover-hidden)').forEach(p => {
      p.classList.add('popover-hidden');
    });
  });

  // Prevent clicks inside popover from closing it
  document.querySelectorAll('.popover-content').forEach(p => {
    p.addEventListener('click', e => e.stopPropagation());
  });


  // ── HOVER CARD ───────────────────────────────────────
  let hovercardTimer = null;

  document.querySelectorAll('[data-hovercard-host]').forEach(host => {
    const card = host.querySelector('.hover-card-content');
    if (!card) return;

    host.addEventListener('mouseenter', () => {
      clearTimeout(hovercardTimer);
      card.classList.remove('hovercard-hidden');
    });

    host.addEventListener('mouseleave', () => {
      hovercardTimer = setTimeout(() => {
        card.classList.add('hovercard-hidden');
      }, 150);
    });
  });


  // ── TOAST ────────────────────────────────────────────
  const toastViewport = document.getElementById('live-toast-viewport');

  function showToast({ title, desc, action, variant = '' }) {
    if (!toastViewport) return;

    const toast = document.createElement('div');
    toast.className = `toast ${variant}`;
    toast.dataset.state = 'open';
    toast.innerHTML = `
      <div class="toast-title">${title}</div>
      ${desc ? `<div class="toast-desc">${desc}</div>` : ''}
      ${action ? `<button class="toast-action btn btn-sm ${variant === 'destructive' ? 'btn-danger' : 'btn-secondary'}">${action}</button>` : ''}
      <div class="toast-close" role="button" aria-label="Close">✕</div>
    `;

    // Slide-in: start translated, then animate to position
    toast.style.transform = 'translateX(calc(100% + 24px))';
    toast.style.transition = 'transform 200ms ease';
    toastViewport.appendChild(toast);

    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        toast.style.transform = 'translateX(0)';
      });
    });

    function dismiss() {
      toast.style.transform = 'translateX(calc(100% + 24px))';
      toast.addEventListener('transitionend', () => toast.remove(), { once: true });
    }

    toast.querySelector('.toast-close').addEventListener('click', dismiss);
    setTimeout(dismiss, 4000);
  }

  const triggerBtn = document.getElementById('toast-trigger');
  if (triggerBtn) {
    triggerBtn.addEventListener('click', () => {
      showToast({
        title: 'Board updated',
        desc: 'Aerospace v2 — 14 images indexed.',
        action: 'Undo',
      });
    });
  }

  const triggerMiniBtn = document.getElementById('toast-trigger-mini');
  if (triggerMiniBtn) {
    triggerMiniBtn.addEventListener('click', () => {
      showToast({
        title: 'System check complete',
        variant: 'toast-mini',
      });
    });
  }

  const triggerErrBtn = document.getElementById('toast-trigger-err');
  if (triggerErrBtn) {
    triggerErrBtn.addEventListener('click', () => {
      showToast({
        title: 'Upload failed',
        desc: '2 images could not be processed.',
        action: 'Retry',
        variant: 'destructive',
      });
    });
  }


  // ── CMD+K ────────────────────────────────────────────
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      const cmdSection = document.getElementById('cmd');
      if (!cmdSection) return;

      cmdSection.scrollIntoView({ behavior: 'smooth', block: 'center' });

      // Brief amber flash on the cmd-dialog
      const dialog = cmdSection.querySelector('.cmd-dialog');
      if (dialog) {
        dialog.style.transition = 'box-shadow 150ms ease';
        dialog.style.boxShadow = '0 0 0 2px var(--accent)';
        setTimeout(() => {
          dialog.style.boxShadow = '';
        }, 600);
      }
    }
  });


  // ── STAGGERED SECTION REVEALS ─────────────────────────
  const sections = document.querySelectorAll('.kit-section');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.05 });

  sections.forEach((section, i) => {
    section.style.transitionDelay = `${i * 20}ms`;
    revealObserver.observe(section);
  });

});
