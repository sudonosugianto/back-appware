from flask_restful import fields

user_fields = {
    "id": fields.Integer,
    "fullname": fields.String, 
    "username": fields.String,
    "email": fields.String,
    "phone_number": fields.String,
    "status":fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
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
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

category_fields = {
    "id":fields.Integer,
    "userID":fields.Integer,
    "category": fields.String,
    "status":fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
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
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
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
    "suppliers.name": fields.String,
    "userPOID": fields.Integer,
    "packagePOID": fields.Integer,
    "packages.Items.item":fields.String,
    "packages.package_name": fields.String,
    "packages.Category.category":fields.String,
    "quantity": fields.Integer,
    "buyingPricePerPackage": fields.Float,
    "totalPrice": fields.Float,
    "notes" : fields.String,
    "status":fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

sale_fields = {
    "id": fields.Integer,
    "userSalesID": fields.Integer,
    "customerSalesID": fields.Integer,
    "customers.fullname": fields.String,
    "packageSalesID": fields.Integer,
    "packages.Items.item":fields.String,
    "packages.package_name": fields.String,
    "packages.Category.category":fields.String,
    "quantity": fields.Integer,
    "sellingPricePerPackage": fields.Float,
    "totalPrice":fields.Float,
    "status": fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

actualstock_fields = {
    "id": fields.Integer,
    "userActualStocksID": fields.Integer,
    "packageActualStocksID": fields.Integer,
    "actual_stock": fields.Integer,
    "packages.package_name": fields.String,
    "packages.Items.item":fields.String,
    "notes": fields.String,
    "status": fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

packagetrack_fields = {
    "id": fields.Integer,
    "POID": fields.Integer,
    "salesID": fields.Integer,
    "packageID": fields.Integer,
    "packages.Items.item":fields.String,
    "packages.package_name":fields.String,
    "code": fields.String,
    "status": fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

subuser_fields = {
    "id": fields.Integer,
    "userID": fields.Integer,
    "fullname": fields.String,
    "email": fields.String,
    "username": fields.String,
    "apiKey": fields.String,
    "phone_number": fields.String,
    "subuser_type": fields.String,
    "status": fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}