# 04 — Otimização on-page (arquitetura do site novo)

Domínio: **marianasalvati.adv.br** (hospedagem ativa, sem site)

## Arquitetura

```
/                                              Home (serviço + quem é a Mariana)
/busca-e-apreensao-de-veiculo/                 PILAR: como funciona (termo do print)
  /notificacao-extrajudicial-o-que-fazer/      satélite
  /quantas-parcelas-atrasadas/                 satélite
  /carro-apreendido-como-recuperar/            satélite (transacional)
  /prazo-de-5-dias-purgacao-da-mora/           satélite
  /busca-e-apreensao-extrajudicial/            satélite (tema novo)
  /notificacao-por-email-e-valida/             satélite (STJ 2025)
  /como-saber-se-o-carro-esta-em-busca-e-apreensao/
  /carro-em-busca-e-apreensao-blitz/
  /adimplemento-substancial/
/advogada-busca-e-apreensao/                   Página de serviço (alvo do termo transacional)
/sobre/                                        Mariana Salvati, OAB/RS 139.028
/contato/
/buscaeapreensao/                         Landing page do Google Ads (noindex)
```

A landing page do Ads leva `noindex` para não competir com a página de serviço.

## Páginas principais

| Página | Keyword principal | Title (≤60) | Meta description (≤160) | H1 |
|---|---|---|---|---|
| Home | advogada busca e apreensão de veículo | Advogada em Busca e Apreensão de Veículo · Mariana Salvati | Defesa para quem tem veículo financiado em busca e apreensão. Análise do contrato e da notificação. Atendimento online em todo o Brasil. | Defesa em busca e apreensão de veículo |
| Pilar | como funciona a busca e apreensão de veículo | Busca e Apreensão de Veículo: Como Funciona e o Que Fazer | Entenda cada etapa da busca e apreensão de veículo financiado: notificação, liminar, prazo de 5 dias e o que você pode fazer em cada fase. | Busca e apreensão de veículo: como funciona, etapa por etapa |
| Serviço | advogado busca e apreensão de veículo | Advogado para Busca e Apreensão de Veículo · Defesa Online | Recebeu notificação ou teve o carro apreendido? Saiba como funciona a defesa e envie seus documentos para análise pelo WhatsApp. | Advogada para defesa em busca e apreensão |
| Notificação | notificação extrajudicial busca e apreensão o que fazer | Recebi Notificação de Busca e Apreensão. O Que Fazer? | A notificação não significa apreensão imediata. Veja o que verificar nela, quais prazos correm e quais documentos separar. | Recebi uma notificação extrajudicial de busca e apreensão. E agora? |
| Apreendido | carro apreendido financiamento como recuperar | Carro Apreendido no Financiamento: Como Recuperar | O que acontece depois da apreensão, o prazo de 5 dias e as opções de defesa. Explicado por advogada, sem juridiquês. | Meu carro foi apreendido. Dá para recuperar? |
| Sobre | Mariana Salvati advogada | Mariana Salvati · Advogada OAB/RS 139.028 | Conheça a advogada Mariana Battimanza Salvati e a atuação do escritório em Direito Bancário e busca e apreensão de veículos. | Mariana Salvati |

## Regras de cada artigo (E-E-A-T para tema jurídico)

- Caixa de autora no topo: foto, "Por Mariana Salvati, advogada, OAB/RS 139.028", link para /sobre/
- "Atualizado em [data]" visível. Revisar quando a lei ou a jurisprudência mudar
- Citar a fonte legal (Decreto-Lei 911/1969, súmulas e decisões do STJ) com link para o texto oficial
- Resposta direta nas 2 primeiras linhas (ajuda o featured snippet e as IAs)
- FAQ ao final + schema FAQPage
- CTA de WhatsApp contextual, nunca "contrate agora"
- **Todo conteúdo jurídico revisado pela Mariana antes de publicar**

## Schema JSON-LD (home)

```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "@id": "https://marianasalvati.adv.br/#escritorio",
  "name": "Mariana Salvati Advocacia",
  "legalName": "Mariana Salvati Sociedade Individual de Advocacia",
  "url": "https://marianasalvati.adv.br/",
  "logo": "https://marianasalvati.adv.br/img/logo.png",
  "image": "https://marianasalvati.adv.br/img/mariana-salvati.jpg",
  "telephone": "+55-51-99207-4913",
  "email": "contato@marianasalvati.adv.br",
  "taxID": "65.564.592/0001-10",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Estrada João Passuelo, 641 - Vila Nova",
    "addressLocality": "Porto Alegre",
    "addressRegion": "RS",
    "postalCode": "91740-550",
    "addressCountry": "BR"
  },
  "areaServed": { "@type": "Country", "name": "Brasil" },
  "knowsAbout": ["Busca e apreensão de veículo", "Alienação fiduciária", "Direito Bancário"],
  "founder": { "@id": "https://marianasalvati.adv.br/sobre/#mariana" },
  "sameAs": ["https://www.instagram.com/salvatiadvogada/"]
}
```

> Se o perfil do Google for de área de atendimento (endereço oculto), remover `streetAddress` do schema.

## Schema JSON-LD (/sobre/)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://marianasalvati.adv.br/sobre/#mariana",
  "name": "Mariana Battimanza Salvati",
  "jobTitle": "Advogada",
  "identifier": { "@type": "PropertyValue", "propertyID": "OAB/RS", "value": "139028" },
  "worksFor": { "@id": "https://marianasalvati.adv.br/#escritorio" },
  "sameAs": ["https://www.instagram.com/salvatiadvogada/"]
}
```

Os artigos usam `Article` com `author` → `#mariana` e `FAQPage` na seção de perguntas.

## Checklist técnico

| Item | Status |
|---|---|
| URLs curtas, minúsculas, com hífen | pendente (site novo) |
| HTTPS + redirecionamento de www | pendente |
| Alt text em todas as imagens | pendente |
| Imagens em WebP, lazy-load | pendente |
| Core Web Vitals mobile (LCP < 2,5s) | pendente |
| sitemap.xml + robots.txt | pendente |
| Canonical em todas as páginas | pendente |
| Open Graph (compartilhar no WhatsApp com foto e título) | pendente |
| Google Search Console + envio do sitemap | pendente |
| GA4 + Tag Manager (evento `clique_whatsapp`) | pendente |
| `noindex` na LP do Ads (/buscaeapreensao/) | pendente |
| Rodapé com nome completo, OAB, CNPJ, endereço (transparência OAB) | pendente |

## Links internos

- Todo satélite → pilar (no 1º parágrafo) + página de serviço (no CTA)
- Pilar → todos os satélites (em cada etapa correspondente)
- Home → pilar, serviço, sobre
- Satélites vizinhos se linkam (ex.: notificação → prazo de 5 dias → apreendido)
