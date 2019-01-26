#!/bin/bash

## Clean previous environments

# Clean Wallet
rm -fr $HOME/.composer

# Clean dockers
echo 'Y' | ./byfn.sh down
docker rm -f $(docker ps -aq)

## Start docker containers and services
echo 'Y' | ./byfn.sh -m generate

echo 'Y' | ./byfn.sh -m up -s couchdb -a
