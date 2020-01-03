# AWS Certification - What I know about Networking in AWS

## Summary

Hey guys! At the moment of writing this article I am still preparing for the AWS Certification Exam - Architect Associate.
This is the topic that I found myself struggling the most. Hopefully I can use this opportunity to improve my knowledge on the subject.
The content is just going to be a bunch of questions with their answers explaining what I know. Do not take this as example questions to practice.

&nbsp;
### What is a VPC?

Virtual Private Cloud. This is a logically isolated section of the Amazon Cloud. In your VPC you have complete control of this virtual network, and you can deploy as many resources as you want. Some of the things that you can do is: select your own IP range, create subnets, configure route tables & network gateways.

&nbsp;
### What are the features of a VPC?

Specify its private IP Addresses range from any range you want. Expand your VPC by adding secondary IP ranges. Divide your private IP Addresses range into one or more private/public subnets. Control inbound/outbound access to/from individual subnets using Network Access Control Lists. Connect VPC with other VPCs. Assign multiple Elastic Network Interfaces to instances in your VPC. Assign Elastic IPs to instances in your VPC so they can be reached  from the internet. Privately connect to your own services or SaaS solutions by AWS PrivateLink. Bridge your VPC and your on-site IT infrastructure with AWS Site-to-site VPN. Use VPC Flow Logs to log information about in/out traffic of network interfaces in your VPC. Enable IPv4 & IPv6. You have traffic mirroring.

&nbsp;
### What are some VPC restrictions/soft limits?

You can:
* have 0-5 VPCs per account, per region.
* have 0-4 secondary IP ranges per VPC.
* create 0-200 subnets per VPC.
* have 0-5 VPC Elastic IPs per account, per region.

&nbsp;
### What is an Elastic IP (EIP)?

A static IPv4 designed for dynamic cloud computing. A common use for this is, to mask the failure of an instance by rapidly re-mapping it to another instance or network interface.

&nbsp;
### How does an EIP work?

You allocate an EIP to your account, and then you assign it to an instance or a network interface.
When you associate an Elastic IP Address to a resource that has already a public IPv4 Address, that instance IP is released back into Amazon's pool of public IPv4 Addresses. You cannot re-use IPv4 Addresses and you cannot convert a Public IPv4 Address to an Elastic IP Address.
You can disassociate an EIP from a resource and associate it with a different resource, any open connections will continue to work. It is recommended to reopen those connections.
A disassociated EIP remains allocated to your account unless you explicitly release it.
Amazon has a small hourly charge for any EIP that is not associated to any running instance, or if it is associated to a stopped instance or an unattached network interface. When the instance is running there is no charge.
An Elastic IP is for use in a specific Region.
When you associate an EIP to an instance, the public DNS hostname of the instance changes to match the EIP.

&nbsp;
### What is VPC Peering?

This is the term used when you connect a VPC with another VPC via private IP Addresses. It is a feature of the VPCs. Instances in either VPC can communicate with each other as if they are within the same network. VPC Peering can be created between your own VPCs, other accounts VPCs, or with a VPC in another AWS Region.


&nbsp;
### Let's suppose that VPC A has VPC Peering enabled to VPC B and VPC C. Can VPC B communicate with VPC C?

No, if you want those two VPCs to be able to communicate, you need to enable VPC Peering in those VPCs.

&nbsp;
### What is an ENI?

Elastic Network Interface, a virtual network interface that can have: primary IPv4 Address, 1+ secondary private IPv4 Addresses, 1 Elastic IP per private IPv4 Address, 1 Public IPv4 Address (That can be auto-assigned to the eth0 interface when the instance is launched), 1+ IPv6 Addresses, 1+ Security Groups, MAC Address, source/destination check flag, description.
You can create a ENI and attach/detach it from an instance and re-attach it to other instance, the ENI will preserve its configuration and new traffic will be redirected to the new instance.
Each instances in the VPN has a default network interface (primary network interface) that is assigned an IPv4 Address. This primary network interface cannot be detached, you can only add other secondary network interfaces. The amount of secondary network interfaces depends on the instance type.

&nbsp;
### When is useful to have multiple ENIs attached?

* Create a management network
* Create a low-budget, high availability solution.
* Create dual-homed instances with workloads/roles on distict subnets.
* Use network and security appliances in your VPC.

&nbsp;
### What is a Route table?

This is a set of rules, called routes. These rules are used to determine where the network traffic is going to be directed from your subnet or gateway.
A subnet can be associated with only one route table. A route table can have multiple subnets associated.

&nbsp;
### What are the key concepts for Route tables?

* __Main route table__ - The route table that comes automatically when you create the VPC. It controls all the subnets that are not specifically associated with other route tables.
* __Custom route table__ - Route table that you create.
* __Route table association__ - Association between a route table and a subnet, internet gateway or virtual private gateway.
* __Subnet route table__ - Route table that is associated to a subnet.
* __Gateway route table__ - Route table associated to an Internet Gateway or Virtual Private Gateway.
* __Local gateway route table__ - Route table associated with an Outpost local gateway.
* __Destination__ - Destination CIDR where you want traffic to go, example: `172.16.0.0/12`
* __Target__ - Target through which send the destination traffic, example: internet gateway.
* __Local route__ - Default route to communicate within the VPN

&nbsp;
#### What is a CIDR?

Classless Inter-Domain Routing, an IP Addressing scheme that is used to create unique identifiers for networks and devices. It helps with the allocation of IP Addresses.
Example CIDR: `172.16.0.0/12`

&nbsp;
### What is a VPC Endpoint?

