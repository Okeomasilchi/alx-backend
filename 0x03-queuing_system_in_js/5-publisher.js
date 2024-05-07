import redis from 'redis';

// Create a Redis publisher client
const publisher = redis.createClient();

// Log when connected to Redis server
publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Log error if connection to Redis server fails
publisher.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message after a specified time
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('holberton school channel', message);
    }, time);
}

// Call the publishMessage function with different messages and times
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300); // This will terminate the subscriber
publishMessage("Holberton Student #3 starts course", 400);
