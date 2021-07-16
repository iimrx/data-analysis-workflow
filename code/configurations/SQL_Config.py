#cloud sql instance configurations(PostgreSQL)
config1 = {
	'user' : 'upiflosvvqddnw', #username as in your postgresql setup
	'password' : '516b8a08f07f33ad589e28756585c3b7f7b4dd61d65918c24eb74d757fae7f16', #username password created on setup
	'host' : 'ec2-52-45-183-77.compute-1.amazonaws.com', #host ip or domain path
	'database' : 'dd043elu66sgq0', #database name
	'port' : 5432 #port used by the postgresql(5432 or 5433)
}
#cloud sql instance configurations(MSSQL)
config2 = {
	'server' : '34.87.176.34', #server or domain path
	'user' : 'sqlserver', #username as in your mssql setup
	'password' : '$%)_zPinNO++', #password created on setup
	'database' : 'testdb', #database name
}
#cloud sql instance confidurations(MYSQL)
config3 = {
    'user': '#', #username as in your mysql setup
    'password': '#', #username password created on setup
    'host': '#', #host ip or domain path
    'database': '#', #database name
    'port': '#' #port used by the mysql(3306)
}
