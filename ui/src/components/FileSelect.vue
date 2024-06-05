<template>
  <q-select v-model="selected" :options="options" option-value="id" emit-value map-options option-label="id" stack-label label="Choose 9 Line"/>
</template>

<script lang="ts">
import { defineComponent, ref} from 'vue';

export default defineComponent({
  name: 'fileSelect',
  setup() {
    const selected = ref(undefined);
    const options = ref([
      {
        "id": "abc",
        "mgrs": "weird string",
        "lat": 20.123,
        "lon": 123.123,
        "frequency": 123.412,
        "urgent": 1,
        "urgent_surgical": 0,
        "priority": 1,
        "routine": 3,
        "convenience": 0,
        "ambulatory": 12,
        "us_military": 1,
        "us_civilian": 2,
        "non_us_civilian": 0,
        "enemy_prisoner_of_war":1,
        "equipment": "Ventilator",
        "audio_file": "/path/to/file",
        "audio_translation": "blah blah blah",
      },
    ])

    return {
      options,
      selected
    }
  }
});
</script>

<style scoped>

</style>