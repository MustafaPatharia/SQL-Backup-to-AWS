import os
import time
#please make sure that S3 module from Amazon was on your sys.path
import boto3
from botocore.exceptions import NoCredentialsError

def upload_db_to_Amazons3():
    AWS_ACCESS_KEY_ID = 'YOUR ACCESS KEY'
    AWS_SECRET_ACCESS_KEY = 'YOUR SECRET KEY'
    BUCKET_NAME = 'AWS_BUCKET_NAME'
    MYSQL_DUMP_PATH = '..\mysql-8.0.23-winx64\bin\mysqldump'
    DATABASE_NAME ='DB_NAME'
    HOST = 'YOUR HOST NAME'
    PORT = 'IF YOUR HAVE ONE'
    DB_USER = 'YOUR USER NAME'
    DB_PASS = 'YOUR PAASWORD'
           
    print "Preparing "+DATABASE_NAME+" database backup................"      
    filestamp = time.strftime('%Y-%m-%d-%I')
    #create data file
    backup = os.popen("mysqldump --column-statistics=0 -h %s -P %s -u %s -p%s %s > %s.sql" % (HOST,PORT,DB_USER,DB_PASS,DATABASE_NAME,DATABASE_NAME+"_"+filestamp))
    
    print("\n|| Database dumped to "+DATABASE_NAME+"_"+filestamp+".sql || ")
    FILE_NAME = DATABASE_NAME+"_"+filestamp+".sql"
   

    print "uploading the "+DATABASE_NAME+" file to Amazon S3..............."
    
    conn = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    #upload file to Amazon S3    
    backup_data = open(os.path.join(os.curdir, FILE_NAME) , "rb").read()

    conn.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)

    print "Upload Successfull... Your DB is safe is AWS"


upload_db_to_Amazons3()
