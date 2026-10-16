# Como importar no Google Ads Editor

Arquivos desta pasta (gerados por `marketing/campanhas/gerar_campanha.py`):

| Arquivo | Conteúdo |
|---|---|
| `campanhas.csv` | 1 campanha de Pesquisa (pausada) |
| `grupos.csv` | 6 grupos de anúncio, com a URL final de cada um |
| `keywords.csv` | 63 palavras-chave (frase e exata) |
| `keywords-negativas.csv` | Negativas da campanha e por grupo |
| `anuncios.csv` | 12 anúncios RSA (15 títulos e 4 descrições cada, com títulos fixados) |
| `extensoes-sitelinks.csv` | 6 sitelinks para o site |
| `extensoes-destaques.csv` | 8 frases de destaque |
| `extensoes-snippets.csv` | Snippet estruturado "Serviços" |
| `extensoes-chamadas.csv` | Recurso de ligação |
| `imagens/` | Imagem quadrada, imagem paisagem e logos para os recursos de imagem |
| `configuracoes.md` | **Ler antes:** configurações, orçamento, conversões e checklist |

## Passo a passo

1. Instale o **Google Ads Editor** (gratuito) e baixe a conta.
2. Importe nesta ordem, em **Conta → Importar → Do arquivo**, revisando a tela de prévia a cada arquivo:
   1. `campanhas.csv`
   2. `grupos.csv`
   3. `keywords.csv`
   4. `keywords-negativas.csv`
   5. `anuncios.csv`
   6. as extensões (`extensoes-*.csv`)
3. **Ajuste no Editor** o que o CSV não define bem:
   - Orçamento diário (está `[DEFINIR]`)
   - Local: Brasil, com a opção **Presença**, e Rio Grande do Sul com +15%
   - Redes: desmarcar Parceiros de pesquisa e Display
4. **Recursos de imagem e logo:** suba os arquivos de `imagens/` pela interface web (Recursos → Imagens / Logotipos).
5. Clique em **Postar** para enviar à conta. Tudo vai **pausado**.
6. Complete o **checklist** do `configuracoes.md`, principalmente as conversões, e só então ative.

> Se o Editor não reconhecer alguma coluna (os nomes variam entre versões), use **Fazer várias alterações** → colar os dados do CSV, ou ajuste o nome da coluna na prévia.

## Para alterar os textos

Edite `marketing/campanhas/gerar_campanha.py` e rode:

    python marketing/campanhas/gerar_campanha.py

O script valida os limites do Google: título 30, descrição 90, caminho 15, sitelink 25/35 e frase de destaque 25. Se algum texto passar do limite, ele aponta qual e não gera os arquivos.
