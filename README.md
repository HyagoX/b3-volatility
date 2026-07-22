# 📈 Análise da Volatilidade de Ativos da B3 no Ano Eleitoral de 2022

Projeto desenvolvido para a disciplina da faculdade com o objetivo de analisar o comportamento da volatilidade de ativos da Bolsa de Valores brasileira (B3) durante o período das eleições presidenciais de 2022.

A aplicação foi desenvolvida utilizando **Python**, **Streamlit**, **Pandas**, **Matplotlib** e **Yahoo Finance (yfinance)** para coleta automática dos dados.

---

## Objetivo

Investigar como eventos políticos podem influenciar o mercado financeiro brasileiro através da análise da volatilidade dos principais ativos da B3.

Foram analisados os seguintes ativos:

- PETR4 (Petrobras)
- VALE3 (Vale)
- BBAS3 (Banco do Brasil)
- BOVA11 (ETF do Ibovespa)

A análise considera:

- Preços de fechamento
- Retornos logarítmicos diários
- Volatilidade anualizada utilizando janela móvel de 21 pregões
- Comparação entre os ativos durante o período eleitoral

---

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas
- NumPy
- Matplotlib
- yfinance

---

## Modelos Matemáticos

### Retorno Logarítmico

O retorno diário é calculado pela expressão

\[
R_t=\ln\left(\frac{P_t}{P_{t-1}}\right)
\]

onde:

- \(P_t\) é o preço no dia atual;
- \(P_{t-1}\) é o preço do pregão anterior.

---

### Volatilidade Diária

A volatilidade diária corresponde ao desvio-padrão amostral dos retornos em uma janela móvel de 21 pregões.

\[
\sigma_d=\sqrt{\frac{\sum(R_i-\bar R)^2}{n-1}}
\]

---

### Volatilidade Anualizada

A volatilidade anualizada é obtida por

\[
\sigma_a=\sigma_d\sqrt{252}
\]

considerando 252 pregões por ano.

---

## Dados Utilizados

| Item | Valor |
|------|-------|
| Fonte | Yahoo Finance |
| Coleta | Novembro/2021 – Dezembro/2022 |
| Período analisado | Janeiro/2022 – Dezembro/2022 |
| Janela móvel | 21 pregões |
| 1º Turno | 02/10/2022 |
| 2º Turno | 30/10/2022 |

---

## Funcionalidades

- Visualização dos preços de fechamento
- Cálculo dos retornos logarítmicos
- Cálculo da volatilidade anualizada
- Comparação entre os quatro ativos
- Estatísticas descritivas
  - média
  - mediana
  - máximo
  - desvio padrão
- Destaque visual das datas do primeiro e segundo turno das eleições
- Roteiro teórico explicando os resultados encontrados

---

## Estrutura do Projeto

```
.
├── app.py
├── content.py
├── requirements.txt
└── README.md
```

---

## Acesse o Projeto

Link: https://b3-volatility-rate.streamlit.app/

---

## Resultados Esperados

Durante o segundo semestre de 2022 observa-se um aumento significativo da volatilidade, principalmente entre setembro e novembro, período que engloba as eleições presidenciais.

Os ativos estatais **PETR4** e **BBAS3** apresentaram maior sensibilidade ao cenário político, enquanto **VALE3** apresentou comportamento relativamente mais estável devido à forte influência do mercado internacional de commodities.

O **BOVA11** serviu como benchmark do mercado brasileiro, apresentando uma volatilidade intermediária em relação aos demais ativos.

---

## Autores

Projeto desenvolvido para fins acadêmicos na disciplina de Introdução a programação de computadores no curso de Matemática Aplicada.

---