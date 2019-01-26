python gen_crts.py

export ORG1=crypto-config/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
cp -p $ORG1/signcerts/A*.pem composer/org1
cp -p $ORG1/keystore/*_sk composer/org1

export ORG2=crypto-config/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
cp -p $ORG2/signcerts/A*.pem composer/org2
cp -p $ORG2/keystore/*_sk composer/org2

composer card create -p composer/org1/byfn-network-org1.json -u PeerAdmin -c composer/org1/Admin@org1.example.com-cert.pem -k composer/org1/*_sk -r PeerAdmin -r ChannelAdmin -f PeerAdmin@byfn-network-org1.card
composer card create -p composer/org2/byfn-network-org2.json -u PeerAdmin -c composer/org2/Admin@org2.example.com-cert.pem -k composer/org2/*_sk -r PeerAdmin -r ChannelAdmin -f PeerAdmin@byfn-network-org2.card

composer card import -f PeerAdmin@byfn-network-org1.card --card PeerAdmin@byfn-network-org1
composer card import -f PeerAdmin@byfn-network-org2.card --card PeerAdmin@byfn-network-org2
