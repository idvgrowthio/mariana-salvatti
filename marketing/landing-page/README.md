# Landing page: busca e apreensão (Google Ads)

Publicar em `https://marianasalvati.adv.br/buscaeapreensao/` (`index.html` + pasta `img/`).

## Antes de publicar

- [x] **Identidade aplicada**: paleta oficial da Orbe, logos (versões claras cortadas em `img/`) e foto da Mariana
- [x] **Imagens**: hero em WebP (com JPG de fallback), foto e logos já em `img/`
- [ ] **Foto do topo**: é um carro americano (Unsplash, licença livre). Trocar por uma foto brasileira quando houver
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
| A. Notificação | `.../buscaeapreensao/?grupo=notificacao` |
| B. Apreendido | `.../buscaeapreensao/?grupo=apreendido` |
| C. Advogado | `.../buscaeapreensao/?grupo=advogado` |

O parâmetro `grupo` troca o título do topo para a situação que a pessoa pesquisou e vai
junto no evento de conversão.
