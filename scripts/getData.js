const axios = require('axios');
const AWS = require('aws-sdk');
// Create an instance of the S3 service
const s3 = new AWS.S3();
axios.get('http://air4thai.pcd.go.th/services/getNewAQI_JSON.php')
  .then(response => {
    // Handle the response and process the data as required
    const data = response.data;
    // Convert the data to JSON string
    const jsonData = JSON.stringify(data);
    // Set the S3 bucket name and destination path
    const bucketName = 'air4thai-api';
    const destinationPath = 's3://air4thai-api/pm25-hourly-data/data.json';
    // Configure the parameters for the S3 upload
    const params = {
      Bucket: bucketName,
      Key: destinationPath,
      Body: jsonData,
    };
    // Upload the data to S3
    s3.upload(params, (err, data) => {
      if (err) {
        console.error('Error uploading data to S3:', err);
      } else {
        console.log('Data uploaded to S3 successfully:', data.Location);
      }
    });
  })
  .catch(error => {
    // Handle any errors that occur during the request
    console.error(error);
  });