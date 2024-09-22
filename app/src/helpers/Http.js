class Http {
  async get(url) {
    return fetch(url)
      .then(this.handleJSON)
      .catch(({ message }) => console.error(message));
  }

  async handleJSON(response) {
    const { ok, statusText } = response;

    if (!ok) throw new Error(statusText);
    return response.json();
  }
}

export const http = new Http();
