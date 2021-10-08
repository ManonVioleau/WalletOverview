import Vue from "vue";
import Vuex from "vuex";
import balances from './modules/balances'
import errors from './modules/errors'
import walletevolutions from './modules/walletevolutions'
import means_trades from './modules/means_trades'
import auth from './modules/auth'
import wallets from './modules/wallets'
import synchronyse from './modules/synchronyse'
import platform from './modules/platform'
import trades_closed from './modules/trades_closed'
import trades_open from './modules/trades_open'
import transferts from './modules/transferts'
import transferts_ordered from './modules/transferts_ordered'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    balances,
    errors,
    walletevolutions,
    means_trades,
    auth,
    wallets,
    synchronyse,
    platform,
    trades_open,
    trades_closed,
    transferts,
    transferts_ordered,
  },
});
