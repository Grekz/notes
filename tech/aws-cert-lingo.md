# AWS Certification - Learning the lingo

## Introduction

Hi there, I have began to prepare myself to take the AWS Certification exam in less than a week now. While I was reading the material in preparation for the test I encountered a lot of terms and acronyms that make little sense to me. I have put together a list with all these, I hope it can help you to get familiar with the lingo used in the AWS Certification materials.
In the beginning is confusing to see some terms you are already familiar with or some acronyms that do not mean the same in AWS.
if you want to go to a place where there is more more info than this article, you can go to [AWS Glossary URL](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

&nbsp;
### Elastic

You would understand in our day and age that elastic means something that can grow and shrink. Something that can Scale up and down. Here if you see this in the name, do not assume it is Elastic.  

&nbsp;
### Scalable

Something that can scale up. You can grow the instances or the resources to handle a bigger load.

&nbsp;
### AWS vs Amazon

Amazon Web Services. A bunch of services that Amazon offers to make your life better.

&nbsp;
### S3 or Amazon S3

Amazon Simple Storage Service. This is an object storage service, it is really important to understand the tradeoffs on using one type over the other. You have the standard S3, Intelligent Tiering, Infrequent Access, One Availability Zone Infrequent Access, Glacier and Glacier Deep Archive. The Bucket is the place where you store your objects in S3. In Glacier the same place is called Vault.

&nbsp;
### EC2 or Amazon EC2

Elastic Compute Cloud. A Service that allows you to have some compute capacity in the cloud. Instances live in here. =)

&nbsp;
### Lambda or AWS Lambda

Serverless Service that allows you to run code without having an instance.

&nbsp;
### RDS or Amazon RDS

Amazon Relational Database Service. Amazon managed relational databases.

&nbsp;
### WAF or AWS WAF

Amazon Web Application Firewall. Application Firewall service to help you protect Web Applications or APIs.

&nbsp;
### CW or Amazon CloudWatch

Amazon CloudWatch. Allows you to have monitoring and observability capabilities in your AWS Services.

&nbsp;
### KMS or AWS KMS

AWS Key Management Service. This helps you manage your keys and makes it easy to use in other AWS Services.

&nbsp;
### DynamoDB or AWS DynamoDB

NoSQL Database provided by AWS. You can use global tables.

&nbsp;
### ACM or AWS Certificate Manager

AWS Certificate Manager. Makes a lot easier to provide and manage SSL/TLS Certificates.

&nbsp;
### IAM or AWS IAM

AWS Identity and Access Management. Allows you to manage access to AWS Services and resources securely.

&nbsp;
### Cognito

Amazon Cognito. Is a service that allows you to sign-up, sing-in and can help you with access control to your applications.

&nbsp;
### EFS or Amazon EFS

Amazon Elastic File Service. Managed by AWS, a Network File System.

&nbsp;
### AWS Region

A Geographic area that is composed of several Availability Zones.

&nbsp;
### AZ

Availability Zone. A logical block that can composed of several datacenters. An Isolated location.

&nbsp;
### EIP

Elastic IP Address. You can use this to allow access to your EC2 instance to the internet.

&nbsp;
### SLA

