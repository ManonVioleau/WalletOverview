import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        walletevolutions: [],
    },
    mutations: {
        SET_WALLETEVOLUTIONS: (state, data) => (state.walletevolutions = data),
    },
    actions: {
        async FETCH_WALLETEVOLUTIONS({ commit }, body) {
            const { data } = await apiBack.get(`/wallet_evolution/user_platform_id/${body.user_id}/${body.platform_id}`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            // commit("errors/SET_ERROR_LOG", { message: "Balances Successfully Fetch" }, { root: true });
            commit("SET_WALLETEVOLUTIONS", data)
        }
    },
    getters: {

    },
}