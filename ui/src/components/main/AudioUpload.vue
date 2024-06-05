<template>
    <div class="text-center">
    <q-form class="q-gutter-md q-pa-lg">
        <q-input square filled clearable v-model="this.resume" label="Paste Resume Content" class="q-py-md" type="textarea" rows="30" overflow="hidden"/>
        <q-btn color = "accent" align="center" @click="submitJob()" :loading="loading">Run Analysis</q-btn>
    </q-form>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref} from 'vue';
import { useApi } from 'src/store/api';
import { useLevelUpState } from 'src/store/levelup'

export default defineComponent({
  name: 'audioUpload',
  setup() {
      const {
        salaryApi
      } = useApi();
      
      const {
          resume,
          extractSkills,
          predictSalary,
          recommendSkill,
          loading,
      } = useLevelUpState();

      return {
          salaryApi,
          extractSkills,
          predictSalary,
          recommendSkill,
          loading,
          resume,
      }
  },
  methods: {
      async submitJob(): Promise<void> {
          this.loading = true;
          await this.extractSkills(this.resume);
          await this.predictSalary(this.resume);
          await this.recommendSkill(this.resume);
          this.loading = false;
      }
  }
});
</script>

<style scoped>

</style>