import redis from 'redis';

const client = redis.createClient ();

client
  .on ('connect', () => {
    console.log ('Redis client connected to the server');
  })
  .on ('error', err => {
    console.log (`Redis client not connected to the server: ${err}`);
  });

const data = [
  ['Portland', '50'],
  ['Seattle', '80'],
  ['New York', '20'],
  ['Bogota', '20'],
  ['Cali', '40'],
  ['Paris', '2'],
];

/**
 * Creates a hash in Redis with the specified key, field, and value.
 *
 * @param {string} key - The key of the hash.
 * @param {string} field - The field of the hash.
 * @param {string} value - The value to be stored in the hash.
 * @returns {void}
 */
function createHash (key, field, value) {
  client.hset (key, field, value, (err, reply) => {
    if (err) {
      console.error (err);
    } else {
      redis.print (`Reply: ${reply}`);
    }
  });
}

data.map (value => {
  createHash ('HolbertonSchools', value[0], value[1]);
});

client.hgetall ('HolbertonSchools', function (err, obj) {
  console.dir (obj);
});

process.on ('exit', () => {
  client.quit ();
});
