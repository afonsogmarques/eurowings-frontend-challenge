import { ref } from 'vue';
import { http } from '../helpers';
import { config } from '../config';
import { defineStore } from 'pinia';

export const useFlightsStore = defineStore('flights', () => {
  /**
   * @typedef { Object } Flight Represents a flight result from getFlights().
   * @property { string } origin Departure city.
   * @property { string } destination Destination city.
   * @property { string } departureDate Departure date for the best offer (may not be the same as in request).
   * @property { string } returnDate Return date for the best offer (same duration as in request).
   * @property { number } seatAvailability Number of available seats.
   * @property { Object } price Price information.
   * @property { number } price.amount Price amount.
   * @property { string } price.currency Price currency.
   * @property { string } offerType Service name.
   * @property { string } uuid Transaction code.
   */

  /** @type { Flight[] } */
  const flights = ref([]);

  /** Fetches all avaialable flights. */
  const fetchFlights = async () =>
    (flights.value = await http.get(config.API_URL));

  return { flights, fetchFlights };
});
