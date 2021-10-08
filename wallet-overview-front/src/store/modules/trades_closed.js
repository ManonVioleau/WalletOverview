import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        trades_closed: [],
        trades_closed_ordered: []
    },
    mutations: {
        SET_TRADES_CLOSED: (state, data) => (state.trades_closed = data),
        SET_TRADES_CLOSED_ORDERED: (state, data) => (state.trades_closed_ordered = data),
    },
    actions: {
        async FETCH_TRADES_CLOSED({ commit }, body) {
            const { data } = await apiBack.get(`/trade_closed/user_platform_id/${body.user_id}/${body.platform_id}/`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            commit("SET_TRADES_CLOSED", data)
            const trades_closed_ordered = data.sort((a, b) => (a.date < b.date && 1) || -1);
            commit("SET_TRADES_CLOSED_ORDERED", trades_closed_ordered)
        }
    },
    getters: {

    },
}