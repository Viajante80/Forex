import streamlit as st
import pandas as pd

ma_test_res = pd.read_pickle("ma_test_res.pkl")
all_trades = pd.read_pickle("all_trades.pkl")

pairs = ma_test_res["pair"].unique()

pair = st.sidebar.selectbox("Pairs", pairs)
st.write("Pair:", pair)

ma_test_res_pair = ma_test_res[ma_test_res["pair"] == pair].copy()
all_trades_pair = all_trades[all_trades["PAIR"] == pair].copy()

ma_test_res_pair["CROSS"] = "MA_" + ma_test_res_pair.mashort.map(str) + "_" + ma_test_res_pair.malong.map(str)
all_trades_pair["CROSS"] = "MA_" + all_trades_pair.MASHORT.map(str) + "_" + all_trades_pair.MALONG.map(str)


ma_test_res_pair = ma_test_res_pair[["CROSS", "num_trades", "total_gain"]]
ma_test_res_pair.sort_values(by="total_gain", ascending=False, inplace=True)


st.dataframe(ma_test_res_pair, hide_index=True)

for index, row in ma_test_res_pair.iterrows():
    if row.total_gain > 0:
        st.write(row.CROSS)
        chart_df = all_trades_pair[all_trades_pair.CROSS == row.CROSS]
        chart_df["CUM_GAIN"] = chart_df.GAIN.cumsum()
        st.line_chart(
            chart_df,
            x="time",
            y="CUM_GAIN",
        )
