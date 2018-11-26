from configs import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

######### Tempat untuk Import Model ########
from modelUsers import Users
from modelItems import Items
from modelCat import Category
from modelPackages import Packages
from modelCustomers import Customers
from modelSales import Sales




from modelSuppliers import Suppliers
from modelPO import PO
from modelPOdetails import PODetails
from modelStocks import Stocks
######### Finish Import Model ########