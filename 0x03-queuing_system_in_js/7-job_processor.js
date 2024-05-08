import Kue from 'kue';

const blackList = ['4153518780', '4153518781'];

/**
 * Sends a notification to a phone number with a given message.
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to include in the notification.
 * @param {object} job - The job object representing the notification job.
 * @param {function} done - The callback function to be called when the job is done.
 */
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress (0, 100);

  if (blackList.includes (phoneNumber)) {
    const error = new Error (`Phone number ${phoneNumber} is blacklisted`);
    job.failed ().error (error);
    console.error (`Notification job ${job.id} failed: ${error.message}`);
  } else {
    job.progress (50, 100);
    console.log (
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    setTimeout (() => {
      job.progress (100, 100);
      job.complete ();
      console.log (`Notification job ${job.id} completed`);
      done ();
    }, 1000);
  }
};

const queue = Kue.createQueue ({concurrency: 2});

queue.process ('push_notification_code_2', 2, (job, done) => {
  const {phoneNumber, message} = job.data;

  sendNotification (phoneNumber, message, job, done);
});
