import { defineStore } from "pinia";
import { ref } from "vue";

export const useGeneralStore = defineStore('general', () => {
  const isLoading = ref(false);
  const setIsLoading = (status) => isLoading.value = status;

  return { isLoading, setIsLoading };
});
