# AWS Certification - What I know about S3 in AWS.

## Summary

I began these notes the day I took my AWS Certified Solutions Architect - Associate certification exam, which I pass, thank you very much. 
This topic, Storage, is really really REALLY important for the certification.
For the certification I believe that the most important topics are: S3, VPC (with all its goodies), EBS, RDS, SQS and EC2.
In this article I will try to remember all I know about S3.
It is important to you go an check out the post where I shared the lingo used in AWS, because I am not going to expand on those in here.

&nbsp;
### What is S3?

Simple Storage Service, as its name states it, helps you to store objects in the cloud. Per object the minimum size can be 0 byte, maximum size can be 5TB. Although the maximum size for a single PUT operation is 5GB. 
It is recommended to use multipart upload for files bigger than 100MB.
All Storage Classes in S3 have a Durability of __11 9s__.
All Storage Classes are replicated in at least 3 AZs, except S3-OneZoneAI.
All Storage Classes have first-byte latency of milliseconds, except Glacier classes.
Availability for the Standard S3 is __4 9s__.

&nbsp;
### What is Glacier?

You can think of Glacier as its own service, but also as an S3 Storage Class. The ideal use for Glacier, is to store objects that are used very rarely and that can wait hours to be retrieved.
The standard retrieval time for Glacier is 3-5 hours.
Availability is __4 9s__.

&nbsp;
### What is S3-IA?

S3 - Infrequent Access. You would want to use this type of storage when the object is used not so often.
The minimum storage duration charge is 30 days. This means that if you put an object and delete it after 2 days, you will still be charged for that object being stored there 30 days.
The minimum capacity charged per object is 128KB. This means that if you store a smaller object, you still get charge for an object of 128KB.
Availability is __3 9s__.

&nbsp;
### What is S3-OneZoneAI?

S3 - One Zone Infrequent Access. This is almost identical to S3-IA with the main difference that there is no multi-AZ replication.
The minimum storage duration and minimum capacity charges from S3-IA are applied.
Availability is __2.5 9s__.

&nbsp;
### What is S3-IntelligentTiering?

This is the Storage class that you would want to use in case that you don't know how frequently are you going to access an object. It will move the files to the most cost-effective access tier automatically.
Availability is __3 9s__.

&nbsp;
### What is Glacier Deep Archive?

This is the lowest-cost storage class. Ideal for long-term retention. For data that may be accessed 1-2 times per year. A common use for this class is to store data from highly regulated industries that need to retain data for 7 or more years.
Retrieval time can be within 12-48 hours.
Availability is __4 9s__.

&nbsp;
### Which are the retrieval options for Glacier?

Expedited. It retrieves your data within 1-5 minutes. For files smaller than 250MB.
Standard. Default option that will retrieve your data within 3-5 hours.
Bulk. This is the lowest-cost retrieval option. It takes within 5-12 hours.

&nbsp;
### What is S3 Select? Does Glacier has a Glacier Select?

&nbsp;
### What is a Bucket?

&nbsp;
### What is a Vault?

&nbsp;
### What is an Object?

&nbsp;
### What is an Archive?

&nbsp;
### How can you leverage CloudFront to improve S3 performance?

&nbsp;
### What is S3 Transfer Acceleration?

&nbsp;
### What are the types of Consistencies that you can have in S3?

&nbsp;
### Who can delete a bucket?

&nbsp;
### What is cross-region replication?

&nbsp;
### What is Versioning?

&nbsp;
### What is a Lifecyle Policy?

&nbsp;
### What is Multipart upload? And how does it help to use it?

&nbsp;
### How can you Encrypt data at-rest in S3?

&nbsp;
### Which options do you have for encryption in S3?

&nbsp;
### What is SSE?

This term refers to Server Side Encryption. It is widely use when talking about data at-rest encryption.

&nbsp;
### What is SSE-C?

Server-Side Encryption with Customer-provided encryption keys. It is a way of encrypting data in S3. This type of encryption allows the user to provide the encryption key as part of the request. Amazon doesn't store the key, meaning that if you lose the key, you lose the object. 

&nbsp;
### What is SS3-S3?

This options let's Amazon handles the key for you. Each object is encrypted with a unique key.

&nbsp;
### What is SSE-KMS?

Server-Side Encryption with Key Management Service (AWS KMS). S3 will use your CMKs (Customer Master Keys) from your AWS KMS to encrypt your objects. This is the most _robust_ of all the solutions. It helps you to keep a record on who has used which keys.

&nbsp;
### Should you move your static files to S3 to improve performance?

&nbsp;
### Can S3 be configured to have a VPC Endpoint? What would be the benefit?

&nbsp;
### Can S3 work with AWS Macie?

&nbsp;
### Can S3 work with Redshift?

&nbsp;
### Can S3 work with Lambda?

&nbsp;
### What is a Signed URL in S3?

&nbsp;
### What is a Presigned URL in S3?