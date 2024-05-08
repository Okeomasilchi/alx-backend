import Kue from 'kue';

const que = Kue.createQueue ();

const sendNotification = (phoneNumber, message) => {
  console.log (
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

que.process ('push_notification_code', (job, done) => {
  const {phoneNumber, message} = job.data;
  sendNotification (phoneNumber, message);
  done ();
});

que.on ('error', err => {
  console.error ('Queue error:', err);
});
