import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

/* eslint-disable no-new */
const store = new Vuex.Store({    
state: {
  files: undefined,
  },
  mutations: {
    setFiles(state, files) {
        state.files = files
    },
  },
  actions: {
    // async getFiles() {
    //     return fetch(API_FUNCTION_GET_FILES)
    //         .then((result) => result.json())
    //         .then((files) => {
    //             this.commit('setFiles', files)
    //         });
    // },
    // async updateFiles() {
    //     await fetch(API_FUNCTION_UPDATE_FILES)
    //     return store.dispatch('getFiles')
    // }
},
})

export default store
