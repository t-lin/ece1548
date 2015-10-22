#!/usr/bin/env python

# vim: tabstop=4 shiftwidth=4 softtabstop=4 expandtab

'''
config.py
===============

This configuration file defines the user parameters and some defualt VM parameters
for cases where they were left out
'''


username=
password=
auth_url='http://iam.savitestbed.ca:5000/v2.0/'

# Prefix, prepend to instance names
instance_prefix=

# Key-pair name
key_name=

# Private key file path (needed to auto-SSH into the VMs)
# Example private key file path: '/home/savitb/user1/.ssh/id_rsa'
private_key_file='/home/savitb/' + username + '/.ssh/id_rsa'

# Default parameters for Nodes if region wasn't specified in the topology2.py file
region_name=
tenant_name=

# Default instances properties
image_name="ECE1548.OFLab"
flavor_name="m1.small"
sec_group_name=
vm_user_name="ubuntu"

