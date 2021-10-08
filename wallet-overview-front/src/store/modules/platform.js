import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        platforms: [],
    },
    mutations: {
        SET_PLATFORMS: (state, data) => (state.platforms = data),
    },
    actions: {
        async FETCH_PLATFORMS({ commit }, body) {
            const { data } = await apiBack.get(`/platform/${body.platform_id}/`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            // commit("errors/SET_ERROR_LOG", { message: "Balances Successfully Fetch" }, { root: true });
            commit("SET_PLATFORMS", data)
        }
    },
    getters: {

    },
}