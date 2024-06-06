import { useApi } from "./api";
import { reactive, toRefs } from 'vue';

const {
    ninelineApi
  } = useApi();

const state = reactive({
    prompt: '',
    allNineLines: [] as any,
    activeNineLine: undefined,
    loading: false,
    coas: [],
});

export async function getNineLines() {
    state.loading = true;
    const resp = await ninelineApi.value.getNinelineGet()
    const { data } = resp;
    console.log(data);
    state.allNineLines = data;
    state.loading = false;
  }

export async function getNineLine(id: string) {
    state.loading = true;
    console.log(id);
    const resp = await ninelineApi.value.getNinelineGet(id)
    const { data } = resp;
    console.log(data);
    state.allNineLines = data;
    state.loading = false;
  }

export async function getCOAS(id: string) {
    state.loading = true;
    const resp = await ninelineApi.value.createNinelineCreatePost
    const { data } = resp;
    console.log(data);
    state.coas = data;
    state.loading = false;
  }

export function useState() {
    return { 
        ...toRefs(state),
        getNineLine,
        getNineLines,
        getCOAS
    };
  }