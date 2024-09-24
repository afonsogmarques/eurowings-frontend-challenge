import { useGeneralStore } from "../stores";
import { sleep } from '../helpers';

class Http {
  /**
   * Generic implementation to fetch data in JSON format.
   * @param { string } url The endpoint to fetch the data from. 
   * @returns { Promise<any | Error> } A promise wrapping the response data or an Error object.
   */
  async get(url) {
    const { setIsLoading } = useGeneralStore();

    setIsLoading(true);
    await sleep(); // I'm sorry... you can just comment this out...

    return fetch(url)
      .then(this.handleJSON)
      .catch(({ message }) => console.error(message))
      .finally(() => setIsLoading(false));
  }

  /**
   * Handle the intermediate step of parsing a JSON response.
   * @param { Response } response 
   * @returns { Promise<Error | any>}
   */
  async handleJSON(response) {
    const { ok, statusText } = response;

    if (!ok) throw new Error(statusText);
    return response.json();
  }
}

export const http = new Http();
