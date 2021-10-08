import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        synchro: false,
    },
    mutations: {
        SET_SYNCHRO: (state, data) => (state.synchro = data),
    },
    actions: {
        async SYNCHRONYSE({ commit }, body) {
            const { data } = await apiBack.post(`/synchronisation/`, {"user_id": body.user_id, "platform_id": body.platform_id, "new_user": true})
                .catch((error) => console.log(JSON.stringify(error.message)));
            console.log(data)
            commit("SET_SYNCHRO", true)
        }
    },
    getters: {

    },
}