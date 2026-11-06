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

    /* rede de segurança: nada de conteúdo preso em opacity 0.
       Se o observer não disparar para algum elemento (rolagem muito rápida,
       captura de tela de página inteira, impressão), tudo aparece assim mesmo. */
    window.setTimeout(function () {
      risers.forEach(function (el) { el.classList.add('is-in'); });
    }, 2500);
    window.addEventListener('beforeprint', function () {
      risers.forEach(function (el) { el.classList.add('is-in'); });
    });
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

  /* --- Origem do visitante nos links de WhatsApp -------------------------
     Visita vinda de anúncio traz utm_* ou gclid na URL. O WhatsApp não aceita
     parâmetros de campanha, então a origem entra como uma linha no fim da
     mensagem já escrita: é assim que a Connect-Air sabe de onde veio o contato.
     Guardado na sessão para sobreviver à rolagem e a cliques internos. */
  var ORIGEM = (function () {
    var CHAVE = 'ca:origem';
    var guardada = null;
    try { guardada = window.sessionStorage.getItem(CHAVE); } catch (e) {}

    var q = new URLSearchParams(window.location.search);
    var gclid = q.get('gclid');
    var fonte = q.get('utm_source');
    var campanha = q.get('utm_campaign');
    var termo = q.get('utm_term');

    var partes = [];
    if (gclid) partes.push('Google Ads');
    else if (fonte) partes.push(fonte);
    if (campanha) partes.push(campanha);
    if (termo) partes.push('"' + termo + '"');

    var atual = partes.length ? partes.join(' · ') : null;
    if (atual) {
      try { window.sessionStorage.setItem(CHAVE, atual); } catch (e) {}
      return atual;
    }
    return guardada;
  })();

  if (ORIGEM) {
    var sufixo = '\n\n(origem: ' + ORIGEM + ')';
    document.querySelectorAll('a[href*="wa.me"]').forEach(function (a) {
      var u;
      try { u = new URL(a.href); } catch (e) { return; }
      var texto = u.searchParams.get('text');
      if (!texto || texto.indexOf('(origem:') !== -1) return;
      u.searchParams.set('text', texto + sufixo);
      a.href = u.toString();
    });
  }

})();
