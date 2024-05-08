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
 * Sets a new school in Redis with the specified school name and value.
 * @param {string} schoolName - The name of the school.
 * @param {string} value - The value associated with the school.
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
 * Displays the value of a school in the Redis database.
 * @param {string} schoolName - The name of the school to retrieve the value for.
 */
function displaySchoolValue (schoolName) {
  client.get (schoolName, (err, value) => {
    if (err) {
      console.error ();
    } else {
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
