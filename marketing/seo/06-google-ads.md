# 06 — Google Ads

> Regra OAB (Provimento 205/2021): comprar palavras-chave é permitido quando o anúncio
> **responde à busca** do usuário com informação. Proibido: "contrate agora", "o melhor
> advogado", promessa de resultado, "garanta seus direitos", "recupere seu carro".
> Na dúvida, levar o texto à Seccional OAB/RS.

## Objetivo

Leads (clique no WhatsApp) **qualificados**. Conversão principal: `clique_whatsapp` na
landing page (GA4 → importado no Google Ads). Mensagem pré-preenchida diferente por
grupo de anúncio, para a Mariana saber de onde veio cada contato.

## Estrutura: 1 campanha de Pesquisa, 3 grupos

| Grupo | Palavras-chave (frase / exata) | Mensagem do WhatsApp pré-preenchida |
|---|---|---|
| **A. Notificação** | "notificação extrajudicial busca e apreensão", "recebi notificação de busca e apreensão", "notificação busca e apreensão o que fazer", "notificação do banco carro atrasado", "busca e apreensão extrajudicial", "notificação de busca e apreensão por email" | "Olá, recebi uma notificação sobre o meu financiamento" |
| **B. Apreendido** | "carro apreendido financiamento", "meu carro foi apreendido", "como recuperar carro apreendido financiamento", "carro apreendido busca e apreensão o que fazer", "moto apreendida financiamento", "caminhão apreendido financiamento" | "Olá, meu veículo foi apreendido" |
| **C. Advogado** | [advogado busca e apreensão], "advogado busca e apreensão de veículo", "advogada busca e apreensão", "advogado para busca e apreensão de carro", "defesa busca e apreensão veículo", "advogado financiamento de veículo atrasado" | "Olá, preciso de ajuda com busca e apreensão" |

Começar com **correspondência de frase e exata**. A ampla só depois de ~30 conversões.

## Negativas (lista compartilhada)

leilão · leilões · comprar · compro · venda · vendo · modelo · petição · peticionamento ·
curso · concurso · pdf · jurisprudência · criminal · penal · polícia · menor · criança ·
guarda · imóvel · casa · apartamento · emprego · vaga · estágio ·
"como entrar com busca e apreensão" · "ajuizar busca e apreensão" *(lado do banco)*

Avaliar antes de negativar: "gratuito"/"grátis"/"defensoria" (pode ser público sem condição
de contratar) · "consórcio" (pode ser cliente).

> Revisar o relatório de **termos de pesquisa** toda semana nas 4 primeiras semanas.

## Anúncios responsivos (RSA)

**Títulos (≤30 caracteres, contados):**
1. Advogada em Busca e Apreensão
2. Recebeu Notificação do Banco?
3. Carro Foi Apreendido?
4. Análise do Seu Caso Online
5. Atendimento pelo WhatsApp
6. Entenda Seus Prazos e Direitos
7. Busca e Apreensão de Veículo
8. Notificação Extrajudicial?
9. Atendimento em Todo o Brasil
10. Dra. Mariana Salvati OAB/RS
11. Defesa em Busca e Apreensão
12. Financiamento em Atraso?
13. Orientação Jurídica Online
14. Saiba Como Funciona o Processo
15. Direito Bancário e Veículos

**Descrições (≤90 caracteres, contadas):**
1. Receber a notificação não significa apreensão imediata. Entenda as etapas do processo.
2. Advogada com atuação em busca e apreensão de veículo. Atendimento online em todo o Brasil.
3. A financeira precisa cumprir requisitos legais. Envie seus documentos para análise.
4. Teve o veículo apreendido? Fale com a advogada pelo WhatsApp e entenda suas opções.

Fixar (pin) na posição 1: grupo A → título 2; grupo B → título 3; grupo C → título 1.

**Recursos (extensões):**
- Sitelinks: Como funciona · Recebi notificação · Carro apreendido · Sobre a advogada
- Frases de destaque: Atendimento online · Todo o Brasil · OAB/RS 139.028 · Análise do contrato
- Ligação: +55 51 99207-4913
- Imagem: foto da Mariana (sem carro de luxo)

## Configurações

| Item | Recomendação |
|---|---|
| Rede | Só Pesquisa. **Desligar** Rede de Display e parceiros de pesquisa |
| Local | Brasil (conforme formulário), opção **"Presença"** (pessoas no local), não "interesse" |
| Horário | Começar 24h e, após 2-3 semanas, concentrar verba nos horários em que a Mariana responde rápido |
| Lance | Semanas 1-3: Maximizar cliques com CPC máximo. Depois de ~15-30 conversões: Maximizar conversões |
| Orçamento | **[aguardando valor da Mariana]**. Não estimar CPC sem o Planejador de Palavras-chave |
| Dispositivos | Mobile primeiro (público chega pelo celular e vai para o WhatsApp) |

## Landing page (`/lp/busca-e-apreensao/`)

Precisa existir antes de ligar a campanha. Estrutura para filtrar o lead:

1. **Topo:** "Recebeu notificação ou teve o veículo apreendido?" + foto da Mariana + OAB
2. **Para quem é:** financiamento de veículo em atraso **e** notificação recebida ou veículo
   apreendido. Para quem *não* é: comprar carro de leilão, dívidas sem relação com veículo etc.
3. **Como funciona o processo:** as etapas (é o conteúdo dos criativos)
4. **O que separar antes de chamar:** contrato, notificação, comprovantes. *Filtra quem está
   só curioso e acelera o atendimento da Mariana.*
5. **Sobre a Mariana** + FAQ curta
6. **Botão do WhatsApp** com mensagem pré-preenchida (evento `clique_whatsapp`)

> A skill `/anuncio-google` gera o CSV de importação a partir deste arquivo.
