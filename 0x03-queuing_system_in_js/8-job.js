/**
 * Creates push notification jobs and adds them to the queue.
 * @param {Array} jobs - An array of job data.
 * @param {Queue} queue - The queue to add the jobs to.
 * @throws {Error} If jobs is not an array.
 */
function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray (jobs)) throw new Error ('Jobs is not an array');

  jobs.forEach (jobData => {
    const job = queue.create ('push_notification_code_3', jobData).save ();
    job
      .on ('enqueue', () => {
        console.log (`Notification job created: ${job.id}`);
      })
      .on ('complete', () => {
        console.log (`Notification job ${job.id} completed`);
      })
      .on ('failed', err => {
        console.log (`Notification job  ${job.id} failed: ${err}`);
      })
      .on ('progress', (progress, data) => {
        console.log (`Notification job ${job.id} ${progress}% complete`);
      });
  });
}

export default createPushNotificationsJobs;
