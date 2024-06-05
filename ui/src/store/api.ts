import { reactive, toRef, toRefs } from 'vue';
import {
  Configuration,
  SalaryApi,
  MetricsApi
} from 'src/generated/salary';

  
const state = reactive({
  salaryApi: new SalaryApi(),
  metricsApi: new MetricsApi(),
  isAdmin: false
});

export function useSalaryApi() {
  state.salaryApi = new SalaryApi();
  return {
    ...toRefs(state)
  };
}

export function useMetricsApi() {
  state.metricsApi = new MetricsApi();
  return {
    ...toRefs(state)
  };
}


export function useApi() {
  const token = localStorage.getItem('token') || '';
  const apiConf = new Configuration({ basePath: '/api', accessToken: token });
  state.salaryApi = new SalaryApi(apiConf);
  state.metricsApi = new MetricsApi(apiConf);

  return {
    ...toRefs(state),
  };
}



  