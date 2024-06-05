import { reactive, toRefs } from 'vue';
import { useApi } from 'src/store/api';

const {
    salaryApi
  } = useApi();



const state = reactive({
    jobtitle: '',
    location: '',
    company:'',
    exp: '',
    companies: ['Capital One', 'MITRE', 'Booz Allen', 'SAIC'],
    experience: ['0-2', '2-5', '5-10', '10-20', '20+'],
});

export function useSummaryState() {
    return { 
        ...toRefs(state) 
    };
  }