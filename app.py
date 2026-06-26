import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf
from matplotlib.figure import Figure

from content import (
    DISCUSSION_SCRIPT,
    SIDEBAR_FORMULAS,
    SIDEBAR_METADATA,
    TAB1_INTRO,
    TAB2_INTRO,
)

# --- Constantes e parâmetros da análise ---

TICKERS = ["PETR4.SA", "VALE3.SA", "BBAS3.SA", "BOVA11.SA"]

TICKER_LABELS = {
    "PETR4.SA": "PETR4",
    "VALE3.SA": "VALE3",
    "BBAS3.SA": "BBAS3",
    "BOVA11.SA": "BOVA11",
}

TICKER_FULL_NAMES = {
    "PETR4.SA": "Petrobras",
    "VALE3.SA": "Vale",
    "BBAS3.SA": "Banco do Brasil",
    "BOVA11.SA": "iShares Ibovespa Index Fund (ETF)",
}

# Período estendido para garantir janela móvel de 21 pregões desde janeiro/2022
DATA_START = "2021-11-01"
DATA_END = "2022-12-31"

# Período exibido nos gráficos
CHART_START = "2022-01-01"
CHART_END = "2022-12-31"

ELECTION_DATES = {
    "1º Turno": "2022-10-02",
    "2º Turno": "2022-10-30",
}

TRADING_DAYS_PER_YEAR = 252


# --- Coleta e processamento de dados ---

def download_prices() -> pd.DataFrame:
    """Baixa preços de fechamento via yfinance e remove valores ausentes."""
    raw = yf.download(TICKERS, start=DATA_START, end=DATA_END, progress=False)

    if isinstance(raw.columns, pd.MultiIndex):
        prices = raw["Close"]
    else:
        prices = raw[["Close"]]
        prices.columns = TICKERS

    return prices.dropna()


