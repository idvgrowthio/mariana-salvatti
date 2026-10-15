"""
Monta a pasta `publicar/` (na raiz do repositório) com exatamente o que vai para o servidor:

    publicar/                     -> raiz do domínio (site institucional)
    publicar/buscaeapreensao/     -> landing page do Google Ads

No Plesk, o "Document root" do domínio aponta para httpdocs/publicar.

Uso (na raiz do projeto MazyOS):   python marketing/publicar.py
Depois: git add publicar && git commit && git push  (o Plesk puxa do GitHub)
"""
import os, shutil, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(RAIZ, 'marketing', 'site')
LP = os.path.join(RAIZ, 'marketing', 'landing-page')
SAIDA = os.path.join(RAIZ, 'publicar')
SLUG_LP = 'buscaeapreensao'

HTACCESS = r'''# Gerado por marketing/publicar.py. Não editar aqui.
Options -Indexes
ErrorDocument 404 /404.html
DirectoryIndex index.html

# Endereço antigo da LP -> novo
Redirect 301 /lp/busca-e-apreensao/ /buscaeapreensao/

AddType font/woff2 .woff2

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/xml text/plain
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 7 days"
  ExpiresByType application/javascript "access plus 7 days"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/x-icon "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
</IfModule>

<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Frame-Options "SAMEORIGIN"
</IfModule>
'''

IGNORAR_SITE = {'_fonte', 'README.md'}
IGNORAR_LP = {'README.md'}


def copiar(origem, destino, ignorar):
    os.makedirs(destino, exist_ok=True)
    for nome in os.listdir(origem):
        if nome in ignorar or nome.startswith('.'):
            continue
        o, d = os.path.join(origem, nome), os.path.join(destino, nome)
        if os.path.isdir(o):
            shutil.copytree(o, d)
        else:
            shutil.copy2(o, d)


# 1) Gera o site (links de produção, sem --local)
subprocess.run([sys.executable, '-I', os.path.join(SITE, '_fonte', 'build.py')], check=True)

# 2) Recria a pasta de publicação do zero
if os.path.isdir(SAIDA):
    shutil.rmtree(SAIDA)
copiar(SITE, SAIDA, IGNORAR_SITE)
copiar(LP, os.path.join(SAIDA, SLUG_LP), IGNORAR_LP)
open(os.path.join(SAIDA, '.htaccess'), 'w', encoding='utf-8').write(HTACCESS)

total = sum(len(f) for _, _, f in os.walk(SAIDA))
print(f'\npublicar/ pronta: {total} arquivos')
print(f'  site  -> https://marianasalvati.adv.br/')
print(f'  LP    -> https://marianasalvati.adv.br/{SLUG_LP}/')
