import requests, pprint, os

pp = pprint.PrettyPrinter(depth=4)
contract_addr = '0xf0F161fDA2712DB8b566946122a5af183995e2eD'

# Gets info from a specific address
def search(address: str):
    url = f'https://explorer.mode.network/api/v2/search?q={address}'
    r = requests.get(url)
    pp.pprint(r.json())

# Gets solidity and dumps source(s)
def fetch(address: str):
    url = f'https://explorer.mode.network/api/v2/smart-contracts/{address}'
    r = requests.get(url)
    sources = r.json()['additional_sources']
    
    for source in sources:
        print(f'''--- Path: {source["file_path"]} --- \n\n--- Content: ---\n{source["source_code"]}\n''')

# search(contract_addr)
fetch(contract_addr)
