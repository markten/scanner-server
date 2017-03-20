# scanner-server

## Background

Some business class HP printers can only store scans internally or send them as an email to an SMTP server. Most people don't have an SMTP server on their home network, so this script acts as a stand-in.

## Dependencies

Just Python 3. All imports are in the core libs.

## Setup

The server listens on the specified port and address. It will strip attachments from the email MIME format that are an allowable type and dump them in a folder. In this case the folder is a samba share that everyone on the network can access. The script has to be run with proper permissions to have access to the network.

This was written for use on a small private network, so don't expect it to be secure.

