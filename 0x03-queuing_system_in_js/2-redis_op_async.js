import redis from 'redis';

const client = redis.createClient ();

client
  .on ('connect', () => {
    console.log ('Redis client connected to the server');
  })
  .on ('error', err => {
    console.log (`Redis client not connected to the server: ${err}`);
  });

function setNewSchool (schoolName, value) {
  client.set (schoolName, value, (err, reply) => {
    if (err) {
      console.error (err);
    } else {
      redis.print (`Reply: ${reply}`);
    }
  });
}

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
