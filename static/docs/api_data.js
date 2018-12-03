define({ "api": [
  {
    "type": "get",
    "url": "/api/subuser/summary/category",
    "title": "Gets category summary",
    "version": "1.0.0",
    "name": "get_category_summary",
    "group": "Category_summary",
    "description": "<p>Gets category summary for subuser who have authorized email and apiKey.</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost/api/subuser/summary/category",
        "type": "json"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>The subuser's email.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "apiKey",
            "description": "<p>The subuser's apiKey.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response :",
          "content": "HTTP/1.1 200 OK\n[\n    {\n        \"category\": \"Komputer\",\n        \"itemsStock\": 31,\n        \"itemsSold\": 51,\n        \"Assets\": -20\n    }\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./views.py",
    "groupTitle": "Category_summary"
  },
  {
    "type": "get",
    "url": "/api/subuser/summary/packages",
    "title": "Gets packages summary",
    "version": "1.0.0",
    "name": "get_packages_summary",
    "group": "Packages_summary",
    "description": "<p>Gets packages summary for subuser who have authorized email and apiKey.</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost/api/subuser/summary/packages",
        "type": "json"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>The subuser's email.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "apiKey",
            "description": "<p>The subuser's apiKey.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response :",
          "content": "HTTP/1.1 200 OK\n[\n    {\n        \"packageID\": 53,\n        \"packageName\": \"kardus\",\n        \"itemName\": \"ASUS ZEN 5AA\",\n        \"categoryName\": \"IT\",\n        \"packageSold\": 14,\n        \"packagePO\": 33,\n        \"assets\": 19\n    }\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./views.py",
    "groupTitle": "Packages_summary"
  },
  {
    "type": "get",
    "url": "/api/subuser/packages/track",
    "title": "Gets packages summary",
    "version": "1.0.0",
    "name": "get_packages_track",
    "group": "Packages_track",
    "description": "<p>Gets packages track for subuser who have authorized email and apiKey.</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost/api/subuser/packages/track",
        "type": "json"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>The subuser's email.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "apiKey",
            "description": "<p>The subuser's apiKey.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>The track's code.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response :",
          "content": "HTTP/1.1 200 OK\n[\n   {\n        \"code\": \"59-PO-35-16-T\",\n        \"packages.Items.id\": 74,\n        \"packages.Items.item\": \"hijab luna maya\",\n        \"packages.id\": 59,\n        \"packages.package_name\": \"lusinn\",\n        \"po.id\": 35,\n        \"po.suppliers.name\": \"PT. Luna Sejahtera\",\n        \"po.quantity\": \"5\",\n        \"sales.id\": 0,\n        \"sales.customers.fullname\": null,\n        \"sales.quantity\": null,\n        \"created_at\": \"Mon, 03 Dec 2018 04:32:54 -0000\",\n        \"updated_at\": \"Mon, 03 Dec 2018 04:32:54 -0000\"\n    }\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./views.py",
    "groupTitle": "Packages_track"
  },
  {
    "type": "get",
    "url": "/api/subuser/summary",
    "title": "Gets summary",
    "version": "1.0.0",
    "name": "get_summary",
    "group": "Summary",
    "description": "<p>Gets summary for subuser who have authorized email and apiKey.</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost/api/subuser/summary",
        "type": "json"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>The subuser's email.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "apiKey",
            "description": "<p>The subuser's apiKey.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "dateStart",
            "description": "<p>The start date of summary that subuser want to see.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "dateEnd",
            "description": "<p>The end date after of summary that subuser want to see.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response :",
          "content": "HTTP/1.1 200 OK\n[\n    {\n        \"message\": \"Summary per Item Package\",\n        \"Package\": \"Harddisk per kardusSSS\",\n        \"itemName\": \"Harddisk\",\n        \"packageName\": \"kardusSSS\",\n        \"Category\": \"Komputer\",\n        \"POQuantity\": 30,\n        \"salesQuantity\": 40,\n        \"stock\": -10,\n        \"adjusment\": 0,\n        \"actualStock\": -10\n    }\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./views.py",
    "groupTitle": "Summary"
  }
] });