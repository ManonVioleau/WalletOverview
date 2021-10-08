import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Dashboard from "../views/Dashboard.vue"
import Trades from "../views/Trades.vue"
import LogIn from "../views/auth/LogIn.vue"
import SignUp from "../views/auth/SignUp.vue"
import LogOut from "../views/auth/LogOut.vue"
import Wallets from "../views/Wallets.vue"
import AddWallet from "../views/AddWallet.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/Home",
    name: "Home",
    component: Home,
  },
  {
    path: "/LogIn",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/SignUp",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/LogOut",
    name: "LogOut",
    component: LogOut,
  },
  {
    path: "/Dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/Wallets",
    name: "Wallets",
    component: Wallets,
  },
  {
    path: "/AddWallet",
    name: "AddWallet",
    component: AddWallet,
  },
  {
    path: "/Trades",
    name: "Trades",
    component: Trades,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
