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

This is the term used when you connect a VPC with another VPC via private IP Addresses. It is a feature of the VPCs.

&nbsp;
### What is a VPC Endpoint?

&nbsp;
### What is a subnet?

&nbsp;
### What is a public subnet?

&nbsp;
### What is a private subnet?

&nbsp;
### What is a Route table?

&nbsp;
### What do Destination and Target mean in Route tables?

&nbsp;
### What is a NAT Gateway?

&nbsp;
### What is a NAT Instance?

&nbsp;
### What is a NACL?

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

### How does AWS WAF + CloudFront work?

### What is Route53?

### What are the configuration options that Route53 has?

### What is a Sticky Session in an Load Balancer?

### What is Cross-Zone Load Balancing?

### How can you have encryption in a ELB?

### What is an A Record?

### What is an Alias Record?

### What is a CNAME?

### What is an ENI?

### What is a Security Group?

### How does Security Groups work with ENIs?

### What are the VPC Flow logs?

### What is the _local_ route in a VPC?

### What is AWS Shield?

### What are some security the best practices?

### What is a PrivateLink?

### What Services can be provided in Edge Locations?

### What is DirectConnect?
