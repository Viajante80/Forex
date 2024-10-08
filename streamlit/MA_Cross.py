import streamlit as st
import pandas as pd

ma_test_res = pd.read_pickle("ma_test_res.pkl")
all_trades = pd.read_pickle("all_trades.pkl")

ma_test_res["CROSS"] = "MA_" + ma_test_res.mashort.map(str) + "_" + ma_test_res.malong.map(str)
all_trades["CROSS"] = "MA_" + all_trades.MASHORT.map(str) + "_" + all_trades.MALONG.map(str)

crosses = ma_test_res["CROSS"].unique()
cross = st.sidebar.selectbox("Cross", crosses)
st.write("Cross:", cross)

ma_test_res_cross = ma_test_res[ma_test_res["CROSS"] == cross].copy()
all_trades_cross = all_trades[all_trades["CROSS"] == cross].copy()

ma_test_res_cross = ma_test_res_cross[["pair", "num_trades", "total_gain"]]

st.dataframe(ma_test_res_cross, hide_index=True)

for index, row in ma_test_res_cross.iterrows():
    st.write(row.pair)
    chart_df = all_trades_cross[all_trades_cross.PAIR == row.pair]
    chart_df["CUM_GAIN"] = chart_df.GAIN.cumsum()
    st.line_chart(
        chart_df,
        x="time",
        y="CUM_GAIN",
    )


# for index, row in ma_test_res_pair.iterrows():
#     if row.total_gain > 0:
#         st.write(row.CROSS)
#         chart_df = all_trades_pair[all_trades_pair.CROSS == row.CROSS]
#         chart_df["CUM_GAIN"] = chart_df.GAIN.cumsum()
#         st.line_chart(
#             chart_df,
#             x="time",
#             y="CUM_GAIN",
#         )
