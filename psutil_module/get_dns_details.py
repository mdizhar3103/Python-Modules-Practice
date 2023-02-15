import dns.resolver

# pip install dnspython

data = dns.resolver.resolve("amazon.com", 'MX')

for rawdata in data:
    print(rawdata)

print(data.qname)
print('---------')
print(data.response)
print('---------')
print(data.rrset)
print('---------')
print(data.canonical_name)
print('---------')