Service Level Agreement. A policy where you an Amazon have an agreement on how to use the service. Sometimes this is referred to the guaranteed features of their products, for instance [AWS S3 SLA.](https://aws.amazon.com/s3/sla/)

&nbsp;
### SPoF

Single Point of Failure. 

&nbsp;
### ELB or CLB

ELB - Elastic Load Balancer. 
CLB - Classic Load Balancer. I found that in the materials these two terms are interchangeable.

&nbsp;
### ALB

Application Load Balancer.

&nbsp;
### NLB

Network Load Balancer. Layer 4 load balancer.

&nbsp;
### VPC

Virtual Private Cloud. A logically isolated section of AWS Cloud, with scope of __region.__

&nbsp;
### 9s or nines

A measure used by amazon usually used in Availability and Reliability. 
For example:
   
* 11 9s (Eleven nines) means 99.999999999%.
* 5 9s (Five nines) means 99.999%.
* 2.5 9s (Two point five nines) means 99.5%

&nbsp;
### HA

High Availability. Refers to a system that is durable and pretty likely to operate continuously without failure for a long time.

&nbsp;
### FT

Fault Tolerance. The ability of a system to continue working even if a component has failed.

&nbsp;
### GSI

Global Secondary Indexes. Used in DynamoDB.

&nbsp;
### EBS

Elastic Block Storage. Block storage system used to persist data in EC2 instances.

&nbsp;
### SCP

Security Control Policy. A type of policy to manage your Organization.

&nbsp;
### ENI

Elastic Network Interface. A logical network component used in the VPC, represents a virtual network card.

&nbsp;
### ACL

Access Control List.

&nbsp;
### NACL

Network Access Control List.

&nbsp;
### gp2

General purpose SSD. A volume type in EBS.

&nbsp;
### io1

Provisioned IOPS SSD. A volume type in EBS.

&nbsp;
### st1

Storage Throughput Optimized HDD. A volume type in EBS.

&nbsp;
### sc1

Storage Cold HDD. A volume type in EBS.

&nbsp;
### IOPS

Inputs/Outputs Operations per Second.

&nbsp;
### PIOPS

Provisioned Inputs/Outputs Operations per Second.

&nbsp;
### IA

Infrequent Access.

&nbsp;
### TCO

Total cost of Ownership. Estimate that helps determine direct and indirect costs of a system.

&nbsp;
### STD

Standard. You can see this when they are referring to the standard option of something.

&nbsp;
### SSM or SSM Agent or AWS SSM

AWS Systems Manager Agent. Helps to configure, update and manage resources.

&nbsp;
### Spot Instances

A type of instance in EC2, that can be pretty cheap. You have to bid for this type of instance. Good to use when flexible start and end times.

&nbsp;
### On-Demand Instances.

A type of instance in EC2. Most common type of instance, where you get your instance in the moment you request it.

&nbsp;
### RI 

Reserved Instance. When you have a predictable usage of your application, you can reserve your instance in advance and get it cheaper if you pay in advance. You have 1 or 3 years terms.

&nbsp;
### DR

Disaster Recovery. A security measure to have a strategy for backup and restore.

&nbsp;
### SSE

Server Side Encryption.

&nbsp;
### IGW

Internet Gateway.

&nbsp;
### VGW

Virtual Private Gateway.

&nbsp;
### CGW

Customer Gateway.

&nbsp;
### EMR

Elastic Map Reduce.

&nbsp;
### STS or AWS STS

Storage Token Service.

&nbsp;
### ETL

Extract, Transform, Load.

&nbsp;
### SRE

Site Reliability Engineer.

&nbsp;
### NFS

Network File Storage.

&nbsp;
### DAX

DynamoDB Accelerator.

&nbsp;
### CNAME

Canonical Name. Used in Networking. Maps a domain name to another domain name.

&nbsp;
### A Record

Maps a domain name to the IP Address that hosts the domain. Used in Networking.

&nbsp;
### IP

Internet Protocol. Used in Networking.

&nbsp;
### Alias Record

Allows you to automatically resolve your domain name to one or more __A records__ at resolution time. Used in Networking.

&nbsp;
### Target Group

Routes the requests to one or more registered targets. Commonly used in CLBs.

&nbsp;
### Route Table

Used in Networking. A Set of rules that determine where the traffic is directed. Each subnet in your VPCs must be associated to a route table. One route table can be associated to many subnets.

&nbsp;
### NAT

Network Address Translation. Mainly used to translate the local addresses to public IP addresses.

&nbsp;
### NAT Gateway

AWS Managed NAT Service. Allows private instances to go to the Internet and sometimes it can be used as Bastion.


&nbsp;
### Bastion/Jumpbox

A host designed and configured with the special purpose of withstanding attacks.