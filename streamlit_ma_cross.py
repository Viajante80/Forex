import streamlit as st
import pandas as pd

ma_test_res = pd.read_pickle("ma_test_res.pkl")
all_trades = pd.read_pickle("all_trades.pkl")

pairs = ma_test_res["pair"].unique()

pair = st.sidebar.selectbox("Pairs", pairs)
st.write("You selected:", pair)

ma_test_res_pair = ma_test_res[ma_test_res["pair"] == pair].copy()
all_trades_pair = all_trades[all_trades["PAIR"] == pair].copy()

ma_test_res_pair["CROSS"] = "MA_" + ma_test_res_pair.mashort.map(str) + "_" + ma_test_res_pair.malong.map(str)
all_trades_pair["CROSS"] = "MA_" + all_trades_pair.MASHORT.map(str) + "_" + all_trades_pair.MALONG.map(str)


ma_test_res_pair = ma_test_res_pair[["CROSS", "num_trades", "total_gain"]]
# ma_test_res_pair = ma_test_res_pair[["CROSS", "num_trades", "total_gain", "min_gain", "max_gain"]]
ma_test_res_pair.sort_values(by="total_gain", ascending=False, inplace=True)


st.dataframe(ma_test_res_pair, hide_index=True)


# for cross in all_trades_pair.CROSS:
#     df_temp = ma_test_res_pair[ma_test_res_pair.CROSS == cross]
#     total_p = df_temp.shape[0]
#     n_good = df_temp[df_temp.total_gain > 0].shape[0]
#     # # print(f"{cross:12} {n_good:4} {(n_good / total_p) * 100:4.0f}%")
#     st.write(f"{cross:12} {n_good:4} {(n_good / total_p) * 100:4.0f}%")

# for total_gain in ma_test_res_pair.total_gain:
#     if total_gain > 0:
#         st.write(total_gain)

for index, row in ma_test_res_pair.iterrows():
    if row.total_gain > 0:
        st.write(row.CROSS)
        chart_df = all_trades_pair[all_trades_pair.CROSS == row.CROSS]
        chart_df["CUM_GAIN"] = chart_df.GAIN.cumsum()
        # st.line_chart(
        #     chart_df,
        #     x="time",
        #     y="GAIN",
        # )
        st.line_chart(
            chart_df,
            x="time",
            y="CUM_GAIN",
        )
    # if row.total_gain <   0:
    # st.write(row)
