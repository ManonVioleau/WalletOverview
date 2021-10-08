import apiBack from "@/common/api-back"

export default {
    namespaced: true,
    state: {
        user: {},
        connected: false,
    },
    mutations: {
        SET_USER: (state, data) => (state.user = data),
        SET_CONNECTED: (state, data) => (state.connected = data),
    },
    actions: {
        async REGISTER({ commit }, body) {
            const { data } = await apiBack.post(`/users/register/`, { "name": body.name, "email": body.email, "password": body.password })
                .catch((error) => console.log(JSON.stringify(error.message)));
            commit("errors/SET_ERROR_LOG", { message: data.message }, { root: true });
            if (data.success) {
                commit("SET_USER", data.data)
                commit("SET_CONNECTED", true)
                if (body.remember) {
                    let d = new Date();
                    d.setTime(d.getTime() + 1 * 24 * 60 * 60 * 1000);
                    let expires = "expires=" + d.toUTCString();
                    let profil = JSON.stringify(data.data);
                    document.cookie = `profil=${profil};${expires};path=/;secure`;
                }
            }
        },
        async LOGIN({ commit }, body) {
            const { data } = await apiBack.post(`/users/login/`, { "name": body.name, "password": body.password })
                .catch((error) => console.log(JSON.stringify(error.message)));
            commit("errors/SET_ERROR_LOG", { message: data.message }, { root: true });
            if (data.success) {
                commit("SET_USER", data.data)
                commit("SET_CONNECTED", true)
                if (body.remember) {
                    let d = new Date();
                    d.setTime(d.getTime() + 1 * 24 * 60 * 60 * 1000);
                    let expires = "expires=" + d.toUTCString();
                    let profil = JSON.stringify(data.data);
                    document.cookie = `profil=${profil};${expires};path=/;secure`;
                }
            }
        }
    },
    getters: {

    },
}