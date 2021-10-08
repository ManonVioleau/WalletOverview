import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        wallets: [],
        had_wallet: false,
        success: false,
    },
    mutations: {
        ADD_WALLET: (state, data) => (state.wallets.push(data)),
        SET_WALLETS: (state, data) => (state.wallets = data),
        SET_SUCCESS:  (state, data) => (state.success = data),
        SET_HAD_WALLET:  (state, data) => (state.had_wallet = data),
    },
    actions: {
        async ADD_WALLET({ commit, dispatch }, body) {
            const { data } = await apiBack.get(`/platform_by_name/${body.platform_name}/`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            const platform = data.data
            if (body.platform_name == "Binance") {
                console.log(body)
                const { data } = await apiBack.post(`/wallet/`, { "user_id": body.user_id, "platform_id": platform.id, "name": body.name, "api_key": body.api_key, "api_secret": body.api_secret })
                    .catch((error) => console.log(JSON.stringify(error.message)));
                console.log(data)
                if (data.success) {
                    commit("errors/SET_ERROR_LOG", { message: "Wallet successfully added, please go to your Wallets to see it !" }, { root: true });
                    commit("SET_SUCCESS", true)
                    dispatch("FETCH_WALLETS", { "user_id": body.user_id, "platform_id": platform.id })
                } else {
                    commit("errors/SET_ERROR_LOG", { message: 'API key format invalid' }, { root: true });
                    commit("SET_SUCCESS", true)
                }
            }
        },
        async FETCH_WALLETS({ commit }, body) {
            const { data } = await apiBack.get(`/wallet/user_id/${body.user_id}`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            if (data.length != 0) {
                console.log('ok')
                commit("SET_WALLETS", data)
                commit("SET_HAD_WALLET", true)
            } else {
                commit("SET_HAD_WALLET", false)
            }
        },
    },
    getters: {

    },
}