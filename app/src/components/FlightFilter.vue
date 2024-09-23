<template>
  <select v-model="filter" class="ellipsis" :disabled="isLoading">
    <option selected :value="null" :hidden="!filter">
      {{ selectLabel }}
    </option>
    <option v-for="entry in uniqueEntries" :value="entry">
      {{ entry }}
    </option>
  </select>
</template>

<script setup>
  import { computed, ref } from 'vue';
  import { useGeneralStore } from '../stores';
  import { storeToRefs } from 'pinia';

  const generalStore = useGeneralStore();
  const { isLoading } = storeToRefs(generalStore);

  const filter = ref(null);

  const props = defineProps({
    label: {
      type: String,
      required: false,
      default: 'Please select',
    },
    mapKey: {
      type: String,
      required: true,
    },
    flights: {
      type: Array,
      reuqired: false,
      default: [],
    },
  });

  /** Returns an array of unique entries. */
  const uniqueEntries = computed(() => {
    const allEntries = props.flights.map((flight) => flight[props.mapKey]);
    const uniqueEntries = new Set(allEntries);
    return [...uniqueEntries];
  });

  /** Label to be displayed in the filter select */
  const selectLabel = computed(() => {
    const defaultLabel = `All ${props.label.toLowerCase()}s`;
    return filter.value ? defaultLabel : props.label;
  });
</script>
