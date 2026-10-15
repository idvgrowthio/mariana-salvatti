/* Mariana Salvati Advocacia — comportamento do site */
(function () {
  var NUMERO = '5551992074913';
  var MENSAGENS = {
    atraso: 'Olá, Dra. Mariana. Estou com parcelas do financiamento do meu veículo em atraso e gostaria de orientação.',
    notificacao: 'Olá, Dra. Mariana. Recebi uma notificação sobre o financiamento do meu veículo e gostaria de uma análise.',
    acao: 'Olá, Dra. Mariana. Fui citado em uma ação de busca e apreensão do meu veículo e preciso de orientação.',
    apreendido: 'Olá, Dra. Mariana. Meu veículo financiado foi apreendido e gostaria de entender o que pode ser feito.',
    geral: 'Olá, Dra. Mariana. Encontrei o seu site e preciso de orientação sobre busca e apreensão de veículo.'
  };
  window.dataLayer = window.dataLayer || [];

  function linkWhats(sit) {
    return 'https://wa.me/' + NUMERO + '?text=' + encodeURIComponent(MENSAGENS[sit] || MENSAGENS.geral);
  }

  // Botões de WhatsApp: link + evento de conversão (situação lida no momento do clique)
  document.querySelectorAll('.js-whats').forEach(function (el) {
    el.href = linkWhats(el.getAttribute('data-situacao'));
    el.target = '_blank';
    el.rel = 'noopener';
    el.addEventListener('click', function () {
      window.dataLayer.push({ event: 'clique_whatsapp', situacao: el.getAttribute('data-situacao') || 'geral', pagina: location.pathname });
    });
  });

  // Menu do celular
  var botao = document.querySelector('.menu-botao'), menu = document.querySelector('.menu');
  if (botao && menu) {
    botao.addEventListener('click', function () {
      var aberto = menu.classList.toggle('aberto');
      botao.setAttribute('aria-expanded', aberto ? 'true' : 'false');
    });
  }

  // Barra fixa do celular aparece depois do primeiro bloco
  var barra = document.querySelector('.barra-fixa'), primeiro = document.querySelector('.hero, .topo-pagina');
  if (barra && primeiro) {
    var checar = function () { barra.classList.toggle('visivel', primeiro.getBoundingClientRect().bottom < 60); };
    addEventListener('scroll', checar, { passive: true });
    checar();
  }

  // Linha do tempo animada (se houver na página)
  var estrada = document.querySelector('.estrada');
  if (estrada) {
    var paradas = [].slice.call(estrada.querySelectorAll('.parada'));
    var sits = ['atraso', 'notificacao', 'acao', 'apreendido', 'apreendido'];
    var cta = document.getElementById('cta-etapas');
    var atual = 0, pausado = false, visivel = false;
    var semMovimento = matchMedia('(prefers-reduced-motion: reduce)').matches;
    var posicionar = function () {
      var er = estrada.getBoundingClientRect();
      var pr = paradas[atual].querySelector('.parada-ponto').getBoundingClientRect();
      if (matchMedia('(max-width: 820px)').matches) {
        estrada.style.setProperty('--prog', Math.max(0, pr.top + pr.height / 2 - er.top - 30) + 'px');
      } else {
        var x = pr.left + pr.width / 2 - er.left;
        estrada.style.setProperty('--pin-x', x + 'px');
        estrada.style.setProperty('--prog', Math.max(0, x - 30) + 'px');
      }
    };
    var ativar = function (n) {
      atual = n;
      paradas.forEach(function (p, k) {
        p.classList.toggle('ativa', k === n);
        p.classList.toggle('passou', k < n);
      });
      posicionar();
      if (cta) { cta.setAttribute('data-situacao', sits[n]); cta.href = linkWhats(sits[n]); }
    };
    paradas.forEach(function (p, k) {
      ['mouseenter', 'focus', 'click'].forEach(function (ev) {
        p.addEventListener(ev, function () { pausado = true; ativar(k); });
      });
    });
    estrada.addEventListener('mouseleave', function () { pausado = false; });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) { visivel = e[0].isIntersecting; }, { threshold: .35 }).observe(estrada);
    } else { visivel = true; }
    addEventListener('resize', posicionar);
    ativar(0);
    if (!semMovimento) {
      setInterval(function () { if (!pausado && visivel) ativar((atual + 1) % paradas.length); }, 2800);
    }
  }
})();
