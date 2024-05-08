import Kue from 'kue';

const que = Kue.createQueue ();

const jobData = {
  phoneNumber: '09123666419',
  message: 'welcome home',
};

const job = que.create ('push_notification_code', jobData).save ();

job
  .on ('enqueue', () => {
    console.log (`Notification job created: ${job.id}`);
  })
  .on ('complete', () => {
    console.log ('Notification job completed');
  })
  .on ('failed', () => {
    console.log ('Notification job failed');
  });

// Kue.app.listen (3000);
