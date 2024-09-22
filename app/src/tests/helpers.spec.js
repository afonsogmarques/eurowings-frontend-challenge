import { expect, test } from 'vitest';
import { http } from '../helpers';
import { config } from '../config';

test('successfully fetches flights', async () => {
  const res = await http.get(config.API_URL);
  expect(res).toBeInstanceOf(Array);
});