A VPC Endpoint allows you to privately connect your VPC to supported AWS Services and VPC endpoints provided by PrivateLink without requiring an Internet Gateway, VPN, DirectConnection or NAT Device. Traffic between the VPC and other AWS Services don't leave the Amazon network. Instances in your VPC don't require public IP to communicate with resources in the service.

VPC Endpoints are virtual devices. They are horizontally scaled, redundant and highly available VPC components that allow communication between your instances in your VPC and services without imposing availability risks or bandwidth constraints on your network traffic.

Allows the traffic to never leave the AWS network.

&nbsp;
### What is an interface VPC endpoint?

Is an elastic network interface with a private IP Address that serves as an entry point for the traffic destined to a supported service.
The services that support this are: API Gateway, AppStream 2.0, App Mesh, App Auto Scaling, Athena, Cloud Directory, CloudFormation, CloudTrail, CloudWatch, CodeBuild, CodeCommit, CodePipeline, Config, DataSync, EC2 API, EC2 AutoScaling, EFS, ELB, ECS, ECR, Glue, KMS, Kinesis Data Firehose/Streams, Rekognition, SageMaker, Secrets Manager, STS, SMS, SQS, SNS, Step Functions, Systems Manager, Storage Gateway, WorkSpaces, Services hosted by other AWS Accounts and AWS Marketplace partner services.
All powered by AWS PrivateLink.

This costs approximately `0.01$/hr`

&nbsp;
### What is a gateway VPC endpoint?

A Gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS Service.
S3 and DynamoDB are supported.
When creating it, you must specify the VPC in which you want to create the endpoint.

This is free.

&nbsp;
### What is a subnet?

&nbsp;
### What is a public subnet?

&nbsp;
### What is a private subnet?


&nbsp;
### What are some best practices about subnets and route tables?

&nbsp;
### What do Destination and Target mean in Route tables?

&nbsp;
### What is a NAT Gateway?

A NAT Gateway is an AWS managed service that allows instances within a private subnet to access the internet, but prevents the internet to connect those instances.
You need to launch these in each AZ.
They need to be in a public subnet.

&nbsp;
### What is a NAT Instance?

A NAT Instance is an EC2 Instance configured to behave as NAT. This is the legacy way of doing it.


&nbsp;
### Can a VPC use another VPC Nat Gateway? What if VPC Peering is enabled?

&nbsp;
### What is a NACL?

Network Access Control List, is like a virtual firewall at the subnet level.
You usually need to have 2 NACLs per action in and out.
A VPC comes with a default NACL. Subnets can only have one NACL associated with.
Contains a set of rules that can allow or deny traffic in/out subnets.
The rules have an order of evaluation, goes from lowest to highest. Highest rule can be 32766. It is recommended to have increments of 10-100 between rules orders (In case you want to add some rule in between in the future).
When creating a NACL it will block all traffic by default.
You can block a single IP Address with NACLs, Security Groups cannot do this.

&nbsp;
### What is the difference between NACLs and ACLs?

&nbsp;
### How does an ELB/CLB work?

&nbsp;
### How does an ALB work?

&nbsp;
### How does a NLB work?

&nbsp;
### How does an ELB is charged?

&nbsp;
### What are the differences between ALB vs CLB vs NLB?

&nbsp;
### What is the pass-though option in a ALB?

&nbsp;
### How can you make the connection secure between an ELB and a EC2 Instance?

&nbsp;
### How is a NAT Gateway charged?

&nbsp;
### What is Guard Duty?

&nbsp;
### What is an Internet Gateway?

&nbsp;
### What is an Internet Gateway - Egress-Only?

&nbsp;
### Tell me about NAT Gateways and VPC Peering

&nbsp;
### What is a Firewall Manager?

&nbsp;
### What is AWS WAF?

&nbsp;
### How does AWS WAF + CloudFront work?

&nbsp;
### What is Route53?

&nbsp;
### What are the configuration options that Route53 has?

&nbsp;
### What is a Sticky Session in an Load Balancer?

&nbsp;
### What is Cross-Zone Load Balancing?

&nbsp;
### How can you have encryption in a ELB?

&nbsp;
### What is an A Record?

&nbsp;
### What is an Alias Record?

&nbsp;
### What is a CNAME?

&nbsp;
### What is a Security Group?

This is like a virtual firewall at the instance level.
They are associated with EC2 Instances.
All inbound traffic is blocked by default.
All outbound traffic is allowed by default.
Security Groups can contain multiple EC2 Instances.
Multiple instances can belong to the same Security Group.
There is no __Deny__ rules in Security Groups.
Each Security Group contains a set of rules that filter traffic in/out instances.
Rules provide security at __Protocol__ and __Port__ access level.
You can specify as source an IP range, IP Address or Security Group.
An instance can belong to many Security Groups, and rules are permissive (not restrictive). If a rule allows something, that is denied by another, the deny doesn't take place.
They are __Stateful__, meaning if traffic is allowed inbound it is also allowed outbound)

You can have:
* 10,000 Security Groups per Region.
* 60 inbound rules.
* 60 outbound rules.
* 16 security groups per ENI.


&nbsp;
### How does Security Groups work with ENIs?

&nbsp;
### What is VPC Flow logs?

This enables you to capture all in/out traffic information of your network interfaces in your VPC.
Can be created for VPC, Subnets and Network interface.
The data is stored in S3 or CloudWatch Logs.
Cannot be tagged, cannot be edited, you can only delete it.
Logs the source and the destination ip addresses.


&nbsp;
### What is the _local_ route in a VPC?

&nbsp;
### What is AWS Shield?

&nbsp;
### What are some security the best practices?

&nbsp;
### What is an AWS PrivateLink?

&nbsp;
### What Services can be provided in Edge Locations?

&nbsp;
### What is DirectConnect?
