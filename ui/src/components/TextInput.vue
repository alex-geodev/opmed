<template>
    <q-input
      v-model="prompt"
      filled
      stack-label
      label="Provide Further Requirements"
      >

    </q-input>
</template>

<script lang="ts">
import { defineComponent, ref} from 'vue';

export default defineComponent({
  name: 'textInput',
  setup() {
    const prompt = ref("");

    return {
      prompt
    }
  }
});
</script>

<style scoped>

</style>