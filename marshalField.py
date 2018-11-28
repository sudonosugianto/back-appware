from flask_restful import fields

user_fields = {
    "id": fields.Integer,
    "fullname": fields.String, 
    "username": fields.String,
    "email": fields.String,
    "phone_number": fields.String,
    "status":fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

item_fields = {
    "id":fields.Integer,
    "userID":fields.Integer,
    "catID": fields.Integer,
    "Category.category": fields.String,
    "item":fields.String,
    "picture":fields.String,
    "size":fields.Integer,
    "unit":fields.String,
    "SKU":fields.Integer,
    "status":fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

category_fields = {
    "id":fields.Integer,
    "userID":fields.Integer,
    "category": fields.String,
    "status":fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

package_fields = {
    "id": fields.Integer,
    "itemID": fields.Integer,
    "package_name": fields.String,
    "Items.item": fields.String,
    "Items.Category.category": fields.String,
    "items_quantity": fields.Integer,
    "status": fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String,
    "Users.fullname": fields.String,
    "Category.category": fields.String,
}

supplier_fields = {
    "id": fields.Integer,
    "userSuppliersID": fields.Integer,
    "name" : fields.String,
    "phone_number" : fields.String,
    "email" : fields.String,
    "address" : fields.String,
    "city" : fields.String,
    "state" : fields.String,
    "zipcode" : fields.String,
    "created_at": fields.String,
    "updated_at": fields.String
}

customer_fields = {
    "id": fields.Integer,
    "userCustomerID": fields.Integer,
    "fullname": fields.String,
    "phoneNumber": fields.String,
    "email": fields.String,
    "address": fields.String,
    "city": fields.String,
    "state": fields.String,
    "zipcode": fields.String,
    "status": fields.Boolean
}

po_fields = {
    "id": fields.Integer,
    "supplierID": fields.Integer,
    "Suppliers.name": fields.String,
    "userPOID": fields.Integer,
    "packagePOID": fields.Integer,
    "Packages.package_name": fields.String,
    "quantity": fields.Integer,
    "buyingPricePerPackage": fields.Float,
    "totalPrice": fields.Float,
    "notes" : fields.String,
    "status":fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

sale_fields = {
    "id": fields.Integer,
    "userSalesID": fields.Integer,
    "customerSalesID": fields.Integer,
    "Customers.fullname": fields.String,
    "packageSalesID": fields.Integer,
    "Packages.package_name": fields.String,
    "quantity": fields.Integer,
    "sellingPricePerPackage": fields.Float,
    "totalPrice":fields.Float,
    "status": fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

actualstock_fields = {
    "id": fields.Integer,
    "userActualStocksID": fields.Integer,
    "packageActualStocksID": fields.Integer,
    "actual_stock": fields.Integer,
    "notes": fields.String,
    "status": fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}