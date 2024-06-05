<template>
</template>

<script lang="ts">
import { defineComponent, ref} from 'vue';

export default defineComponent({
  name: 'summary',
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