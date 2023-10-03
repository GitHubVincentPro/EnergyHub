js
export const mutations = {
SET_SCENARIO(state, scenario) {
state.scenario = scenario
},

START_SIMULATION(state) {
state.status = 'running'
},

UPDATE_RESULTS(state, results) {
state.results = results
}
}

