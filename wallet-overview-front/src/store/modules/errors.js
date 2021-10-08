export default {
    namespaced: true,
    state: {
      errors: {},
    },
    mutations: {
      SET_ERROR_LOG: (rootState, errors) => rootState.errors = errors
    },
    actions: {
      UPDATE_ERRORS({commit}, errors) {
        commit('SET_ERROR_LOG', errors);
      }
    }
}