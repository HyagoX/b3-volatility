SIDEBAR_FORMULAS = """
### Fundamentos Matemáticos

Este painel aplica modelos quantitativos padrão de finanças para medir o risco dos ativos.

**Retorno logarítmico diário**

Mede a variação percentual contínua do preço entre dois pregões consecutivos.

**Volatilidade diária amostral**

Desvio-padrão amostral dos retornos em uma janela móvel de 21 pregões (~1 mês).

**Volatilidade anualizada**

Escala a volatilidade diária para o horizonte de um ano bolsista (252 pregões).
"""

SIDEBAR_METADATA = """
### Parâmetros da Análise

| Item | Valor |
|------|-------|
| Ativos | PETR4, VALE3, BBAS3, BOVA11 |
| Coleta de dados | Nov/2021 – Dez/2022 |
| Período visual | Jan – Dez/2022 |
| Janela móvel | 21 pregões |
| 1º Turno | 02/10/2022 |
| 2º Turno | 30/10/2022 |
"""

TAB1_INTRO = """
Observe como os **picos de volatilidade** se concentram no segundo semestre, especialmente nas semanas que antecedem e sucedem as eleições presidenciais.
As linhas tracejadas vermelha e azul marcam o **1º Turno (02/10)** e o **2º Turno (30/10)**.
"""

TAB2_INTRO = """
Este gráfico compara a volatilidade anualizada móvel dos quatro ativos no mesmo período.
Ativos com linhas mais elevadas e com oscilações bruscas foram **mais sensíveis ao cenário político**.
Use a tabela abaixo para quantificar médias, medianas e picos de cada papel.
"""

DISCUSSION_SCRIPT = """
## 1. Contexto: Eleições Presidenciais de 2022

O ano de 2022 foi marcado por um ciclo eleitoral polarizado no Brasil. Dois candidatos com propostas
econômicas distintas disputaram a Presidência em dois turnos: o **1º Turno em 02 de outubro** e o
**2º Turno em 30 de outubro**. Em mercados financeiros, incertezas políticas elevam o risco percebido
pelos investidores, o que se manifesta diretamente na **volatilidade** — nossa métrica de análise.

Utilizamos quatro ativos representativos da B3: **PETR4** (petróleo, estatal), **BBAS3** (banco
estatal), **VALE3** (mineração, capital aberto) e **BOVA11** (ETF do Ibovespa, carteira diversificada).

---

## 2. Picos de Volatilidade em Setembro e Outubro

Ao observar os gráficos de volatilidade anualizada, identificamos um padrão claro: a partir de
**setembro de 2022**, todos os ativos apresentam **elevação sustentada da volatilidade**, com picos
acentuados nas proximidades das datas eleitorais.

Isso ocorre porque o mercado precifica incerteza em tempo real. Pesquisas eleitorais apertadas,
debates televisivos e declarações sobre política fiscal, estatais e regulação alimentam expectativas
de revisão de preços dos ativos. Nos gráficos, as **linhas verticais tracejadas** coincidem com
momentos em que a volatilidade já estava elevada ou acelerou — evidenciando que o mercado antecipou
parte do risco antes mesmo do dia da votação.

O período entre o 1º e o 2º turno foi particularmente tenso: com a disputa ainda indefinida,
investidores ajustaram posições defensivas, ampliando oscilações diárias e, consequentemente,
a volatilidade móvel de 21 dias.

---

## 3. PETR4 e BBAS3: Maior Sensibilidade Política

**PETR4** (Petrobras) e **BBAS3** (Banco do Brasil) são empresas de **economia mista com forte
componente estatal**. Seus preços refletem não apenas resultados operacionais, mas também
**expectativas sobre interferência política** — política de preços de combustíveis, dividendos
extraordinários, indicações para conselhos e mudanças na governança.

Durante 2022, debates sobre o papel das estatais no novo governo geraram **picos de volatilidade
muito mais agressivos** nesses papéis do que em empresas privadas. Nos gráficos comparativos,
PETR4 e BBAS3 frequentemente ocupam as faixas superiores de volatilidade, com saltos abruptos
que refletem notícias políticas pontuais (anúncios de troca de comando, discussões sobre
subsídios, medidas de contenção de preços).

Em termos econômicos, ativos estatais carregam um **prêmio de risco político**: o investidor
exige retorno adicional para compensar a incerteza regulatória e a possibilidade de decisões
que não maximizem valor para acionistas minoritários.

---

## 4. VALE3: Estabilidade Relativa Frente ao Cenário Doméstico

**VALE3** (Vale) apresentou comportamento **visivelmente mais estável** ao longo do ano eleitoral.
Embora não tenha ficado imune aos movimentos do mercado brasileiro, sua volatilidade foi
sistematicamente **inferior à de PETR4 e BBAS3**.

A explicação está na natureza do negócio: a Vale é uma das maiores produtoras de minério de ferro
do mundo, com receita fortemente atrelada à **demanda chinesa** e aos **preços internacionais de
commodities**. Enquanto o risco político doméstico dominava as discussões eleitorais, o preço do
minério e os indicadores globais de atividade industrial exerciam influência comparável — ou até
superior — sobre o papel.

Assim, a VALE3 funcionou como um ativo cuja volatilidade foi **ancorada no mercado externo**,
diluindo o impacto relativo dos eventos eleitorais brasileiros. Isso não significa ausência de risco,
mas sim que o canal de transmissão política → preço foi menos intenso do que nas estatais.

---

## 5. BOVA11: Linha de Base pela Diversificação

**BOVA11** é um ETF que replica o índice Ibovespa, reunindo dezenas de ações de diferentes setores.
Por construção, sua volatilidade reflete a **média ponderada** do mercado acionário brasileiro,
suavizando idiossincrasias de papéis individuais.

Nos gráficos comparativos, BOVA11 tende a ocupar uma posição **intermediária**: mais volátil que
VALE3 em momentos de estresse, mas menos extremo que PETR4 e BBAS3 nos picos políticos. Essa
característica o torna uma **linha de base (benchmark)** útil — qualquer ativo que se desvie
significativamente para cima está expondo o investidor a riscos específicos além do mercado.

A diversificação interna do índice absorve parte dos choques setoriais: quando estatais disparam
em volatilidade, outros setores (como consumo ou utilities) podem compensar parcialmente,
resultando em uma curva mais suave para o BOVA11.

---

## 6. Conclusão

A análise quantitativa de volatilidade com janela móvel de 21 pregões confirma que o **ciclo
eleitoral de 2022 foi um catalisador de risco** para a B3, com efeitos concentrados entre
setembro e novembro. Os ativos estatais **PETR4** e **BBAS3** demonstraram **maior sensibilidade
política**, enquanto **VALE3** manteve perfil mais estável graças à exposição global a commodities.
O **BOVA11**, por sua diversificação, ofereceu a referência mais equilibrada do mercado como um todo.

Esses resultados reforçam um princípio fundamental de finanças: **volatilidade é a linguagem
quantitativa da incerteza** — e em anos eleitorais, a incerteza política se traduz diretamente
nos gráficos que acabamos de analisar.
"""
