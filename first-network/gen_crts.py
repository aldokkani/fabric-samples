with open('crypto-config/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt', 'r') as f:
    ORG1_CRT = f.read().replace('\r', '').replace('\n', '\\n')

with open('crypto-config/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt', 'r') as f:
    ORG2_CRT = f.read().replace('\r', '').replace('\n', '\\n')

with open('crypto-config/ordererOrganizations/example.com/orderers/orderer.example.com/tls/ca.crt', 'r') as f:
    ORDERER_CRT = f.read().replace('\r', '').replace('\n', '\\n')


def content_replace(content):
    return content.replace('INSERT_ORG1_CA_CERT', ORG1_CRT).replace('INSERT_ORG2_CA_CERT', ORG2_CRT).replace('INSERT_ORDERER_CA_CERT', ORDERER_CRT)

with open('composer/byfn-network.json', 'r+') as f:
    content = content_replace(f.read()) 
    f.seek(0)
    f.write(content)

with open('composer/org1/byfn-network-org1.json', 'r+') as f:
    content = content_replace(f.read()) 
    f.seek(0)
    f.write(content)

with open('composer/org2/byfn-network-org2.json', 'r+') as f:
    content = content_replace(f.read()) 
    f.seek(0)
    f.write(content)
