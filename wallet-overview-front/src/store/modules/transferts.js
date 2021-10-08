import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        transferts: [],
    },
    mutations: {
        SET_TRANSFERTS: (state, data) => (state.transferts = data),
    },
    actions: {
        async FETCH_TRANSFERTS({ commit }, body) {
            const { data } = await apiBack.get(`/transfert/user_platform_id/${body.user_id}/${body.platform_id}/`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            commit("SET_TRANSFERTS", data)
        }
    },
    getters: {

    },
}