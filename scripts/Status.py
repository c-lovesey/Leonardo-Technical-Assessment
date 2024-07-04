#import required libraries
import requests 
import datetime

#define constants
jenkins_url = 'http://localhost:8080'  #set url for jenkins
job_name = 'HelloWorld-Pipeline' #set job name
jenkins_api_token = '11bc2ddd3fb227c1deac0b1d70375fe4f7' #set api token
jenkins_api_endpoint = f'{jenkins_url}/job/{job_name}/lastBuild/api/json' #define api endpoint

#function to send GET request to Jenkins API
def latest_build_information():
    try:
        response = requests.get(jenkins_api_endpoint, auth=('admin', jenkins_api_token)) #gets response from jenkins 

        if response.status_code == 200: #check if response is ok
            #if the response status code is 200 then the data is parsed as Json
            build_info = response.json()

            build_status = build_info['result'] #sets status as the result from Json 
            build_duration_ms = build_info['duration']#sets duration from Json (in milliseconds)
            build_timestamp_ms = build_info['timestamp']#sets to the start time of the build (Unix timestamp)

            build_timestamp_s = build_timestamp_ms / 1000  #converts milliseconds to seconds
            build_datetime = datetime.datetime.fromtimestamp(build_timestamp_s).strftime('%Y-%m-%d %H:%M:%S') #formats datetime in a readable format

            #Print build information
            print(f'Build Status: {build_status}') 
            print(f'Build Duration: {build_duration_ms} ms')
            print(f'Build Timestamp: {build_datetime}')

        else:
            print(f'Failed to retrieve build information. Status code: {response.status_code}') #error message for when responce code is not 200

    except Exception as e:
        print(f'Error fetching build information: {str(e)}') #error message when the api endpoint is not available and it outputs the error message

#run the function
latest_build_information() 