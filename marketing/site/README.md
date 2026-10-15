# Site: marianasalvati.adv.br

Site estático (HTML + CSS + JS, sem WordPress), na identidade da Orbe.

## Páginas (1ª entrega)

| URL | Arquivo-fonte | Alvo de SEO |
|---|---|---|
| `/` | `_fonte/paginas/01-home.html` | advogada busca e apreensão de veículo |
| `/advogada-busca-e-apreensao/` | `02-servico.html` | advogado busca e apreensão de veículo |
| `/sobre/` | `03-sobre.html` | Mariana Salvati advogada (autoria / E-E-A-T) |
| `/contato/` | `04-contato.html` | — |
| `/busca-e-apreensao-de-veiculo/` | `05-pilar.html` | **como funciona a busca e apreensão de veículo** (pilar) |
| `/busca-e-apreensao-de-veiculo/notificacao-extrajudicial-o-que-fazer/` | `06-notificacao.html` | notificação extrajudicial busca e apreensão o que fazer |
| `/busca-e-apreensao-de-veiculo/carro-apreendido-como-recuperar/` | `07-apreendido.html` | carro apreendido financiamento como recuperar |
| `404.html` | `99-404.html` | — |

Também são gerados `sitemap.xml` e `robots.txt`. Cada página tem dados estruturados: LegalService, Person, Article, FAQPage e BreadcrumbList.

## Avaliações do Google

O bloco "Quem já foi atendido" aparece na Home e em Atendimento. Os dados ficam em `_fonte/avaliacoes.json`:

```json
"nota": 5.0, "total": 12,
"avaliacoes": [
  {"nome": "Carlos M.", "estrelas": 5, "texto": "Atendimento atencioso…", "quando": "há 2 meses"}
]
```

- **Somente avaliações reais**, com nome abreviado, e que falem do **atendimento**, nunca do resultado do processo (Provimento 205/2021 da OAB).
- Enquanto a lista estiver vazia, o bloco mostra só os botões "Ver avaliações no Google" e "Deixe a sua avaliação".
- **Não** marcar as estrelas com schema `AggregateRating`: o Google não aceita avaliações de terceiros republicadas pelo próprio negócio e pode aplicar ação manual.
- Trocar `perfil_google` pelo **link direto de avaliação** (no Perfil da Empresa: "Pedir avaliações"), que abre a caixa de avaliação de uma vez.

## Como editar

1. Edite o conteúdo em `_fonte/paginas/*.html`. A primeira linha de cada arquivo traz título, descrição e schema.
2. Cabeçalho, menu, rodapé e `<head>` ficam em `_fonte/build.py` e são iguais em todas as páginas.
3. Rode na pasta `marketing/site`: `python _fonte/build.py`

Atalhos dentro das páginas: `{{CTA}}` (texto padrão do botão), `{{P}}` (caminho até a raiz) e `{{L:/caminho/}}` (link interno).

**Revisar localmente:** `python _fonte/build.py --local` gera links que funcionam abrindo os arquivos direto do disco. **Antes de publicar, rode de novo sem `--local`.**

## Como publicar (GitHub + Plesk)

Endereços finais:
- Site: `https://marianasalvati.adv.br/`
- LP do Google Ads: `https://marianasalvati.adv.br/buscaeapreensao/`

**A cada atualização:**
1. Na raiz do projeto, rode `python marketing/publicar.py`. Ele gera o site e monta a pasta `publicar/` com o site na raiz, a LP em `buscaeapreensao/` e o `.htaccess`.
2. Faça `git add -A && git commit -m "..." && git push`.
3. O Plesk puxa do GitHub e o site é atualizado.

**Configuração única no Plesk:**
1. **Git:** Sites e Domínios → Git → adicionar repositório remoto (URL do GitHub). Modo de implantação: automático. Caminho no servidor: `/httpdocs`.
2. **Document root:** Hospedagem e DNS → Configurações de hospedagem → "Document root" = `httpdocs/publicar`.
3. **HTTPS:** SSL/TLS → Let's Encrypt. Depois, em Configurações de hospedagem, ative "Redirecionamento 301 permanente de HTTP para HTTPS".
4. **Domínio preferido:** Configurações de hospedagem → "Domínio preferido" = `marianasalvati.adv.br` (sem www). Os links canônicos do site usam a versão sem www.
5. **GitHub privado:** o repositório tem `_memoria/` e arquivos internos. Para o Plesk acessar um repositório privado, adicione a chave SSH que o Plesk mostra em GitHub → Settings → Deploy keys.

O `.htaccess` gerado já cuida da página 404, da compressão, do cache de imagens e CSS e do redirecionamento do endereço antigo `/lp/busca-e-apreensao/`. Ele funciona com Apache, que é o padrão do Plesk (nginx + Apache).

**Depois de publicar:** cadastre o domínio no Google Search Console, envie o `sitemap.xml` e teste as páginas no PageSpeed Insights.

## Antes de publicar

- [ ] **Revisão jurídica da Mariana nos 3 artigos.** Eles citam o Decreto-Lei 911/1969, as Súmulas e Temas do STJ (72, 722, 1132), o REsp sobre e-mail (2025), a Lei 14.711/2023 e o Provimento CNJ 196/2025. Os textos foram escritos com base em pesquisa, mas a responsabilidade técnica é dela.
- [ ] "Especialista" no botão: confirmar o título de especialização (regra da OAB)
- [ ] Trocar `GTM-XXXXXXX` (no `build.py`) pelo ID real e rodar o build de novo
- [ ] Confirmar se o endereço pode aparecer (ver `marketing/seo/03-google-meu-negocio.md`)
- [ ] FAQ "Quanto custa": confirmar com a Mariana a frase sobre a tabela da OAB/RS

## Próximos artigos (plano em `marketing/seo/05-estrategia-conteudo.md`)

3. Busca e apreensão extrajudicial · 4. Notificação por e-mail vale? · 5. Quantas parcelas atrasadas ·
6. Prazo de 5 dias · 7. Como saber se o carro está em busca e apreensão · 8. Blitz · 10. Carro de trabalho

Para cada artigo novo: crie `_fonte/paginas/08-....html` copiando um artigo existente, adicione o link no
rodapé (`build.py`, lista "Artigos"), na Home e no pilar, e rode o build.

> ⚠️ Não escrever sobre "adimplemento substancial" como defesa: o STJ não aceita esse argumento,
> sozinho, para barrar a busca e apreensão do Decreto-Lei 911 (REsp 1.622.555/MG).
