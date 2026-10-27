/* Connect-Air — comportamento da página.
   Sem biblioteca. Nada aqui é necessário para ler a página nem para falar com
   a empresa: se o script falhar, todo o conteúdo continua visível e todos os
   links continuam funcionando. */
(function () {
  'use strict';

  document.documentElement.classList.add('js');

  var quieter = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  /* --- Entradas discretas por parte de seção ----------------------------- */
  var risers = document.querySelectorAll('[data-rise]');
  if (!hasIO || quieter) {
    risers.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (e, i) {
        if (!e.isIntersecting) return;
        var el = e.target;
        setTimeout(function () { el.classList.add('is-in'); }, i * 70);
        seen.unobserve(el);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });
    risers.forEach(function (el) { seen.observe(el); });
  }

  /* --- A barra ganha um fio ao descolar do topo -------------------------- */
  var bar = document.getElementById('bar');
  if (bar) {
    var onScroll = function () {
      bar.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* --- Navegação: marca a seção em que o visitante está ------------------ */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.bar__nav a'));
  if (navLinks.length && hasIO) {
    var byId = {};
    var watched = [];
    navLinks.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      var sec = document.getElementById(id);
      if (sec) { byId[id] = a; watched.push(sec); }
    });

    var visible = {};
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });
      var current = null;
      for (var i = 0; i < watched.length; i++) {
        if (visible[watched[i].id]) { current = watched[i].id; break; }
      }
      navLinks.forEach(function (a) { a.removeAttribute('aria-current'); });
      if (current && byId[current]) byId[current].setAttribute('aria-current', 'true');
    }, { rootMargin: '-45% 0px -45% 0px' });

    watched.forEach(function (s) { spy.observe(s); });
  }

  /* --- Serviços: o nome apontado escreve na coluna vazia ----------------- */
  var echo = document.getElementById('svc-echo');
  if (echo) {
    var resting = echo.textContent;
    document.querySelectorAll('.svc__list button').forEach(function (b) {
      var show = function () { echo.textContent = b.dataset.echo; };
      var rest = function () { echo.textContent = resting; };
      b.addEventListener('mouseenter', show);
      b.addEventListener('focus', show);
      b.addEventListener('mouseleave', rest);
      b.addEventListener('blur', rest);
      b.addEventListener('click', show);
    });
  }

  /* --- Os sistemas: a lista ativa troca a fotografia fixa ---------------- */
  var list = document.getElementById('sys-list');
  var photo = document.getElementById('sys-photo');

  if (list && photo) {
    var rows = Array.prototype.slice.call(list.querySelectorAll('.sys__row'));

    /* com script, só o sistema ativo fica aberto */
    rows.forEach(function (row, i) {
      var panel = row.querySelector('.sys__panel');
      var btn = row.querySelector('button');
      if (panel) panel.hidden = i !== 0;
      if (btn) btn.setAttribute('aria-expanded', String(i === 0));
    });

    var activate = function (row) {
      if (row.dataset.active === 'true') return;

      rows.forEach(function (r) {
        var on = r === row;
        r.dataset.active = on ? 'true' : 'false';
        var p = r.querySelector('.sys__panel');
        var b = r.querySelector('button');
        if (p) p.hidden = !on;
        if (b) b.setAttribute('aria-expanded', String(on));
      });

      var stem = row.dataset.photo;
      var w = (row.dataset.w || '').split(',');
      if (!stem || w.length !== 2) return;

      var swap = function () {
        photo.src = 'assets/img/' + stem + '-' + w[0] + '.webp';
        photo.srcset = 'assets/img/' + stem + '-' + w[0] + '.webp ' + w[0] + 'w, ' +
                       'assets/img/' + stem + '-' + w[1] + '.webp ' + w[1] + 'w';
        photo.alt = row.dataset.alt || '';
        photo.classList.remove('is-fading');
      };

      if (quieter) { swap(); return; }
      photo.classList.add('is-fading');
      window.setTimeout(swap, 280);
    };

    rows.forEach(function (row) {
      var btn = row.querySelector('button');
      if (!btn) return;
      btn.addEventListener('click', function () { activate(row); });
      btn.addEventListener('mouseenter', function () { activate(row); });
      btn.addEventListener('focus', function () { activate(row); });
    });
  }

  /* --- O flutuante recua onde o contato já oferece o WhatsApp ------------ */
  var float_ = document.getElementById('wa-flutuante');
  var contact = document.getElementById('contato');
  if (float_ && contact && hasIO) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { float_.classList.toggle('is-away', e.isIntersecting); });
    }, { threshold: 0.25 }).observe(contact);
  }

  /* --- Credenciamentos: um nome aceso de cada vez ------------------------ */
  var names = document.querySelectorAll('.creds__name');
  if (names.length && !quieter) {
    var at = 0, timer = null;
    var creds = document.querySelector('.creds');

    var step = function () {
      names.forEach(function (n) { n.classList.remove('is-lit'); });
      names[at].classList.add('is-lit');
      at = (at + 1) % names.length;
    };

    if (hasIO && creds) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && !timer) { step(); timer = setInterval(step, 1800); }
          else if (!e.isIntersecting && timer) { clearInterval(timer); timer = null; }
        });
      }, { threshold: 0.2 }).observe(creds);
    } else {
      step(); setInterval(step, 1800);
    }
  }
})();
