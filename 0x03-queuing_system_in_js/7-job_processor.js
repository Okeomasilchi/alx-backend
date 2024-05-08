import Kue from 'kue';

const blackList = ['4153518780', '4153518781'];

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
