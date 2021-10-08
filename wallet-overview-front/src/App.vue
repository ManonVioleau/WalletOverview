<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  components: {
    NavBar,
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600;700;800;900&display=swap");

* {
  font-family: "Roboto", sans-serif;
  margin: 0;
  padding: 0;
  color: rgba(0, 0, 0, 0.75);
  font-weight: 400;
  font-size: 1rem;
  text-decoration: none;
  transition: 0.25s;
}

button {
  background-color: #ffae42;
  border: none;
  padding: 0 1rem;
  margin: 1rem 0;
  border-radius: 0.5rem;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 600;
  cursor: pointer;
}

button:hover {
  background-color: #ffae42;
  opacity: 0.75;
}

body {
  background-color: rgba(0, 0, 0, 0.1);
}

#app {
  margin: 2rem 8rem;
}

a {
  color: rgba(0, 0, 0, 0.65);
  &.router-link-exact-active {
    color: #ffae42;
  }
}

// NAV
#nav {
  display: flex;
  justify-content: space-between;
  position: relative;
  background-color: rgba(255, 255, 255, 0.5);
  padding: 2rem;
  border-radius: 5rem;
  box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.05), -3px -3px 5px white;
  overflow: hidden;
}

#nav a {
  font-weight: 500;
  margin: auto;
  margin: auto 2rem;
  position: relative;
}

#nav .underline:hover::after {
  width: 100%;
}

#nav .underline::after {
  content: "";
  background-color: #ffae42;
  position: absolute;
  top: 1.5rem;
  left: 0;
  width: 0;
  height: 3px;
  transition: 0.25s;
}

#nav h1,
#nav span {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 800;
  font-family: "Nunito", sans-serif;
}

#nav span {
  color: #ffae42;
}

#sub_nav {
  display: flex;
  justify-content: space-between;
}

.middle {
  margin: auto 0;
  display: flex;
}

.menu_icon {
  display: none;
  position: absolute;
  right: 3.5rem;
  top: 2rem;
  height: 2.5rem;
}

img {
  cursor: pointer;
}
// END NAV
// DASHBOARD

.title {
  display: flex;
  justify-content: space-between;
}

.section {
  margin: 3rem 0;
  // attention
  // padding-right: 2rem;
}

h1 {
  font-weight: 600;
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
}

h2 {
  font-weight: 400;
  font-size: 1.5rem;
  margin-bottom: 1rem;
  text-align: center;
}

h2 span {
  font-weight: 600;
  font-size: 1.5rem;
  margin-bottom: 1rem;
  text-align: center;
}

.content {
  display: grid;
  width: 100%;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(4, 1fr);
  grid-gap: 1rem;
}

.square {
  background-color: rgba(255, 255, 255, 0.5);
  padding: 2rem;
  margin-bottom: 1rem;
  box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.05);
}

.content img {
  width: 100%;
}

.column {
  margin-bottom: -1rem;
}

#walletevolution {
  grid-column-start: 2;
  grid-column-end: 5;
}

#lasttrades {
  grid-column-start: 1;
  grid-column-end: 3;
}

#lasttradesopen {
  grid-column-start: 3;
  grid-column-end: 5;
}

.last_update {
  font-size: 0.8rem;
  color: rgba(0, 0, 0, 0.5);
  margin-top: 1rem;
  font-style: italic;
  font-weight: 400;
}

#trades-datas {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

#trades-datas p {
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.1);
  padding: 0.5rem 0;
}

.auth h1 {
  text-align: center;
  margin-top: 1rem;
}

.auth {
  width: 20rem;
  margin: auto;
  margin-top: 3rem;
  padding: 1rem;
}

.auth p {
  text-align: center;
}

.auth form {
  display: grid;
  grid-template-columns: 1fr;
}

.auth form input {
  margin: 0.5rem 0;
  padding: 0.5rem;
}

