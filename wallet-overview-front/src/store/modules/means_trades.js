import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        means_trades: [],
    },
    mutations: {
        SET_MEANS_TRADES: (state, data) => (state.means_trades = data),
    },
    actions: {
        async FETCH_MEANS_TRADES({ commit }, body) {
            const { data } = await apiBack.get(`/mean_trade/user_platform_id/${body.user_id}/${body.platform_id}`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            // commit("errors/SET_ERROR_LOG", { message: "Balances Successfully Fetch" }, { root: true });
            commit("SET_MEANS_TRADES", data)
        }
    },
    getters: {

    },
}