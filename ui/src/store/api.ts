import { reactive, toRefs } from "vue";
import {
  Configuration,
  NineLineApi
} from 'src/generated/';

  
const state = reactive({
  ninelineApi: new NineLineApi(),
  isAdmin: false
});

export function useNinelineApi() {
  state.ninelineApi = new NineLineApi();
  return {
    ...toRefs(state)
  };
}


export function useApi() {
  const token = localStorage.getItem('token') || '';
  const apiConf = new Configuration({ basePath: '/api', accessToken: token });
  state.ninelineApi = new NineLineApi(apiConf);

  return {
    ...toRefs(state),
  };
}



  