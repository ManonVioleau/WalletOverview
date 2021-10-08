import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        transferts_ordered: [],
    },
    mutations: {
        SET_TRANSFERTS_ORDERED: (state, data) => (state.transferts_ordered = data),
    },
    actions: {
        async FETCH_TRANSFERTS_ORDERED({ commit }, body) {
            const { data } = await apiBack.get(`/transfert_ordered/user_platform_id/${body.user_id}/${body.platform_id}/`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            commit("SET_TRANSFERTS_ORDERED", data)
        }
    },
    getters: {

    },
}