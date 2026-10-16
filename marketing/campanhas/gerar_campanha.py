"""
Gera a campanha do Google Ads (CSVs para o Google Ads Editor) da Mariana Salvati Advocacia.
Valida limites do Google (título 30, descrição 90, caminho 15, sitelink 25/35, frase de destaque 25).

Uso (na raiz do MazyOS):  python marketing/campanhas/gerar_campanha.py
"""
import csv, os

PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'google-ads-2026-10-16')
CAMPANHA = 'MSA | Pesquisa | Busca e Apreensão'
LP = 'https://marianasalvati.adv.br/buscaeapreensao/'
SITE = 'https://marianasalvati.adv.br'
SUFIXO = 'utm_source=google&utm_medium=cpc&utm_campaign=busca-apreensao&utm_content={adgroupid}&utm_term={keyword}'

# --------------------------------------------------------------------------------------------
# Títulos comuns (reaproveitados nos grupos) — sem promessa de resultado (Provimento 205/2021)
COMUNS = [
    'Dra. Mariana Salvati OAB/RS', 'Advogada Especialista', 'Atendimento pelo WhatsApp',
    'Atendimento em Todo o Brasil', 'Calma, Posso Te Ajudar', 'Análise do Seu Caso Online',
    'Entenda Seus Prazos e Direitos', 'Bem Avaliada no Google', 'Direito Bancário e Veículos',
    'Atendimento Direto e Humano',
]
DESC_COMUNS = [
    'Advogada OAB/RS 139.028 com atuação em busca e apreensão. Atendimento online no Brasil.',
    'A financeira precisa cumprir a lei. Envie seus documentos pelo WhatsApp para análise.',
    'Atendimento direto com a advogada, sem intermediários. Converse pelo WhatsApp.',
]

