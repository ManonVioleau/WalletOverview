import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        balances: [],
        balance: {},
        total: 0,
        datas: [],
    },
    mutations: {
        SET_BALANCES: (state, data) => (state.balances = data),
        SET_BALANCE: (state, data) => (state.balance = data),
        SET_TOTAL: (state, data) => (state.total = data),
        SET_DATAS_GRAPH: (state, data) => (state.datas = data),
    },
    actions: {
        async FETCH_BALANCES({ commit }, body) {
            const { data } = await apiBack.get(`/balance/user_platform_id/${body.user_id}/${body.platform_id}`)
                .catch((error) => console.log(JSON.stringify(error.message)));
            let total = 0;
            if (data != []) {
                data.sort((a, b) => (a.value < b.value && 1) || -1);
                data.forEach((balance) => {
                    total += balance.value;
                });
                let limit = (total / data.length) / 1.5;
                let datas = []
                let others = {'data': 0, 'label': 'Others'}
                data.forEach((balance) => {
                    if (balance.value > limit) {
                        datas.push({'data': balance.value, 'label': balance.coin})
                    } else {
                         others.data += balance.value
                    }
                });
                datas.push(others)
                commit("SET_BALANCES", data)
                commit("SET_DATAS_GRAPH", datas)
                commit("SET_TOTAL", total)
                commit("synchronyse/SET_SYNCHRO", true, { root: true });
                
            } else {
                commit("synchronyse/SET_SYNCHRO", false, { root: true });
            }
        }
    },
    getters: {

    },
}