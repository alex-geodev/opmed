<template>
    <q-input
      v-model="radioText"
      filled
      stack-label
      label="Radio Chatter"
      >

    </q-input>
</template>

<script lang="ts">
import { defineComponent} from 'vue';
import { useState } from 'src/store/main'

export default defineComponent({
  name: 'radioInput',
  setup() {
    const {
        radioText
      } = useState();

    return {
      radioText
    }
  }
});
</script>

<style scoped>

</style>