def compute_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Calcula retornos logarítmicos diários: R_t = ln(P_t / P_{t-1})."""
    returns = np.log(prices / prices.shift(1))
    return returns.dropna()


def compute_annualized_volatility(returns: pd.DataFrame) -> pd.DataFrame:
    """Volatilidade diária amostral (janela 21) anualizada por sqrt(252)."""
    daily_vol = returns.rolling(window=21).std()
    return daily_vol * np.sqrt(TRADING_DAYS_PER_YEAR)


def filter_2022(df: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    """Filtra séries para exibição estritamente no ano de 2022."""
    return df.loc[CHART_START:CHART_END]


def load_market_data() -> dict:
    """Pipeline completo: preços, retornos e volatilidade anualizada."""
    prices = download_prices()
    returns = compute_log_returns(prices)
    annual_vol = compute_annualized_volatility(returns)

    return {
        "prices": prices,
        "returns": returns,
        "annual_vol": annual_vol,
    }


@st.cache_data(ttl=3600)
def get_data() -> dict:
    """Carrega e cacheia os dados de mercado para evitar re-downloads."""
    return load_market_data()


# --- Visualização (Matplotlib) ---

COMPARATIVE_COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]


def _style_axes(ax: plt.Axes, title: str, y_label: str) -> None:
    """Aplica estilo padrão aos eixos, limitando a exibição ao ano de 2022."""
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Data")
    ax.set_ylabel(y_label)
    ax.set_xlim(pd.Timestamp(CHART_START), pd.Timestamp(CHART_END))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b/%Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.grid(True, alpha=0.3, linestyle="--")
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")


def add_election_lines(ax: plt.Axes) -> None:
    """Adiciona linhas verticais tracejadas nas datas do 1º e 2º turno."""
    colors = ["#E63946", "#457B9D"]
    ymin, ymax = ax.get_ylim()

    for (label, date_str), color in zip(ELECTION_DATES.items(), colors):
        date = pd.Timestamp(date_str)
        ax.axvline(date, color=color, linestyle="--", linewidth=2)
        ax.text(
            date,
            ymax,
            f"  {label}",
            color=color,
            fontsize=10,
            fontweight="bold",
            verticalalignment="top",
            horizontalalignment="left",
        )

    ax.set_ylim(ymin, ymax)


def plot_prices(series: pd.Series, ticker: str) -> Figure:
    """Série temporal de preços de fechamento em 2022."""
    data = filter_2022(series)
    label = TICKER_LABELS.get(ticker, ticker)

    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(data.index, data.values, linewidth=2, color="#1f77b4")
    _style_axes(ax, f"Preço de Fechamento — {label}", "Preço (R$)")
    add_election_lines(ax)
    fig.tight_layout()
    return fig


def plot_log_returns(series: pd.Series, ticker: str) -> Figure:
    """Série temporal de retornos logarítmicos diários em 2022."""
    data = filter_2022(series)
    label = TICKER_LABELS.get(ticker, ticker)

    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(data.index, data.values, linewidth=1.5, color="#2A9D8F")
    _style_axes(ax, f"Retornos Logarítmicos Diários — {label}", "R_t")
    add_election_lines(ax)
    fig.tight_layout()
    return fig


def plot_annualized_vol(series: pd.Series, ticker: str) -> Figure:
    """Evolução da volatilidade anualizada móvel (21 pregões) em 2022."""
    data = filter_2022(series.dropna())
    label = TICKER_LABELS.get(ticker, ticker)

    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(data.index, data.values, linewidth=2, color="#E76F51")
    _style_axes(ax, f"Volatilidade Anualizada (janela 21) — {label}", "σ_a,t")
    add_election_lines(ax)
    fig.tight_layout()
    return fig


def plot_comparative_vol(vol_df: pd.DataFrame) -> Figure:
    """Sobrepõe a volatilidade anualizada dos quatro ativos no mesmo gráfico."""
    data = filter_2022(vol_df.dropna(how="all"))

    fig, ax = plt.subplots(figsize=(12, 4.5))
    for ticker, color in zip(data.columns, COMPARATIVE_COLORS):
        label = TICKER_LABELS.get(ticker, ticker)
        ax.plot(data.index, data[ticker], linewidth=2, label=label, color=color)

    _style_axes(ax, "Volatilidade Anualizada Comparativa — Todos os Ativos", "σ_a,t")
    add_election_lines(ax)
    ax.legend(loc="upper left", framealpha=0.9)
    fig.tight_layout()
    return fig


# --- Interface Streamlit ---

def render_header() -> None:
    """Cabeçalho principal com título e nomes completos dos ativos em destaque."""
    st.title("Análise de Volatilidade — B3 no Ano Eleitoral de 2022")

    legend_items = " &nbsp;&nbsp;|&nbsp;&nbsp; ".join(
        f"<span style='font-size: 1.75rem;'><strong>{TICKER_LABELS[ticker]}</strong> = {TICKER_FULL_NAMES[ticker]}</span>"
        for ticker in TICKERS
    )
    st.markdown(
        f"<div style='margin-top: -0.25rem; margin-bottom: 0.75rem; line-height: 1.6;'>{legend_items}</div>",
        unsafe_allow_html=True,
    )

    st.caption(
        "Retornos logarítmicos e volatilidade anualizada com janela móvel de 21 pregões"
    )


def render_sidebar() -> None:
    st.sidebar.title("Referência Técnica")
    st.sidebar.markdown(SIDEBAR_FORMULAS)

    st.sidebar.latex(r"R_t = \ln\left(\frac{P_t}{P_{t-1}}\right)")
    st.sidebar.latex(
        r"\sigma_{d,t} = \sqrt{\frac{\sum_{i=t-20}^{t} (R_i - \bar{R})^2}{21 - 1}}"
    )
    st.sidebar.latex(r"\sigma_{a,t} = \sigma_{d,t} \sqrt{252}")

    st.sidebar.markdown(SIDEBAR_METADATA)


def build_summary_table(annual_vol: pd.DataFrame) -> pd.DataFrame:
    """Tabela resumo de estatísticas de volatilidade anualizada em 2022."""
    vol_2022 = filter_2022(annual_vol).dropna(how="all")

    rows = []
    for ticker in TICKERS:
        series = vol_2022[ticker].dropna()
        label = TICKER_LABELS[ticker]
        rows.append(
            {
                "Ativo": label,
                "Média": series.mean(),
                "Mediana": series.median(),
                "Máximo": series.max(),
                "Desvio Padrão": series.std(),
            }
        )

    summary = pd.DataFrame(rows)
    for col in ["Média", "Mediana", "Máximo", "Desvio Padrão"]:
        summary[col] = summary[col].map(lambda x: f"{x:.2%}")
    return summary


def render_tab_graficos(data: dict) -> None:
    st.markdown(TAB1_INTRO)

    label_to_ticker = {v: k for k, v in TICKER_LABELS.items()}
    selected_label = st.selectbox(
        "Selecione o ativo para análise individual:",
        options=list(label_to_ticker.keys()),
    )
    ticker = label_to_ticker[selected_label]

    vol_2022 = filter_2022(data["annual_vol"][ticker]).dropna()
    col1, col2, col3 = st.columns(3)
    col1.metric("Volatilidade Média (2022)", f"{vol_2022.mean():.2%}")
    col2.metric("Volatilidade Máxima (2022)", f"{vol_2022.max():.2%}")
    col3.metric("Data do Pico", vol_2022.idxmax().strftime("%d/%m/%Y"))

    st.pyplot(plot_prices(data["prices"][ticker], ticker), clear_figure=True)
    st.pyplot(plot_log_returns(data["returns"][ticker], ticker), clear_figure=True)
    st.pyplot(plot_annualized_vol(data["annual_vol"][ticker], ticker), clear_figure=True)


def render_tab_comparativa(data: dict) -> None:
    st.markdown(TAB2_INTRO)

    st.pyplot(plot_comparative_vol(data["annual_vol"]), clear_figure=True)

    st.subheader("Estatísticas de Volatilidade Anualizada — 2022")
    st.dataframe(build_summary_table(data["annual_vol"]), use_container_width=True, hide_index=True)


def render_tab_roteiro() -> None:
    st.markdown(DISCUSSION_SCRIPT)


def main() -> None:
    st.set_page_config(
        page_title="Volatilidade B3 — Eleições 2022",
        page_icon="📈",
        layout="wide",
    )

    render_header()
    render_sidebar()

    with st.spinner("Carregando dados da B3 via yfinance..."):
        data = get_data()

    tab_graficos, tab_comparativa, tab_roteiro = st.tabs(
        [
            "📈 Gráficos Interativos",
            "📊 Análise Comparativa",
            "📝 Roteiro de Discussão Teórica",
        ]
    )

    with tab_graficos:
        render_tab_graficos(data)

    with tab_comparativa:
        render_tab_comparativa(data)

    with tab_roteiro:
        render_tab_roteiro()


if __name__ == "__main__":
    main()
