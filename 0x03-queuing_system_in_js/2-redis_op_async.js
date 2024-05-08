import redis from 'redis';

const client = redis.createClient ();

client
  .on ('connect', () => {
    console.log ('Redis client connected to the server');
  })
  .on ('error', err => {
    console.log (`Redis client not connected to the server: ${err}`);
  });

/**
 * Sets a new school in Redis with the given school name and value.
 *
 * @param {string} schoolName - The name of the school.
 * @param {string} value - The value associated with the school.
 * @returns {void}
 */
function setNewSchool (schoolName, value) {
  client.set (schoolName, value, (err, reply) => {
    if (err) {
      console.error (err);
    } else {
      redis.print (`Reply: ${reply}`);
    }
  });
}

/**
 * Retrieves and displays the value of a school from Redis.
 * @param {string} schoolName - The name of the school to retrieve the value for.
 * @returns {Promise<void>} - A Promise that resolves once the value is displayed.
 */
async function displaySchoolValue (schoolName) {
  await client.get (schoolName, (err, value) => {
    if (err) {
      console.error (err);
    } else {
      if (value === null) {
        console.log ('School');
        return;
      }
      console.log (value);
    }
  });
}

displaySchoolValue ('Holberton');
setNewSchool ('HolbertonSanFrancisco', '100');
displaySchoolValue ('HolbertonSanFrancisco');

process.on ('exit', () => {
  client.quit ();
});
