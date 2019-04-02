import teslajson
import time
is_online = 0
retries = 5
interval_data_req=1 #sec
interval_data_error=10 #sec

#TODO(ehsaan): save token instead the first time, next times reuse
#Needs the teslajson to support returnin token, to investigate.
email=input("Enter tesla email for Tesla.com account:>")
password=input("Enter tesla password for "+email+":>")

#barrier to stop if car is not online. 
#TODO(ehsaan): verify if it means (a)car has no LTE or (b) car is asleep. 
while is_online==0:
	c = teslajson.Connection(email, password)
	v = c.vehicles[0]
	print(v)
	if v["state"]=="online":
		is_online=1
		print("Vehicle online")
	else:
		print("waiting...")
		time.sleep(60)	


#v.wake_up()
#v.data_request('charge_state')
#v.command('charge_start')

#if connection to car is lost, do not give up immediately
while retries:
	print(v)
	try:
		vehicle_data=v.data_request('drive_state')
		#TODO(ehsaan): save with pickle, have another plot class pick it up. or plot live
		print("Speed=\t"+str(vehicle_data['speed']))
		print("Power=\t"+str(vehicle_data['power']))
		#reset retries
		retries=5
		time.sleep(interval_data_req)
	except:
		#probably device went offline, retry 5 times
		print("Could not get data, retries left:"+retries)
		retries-=1
		time.sleep(interval_data_error)
