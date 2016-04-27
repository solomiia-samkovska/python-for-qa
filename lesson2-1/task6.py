tuple_test = ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
properties = ('dialect', 'host', 'port', 'database name', 'user name', 'password')

prod_config = dict(zip(properties, tuple_test))
staging_config = prod_config.copy()
staging_config['host'] = 'semantic.amazonaws-staging.com'
staging_config['password'] = 'root'

print(prod_config)
print(staging_config)

print 'Connection string for prod_config'
print "{0[dialect]}://{0[user name]}:{0[password]}@{0[host]}:{0[port]}/{0[database name]}".format(prod_config)

print 'Connection string for staging_config'
print "{0[dialect]}://{0[user name]}:{0[password]}@{0[host]}:{0[port]}/{0[database name]}".format(staging_config)