import boto3


rds=boto3.client('rds',region_name='ap-south-1',aws_access_key_id='AKIAJNTQWVOBWUQWEN2A',aws_secret_access_key='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')
try:
    dbs=rds.describe_db_instances()
    for db in dbs['DBInstances']:
        print(f"{db['MasterUsername']}@{db['Endpoint']['Address']}:{db['Endpoint']['Port']} {db['DBInstanceStatus']}")
except Exception as e:
    print(e)        

response=rds.create_db_instance(
    DBInstanceIdentifier="database-2",
    MasterUsername="prj",
    MasterUserPassword="Amrutha2418",
    DBInstanceClass="db.t2.micro",
    Engine="mysql",
    AllocatedStorage=5
)

print(response)
