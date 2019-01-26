composer network install --card PeerAdmin@byfn-network-org1 --archiveFile block-drive.bna
composer network install --card PeerAdmin@byfn-network-org2 --archiveFile block-drive.bna

composer identity request -c PeerAdmin@byfn-network-org1 -u admin -s adminpw -d org1admin
composer identity request -c PeerAdmin@byfn-network-org2 -u admin -s adminpw -d org2admin

composer network start -c PeerAdmin@byfn-network-org1 -n block-drive -V 0.0.9-deploy.0 -o endorsementPolicyFile=composer/endorsement-policy.json -A org1admin -C org1admin/admin-pub.pem -A org2admin -C org2admin/admin-pub.pem

composer card create -p composer/org1/byfn-network-org1.json -u org1admin -n block-drive -c org1admin/admin-pub.pem -k org1admin/admin-priv.pem
composer card import -f org1admin@block-drive.card

composer card create -p composer/org2/byfn-network-org2.json -u org2admin -n block-drive -c org2admin/admin-pub.pem -k org2admin/admin-priv.pem
composer card import -f org2admin@block-drive.card
