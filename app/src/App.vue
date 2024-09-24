<template>
  <div class="flex flex-column gap-sm w-100 container">
    <header class="header">
      <img
        src="./assets/eurowings-logo.svg"
        alt="Eurowings logo"
        class="logo"
      />
      <div class="flex flex-1 gap-sm items-center filter-container">
        <FlightFilter
          :flights
          label="Origin"
          v-model="originFilter"
          mapKey="origin"
        />
        <FlightFilter
          :flights
          label="Destination"
          v-model="destinationFilter"
          mapKey="destination"
        />
        <FlightSort v-model="sortValue" />
      </div>
    </header>
    <div
      class="flex flex-column gap-sm flex-1 items-center"
      :class="resultsWrapperClasses"
    >
      <LoadingSpinner v-if="isLoading" />
      <FlightCard
        v-else-if="filteredFlights?.length"
        v-for="flight in filteredFlights"
        :flight
      />
      <p v-else class="text-center">
        No flights found matching your criteria 🥲
      </p>
    </div>
  </div>
</template>

<script setup>
  import FlightCard from './components/FlightCard.vue';
  import FlightFilter from './components/FlightFilter.vue';
  import LoadingSpinner from './components/ui/LoadingSpinner.vue';

  import { storeToRefs } from 'pinia';
  import { computed, ref, onBeforeMount } from 'vue';
  import { useFlightsStore, useGeneralStore } from './stores';
  import FlightSort from './components/FlightSort.vue';

  /** I know a store is overkill in this specific situation, but the
   * flights info is probably something that would make sense to keep in a
   * store in a larger app in order to share it across different components.
   */
  const flightsStore = useFlightsStore();
  const { fetchFlights } = flightsStore;
  const { flights } = storeToRefs(flightsStore);

  const generalStore = useGeneralStore();
  const { isLoading } = storeToRefs(generalStore);

  const originFilter = ref(null);
  const destinationFilter = ref(null);

  onBeforeMount(fetchFlights);

  const resultsWrapperClasses = computed(() => ({
    'content-center': isLoading.value || !filteredFlights.value.length,
  }));

  const sortValue = ref(undefined);

  /** Returns all flights matching the origin and destination filters. */
  const filteredFlights = computed(() => {
    if (!flights.value) return [];

    const filteredFlights = flights.value.filter(filterFlights);
    const sortFn = sortFlights(sortValue.value);

    return filteredFlights.sort(sortFn);
  });

  /**
   * Filters flights based on currently active origin and destination filters.
   * To be used as an Array.prototype.filter() callback.
   * @param { Object } flight - The flight object to check.
   * @return { boolean } - True if the flight matches the active filters, otherwise false.
   */
  function filterFlights(flight) {
    const matchesDestination =
      !destinationFilter.value ||
      flight.destination === destinationFilter.value;

    const matchesOrigin =
      !originFilter.value || flight.origin === originFilter.value;

    return matchesOrigin && matchesDestination;
  }

  /**
   * Implements a custom sort using currying. I'm aware this doesn't
   * account for sort order and could be improved towards such a solution.
   * @param { string | number } sortValue The value to access on a flight Object.
   * @returns { Object[] }
   */
  function sortFlights(sortValue) {
    return function (a, b) {
      const isValid = sortValue && typeof sortValue === 'string';

      // Keeps sort order the same.
      if (!isValid) return 0;

      const isDate =
        sortValue === 'returnDate' || sortValue === 'departureDate';
      const isAmount = sortValue === 'amount';

      // Handles the "price" corner case.
      if (isAmount) return +a.price[sortValue] - +b.price[sortValue];

      // Handles the "dates" corner case.
      if (isDate) return Date.parse(a[sortValue]) - Date.parse(b[sortValue]);

      const isNumber = Number.isFinite(a[sortValue]);

      return isNumber
        ? a[sortValue] - b[sortValue]
        : a[sortValue].localeCompare(b[sortValue]);
    };
  }
</script>

<style scoped>
  .container {
    max-width: 1000px;
    flex: 1;
  }

  .logo {
    align-self: flex-start;
  }

  .header {
    display: flex;
    justify-content: space-between;

    position: sticky;
    top: 0;
    padding: 2rem 0;

    flex-wrap: wrap;
    gap: 20px;
  }

  .filter-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;

    margin-left: auto;
    max-width: 500px;
  }
</style>