# grupo -> (parâmetro da LP, caminho 2, títulos próprios, descrição própria, palavras-chave)
# palavras-chave: ('termo', 'Exata'|'Frase')
GRUPOS = {
    'Notificação extrajudicial': ('notificacao', 'notificacao', [
        'Recebeu Notificação do Banco?', 'Notificação Extrajudicial?', 'Notificação Não Leva Seu Carro',
        'Envie a Sua Notificação', 'Verifique Sua Notificação'],
        'Receber a notificação não significa perder o carro. Entenda as etapas e os seus prazos.', [
        ('notificação de busca e apreensão', 'Exata'), ('notificação extrajudicial busca e apreensão', 'Frase'),
        ('recebi notificação de busca e apreensão', 'Frase'), ('notificação busca e apreensão o que fazer', 'Frase'),
        ('notificação extrajudicial financiamento veículo', 'Frase'), ('notificação extrajudicial carro atrasado', 'Frase'),
        ('carta de busca e apreensão', 'Frase'), ('notificação do banco carro', 'Frase'),
        ('notificação de busca e apreensão por email', 'Frase'), ('aviso de busca e apreensão', 'Frase'),
        ('notificação cartório financiamento carro', 'Frase'), ('carta do banco busca e apreensão', 'Frase')]),

    'Intimação e processo': ('intimacao', 'intimacao', [
        'Intimação de Busca e Apreensão', 'Recebeu uma Intimação?', 'Foi Citado no Processo?',
        'Ação de Busca e Apreensão', 'Liminar de Busca e Apreensão'],
        'Recebeu intimação de busca e apreensão? Calma, posso te ajudar a resolver. Fale comigo.', [
        ('intimação busca e apreensão', 'Exata'), ('intimação de busca e apreensão', 'Frase'),
        ('citação busca e apreensão', 'Frase'), ('fui citado busca e apreensão', 'Frase'),
        ('ação de busca e apreensão de veículo', 'Frase'), ('processo de busca e apreensão', 'Frase'),
        ('liminar de busca e apreensão', 'Frase'), ('mandado de busca e apreensão de veículo', 'Frase'),
        ('busca e apreensão de veículo financiado', 'Frase'), ('defesa em ação de busca e apreensão', 'Frase'),
        ('carro com busca e apreensão', 'Frase'), ('saber se meu carro está em busca e apreensão', 'Frase')]),

    'Veículo apreendido': ('apreendido', 'apreendido', [
        'Carro Foi Apreendido?', 'Veículo Apreendido?', 'Prazo de 5 Dias Corre Rápido',
        'Moto ou Caminhão Apreendido?', 'Ainda Existem Caminhos'],
        'Depois da apreensão, a lei dá 5 dias para pagar a dívida. Não deixe o prazo passar.', [
        ('meu carro foi apreendido', 'Exata'), ('carro apreendido financiamento', 'Frase'),
        ('meu carro foi apreendido financiamento', 'Frase'), ('carro apreendido busca e apreensão', 'Frase'),
        ('recuperar carro apreendido financiamento', 'Frase'), ('carro apreendido o que fazer', 'Frase'),
        ('moto apreendida financiamento', 'Frase'), ('caminhão apreendido financiamento', 'Frase'),
        ('carro apreendido em blitz busca e apreensão', 'Frase'), ('prazo de 5 dias busca e apreensão', 'Frase'),
        ('veículo apreendido financiamento', 'Frase'), ('banco tomou meu carro', 'Frase'),
        ('financeira tomou meu carro', 'Frase')]),

    'Advogado busca e apreensão': ('advogado', 'advogada', [
        'Advogada em Busca e Apreensão', 'Advogado Busca e Apreensão', 'Defesa em Busca e Apreensão',
        'Advogada de Direito Bancário', 'Fale com a Advogada Hoje'],
        'Recebeu notificação ou teve o carro apreendido? Calma, posso te ajudar a resolver.', [
        ('advogado busca e apreensão', 'Exata'), ('advogada busca e apreensão', 'Exata'),
        ('advogado busca e apreensão de veículo', 'Frase'), ('advogado especialista em busca e apreensão', 'Frase'),
        ('advogado para busca e apreensão', 'Frase'), ('advogado busca e apreensão online', 'Frase'),
        ('advogado financiamento de veículo', 'Frase'), ('advogado carro financiado atrasado', 'Frase'),
        ('advogado alienação fiduciária', 'Frase'), ('advogado contra financeira', 'Frase'),
        ('advogado direito bancário veículo', 'Frase')]),

    'Busca e apreensão extrajudicial': ('extrajudicial', 'cartorio', [
        'Busca e Apreensão em Cartório', 'Apreensão Extrajudicial?', 'Marco Legal das Garantias',
        'Cartório Pediu Seu Veículo?', 'Verifique Seu Contrato'],
        'A apreensão em cartório exige cláusula no contrato e notificação. Verifique a sua.', [
        ('busca e apreensão extrajudicial', 'Exata'), ('busca e apreensão extrajudicial', 'Frase'),
        ('busca e apreensão em cartório', 'Frase'), ('busca e apreensão extrajudicial veículo', 'Frase'),
        ('busca e apreensão cartório veículo', 'Frase'), ('marco legal das garantias busca e apreensão', 'Frase'),
        ('busca e apreensão sem processo', 'Frase')]),

    'Porto Alegre': ('portoalegre', 'porto-alegre', [
        'Advogada em Porto Alegre', 'Busca e Apreensão em POA', 'Moinhos de Vento, Porto Alegre',
        'Presencial ou Online', 'Escritório no Moinhos'],
        'Escritório no Moinhos de Vento, em Porto Alegre, com atendimento online em todo o Brasil.', [
        ('advogado busca e apreensão porto alegre', 'Exata'), ('advogado busca e apreensão porto alegre', 'Frase'),
        ('advogada busca e apreensão porto alegre', 'Frase'), ('busca e apreensão porto alegre', 'Frase'),
        ('advogado direito bancário porto alegre', 'Frase'), ('advogado financiamento veículo porto alegre', 'Frase'),
        ('advogado busca e apreensão rs', 'Frase'), ('advogado busca e apreensão rio grande do sul', 'Frase')]),
}

