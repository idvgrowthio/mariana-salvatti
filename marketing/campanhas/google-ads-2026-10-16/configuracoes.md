# Campanha Google Ads: configurações e plano

**Cliente:** Mariana Salvati Advocacia · **Gerada em:** 16/out/2026 · **Status ao importar:** tudo **pausado**

## Estrutura

```
MSA | Pesquisa | Busca e Apreensão   (só Rede de Pesquisa)
├── Notificação extrajudicial      12 palavras-chave → LP ?grupo=notificacao
├── Intimação e processo           12 palavras-chave → LP ?grupo=intimacao
├── Veículo apreendido             13 palavras-chave → LP ?grupo=apreendido
├── Advogado busca e apreensão     11 palavras-chave → LP ?grupo=advogado
├── Busca e apreensão extrajudicial 7 palavras-chave → LP ?grupo=extrajudicial
└── Porto Alegre                    8 palavras-chave → LP ?grupo=portoalegre
```

- **63 palavras-chave** (frase e exata; nenhuma ampla no início)
- **68 negativas:** 56 da campanha + 12 por grupo, para cada busca cair no grupo certo
- **12 anúncios RSA**, 2 por grupo:
  - **A, a dor do cliente:** título do grupo fixo na 1ª posição
  - **B, autoridade:** "Dra. Mariana Salvati OAB/RS" fixo na 1ª posição e o título do grupo na 2ª
- **Recursos:** 6 sitelinks, 8 frases de destaque, 1 snippet de serviços, ligação, imagens e logo

Cada grupo leva para a LP com um `?grupo=` próprio. A LP troca o título do topo para a situação que a pessoa pesquisou, e a mensagem do anúncio fica igual à da página, o que eleva o Índice de Qualidade. O mesmo parâmetro vai junto no evento de conversão.

## Configurações da campanha

| Item | Valor |
|---|---|
| Tipo | Pesquisa (Search) |
| Redes | **Só Pesquisa Google.** Desmarcar "Parceiros de pesquisa" e "Rede de Display" |
| Local | **Brasil**, com a opção **"Presença: pessoas que estão ou costumam estar no local"**, nunca "interesse" |
| Ajuste de lance por local | Rio Grande do Sul **+15%** (o escritório é físico em Porto Alegre e converte melhor) |
| Idioma | Português |
| Estratégia de lance | **Semanas 1 a 2:** Maximizar cliques com **CPC máximo** (definir com o Planejador). **Depois de cerca de 15 a 30 conversões:** Maximizar conversões. **Depois de cerca de 50:** CPA desejado |
| Rotação de anúncios | Otimizar |
| Sufixo de URL final | `utm_source=google&utm_medium=cpc&utm_campaign=busca-apreensao&utm_content={adgroupid}&utm_term={keyword}` |
| Dispositivos | Sem redução no celular (o público chega pelo celular e vai para o WhatsApp). Revisar desktop e tablet depois de 2 semanas |
| Programação | **Começar 24 horas** para coletar dados. Depois, concentrar o orçamento nos horários em que a Mariana responde o WhatsApp rápido. Lead que espera horas esfria |
| Recurso de ligação | Mostrar **só em horário comercial**. Ela atende sozinha, e ligação não atendida é dinheiro perdido |

## Orçamento

**Não há CPC público confiável para este nicho no Brasil**, então não vou chutar um valor. Antes de ativar:

1. Abra **Ferramentas → Planejador de palavras-chave → Ver volume de pesquisa e previsões** e cole as 63 palavras-chave de `keywords.csv`.
2. Anote a faixa de **lance da parte superior da página (alta)** dos termos dos grupos Advogado, Veículo apreendido e Notificação.
3. **Orçamento diário de teste = CPC alto × 15 cliques.** Com menos de cerca de 10 cliques por dia, o Google demora semanas para aprender.
4. Rode **30 dias sem mexer na estrutura**, só adicionando negativas, e depois avalie o custo por lead qualificado.

Como referência geral, sem ser específica do nicho, relatórios internacionais colocam serviços jurídicos entre os CPCs mais caros do Google Ads.

## Conversões (obrigatório antes de ativar)

Sem conversão medida, o Google não otimiza e o lance "Maximizar conversões" não funciona.

1. ✅ **Tags instaladas** em todas as páginas (16/out/2026): Tag Manager `GTM-T8BF26VH` (no `<head>` e o noscript logo após o `<body>`) e a tag do Google Ads `AW-18517050566`.
2. **No Google Ads:** Metas → Conversões → Nova ação → Site → **"Clique no WhatsApp"**:
   - Categoria: **Contato**
   - Valor: igual para todas
   - Contagem: **Uma**
   - Janela: 30 dias
3. **No Tag Manager:**
   - Acionador **Evento personalizado** com nome `clique_whatsapp`
   - Tag **Acompanhamento de conversões do Google Ads**, com o ID e o rótulo do passo 2
   - Tag **Vinculador de conversões**, disparada em todas as páginas
4. **Teste no Modo de visualização do Tag Manager:** clique em um botão de WhatsApp da LP e confira se a tag disparou.
5. **Opcional, o mais valioso:** importar como conversão offline só os contatos que **viraram cliente**. A Mariana anota o gclid ou a origem da mensagem pré-preenchida. É assim que o Google aprende a buscar lead qualificado, e não apenas clique.

## Checklist antes de ativar

- [ ] Conversão `clique_whatsapp` testada e marcada como **principal**
- [ ] **Verificação do anunciante** concluída no Google Ads (o Google pede para a maioria dos anunciantes)
- [ ] Faturamento configurado (CNPJ do escritório)
- [ ] Orçamento e CPC máximo definidos pelo Planejador
- [ ] **"Especialista":** a Mariana confirmou o título de especialização. Se não tiver, trocar o título "Advogada Especialista" em `gerar_campanha.py`, gerar de novo e reimportar. Isso também vale para a LP e o site
- [ ] **"Presencial ou Online"** e **"Escritório no Moinhos"** (grupo Porto Alegre): confirmar que ela recebe clientes na sala 501
- [ ] Revisão OAB: os textos não prometem resultado e não usam "contrate", "o melhor" ou "garantido"
- [ ] Imagens e logo enviadas (pasta `imagens/`)
- [ ] Campanha e grupos ativados **manualmente**, depois de tudo acima

## Rotina de otimização

| Quando | O que fazer |
|---|---|
| **Diário, semana 1** | Abrir **Termos de pesquisa** e negativar o que não é cliente (leilão, outra área do direito, lado do banco) |
| **Semanal, semanas 2 a 4** | Termos de pesquisa e negativas · Pausar palavras com gasto alto e 0 conversões · Ver o "Desempenho dos recursos" e trocar títulos com desempenho "Baixo" · Perguntar à Mariana **quantos contatos eram do perfil** |
| **Mensal** | Relatório com `/relatorio-ads`: custo por lead, custo por lead qualificado, diagnóstico e próximo passo (é o que a Mariana pediu no formulário) · Avaliar a troca para Maximizar conversões |
| **Depois de 60 dias** | Testar correspondência ampla nos 2 grupos que mais convertem, com Maximizar conversões |

## Indicadores para acompanhar

- **Custo por conversão** (clique no WhatsApp)
- **Taxa de conversão da LP:** a referência para LP jurídica boa é de 5% a 15% dos cliques
- **% de leads qualificados**, que a Mariana informa: o número que realmente importa
- **Parcela de impressões perdida (orçamento)** nos grupos que convertem: se for alta, aumentar a verba ali
- **Índice de Qualidade** por palavra-chave: meta de 7 ou mais
