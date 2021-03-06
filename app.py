import requests
import boto3
import time

bucket="bucketpunto2descarga"
def handler(event,context):

	localtime=time.localtime()
	print("Getting html content...")
	
	s3 = boto3.resource('s3')
	print("Loading in s3...")
	getHTMLNewspaper("eltiempo","https://www.eltiempo.com/",localtime,bucket,s3)
	getHTMLNewspaper("elespectador","https://www.elespectador.com/",localtime,bucket,s3)
	print("files uploaded!")
	return {
			"status_code":200
		}

def getHTMLNewspaper(name, url,localtime,bucketname,s3):	
	
	r = requests.get(url)
	print("Creating temporaly file...")
	filepath="/tmp/"+name+".html"
	f = open(filepath,"w")
	print("Saving file from "+name)
	f.write(r.text)
	f.close()
	data={
		'file':filepath,
		'bucket':bucketname,
		'path':'headlines/raw/periodico='+name+'/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/'+str(localtime.tm_hour)+str(localtime.tm_min)+str(localtime.tm_sec)+'page.html'
	}
	s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])