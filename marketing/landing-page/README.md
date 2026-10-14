# Landing page: busca e apreensão (Google Ads)

Publicar em `https://marianasalvati.adv.br/lp/busca-e-apreensao/` (`index.html` + pasta `img/`).

## Antes de publicar

- [ ] **Imagens** em `img/`:
  - `logo-horizontal-caramelo.png` (cópia de `identidade/logos/MSA_Horizontal_Caramelo.png`, para o fundo azul)
  - `mariana.jpg` (foto da citação, vertical 4:5, ~400×500)
  - `mariana-2.jpg` (foto do "Sobre", vertical 4:5, ~840×1050)
  - Enquanto as fotos não chegam, aparece um monograma "MS" no lugar
  - `hero-guincho.jpg` / `hero-guincho-mobile.jpg`: **já incluídas** (Unsplash, licença livre para uso comercial,
    foto 1686966933735-305bd8fe0a77). Converter para WebP antes de publicar (a de desktop tem ~530 KB)
- [ ] **Cores**: trocar os hex provisórios no topo do `<style>` (`--azul`, `--caramelo`) pelos do PDF da Orbe
- [ ] **Fontes**: trocar Source Serif 4/Inter se o PDF da Orbe definir outras
- [ ] **GTM**: trocar `GTM-XXXXXXX` pelo ID real
- [ ] **Revisão jurídica da Mariana**: seções "Etapas" e "Perguntas comuns"
- [ ] Confirmar se o endereço pode aparecer (ver `marketing/seo/03-google-meu-negocio.md`)

## Rastreamento

Todo botão de WhatsApp envia ao `dataLayer`:

```js
{ event: 'clique_whatsapp', situacao: 'notificacao' | 'apreendido' | 'geral', grupo_anuncio: '<grupo>' }
```

No GTM: acionador "Evento personalizado = clique_whatsapp" → tag de conversão do Google Ads
(e evento GA4). Marcar como conversão principal da campanha.

## URL final por grupo de anúncio

| Grupo | URL final |
|---|---|
| A. Notificação | `.../lp/busca-e-apreensao/?grupo=notificacao` |
| B. Apreendido | `.../lp/busca-e-apreensao/?grupo=apreendido` |
| C. Advogado | `.../lp/busca-e-apreensao/?grupo=advogado` |

O parâmetro `grupo` troca o título do topo para a situação que a pessoa pesquisou e vai
junto no evento de conversão.
