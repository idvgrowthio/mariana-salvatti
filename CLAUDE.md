# Mariana Salvati Advocacia — MazyOS

Sua empresa roda em cima desse arquivo. Aqui ficam as regras de operação
do MazyOS — como o Claude lê o contexto, aprende com correções, mantém
tudo atualizado e cria skills novas conforme a operação evolui.

Esse arquivo é editável. Quando o `/instalar` rodar, ele complementa o
final dessa página com as regras específicas do seu negócio.

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem
e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, prazos

Usar essas informações como base pra qualquer resposta ou decisão. Ao
sugerir prioridades, formatos ou abordagens, considerar o foco atual
descrito em `estrategia.md`.

Pra qualquer tarefa visual (carrossel, post, landing page), consultar
`identidade/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas
usar o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante
em `.claude/skills/`. Se encontrar, seguir as instruções da skill. Se
não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o
usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o
padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma
instrução que parece permanente (frases como "na verdade é assim", "não
faça mais isso", "prefiro assim", "sempre que...", "evita...", "da
próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (clientes, serviços, mercado) → `_memoria/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato, o que evitar) → `_memoria/preferencias.md`
- **Sobre prioridades e foco** (projetos, metas, prazos) → `_memoria/estrategia.md`
- **Regra de comportamento nessa pasta** → próprio `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro.
Confirmar mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na
verdade o arquivo se chama X"). Só perguntar quando a informação tiver
valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (cliente novo, skill
nova, mudança de foco, processo novo, ferramenta instalada, estrutura
alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

Se sim, identificar o que atualizar:

- **Cliente, serviço, ferramenta, equipe** → `_memoria/empresa.md`
- **Mudança de prioridade ou foco** → `_memoria/estrategia.md`
- **Tom ou estilo** → `_memoria/preferencias.md`
- **Pasta, regra de organização, skill criada** → `CLAUDE.md`
- **Visual (cores, fontes, logo)** → `identidade/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo
inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais sem impacto no contexto (escrever um email avulso, criar um post)
- Perguntas simples ou conversas sem ação
- Mudanças já salvas pelo bloco "Aprender com correções"

**Dica:** rode `/atualizar` pra uma varredura completa quando houver dúvida.

---

## Criação de skills

Quando o usuário pedir skill nova:

1. Verificar se existe template relevante em `templates/skills/`. Se
   existir, usar como base e adaptar pro contexto
2. Perguntar se é específica desse projeto ou útil em qualquer:
   - Específica → `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Universal → `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` pra calibrar
   o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, exemplos),
   criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code

---

# Perfil: Mariana Salvati Advocacia (freelancer)

## O que é esse workspace

Operação de marketing digital do escritório **Mariana Salvati Sociedade
Individual de Advocacia** (Dra. Mariana Battimanza Salvati, OAB/RS 139.028).
Quem opera é João Guilherme, responsável por tráfego pago, site e landing
page. A Mariana atende sozinha e o canal de atendimento é o WhatsApp.

**Estrutura de pastas:**
- `_memoria/`: quem é a Mariana, como ela fala, o foco atual
- `identidade/`: paleta (Orbe Estúdio), logos MSA, fotos
- `marketing/site/`: site institucional e páginas de SEO
- `marketing/landing-page/`: landing page de busca e apreensão
- `marketing/google-ads/`: estrutura de campanha, palavras-chave, negativas, anúncios
- `marketing/meta-ads/`: transcrições e referências dos criativos em vídeo
- `saidas/`: relatórios para a Mariana, e-mails, documentos pontuais
- `dados/`: exports do Google Ads, termos de pesquisa, planilhas (não versionado)

## O que o escritório faz

Defesa de consumidores em busca e apreensão de veículos (financiamento com
alienação fiduciária). Cliente típico: financiou um veículo, atrasou parcelas
e recebeu notificação extrajudicial, ou já teve o carro apreendido. Anúncios
rodam para todo o Brasil.

## Regras do sistema

- **Compliance OAB (Provimento 205/2021) em toda peça:** sem promessa de resultado,
  sem mercantilização, sem urgência fabricada. "Especialista" só se ela tiver
  título de especialização (pendente de confirmação).
- **Políticas do Google Ads** para serviços jurídicos: revisar o texto antes de publicar.
- **Objetivo de toda peça:** lead *qualificado* no WhatsApp. Filtrar quem não é
  público antes do clique (deixar claro quem ela atende).
- **Relatórios para a Mariana:** sempre com diagnóstico + próximo passo, não só
  números. Ela quer entender por que algo funciona ou não e quais são as soluções.
- **Dados pessoais** (RG, CNH, data de nascimento) nunca entram neste repositório.
- Texto público em "você". O "tu" fica só para o Instagram, se ela quiser.

## Ferramentas conectadas

- [ ] Google Ads
- [ ] Google Analytics / Tag Manager (conversão do clique no WhatsApp)
- [ ] Google Search Console (SEO)
- [x] Meta Ads (conector disponível nesta sessão)
