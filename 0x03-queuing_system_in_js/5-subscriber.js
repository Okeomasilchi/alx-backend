import redis from 'redis';

// Create a Redis subscriber client
const subscriber = redis.createClient();

// Subscribe to the 'holberton school channel'
subscriber.on('subscribe', (channel) => {
    console.log(`Subscribed to channel: ${channel}`);
});

// Log when connected to Redis server
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Log error if connection to Redis server fails
subscriber.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Handle messages received on the subscribed channel
subscriber.on('message', (channel, message) => {
    console.log(`Received message on channel ${channel}: ${message}`);

    // Check for 'KILL_SERVER' message to unsubscribe and quit
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});

// Subscribe to the 'holberton school channel'
subscriber.subscribe('holberton school channel');
