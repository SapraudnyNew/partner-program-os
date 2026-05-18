/* Sidebar Component — Partner Program OS v2 */
(function () {
  'use strict';
  var hamburger = document.querySelector('.hamburger');
  var sidebar = document.querySelector('.sidebar');
  var overlay = document.querySelector('.sidebar-overlay');

  function openSidebar() {
    sidebar && sidebar.classList.add('open');
    overlay && overlay.classList.add('visible');
    document.body.style.overflow = 'hidden';
  }
  function closeSidebar() {
    sidebar && sidebar.classList.remove('open');
    overlay && overlay.classList.remove('visible');
    document.body.style.overflow = '';
  }
  hamburger && hamburger.addEventListener('click', function () {
    sidebar && sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
  });
  overlay && overlay.addEventListener('click', closeSidebar);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSidebar(); });

  // Collapsible sections
  document.querySelectorAll('.sidebar__heading').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var list = this.nextElementSibling;
      if (!list) return;
      var isCollapsed = list.classList.contains('collapsed');
      if (isCollapsed) {
        list.classList.remove('collapsed');
        list.style.maxHeight = list.scrollHeight + 'px';
        this.classList.remove('collapsed');
      } else {
        list.classList.add('collapsed');
        list.style.maxHeight = '0';
        this.classList.add('collapsed');
      }
    });
  });
  document.querySelectorAll('.sidebar__list').forEach(function (l) { l.style.maxHeight = l.scrollHeight + 'px'; });

  // Highlight current page
  var cur = window.location.pathname.replace(/\/index\.html$/, '/').replace(/\/$/, '') || '/';
  document.querySelectorAll('.sidebar__item a').forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href) return;
    var lp = new URL(href, window.location.origin + window.location.pathname).pathname;
    lp = lp.replace(/\/index\.html$/, '/').replace(/\/$/, '') || '/';
    if (lp === cur) {
      link.classList.add('active');
      var parent = link.closest('.sidebar__list');
      while (parent) {
        parent.classList.remove('collapsed');
        parent.style.maxHeight = parent.scrollHeight + 'px';
        var h = parent.previousElementSibling;
        if (h && h.classList.contains('sidebar__heading')) h.classList.remove('collapsed');
        parent = parent.parentElement && parent.parentElement.closest('.sidebar__list');
      }
      setTimeout(function () { link.scrollIntoView({ block: 'center', behavior: 'smooth' }); }, 100);
    }
  });
  if (window.innerWidth <= 768) {
    document.querySelectorAll('.sidebar__item a').forEach(function (l) { l.addEventListener('click', closeSidebar); });
  }
})();
