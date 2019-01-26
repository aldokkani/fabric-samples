[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Bock-Drive is a sample filesharing platform based on Private Blockchain (Hyperledger)


## Prerequisites
- Docker
- Docker Compose
- Python 3.5 or higher
- Node.js

Reference: [https://hyperledger-fabric.readthedocs.io/en/latest/prereqs.html](https://hyperledger-fabric.readthedocs.io/en/latest/prereqs.html)

## Installation
1. `git clone git@github.com:aldokkani/fabric-samples.git && cd fabric-samples`

2. Download the platform binaries:  
`curl -sSL http://bit.ly/2ysbOFE | bash -s 1.2.1 1.2.1 0.4.10`

3. `cd first-network`

4. Generate Fabric network / security artifacts / Docker containers and all required resources by running:  
`./setup_env.sh`  
verify that you see the following output before proceeding:
```bash
========= All GOOD, BYFN execution completed ===========


_____   _   _   ____
| ____| | \ | | |  _ \
|  _|   |  \| | | | | |
| |___  | |\  | | |_| |
|_____| |_| \_| |____/
```
5. Then run `./step_wallet.sh`

6. And finally `./network_init.sh`


## Usage
After finishing the installtion you are now provided with 2 admin cards, one admin for each orginization of the total two orginizations who are running the network.  
1- `org1admin@blockdrive`  
2- `org2admin@blockdrive`  
If you don't provide the `--card` argument in the commands, `org1admin@blockdrive` is used by default.  

The python script `network.py` provides a simple interface to interact with the network. Run `python network.py -h` for help.

### Commands examples:
- `python network.py --ping -c <admin card>` Check network health
- `python network.py --trans -f <file path> -c <admin card>` Uploads the given file to the network.
- `python network.py --list -c <admin card>` List all the files on the network.
- `python network.py --retrieve -i '<File's ID>' -c <admin card>` Donwloads a file inside `downloads/` dir.

## License <a name="license"></a>

Hyperledger Project source code files are made available under the Apache
License, Version 2.0 (Apache-2.0), located in the [LICENSE](LICENSE) file.
Hyperledger Project documentation files are made available under the Creative
Commons Attribution 4.0 International License (CC-BY-4.0), available at http://creativecommons.org/licenses/by/4.0/.
