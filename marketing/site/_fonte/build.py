"""
Gera o site estático da Mariana Salvati Advocacia.

Cada página fica em _fonte/paginas/<nome>.html. A primeira linha é um comentário
com os metadados em JSON:  <!--meta {"caminho": "/sobre/", "titulo": "...", ...} -->
O resto do arquivo é o conteúdo do <main>. Cabeçalho, menu, rodapé e <head> são
iguais em todas as páginas e saem daqui.

Uso (na pasta marketing/site):   python _fonte/build.py
"""
import json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTE = os.path.join(RAIZ, '_fonte', 'paginas')
DOMINIO = 'https://marianasalvati.adv.br'
CTA = 'Fale com uma advogada especialista em busca e apreensão de veículo'

MENU = [
    ('/', 'Início'),
    ('/busca-e-apreensao-de-veiculo/', 'Como funciona'),
    ('/advogada-busca-e-apreensao/', 'Atendimento'),
    ('/sobre/', 'Sobre'),
    ('/contato/', 'Contato'),
]

ESTRELA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m12 2.8 2.8 6 6.5.6-4.9 4.3 1.5 6.4L12 16.8 6.1 20.1l1.5-6.4-4.9-4.3 6.5-.6z"/></svg>'


def bloco_avaliacoes():
    """Avaliações reais do Google. Sem avaliações cadastradas, mostra só o convite para ver o perfil."""
    d = json.load(open(os.path.join(RAIZ, '_fonte', 'avaliacoes.json'), encoding='utf-8'))
    perfil = d['perfil_google']
    lista = d.get('avaliacoes') or []
    resumo = ''
    if d.get('nota') and d.get('total'):
        resumo = (f'<div class="nota-google"><strong>{str(d["nota"]).replace(".", ",")}</strong>'
                  f'<span class="estrelas">{ESTRELA * 5}</span><small>{d["total"]} avaliações no Google</small></div>')
    cards = ''
    for a in lista[:12]:
        n = int(a.get('estrelas', 5))
        cards += (f'<figure class="avaliacao"><div class="g"><span class="estrelas" aria-label="{n} de 5 estrelas">{ESTRELA * n}</span><svg class="logo-g" aria-label="Google"><use href="#i-google"/></svg></div>'
                  f'<blockquote>{a["texto"]}</blockquote>'
                  f'<figcaption><strong>{a["nome"]}</strong>{a.get("quando", "")}</figcaption></figure>')
    # Carrossel contínuo: duas cópias da lista lado a lado, a trilha anda 50% e recomeça sem emenda
    grade = (f'<div class="avaliacoes-carrossel"><div class="avaliacoes-trilho" style="--duracao:{max(30, len(lista[:12]) * 9)}s">'
             f'<div class="avaliacoes">{cards}</div><div class="avaliacoes" aria-hidden="true">{cards}</div>'
             f'</div></div>') if cards else ''
    sub = ('O que os clientes contam sobre o atendimento.' if cards
           else 'Veja o que os clientes contam sobre o atendimento no perfil oficial do escritório no Google.')
    return f'''<section class="sec sec-branca" id="avaliacoes">
  <div class="wrap">
    <div class="avaliacoes-topo">
      <div>
        <div class="rotulo">Avaliações no Google</div>
        <h2 class="sec-titulo">Quem já foi atendido</h2>
        <p class="sec-sub">{sub}</p>
      </div>
      {resumo}
    </div>
    {grade}
    <div class="avaliacoes-acoes">
      <a class="btn btn-contorno" href="{perfil}" target="_blank" rel="noopener"><svg><use href="#i-google"/></svg>Ver avaliações no Google</a>
      <a class="link-avaliar" href="{perfil}" target="_blank" rel="noopener">Já é cliente? Deixe a sua avaliação →</a>
    </div>
  </div>
</section>'''


