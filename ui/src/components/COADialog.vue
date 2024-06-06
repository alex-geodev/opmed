<template>
  <q-dialog v-model="coaDialog" style="height:80vh; width:80vw">
    <q-card class="text-center q-pa-xl" style="height:80vh; min-width:80vw">
      <q-table
        :rows="rows"
        :columns="columns"
      >

      </q-table>
    </q-card>
  </q-dialog>
</template>

<script lang="ts">
import { defineComponent} from 'vue';
import { useState } from 'src/store/main'

export default defineComponent({
  name: 'coaDialog',
  setup() {
    const {
        activeCOA,
        rows,
        coaDialog
      } = useState();

    const columns = [
    { name: 'key', label: 'Name', field: 'key', sortable: true, align: "center"},
    { name: 'value', label: 'Value', field: 'value', align: "center" },
    ]


    return {
      activeCOA,
      coaDialog,
      columns,
      rows
    }
  }
});
</script>

<style scoped>

</style>