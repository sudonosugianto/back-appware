from flask import Flask
from flask_apidoc import ApiDoc

app = Flask(__name__)
doc = ApiDoc(app=app)

@app.route('/api/subuser/summary')
def get_summary():
    """
    @api {get} api/subuser/summary Gets summary
    @apiVersion 1.0.0
    @apiName get_summary
    @apiGroup Summary
    @apiDescription Gets summary for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/summary
    @apiParam {String}      email           Mandatory The subuser's email.
    @apiParam {String}      apiKey          Mandatory The subuser's apiKey.
    @apiParam {String}      [dateStart]     Optional The start date of summary that subuser want to see.
    @apiParam {String}      [dateEnd]       Optional The end date after of summary that subuser want to see.
    @apiSuccess {String}    message         The description of HTTP response.
    @apiSuccess {String}    Package         The description of item name per package name.
    @apiSuccess {String}    itemName        Item name
    @apiSuccess {String}    packageName     Package name.
    @apiSuccess {String}    Category        Category of item or package.
    @apiSuccess {Number}    POQuantity      Total quantity of PO of package.
    @apiSuccess {Number}    salesQuantity   Total quantity of sales of package.
    @apiSuccess {Number}    stock           Total quantity of assets of package.
    @apiSuccess {Number}    adjusment       Total quantity of adjustments of package.
    @apiSuccess {Number}    actualStock     Total quantity of actual stock of package.

    @apiSuccessExample {json}    Success-Response :
        HTTP/1.1 200 OK
        [
            {
                "message": "Summary per Item Package",
                "Package": "Harddisk per kardusSSS",
                "itemName": "Harddisk",
                "packageName": "kardusSSS",
                "Category": "Komputer",
                "POQuantity": 40,
                "salesQuantity": 30,
                "stock": 10,
                "adjusment": 0,
                "actualStock": 10
            }
        ]
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 404 Not Found
        {
            "message": "data not found"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 401 Unauthorized
        {
            "message": "unauthorized"
        }
    """
    return

@app.route('/api/subuser/summary/category')
def get_category_summary():
    """
    @api {get} api/subuser/summary/category Gets category summary
    @apiVersion 1.0.0
    @apiName get_category_summary
    @apiGroup Category summary
    @apiDescription Gets category summary for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/summary/category
    @apiParam {String}      email           Mandatory The subuser's email.
    @apiParam {String}      apiKey          Mandatory The subuser's apiKey.
    @apiSuccess {String}    category        The name of category that will be summarize.
    @apiSuccess {Number}    itemsStock      Total quantity of PO of category.
    @apiSuccess {Number}    itemsSold       Total quantity of sales of category.
    @apiSuccess {Number}    Assets          Total quantity of assets of category.

    @apiSuccessExample {json}    Success-Response :
        HTTP/1.1 200 OK
        [
            {
                "category": "Komputer",
                "itemsStock": 51,
                "itemsSold": 31,
                "Assets": 20
            }
        ]
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 404 Not Found
        {
            "message": "data not found"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 401 Unauthorized
        {
            "message": "unauthorized"
        }
    """
    return

@app.route('/api/subuser/summary/packages')
def get_packages_summary():
    """

    @api {get} api/subuser/summary/packages Gets packages summary
    @apiVersion 1.0.0
    @apiName get_packages_summary
    @apiGroup Packages summary
    @apiDescription Gets packages summary for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/summary/packages
    @apiParam {String}      email           Mandatory The subuser's email.
    @apiParam {String}      apiKey          Mandatory The subuser's apiKey.
    @apiSuccess {Number}    packageID       The id of package that will be summarize.
    @apiSuccess {String}    packageName     Package name that will be summarize.
    @apiSuccess {String}    itemName        Item name that will be summarize.
    @apiSuccess {String}    categoryName    Category of the package that will be summarize.
    @apiSuccess {Number}    packageSold     Total quantity of sales of package.
    @apiSuccess {Number}    packagePO       Total quantity of PO of package.
    @apiSuccess {Number}    assets          Total quantity of assets of package.

    @apiSuccessExample {json}    Success-Response :
        HTTP/1.1 200 OK
        [
            {
                "packageID": 53,
                "packageName": "kardus",
                "itemName": "ASUS ZEN 5AA",
                "categoryName": "IT",
                "packageSold": 14,
                "packagePO": 33,
                "assets": 19
            }
        ]
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 404 Not Found
        {
            "message": "data not found"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 401 Unauthorized
        {
            "message": "unauthorized"
        }
    """
    return

@app.route('/api/subuser/packages/track')
def get_packages_track():
    """
    @api {get} api/subuser/packages/track Gets packages summary
    @apiVersion 1.0.0
    @apiName get_packages_track
    @apiGroup Packages track
    @apiDescription Gets packages track for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/packages/track
    @apiParam {String}      email                       Mandatory The subuser's email.
    @apiParam {String}      apiKey                      Mandatory The subuser's apiKey.
    @apiParam {String}      code                        Mandatory The track's code.
    @apiSuccess {String}    code                        The track's code.
    @apiSuccess {Number}    packages.Items.id           The id's of item.
    @apiSuccess {String}    packages.Items.item         Name of item.
    @apiSuccess {Number}    packages.id                 The id's of package.
    @apiSuccess {String}    packages.package_name       Name of package.
    @apiSuccess {Number}    po.id                       The id's of PO.
    @apiSuccess {String}    po.suppliers.name           Name of supplier.
    @apiSuccess {Number}    po.quantity                 The quantity of PO.
    @apiSuccess {Number}    sales.id                    The id's of sales.
    @apiSuccess {String}    sales.customers.fullname    Name of customer.
    @apiSuccess {Number}    sales.quantity              The quantity of sales.
    @apiSuccess {String}    created_at                  the time when the sale occurred.
    @apiSuccess {String}    updated_at                  the time when the sale updated.
    @apiSuccessExample {json}    Success-Response :
        HTTP/1.1 200 OK
        [
           {
                "code": "59-PO-35-16-T",
                "packages.Items.id": 74,
                "packages.Items.item": "hijab luna maya",
                "packages.id": 59,
                "packages.package_name": "lusinn",
                "po.id": 35,
                "po.suppliers.name": "PT. Luna Sejahtera",
                "po.quantity": "5",
                "sales.id": 0,
                "sales.customers.fullname": null,
                "sales.quantity": null,
                "created_at": "Mon, 03 Dec 2018 04:32:54 -0000",
                "updated_at": "Mon, 03 Dec 2018 04:32:54 -0000"
            }
        ]
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 401 Unauthorized
        {
            "message": "unauthorized"
        }

    @apiErrorExample {json} Error-Response:
        HTTP/1.1 404 Not Found
        {
            "message":"Items / Package not Found or maybe it has been sold"
        }
    """
    return