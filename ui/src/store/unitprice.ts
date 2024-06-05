import { reactive, toRefs } from 'vue';
import { useApi } from 'src/store/api';

const {
    salaryApi,
    metricsApi
  } = useApi();

const state = reactive({
    jobdesc: '',
    expectedSalary: null,
    avgSalary: null,
    stdSalary: null,
    extractedSkills: [],
    skillBins: [],
    similarity: {vals: []},
    chartOptionsRadial: {
      chart: {
        height: 350,
        type: 'radialBar',
      },
      title: {
        text: 'Skillset Match Percentage by Job Title',
        align: 'center'
      },
      plotOptions: {
        radialBar: {
          dataLabels: {
            name: {
              fontSize: '22px',
            },
            value: {
              fontSize: '16px',
            },
            total: {
              show: true,
              label: 'Average Similarity Score',
            }
          }
        }
      },
      labels: []
    },
});

export async function predictSalary(jobdesc: string) {
  const resp = await salaryApi.value.predictSalaryPredictPost(jobdesc);
  const { data } = resp;
  state.expectedSalary = data;
}

export async function extractSkills(jobdesc: string) {
  const resp = await salaryApi.value.skillsSalarySkillsPost(jobdesc);
  const { data } = resp;
  state.extractedSkills = [
    {
      name: "Skill Breakdown",
      data: data
    }
  ]
}

export async function extractSkillSalaryBins(jobdesc: string) {
  const resp = await salaryApi.value.skillsalbinSalarySkillsalbinGet(jobdesc);
  const { data } = resp;
  state.skillBins = data;
}

export async function extractSkillSimilarity(jobdesc: any) {
  const resp = await salaryApi.value.skillsimSalarySkillsimGet(jobdesc);
  const { data } = resp;
  state.similarity.vals = data.score;
  console.log(data.title);
  state.chartOptionsRadial = {...this.chartOptionsRadial, ...{
    chart: {
      height: 350,
      type: 'radialBar',
    },
    title: {
      text: 'Skillset Match Percentage by Job Title',
      align: 'center'
    },
    plotOptions: {
      radialBar: {
        dataLabels: {
          name: {
            fontSize: '22px',
          },
          value: {
            fontSize: '16px',
          },
          total: {
            show: true,
            label: 'Average Similarity Score',
          }
        }
      }
    },
    labels: data.title
}}
}

export async function getSalaryStats() {
  const resp = await metricsApi.value.generalMetricsGet();
  const { data } = resp;
  state.avgSalary = data.average_salary
  state.stdSalary = data.std_salary
}

export function useUnitState() {
    return { 
        ...toRefs(state) ,
        predictSalary,
        extractSkills,
        getSalaryStats,
        extractSkillSalaryBins,
        extractSkillSimilarity
    };
  }


  
  
