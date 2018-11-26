import sys, json
from configs import app
from configs import manager
from configs import api

###### Tempat Untuk Import Resource #########

from resourceUser import UserResources
from resourceLogin import LoginResources
from resourceItem import ItemResources
from resourceCategory import CategoryResources
from resourcePackages import PackageResources
from resourceSuppliers import SupplierResources
from resourceCustomers import CustomerResources
from resourceSales import SaleResources

############## Finish Style ##################


######### Tempat untuk Membuat Endpoint ################
api.add_resource(UserResources, "/api/users")
api.add_resource(LoginResources, "/api/users/login")
api.add_resource(ItemResources, "/api/users/item", "/api/users/item/<int:id>")
api.add_resource(CategoryResources, "/api/users/category","/api/users/category/<int:id>")
api.add_resource(PackageResources, "/api/users/packages","/api/users/packages/<int:id>")
api.add_resource(SupplierResources, "/api/users/suppliers","/api/users/suppliers/<int:id>")
api.add_resource(CustomerResources, "/api/users/customers","/api/users/customers/<int:id>")
################# Finished Endpoint ################

if __name__ == '__main__':
    try:
        if  sys.argv[1] == 'db':
            manager.run()
        else:
            app.run(debug=True, host = '0.0.0.0', port = 5000)
    except  IndexError as p:
        app.run(debug=True, host = '0.0.0.0', port = 5000)