import { reactive, toRefs } from 'vue';
import { useApi } from 'src/store/api';

const {
    salaryApi
  } = useApi();

const state = reactive({
    resume: '',
    expectedSalary: '',
    loading: false,
    recRows: [],
    skills: []
});

export async function extractSkills(resume: string) {
  const resp = await salaryApi.value.skillsSalarySkillsPost(resume);
  const { data } = resp;
  console.log(data);
  state.skills = data
}

export async function predictSalary(resume: string) {
  const resp = await salaryApi.value.predictSalaryPredictPost(resume);
  const { data } = resp;
  state.expectedSalary = data;
}

export async function recommendSkill(resume: string) {
  const resp = await salaryApi.value.recSalaryRecommendGet(resume);
  const { data } = resp;
  state.recRows = data;
}

export function useLevelUpState() {
    return { 
        ...toRefs(state) ,
        extractSkills,
        predictSalary,
        recommendSkill
    };
  }