#! /usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect
t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other lab onusing id_rsa private / public keypairs)
t.connect(username="bender", password="alta3")

## make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)


