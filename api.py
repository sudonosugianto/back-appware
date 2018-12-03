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
from resourcePO import POResources
from resourceActualStock import ActualStockResources
from resourceSummary import SummaryResources
from resourceCatByVol import CatByVolResources
from resourceTopItemsByCategory import TopItemsByCatResources
from resourceTransactionsSummary import TransactionsSummaryResources
from resourcePackagesSummary import PackagesSummaryResources

from resourceCatSummary import CategorySummaryResources
from resourcePOSalesTransactions import POSalesTransactionResources
from resourcePackagesTrack import PackageTrackDetail
############## Finish Style ##################
from resourceSubusers import SubuserResources

# Import resource untuk api subusers
from resourceSubuserCatSummary import SubuserCategorySummaryResources
from resourceSubuserSummary import SubuserSummaryResources
from resourceSubuserPackagesSummary import SubuserPackagesSummaryResources
from resourceSubuserPackagesTrack import SubuserPackageTrackDetail

############## Finish import resources ##################


######### Tempat untuk Membuat Endpoint ################
api.add_resource(UserResources, "/api/users", "/api/users/<int:id>")
api.add_resource(LoginResources, "/api/users/login")
api.add_resource(ItemResources, "/api/users/item", "/api/users/item/<int:id>")
api.add_resource(CategoryResources, "/api/users/category","/api/users/category/<int:id>")
api.add_resource(PackageResources, "/api/users/packages","/api/users/packages/<int:id>")
api.add_resource(SupplierResources, "/api/users/suppliers","/api/users/suppliers/<int:id>")
api.add_resource(CustomerResources, "/api/users/customers","/api/users/customers/<int:id>")
api.add_resource(POResources, "/api/users/po","/api/users/po/<int:id>")
api.add_resource(SaleResources, "/api/users/sales","/api/users/sales/<int:id>")
api.add_resource(ActualStockResources, "/api/users/actualstock","/api/users/actualstock/<int:id>")
api.add_resource(SummaryResources, "/api/users/summary")
api.add_resource(CatByVolResources, "/api/user/catbyvol")
api.add_resource(TopItemsByCatResources,"/api/user/topitemcat")
api.add_resource(TransactionsSummaryResources, "/api/users/transactionssummary")
api.add_resource(PackagesSummaryResources, "/api/users/packagessummary")
api.add_resource(CategorySummaryResources, "/api/user/categorysummary")
api.add_resource(POSalesTransactionResources, "/api/users/posalestransactions")
api.add_resource(SubuserResources, "/api/users/subusers", "/api/users/subusers/<int:id>")

api.add_resource(PackageTrackDetail, "/api/users/track")
# api.add_resource()
# Endpoint untuk api subusers
api.add_resource(SubuserSummaryResources, "/api/subuser/summary")
api.add_resource(SubuserCategorySummaryResources, "/api/subuser/summary/category")
api.add_resource(SubuserPackagesSummaryResources, "/api/subuser/summary/packages")
api.add_resource(SubuserPackageTrackDetail, "/api/subuser/packages/track")

################# Finished Endpoint ################

if __name__ == '__main__':
    try:
        if  sys.argv[1] == 'db':
            manager.run()
        else:
            app.run(debug=True, host = '0.0.0.0', port = 5000)
    except  IndexError as p:
        app.run(debug=True, host = '0.0.0.0', port = 5000)