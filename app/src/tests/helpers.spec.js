import { config } from '../config';
import { expect, test } from 'vitest';

/** Wish I could document this but I really don't know what I'm doing here */
test('successfully fetches flights', async () => {
  const req = await fetch(config.API_URL);

  expect(req.headers.get('content-type'))
    .toBe('application/json');

  expect(req.status).toBe(200);
});
