Freefill.com - https://freefill.com

The files in this repository consitute the Freefill.com application running in AWS. This application consists of:

• A Lambda function written in Python managed by the Serverless Framework: https://serverless.com

• An API fronting this Lambda function, exposing it to the public

The Lambda function simply and randomly displays one of two HTML pages stored in S3 based on the epoch time. An API built using API Gateway allows GET requests using a Lambda integration.

All AWS resources are created using CloudFormation templates - see freefill.yml. A second template, IAM.yml, demonstrates how to create IAM users and groups -- but was not used to actually create them.

Note that while Route53 is not currently used for DNS resolution, a simple extension of the template would allow for this.
