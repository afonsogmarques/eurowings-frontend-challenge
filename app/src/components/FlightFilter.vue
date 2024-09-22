<template>
  <select v-model="filter">
    <option
      selected
      :value="null"
    >
      {{ selectLabel }}
    </option>
    <option
      v-for="entry in uniqueEntries"
      :value="entry"
    >
      {{ entry }}
    </option>
  </select>
</template>

<script setup>
  import { computed, ref } from 'vue';

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

<style scoped>
  select {
    flex: 1;

    padding: 5px;
    height: 40px;
    max-width: 200px;

    border: 0.1px solid rgb(194, 194, 194);
    border-radius: 30px;
    cursor: pointer;

    font-size: 14px;
    box-shadow: var(--drop-shadow);
  }

  @media (max-width: 415px) {
    select {
      max-width: 100px;
    }
  }
</style>
