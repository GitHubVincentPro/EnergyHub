js
export default {
runSimulation(scenario) {
return this.$http.post('/api/simulation', scenario)
},

updateResults(results) {
// Emettre un événement
}
}