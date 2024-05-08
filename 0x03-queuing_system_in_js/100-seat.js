const express = require ('express');
const redis = require ('redis');
const kue = require ('kue');
const {promisify} = require ('util');

const app = express ();
const PORT = 1245;

const client = redis.createClient ();
const queue = kue.createQueue ();

const reserveSeat = async number => {
  const setAsync = promisify (client.set).bind (client);
  await setAsync ('available_seats', number.toString ());
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify (client.get).bind (client);
  const seats = await getAsync ('available_seats');
  return parseInt (seats) || 0;
};

let reservationEnabled = true;

// Initialize available seats to 50 when launching the application
reserveSeat (50);

app.use (express.json ());

app.get ('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats ();
  res.json ({numberOfAvailableSeats});
});

app.get ('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json ({status: 'Reservation are blocked'});
  }

  const job = queue.create ('reserve_seat').save (err => {
    if (err) {
      return res.json ({status: 'Reservation failed'});
    }
    res.json ({status: 'Reservation in process'});
  });
});

app.get ('/process', async (req, res) => {
  res.json ({status: 'Queue processing'});

  queue.process ('reserve_seat', async (job, done) => {
    try {
      let currentSeats = await getCurrentAvailableSeats ();
      if (currentSeats > 0) {
        await reserveSeat (currentSeats - 1);
        currentSeats--;

        if (currentSeats === 0) {
          reservationEnabled = false;
        }

        console.log (`Seat reservation job ${job.id} completed`);
        done ();
      } else {
        throw new Error ('Not enough seats available');
      }
    } catch (error) {
      console.error (`Seat reservation job ${job.id} failed: ${error.message}`);
      done (error);
    }
  });
});

app.listen (PORT, () => {
  console.log (`Server is running on port ${PORT}`);
});