# Negativas da campanha (lista compartilhada). Frase, salvo indicação.
NEGATIVAS = [
    'leilão', 'leilao', 'leilões', 'comprar', 'compro', 'venda', 'vendo', 'à venda', 'modelo', 'modelos',
    'petição', 'peticao', 'peticionamento', 'curso', 'concurso', 'pdf', 'jurisprudência', 'doutrina',
    'criminal', 'penal', 'polícia', 'policial', 'delegacia', 'drogas', 'arma', 'celular',
    'menor', 'criança', 'guarda', 'pensão', 'divórcio', 'inventário', 'trabalhista',
    'imóvel', 'imovel', 'casa', 'apartamento', 'terreno', 'emprego', 'vaga', 'vagas', 'estágio', 'salário',
    'ajuizar', 'como entrar com', 'como fazer busca e apreensão', 'empresa de busca e apreensão',
    'localizador', 'recuperadora', 'assessoria de cobrança', 'oficial de justiça concurso',
    'o que é', 'significado', 'wikipedia', 'exame da ordem', 'oab exame',
]
# Negativas por grupo, para cada busca cair no grupo certo (evita grupos competindo entre si)
NEG_GRUPO = {g: ['porto alegre', 'poa'] for g in GRUPOS if g != 'Porto Alegre'}
NEG_GRUPO['Advogado busca e apreensão'] += ['extrajudicial', 'cartório']

SITELINKS = [  # texto (25), linha 1 (35), linha 2 (35), url
    ('Como Funciona', 'Cada etapa, do atraso ao leilão', 'Explicado sem juridiquês', f'{SITE}/busca-e-apreensao-de-veiculo/'),
    ('Recebi a Notificação', 'O que conferir na carta', 'Prazos e documentos', f'{SITE}/busca-e-apreensao-de-veiculo/notificacao-extrajudicial-o-que-fazer/'),
    ('Meu Carro Foi Apreendido', 'O prazo de 5 dias para pagar', 'E a defesa em 15 dias', f'{SITE}/busca-e-apreensao-de-veiculo/carro-apreendido-como-recuperar/'),
    ('Sobre a Advogada', 'Mariana Salvati, OAB/RS 139.028', 'Atendimento direto com ela', f'{SITE}/sobre/'),
    ('Avaliações de Clientes', 'Veja quem já foi atendido', 'Avaliações no Google', f'{SITE}/#avaliacoes'),
    ('Contato', 'WhatsApp, e-mail e escritório', 'Moinhos de Vento, Porto Alegre', f'{SITE}/contato/'),
]
DESTAQUES = ['Atendimento Online', 'Todo o Brasil', 'OAB/RS 139.028', 'Análise do Contrato',
             'Atendimento Direto', 'Resposta pelo WhatsApp', 'Sem Sair de Casa', 'Escritório em POA']
SNIPPET = ('Serviços', ['Análise de notificação', 'Defesa em apreensão', 'Análise de contrato',
                        'Apreensão em cartório', 'Revisão de valores'])

# --------------------------------------------------------------------------------------------
erros = []
def checa(txt, limite, onde):
    if len(txt) > limite: erros.append(f'{onde}: "{txt}" tem {len(txt)} (máx {limite})')
    return txt

def rsa(grupo, proprios, desc_propria, variante):
    """Duas variações: A (dor do cliente fixada na posição 1) e B (autoridade fixada na posição 1)."""
    titulos = proprios + [t for t in COMUNS][:10]
    titulos = titulos[:15]
    if variante == 'A':
        pins = {0: '1'}                      # título do grupo sempre na 1ª posição
        descs = [desc_propria] + DESC_COMUNS
    else:
        titulos = [COMUNS[0]] + [t for t in titulos if t != COMUNS[0]]
        titulos = titulos[:15]
        pins = {0: '1', 1: '2'}              # nome + OAB na 1ª, situação do grupo na 2ª
        titulos[1], titulos[titulos.index(proprios[0])] = proprios[0], titulos[1]
        descs = [DESC_COMUNS[0], desc_propria, DESC_COMUNS[1], DESC_COMUNS[2]]
    assert len(titulos) == 15 and len(set(titulos)) == 15, (grupo, variante, titulos)
    for i, t in enumerate(titulos): checa(t, 30, f'{grupo}/{variante} título {i+1}')
    for i, d in enumerate(descs): checa(d, 90, f'{grupo}/{variante} descrição {i+1}')
    return titulos, pins, descs

