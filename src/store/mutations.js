import Vue from "vue"

export default {
    setSessionToken(state, payload){
        Vue.set(state.session,'jsToken',payload)
    }
}