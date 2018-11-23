import sys, json
from configs import app
from configs import manager
from configs import api

###### Tempat Untuk Import Resource #########
# from resourceClient import Client
from resourceUser import UserResources
from resourceLogin import LoginResources
############## Finish Style ##################


######### Tempat untuk Membuat Endpoint ################
# api.add_resource(Client, '/client/<int:id>' , '/client')
api.add_resource(UserResources, "/api/users")
api.add_resource(LoginResources, "/api/users/login")
################# Finished Endpoint ################

if __name__ == '__main__':
    try:
        if  sys.argv[1] == 'db':
            manager.run()
        else:
            app.run(debug=True, host = '0.0.0.0', port = 5000)
    except  IndexError as p:
        app.run(debug=True, host = '0.0.0.0', port = 5000)