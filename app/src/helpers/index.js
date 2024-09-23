/**
 * Can be used to pause execution for the specified amount of seconds.
 * @param { number } seconds The amount of time to halt execution for.
 * @returns { Promise<undefined> }
 */
export async function sleep(seconds = 1) {
  return new Promise((resolve) =>
    setTimeout(resolve, seconds * 1000));
}
