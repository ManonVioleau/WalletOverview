import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        trades_open: [],
        trades_open_ordered: []
    },
    mutations: {
        SET_TRADES_OPEN: (state, data) => (state.trades_open = data),
        SET_TRADES_OPEN_ORDERED: (state, data) => (state.trades_open_ordered = data),
    },
    actions: {
        async FETCH_TRADES_OPEN({ commit }, body) {
            const { data } = await apiBack.get(`/trade_open/user_platform_id/${body.user_id}/${body.platform_id}/`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            commit("SET_TRADES_OPEN", data)
            const trades_closed_ordered = data.sort((a, b) => (a.date < b.date && 1) || -1);
            commit("SET_TRADES_OPEN_ORDERED", trades_closed_ordered)
        }
    },
    getters: {

    },
}