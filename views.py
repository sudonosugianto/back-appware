from flask import Flask
from flask_apidoc import ApiDoc

app = Flask(__name__)
doc = ApiDoc(app=app)

@app.route('/api/subuser/summary')
def get_summary():
    """
    @api {get} /api/subuser/summary Gets summary
    @apiVersion 1.0.0
    @apiName get_summary
    @apiGroup Summary
    @apiDescription Gets summary for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/summary
    @apiParam {String}      email           The subuser's email.
    @apiParam {String}      apiKey          The subuser's apiKey.
    @apiParam {String}      dateStart       The start date of summary that subuser want to see.
    @apiParam {String}      dateEnd         The end date after of summary that subuser want to see.
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
    @api {get} /api/subuser/summary/category Gets category summary
    @apiVersion 1.0.0
    @apiName get_category_summary
    @apiGroup Category summary
    @apiDescription Gets category summary for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/summary/category
    @apiParam {String}      email           The subuser's email.
    @apiParam {String}      apiKey          The subuser's apiKey.
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

    @api {get} /api/subuser/summary/packages Gets packages summary
    @apiVersion 1.0.0
    @apiName get_packages_summary
    @apiGroup Packages summary
    @apiDescription Gets packages summary for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/summary/packages
    @apiParam {String}      email           The subuser's email.
    @apiParam {String}      apiKey          The subuser's apiKey.
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
    @api {get} /api/subuser/packages/track Gets packages summary
    @apiVersion 1.0.0
    @apiName get_packages_track
    @apiGroup Packages track
    @apiDescription Gets packages track for subuser who have authorized email and apiKey.
    @apiExample Example usage:
    curl -i https://api.appware.tech/api/subuser/packages/track
    @apiParam {String}      email           The subuser's email.
    @apiParam {String}      apiKey          The subuser's apiKey.
    @apiParam {String}      code            The track's code.
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