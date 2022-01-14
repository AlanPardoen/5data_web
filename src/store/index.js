import Vue from 'vue'
import Vuex from 'vuex'
import actions from './actions'
import getters from './getters'
import mutations from './mutations'
import state from './state'

Vue.use(Vuex)

/* eslint-disable no-new */
const store = new Vuex.Store({    
  state: state.getState(),
  mutations: mutations,
  actions: actions,
  getters:getters
})

export default store
