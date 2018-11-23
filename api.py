import sys, json
from functools import wraps
from configs import app
from configs import manager
from configs import api

###### Tempat Untuk Import Resource #########
from resourceClient import Client
############## Finish Style ##################


######### Tempat untuk Membuat Endpoint ################
api.add_resource(Client, '/client/<int:id>' , '/client')
################# Finished Endpoint ################

if __name__ == '__main__':
    try:
        if  sys.argv[1] == 'db':
            manager.run()
        else:
            app.run(debug=True, host = '0.0.0.0', port = 5000)
    except  IndexError as p:
        app.run(debug=True, host = '0.0.0.0', port = 5000)