<template>
  <select class="ellipsis" :disabled="isLoading" v-model="sortValue">
    <option :value="undefined" :disabled="!sortValue" :hidden="!sortValue">
      {{ sortLabel }}
    </option>
    <option value="returnDate">Return date</option>
    <option value="departureDate">Departure date</option>
    <option value="amount">Price: cheapest first</option>
    <option value="origin">Departure airport: from A to Z</option>
  </select>
</template>

<script setup>
  import { ref, computed } from 'vue';
  import { storeToRefs } from 'pinia';
  import { useGeneralStore } from '../stores';

  const generalStore = useGeneralStore();
  const { isLoading } = storeToRefs(generalStore);

  const sortValue = ref(undefined);
  const sortLabel = computed(() =>
    sortValue.value ? 'Reset sort' : 'Sort by'
  );
</script>
