import json
import urllib3


http = urllib3.PoolManager()
# g = http.request('GET', 'https://reqres.in/api/users/23') #this one should have an error for test the status code.
g = http.request('GET', 'https://reqres.in/api/unknown/2') #this one works fine.
# check if there is no response from the server.
if g.status != 200:
    print('Something went wrong!')
    print('Error: ', g.status)
else:
    print(g.status)
    print(type(g.data))
    # check the data if it is a string or not.
    if type(g.data) == str:
        print('It is a string')
    else:
        print('It is not a string')
    # decode the data to be a json format.
    data = json.loads(g.data.decode('utf-8'))
    print("this is the whole data:")
    print(data)
    print("this is the data we need:")
    print('Name:',data['data']['name'])
    print('Year:',data['data']['year'])
    print('Color',data['data']['color'])

# create a post request.
r = http.request('POST', 'https://reqres.in/api/users', body=json.dumps({'name': 'morpheus', 'job': 'leader'}), headers={'Content-Type': 'application/json'})
print(r.status)
print(r.data)



