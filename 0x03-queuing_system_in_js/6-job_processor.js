import Kue from 'kue';

const que = Kue.createQueue ();

/**
 * Sends a notification to the specified phone number.
 *
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to include in the notification.
 * @returns {void}
 */
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