SVG = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-whats" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.7.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.2-.3-.2-.5-.4Z"/></symbol>
  <symbol id="i-carro" viewBox="0 0 32 32"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 20v-4l2.5-6a2 2 0 0 1 1.8-1.2h13.4a2 2 0 0 1 1.8 1.2L27 16v4"/><path d="M4 16h24v6a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/><circle cx="9.5" cy="23.5" r="2.5"/><circle cx="22.5" cy="23.5" r="2.5"/></g></symbol>
  <symbol id="i-carta" viewBox="0 0 32 32"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="5" y="8" width="22" height="16" rx="1.5"/><path d="m5 9.5 11 8 11-8"/></g></symbol>
  <symbol id="i-martelo" viewBox="0 0 32 32"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m14 6 8 8M10.5 9.5l8 8M12.5 7.5l6-6 8 8-6 6M16 16 6 26"/><path d="M4 28h12"/></g></symbol>
  <symbol id="i-guincho" viewBox="0 0 32 32"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 22V12h7l3 5h4V22"/><path d="M17 17h12v5H17"/><path d="m13 12 9-6 4 3"/><circle cx="8" cy="23.5" r="2.5"/><circle cx="24" cy="23.5" r="2.5"/></g></symbol>
  <symbol id="i-relogio" viewBox="0 0 32 32"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="16" cy="17" r="10"/><path d="M16 11v6l4 3M13 3h6"/></g></symbol>
  <symbol id="i-telefone" viewBox="0 0 32 32"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M11 4H7.5A2.5 2.5 0 0 0 5 6.6C5.6 18 14 26.4 25.4 27a2.5 2.5 0 0 0 2.6-2.5V21l-5.5-2.2-2.7 2.7a17 17 0 0 1-8.3-8.3l2.7-2.7z"/></symbol>
  <symbol id="i-local" viewBox="0 0 32 32"><g fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16 29s9-8.2 9-15a9 9 0 0 0-18 0c0 6.8 9 15 9 15Z"/><circle cx="16" cy="14" r="3.2"/></g></symbol>
  <symbol id="i-google" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.5 12.3c0-.8-.1-1.5-.2-2.2H12v4.2h5.9a5 5 0 0 1-2.2 3.3v2.7h3.5c2.1-1.9 3.3-4.7 3.3-8z"/><path fill="#34A853" d="M12 23c3 0 5.5-1 7.3-2.7l-3.5-2.7c-1 .7-2.3 1.1-3.8 1.1-2.9 0-5.4-2-6.3-4.7H2.1v2.8A11 11 0 0 0 12 23z"/><path fill="#FBBC05" d="M5.7 14a6.6 6.6 0 0 1 0-4.2V7H2.1a11 11 0 0 0 0 9.9z"/><path fill="#EA4335" d="M12 5.4c1.6 0 3.1.6 4.2 1.7l3.2-3.2A11 11 0 0 0 2.1 7l3.6 2.8C6.6 7.3 9.1 5.4 12 5.4z"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></symbol>
</svg>'''


def rel(prefixo, caminho):
    """Link relativo (funciona aberto direto do disco e publicado na raiz do domínio)."""
    alvo = caminho.strip('/')
    return prefixo + (alvo + '/' if alvo else '') + ('index.html' if LOCAL else '')


def cabecalho(prefixo, atual):
    itens = ''.join(
        '<a href="%s"%s>%s</a>' % (rel(prefixo, c), ' aria-current="page"' if c == atual else '', n)
        for c, n in MENU)
    return f'''<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="cabecalho">
  <div class="wrap">
    <a class="marca" href="{rel(prefixo, '/')}"><picture><source media="(max-width: 820px)" srcset="{prefixo}img/logo-principal-claro.png"><img src="{prefixo}img/logo-horizontal-claro.png" alt="Mariana Salvati Advocacia &amp; Consultoria" width="379" height="24"></picture></a>
    <button class="menu-botao" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu"><svg><use href="#i-menu"/></svg></button>
    <nav class="menu" id="menu" aria-label="Principal">{itens}<a class="btn btn-whats js-whats" data-situacao="geral" href="#"><svg><use href="#i-whats"/></svg>WhatsApp</a></nav>
  </div>
</header>'''


def rodape(prefixo):
    links = ''.join('<a href="%s">%s</a>' % (rel(prefixo, c), n) for c, n in MENU)
    artigos = ''.join('<a href="%s">%s</a>' % (rel(prefixo, c), n) for c, n in [
        ('/busca-e-apreensao-de-veiculo/notificacao-extrajudicial-o-que-fazer/', 'Recebi a notificação. E agora?'),
        ('/busca-e-apreensao-de-veiculo/carro-apreendido-como-recuperar/', 'Meu carro foi apreendido'),
        ('/busca-e-apreensao-de-veiculo/', 'Como funciona a busca e apreensão'),
    ])
    return f'''<footer>
  <div class="padrao" aria-hidden="true"></div>
  <div class="wrap">
    <div class="rodape-logo"><img src="{prefixo}img/logo-principal-claro.png" alt="Mariana Salvati Advocacia &amp; Consultoria" width="600" height="160" loading="lazy"></div>
    <nav aria-label="Rodapé"><b>Navegação</b>{links}</nav>
    <nav aria-label="Artigos"><b>Artigos</b>{artigos}</nav>
    <div>
      <b>Escritório</b>
      <p><strong>Mariana Salvati Sociedade Individual de Advocacia</strong></p>
      <p>CNPJ 65.564.592/0001-10</p>
      <p>Estrada João Passuelo, 641 · Vila Nova<br>Porto Alegre/RS · CEP 91740-550</p>
      <p><a href="mailto:contato@marianasalvati.adv.br">contato@marianasalvati.adv.br</a><br>(51) 99207-4913</p>
      <p><a href="{json.load(open(os.path.join(RAIZ, '_fonte', 'avaliacoes.json'), encoding='utf-8'))['perfil_google']}" target="_blank" rel="noopener">Perfil no Google</a> · <a href="{rel(prefixo, '/politica-de-privacidade/')}">Política de privacidade</a></p>
    </div>
    <p class="rodape-oab">Responsável técnica: Mariana Battimanza Salvati · OAB/RS 139.028. Conteúdo de caráter informativo, conforme o Provimento 205/2021 do Conselho Federal da OAB. Não constitui promessa de resultado nem substitui a análise individual do caso.</p>
  </div>
