<template>
  <q-select v-model="activeNineLine" :options="allNineLines" emit-value map-options option-label="id" stack-label label="Choose 9 Line"/>
</template>

<script lang="ts">
import { defineComponent, onMounted} from 'vue';
import { useState } from 'src/store/main';

export default defineComponent({
  name: 'fileSelect',
  setup() {
      const {
        allNineLines,
        activeNineLine,
        getNineLines
      } = useState();

      onMounted(() => {
        getNineLines();
      })

      return {
        allNineLines,
        activeNineLine,
      }
  }
});
</script>

<style scoped>

</style>