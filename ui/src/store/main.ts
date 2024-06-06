import { useApi } from './api';
import { reactive, toRefs } from 'vue';

const { ninelineApi } = useApi();

const state = reactive({
  chatText: '',
  radioText: '',
  allNineLines: [] as any,
  activeNineLine: undefined,
  activeCOA: undefined,
  loadingStatus: false,
  coaDialog: false,
  rows: [],
  coas: [],
  chatResponse: '',
});

export async function getCOATable(coa) {
  state.activeCOA = coa
  state.rows = []
  state.coaDialog = true;

  const vals = Object.values(state.activeCOA.node1);
  const keys = Object.keys(state.activeCOA.node1);

  for (let index = 0; index < keys.length; index++) {
    const temp = {}
    temp["key"] = keys[index];
    temp["value"] = vals[index];
    state.rows.push(temp);
  }
}

export async function getNineLines() {
  state.loadingStatus = true;
  const resp = await ninelineApi.value.getNinelineGet();
  const { data } = resp;
  console.log(data);
  state.allNineLines = data;
  state.loadingStatus = false;
}

export async function getChatBotAnswer() {
  state.loadingStatus = true;
  state.chatResponse = 'response placeholder';
  state.loadingStatus = false;
}

export async function getNineLine(id: string) {
  state.loadingStatus = true;
  console.log(id);
  const resp = await ninelineApi.value.getNinelineGet(id);
  const { data } = resp;
  console.log(data);
  state.allNineLines = data;
  state.loadingStatus = false;
}

export async function getCOAS(id: string, chatText: string, radioText: string) {
  state.loadingStatus = true;
  setTimeout(() => {
    state.coas= [
      {
        "km": 200.12,
        "score": 1223.12,
        "node1": {
          "n_beds": 23,
          "n_masks": 12,
          "name": "Hospital",
          "surgeons": "true",
          "masks": "true",
        }
      },
      {
        "km": 80.12,
        "score": 110203.12,
        "node1": {
          "n_beds": 23,
          "n_masks": 12,
          "name": "Hospital",
          "surgeons": "true",
          "masks": "true",
        }
      },
      {
        "km": 100.12,
        "score": 12203.12,
        "node1": {
          "n_beds": 23,
          "n_masks": 12,
          "name": "Hospital",
          "surgeons": "true",
          "masks": "true",
        }
      }
    ]
  }, 1000);
  state.loadingStatus = false;
}

export function useState() {
  return {
    ...toRefs(state),
    getNineLine,
    getNineLines,
    getCOAS,
    getChatBotAnswer,
    getCOATable
  };
}
