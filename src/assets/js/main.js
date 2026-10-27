/* Connect-Air — comportamento da página.
   Sem biblioteca. Nada aqui é necessário para ler a página: se o script falhar,
   todo o conteúdo continua visível e todos os links continuam funcionando. */
(function () {
  'use strict';

  document.documentElement.classList.add('js');

  var quieter = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Entradas discretas por seção ------------------------------------- */
  var risers = document.querySelectorAll('[data-rise]');
  if (!('IntersectionObserver' in window) || quieter) {
    risers.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (e, i) {
        if (!e.isIntersecting) return;
        var el = e.target;
        setTimeout(function () { el.classList.add('is-in'); }, i * 75);
        seen.unobserve(el);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    risers.forEach(function (el) { seen.observe(el); });
  }

  /* --- Serviços: o nome apontado escreve na coluna vazia ----------------- */
  var echo = document.getElementById('services-echo');
  if (echo) {
    var resting = echo.textContent;
    document.querySelectorAll('.services__list button').forEach(function (b) {
      function show() { echo.textContent = b.dataset.echo; }
      function rest() { echo.textContent = resting; }
      b.addEventListener('mouseenter', show);
      b.addEventListener('focus', show);
      b.addEventListener('mouseleave', rest);
      b.addEventListener('blur', rest);
      b.addEventListener('click', show);
    });
  }

  /* --- Os sistemas: a lista ativa troca a fotografia fixa ---------------- */
  var list  = document.getElementById('systems-list');
  var photo = document.getElementById('systems-photo');

  if (list && photo) {
    var rows = Array.prototype.slice.call(list.querySelectorAll('.systems__row'));

    /* com script, só o sistema ativo fica aberto */
    rows.forEach(function (row, i) {
      var panel = row.querySelector('.systems__panel');
      if (panel) panel.hidden = i !== 0;
      var btn = row.querySelector('button');
      if (btn) btn.setAttribute('aria-expanded', String(i === 0));
    });

    function widthsFor(stem) {
      return stem === 'duto-1957' || stem === 'casa-de-maquinas'
        ? [420, 840] : [520, 1040];
    }

    function activate(row) {
      if (row.dataset.active === 'true') return;

      rows.forEach(function (r) {
        var on = r === row;
        r.dataset.active = on ? 'true' : 'false';
        var p = r.querySelector('.systems__panel');
        var b = r.querySelector('button');
        if (p) p.hidden = !on;
        if (b) b.setAttribute('aria-expanded', String(on));
      });

      var stem = row.dataset.photo;
      if (!stem) return;
      var w = widthsFor(stem);
      var swap = function () {
        photo.src = 'assets/img/' + stem + '-' + w[0] + '.webp';
        photo.srcset = 'assets/img/' + stem + '-' + w[0] + '.webp ' + w[0] + 'w, ' +
                       'assets/img/' + stem + '-' + w[1] + '.webp ' + w[1] + 'w';
        photo.alt = row.dataset.alt || '';
        photo.classList.remove('is-fading');
      };

      if (quieter) { swap(); return; }
      photo.classList.add('is-fading');
      window.setTimeout(swap, 300);
    }

    rows.forEach(function (row) {
      var btn = row.querySelector('button');
      if (!btn) return;
      btn.addEventListener('click', function () { activate(row); });
      btn.addEventListener('mouseenter', function () { activate(row); });
      btn.addEventListener('focus', function () { activate(row); });
    });
  }

  /* --- O flutuante recua onde o cartão de contato já oferece o WhatsApp -- */
  var float_ = document.getElementById('wa-flutuante');
  var contact = document.getElementById('contato');
  if (float_ && contact && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        float_.classList.toggle('is-away', e.isIntersecting);
      });
    }, { threshold: 0.3 }).observe(contact);
  }

  /* --- Credenciamentos: um nome aceso de cada vez ------------------------ */
  var names = document.querySelectorAll('.creds__name');
  if (names.length && !quieter) {
    var at = 0, timer = null;
    var creds = document.querySelector('.creds');

    function step() {
      names.forEach(function (n) { n.classList.remove('is-lit'); });
      names[at].classList.add('is-lit');
      at = (at + 1) % names.length;
    }

    /* só corre enquanto a seção está à vista */
    if ('IntersectionObserver' in window && creds) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && !timer) { step(); timer = setInterval(step, 2000); }
          else if (!e.isIntersecting && timer) { clearInterval(timer); timer = null; }
        });
      }, { threshold: 0.2 }).observe(creds);
    } else {
      step(); setInterval(step, 2000);
    }
  }
})();