.auth form button {
  padding: 0.5rem 0;
}

#sync-navbar {
  display: flex;
  cursor: default;
}

#sync-navbar p {
  margin: auto;
}

#sync-navbar img {
  width: 2.5rem;
}

#sync-navbar img:hover {
  transform: scale(1.1);
}

.errors,
.messages {
  background-color: rgba(255, 0, 0, 0.1);
  padding: 0.5rem;
  width: 21rem;
  margin: auto;
  margin-top: 2rem;
  margin-bottom: -1rem;
  display: flex;
  justify-content: space-between;
}

.errors p,
.messages p {
  margin: auto;
  margin-left: 0;
}

.errors img:hover,
.messages img:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.addwallet .errors {
  margin: 0;
  margin-bottom: 1rem;
  width: 98%;
}
.addwallet .messages {
  margin: 0;
  margin-bottom: 1rem;
  width: 100%;
}

.messages {
  background-color: rgba(0, 255, 0, 0.1);
}

.auth form div {
  display: flex;
}

.auth form div p {
  margin: auto;
  margin-left: 0.5rem;
  color: rgba(0, 0, 0, 0.65);
}

.wallet-content {
  display: grid;
  grid-template-columns: 20% 80%;
  grid-gap: 1rem;
}

.wallet-content h2 {
  margin: 0;
  text-align: left;
}

.wallet-content .last_update {
  margin-top: 0.5rem;
}

.addwallet h1 {
  text-align: center;
}

.addwallet {
  width: 90%;
  margin: auto;
  margin-top: 3rem;
  padding: 1rem;
}

.infos-add-wallet {
  line-height: 1.5rem;
}

.section-add-wallet h3 {
  font-size: 1.1rem;
  margin: 0.5rem 0;
}

.section-add-wallet input {
  padding: 0.5rem;
  width: 90%;
}

.section-add-wallet button {
  padding: 0.75rem;
}

.infos-add-wallet span {
  font-weight: 600;
}

.section-add-wallet {
  display: grid;
  grid-template-columns: 50% 50%;
  grid-gap: 1rem;
}

.addwallet .square,
.addwallet h2 {
  text-align: left;
}

.addwallet select {
  width: 18rem;
  padding: 0.5rem;
  font-size: 1rem;
}

.wallet-content h3 {
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.trades-tab {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
}

.trades-tab p {
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.1);
  padding: 0.5rem 0;
}

// END DASHBOARD

@media (max-width: 1200px) {
  #app {
    margin: 2rem 5rem;
  }
  #nav {
    display: grid;
    grid-template-columns: 1fr;
    padding: 2rem;
    min-height: 2.5rem;
  }
  #nav h1 {
    position: absolute;
    top: 0.25rem;
  }
  .middle {
    overflow: hidden;
    transition: 0.5s;
    display: grid;
    height: 0;
    transform: translateY(-20rem);
    text-align: center;
    line-height: 2rem;
    margin: 0;
  }

  .wallet-content {
    grid-template-columns: 1fr;
  }

  .middle a {
    font-size: 1.25rem;
    color: rgba(255, 255, 255, 0.75);
    color: rgba(0, 0, 0, 0.75);
  }
  #first {
    margin-top: 3rem;
  }
  .menu_icon {
    display: flex;
  }
  #nav .underline:hover::after {
    width: 0;
  }
  #nav a:hover {
    opacity: 0.5;
  }
  .content {
    display: grid;
    grid-template-columns: 1fr;
    grid-gap: 0;
  }

  #walletevolution, #lasttrades, #lasttradesopen {
    grid-column: 1;
  }
}

@media (max-width: 600px) {
  #app {
    margin: 2rem;
  }
}

@media (max-width: 400px) {
  #app {
    margin: 2rem;
  }

  #nav {
    display: contents;
  }

  #nav h1,
  #nav .menu_icon {
    display: flex;
    justify-content: center;
  }
}
</style>
