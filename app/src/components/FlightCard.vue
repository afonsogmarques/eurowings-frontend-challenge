<template>
  <div class="card flex content-between">
    <div>
      <div class="flex gap-sm">
        <span class="bold">{{ flight.origin }}</span
        ><span>➡️</span><span class="bold">{{ flight.destination }}</span>
      </div>
      <p>🛫 {{ flight.departureDate }}</p>
      <p>🛬 {{ flight.returnDate }}</p>
    </div>
    <p class="bold">€{{ flight.price.amount }}</p>
  </div>
</template>

<script setup>
  const props = defineProps({
    flight: {
      type: Object,
      required: true,
    },
  });
</script>

<style scoped>
  .card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: var(--drop-shadow);
    width: 100%;
  }
</style>