</footer>

<div class="rodape-final">
  <div class="wrap">
    <p>Este site não faz parte do Google nem do Facebook ou do Facebook Inc. Além disso, não oferecemos nenhum tipo de serviço oficial do governo, NÃO praticamos fraude, não somos uma empresa que vende criptoativos ou qualquer outro serviço.</p>
    <p>Essa empresa trabalha exclusivamente com serviços jurídicos.</p>
    <p>Nós NÃO compartilharemos seus dados com ninguém.</p>
    <p>© Todos os Direitos Reservados 2026 | <a href="https://www.instagram.com/idvgrowth/" target="_blank" rel="noopener">Feito por @idvgrowth</a>.</p>
  </div>
</div>

<div class="barra-fixa"><a class="btn btn-whats js-whats" data-situacao="geral" href="#"><svg><use href="#i-whats"/></svg>{CTA}</a></div>'''


def cabeca(meta, prefixo):
    url = DOMINIO + meta['caminho']
    schemas = ''.join('<script type="application/ld+json">%s</script>\n' % json.dumps(s, ensure_ascii=False, indent=1)
                      for s in meta.get('schema', []))
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta['titulo']}</title>
<meta name="description" content="{meta['descricao']}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#161B1E">
<meta property="og:type" content="{meta.get('og_tipo', 'website')}">
<meta property="og:title" content="{meta['titulo']}">
<meta property="og:description" content="{meta['descricao']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/img/compartilhar.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefixo}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="{prefixo}img/favicon-48.png">
<link rel="apple-touch-icon" href="{prefixo}img/apple-touch-icon.png">
<!-- Google Search Console: se for verificar por meta tag, cole aqui -->
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Mariana Salvati Advocacia">
<!-- Google Tag Manager: trocar GTM-XXXXXXX pelo ID real -->
<script>
  window.dataLayer = window.dataLayer || [];
  (function(w,d,s,l,i){{if(i.indexOf('XXXX')>-1)return;w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});
  var f=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i;
  f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-XXXXXXX');
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefixo}assets/site.css">
{schemas}</head>'''


def gerar():
    paginas = sorted(f for f in os.listdir(FONTE) if f.endswith('.html'))
    urls = []
    for nome in paginas:
        bruto = open(os.path.join(FONTE, nome), encoding='utf-8').read()
        m = re.match(r'<!--meta\s*(\{.*?\})\s*-->\s*', bruto, re.S)
        meta = json.loads(m.group(1))
        corpo = bruto[m.end():]
        caminho = meta['caminho']
        prof = len([p for p in caminho.strip('/').split('/') if p])
        prefixo = '../' * prof
        if caminho == '/404/':
            prefixo = '/'  # a 404 é servida em qualquer URL, então usa caminhos absolutos
        corpo = corpo.replace('{{AVALIACOES}}', bloco_avaliacoes())
        corpo = corpo.replace('{{P}}', prefixo).replace('{{CTA}}', CTA)
        corpo = re.sub(r'\{\{L:(.*?)\}\}', lambda x: rel(prefixo, x.group(1)), corpo)
        html = (cabeca(meta, prefixo) + '\n<body>\n' + SVG + '\n' + cabecalho(prefixo, meta.get('menu', caminho))
                + '\n\n<main id="conteudo">\n' + corpo.strip() + '\n</main>\n\n' + rodape(prefixo)
                + f'\n\n<script src="{prefixo}assets/site.js"></script>\n</body>\n</html>\n')
        destino = os.path.join(RAIZ, *[p for p in caminho.strip('/').split('/') if p], 'index.html') \
            if caminho != '/404/' else os.path.join(RAIZ, '404.html')
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        open(destino, 'w', encoding='utf-8').write(html)
        if not meta.get('fora_do_sitemap'):
            urls.append((caminho, meta.get('prioridade', '0.7')))
        print('ok', caminho)
    if not LOCAL:
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for c, pr in urls:
            sm.append(f'  <url><loc>{DOMINIO}{c}</loc><lastmod>2026-10-14</lastmod><priority>{pr}</priority></url>')
        sm.append('</urlset>')
        open(os.path.join(RAIZ, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
        open(os.path.join(RAIZ, 'robots.txt'), 'w', encoding='utf-8').write(
            # a LP do Ads (/buscaeapreensao/) não é bloqueada aqui: ela já tem "noindex", e o Google precisa rastreá-la para ver isso
            'User-agent: *\nAllow: /\n\nSitemap: ' + DOMINIO + '/sitemap.xml\n')


# --local: links terminam em index.html (para abrir os arquivos direto do disco e revisar)
LOCAL = '--local' in sys.argv
gerar()
