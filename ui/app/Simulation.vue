html
<template>
<div>

<!-- Configuration du scénario -->
<ScenarioConfig
v-model="scenario"
/>

<!-- Affichage des résultats -->
<SimulationResults
v-if="results"
:results="results"
/>

<button
@click="startSimulation"
>
Lancer
</button>

</div>
</template>

<script>
import ScenarioConfig from './ScenarioConfig.vue'
import SimulationResults from './SimulationResults.vue'

export default {
components: {
ScenarioConfig,
SimulationResults
},

data() {
return {
scenario: {},
results: null
}
},

methods: {
async startSimulation() {
// Appeler le service de simulation
}
}
}
</script>