os.makedirs(PASTA, exist_ok=True)
def escreve(nome, cab, linhas):
    with open(os.path.join(PASTA, nome), 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(cab); w.writerows(linhas)

# campanhas.csv
escreve('campanhas.csv',
        ['Campaign', 'Campaign Type', 'Networks', 'Budget', 'Budget type', 'Bid Strategy Type', 'Campaign Status',
         'Languages', 'Final URL suffix', 'Ad rotation'],
        [[CAMPANHA, 'Search', 'Google search', '[DEFINIR]', 'Daily', 'Maximize clicks', 'Paused', 'pt',
          SUFIXO, 'Optimize']])

g_lin, k_lin, a_lin, n_lin = [], [], [], []
total_kw = 0
for grupo, (param, path2, proprios, dprop, kws) in GRUPOS.items():
    url = f'{LP}?grupo={param}'
    checa(path2, 15, f'{grupo} caminho 2')
    g_lin.append([CAMPANHA, grupo, 'Paused', '', url])
    for termo, tipo in kws:
        k_lin.append([CAMPANHA, grupo, termo, tipo, 'Paused', url]); total_kw += 1
    for v in ('A', 'B'):
        t, pins, d = rsa(grupo, proprios, dprop, v)
        linha = [CAMPANHA, grupo, 'Responsive search ad', 'Paused', url, 'busca-apreensao', path2]
        for i in range(15):
            linha += [t[i], pins.get(i, '')]
        linha += d
        a_lin.append(linha)
    for neg in NEG_GRUPO.get(grupo, []):
        n_lin.append([CAMPANHA, grupo, neg, 'Negative phrase'])
for neg in NEGATIVAS:
    n_lin.append([CAMPANHA, '', neg, 'Campaign negative phrase'])

escreve('grupos.csv', ['Campaign', 'Ad group', 'Ad group status', 'Max CPC', 'Final URL'], g_lin)
escreve('keywords.csv', ['Campaign', 'Ad group', 'Keyword', 'Criterion Type', 'Status', 'Final URL'], k_lin)
cab = ['Campaign', 'Ad group', 'Ad type', 'Status', 'Final URL', 'Path 1', 'Path 2']
for i in range(1, 16): cab += [f'Headline {i}', f'Headline {i} position']
cab += [f'Description {i}' for i in range(1, 5)]
escreve('anuncios.csv', cab, a_lin)
escreve('keywords-negativas.csv', ['Campaign', 'Ad group', 'Keyword', 'Criterion Type'], n_lin)

checa('busca-apreensao', 15, 'caminho 1')
sl = []
for t, l1, l2, u in SITELINKS:
    sl.append([CAMPANHA, checa(t, 25, 'sitelink'), checa(l1, 35, 'sitelink l1'), checa(l2, 35, 'sitelink l2'), u])
escreve('extensoes-sitelinks.csv', ['Campaign', 'Sitelink text', 'Description line 1', 'Description line 2', 'Final URL'], sl)
escreve('extensoes-destaques.csv', ['Campaign', 'Callout text'], [[CAMPANHA, checa(c, 25, 'destaque')] for c in DESTAQUES])
escreve('extensoes-snippets.csv', ['Campaign', 'Header', 'Snippet values'],
        [[CAMPANHA, SNIPPET[0], ';'.join(checa(v, 25, 'snippet') for v in SNIPPET[1])]])
escreve('extensoes-chamadas.csv', ['Campaign', 'Phone number', 'Country code'], [[CAMPANHA, '51992074913', 'BR']])

if erros:
    print('ERROS DE LIMITE:'); print('\n'.join(erros)); raise SystemExit(1)
print(f'ok: 1 campanha, {len(GRUPOS)} grupos, {total_kw} palavras-chave, {len(n_lin)} negativas, {len(a_lin)} anúncios RSA')
