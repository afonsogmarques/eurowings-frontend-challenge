<template>
  <div class="flex flex-column gap-sm w-100 container">
    <header class="header gap-sm">
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
        <select class="ellipsis" :disabled="isLoading">
          <option value="arrival">Arrival date</option>
          <option value="departure">Departure date</option>
          <option disabled selected hidden>Sort by</option>
          <option value="price">Price: cheapest first</option>
          <option value="airport">Departure airport: from A to Z</option>
        </select>
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
  import { useFlightsStore, useGeneralStore } from './stores';
  import { computed, ref, onBeforeMount } from 'vue';

  /** I know a store is overkill in this specific situation, but the
   * flights info is probably something that would make sense to keep in a store in a larger app
   * in order to share it across different components.
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

  /** Returns all flights matching the origin and destination filters. */
  const filteredFlights = computed(() => {
    /**
     * Filters an array of flights based on both origin and destination filters.
     * @param flight The flight in the current iteration
     * @returns { boolean }
     */
    const filterFlights = (flight) => {
      const matchesOrigin =
        !originFilter.value || flight.origin === originFilter.value;

      const matchesDestination =
        !destinationFilter.value ||
        flight.destination === destinationFilter.value;

      return matchesOrigin && matchesDestination;
    };

    return flights.value?.filter(filterFlights) || [];
  });
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
  }

  .filter-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
  }
</style>
