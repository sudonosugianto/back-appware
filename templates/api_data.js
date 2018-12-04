define({ "api": [
  {
    "type": "get",
    "url": "/api/users/packagessummary",
    "title": "2. Mendapatkan Packages Summary",
    "version": "0.1.0",
    "name": "getPackageSummary",
    "group": "Summary",
    "permission": [
      {
        "name": "APIkey"
      }
    ],
    "description": "<p>Digunakan untuk mendapatkan Summary dari sebuah Pacakages</p>",
    "examples": [
      {
        "title": "Cara penggunaan:",
        "content": "http://3.0.98.109/api/users/packagessummary",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Contoh data yang berhasil :",
          "content": "[\n   {\n       \"packageID\": 51,\n       \"packageName\": \"kardus\",\n       \"itemName\": \"Keripik Tempe\",\n       \"categoryName\": \"Uncategorized\",\n       \"packageSold\": 40,\n       \"netSales\": 600000000,\n       \"profit\": 150000000\n   }\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./appware.js",
    "groupTitle": "Summary"
  },
  {
    "type": "get",
    "url": "/api/users/summary?dateStart=:dateStart&dateEnd=:dateEnd",
    "title": "1.Mendapatkan Summary dari Inventory di Gudang",
    "version": "0.1.0",
    "name": "getSummary",
    "group": "Summary",
    "permission": [
      {
        "name": "APIkey"
      }
    ],
    "description": "<p>Digunakan untuk mendapatkan data summary inventory</p>",
    "examples": [
      {
        "title": "Cara penggunaan:",
        "content": "http://3.0.98.109/api/users/summary?dateStart=2018-11-28 00:00:00&dateEnd=2018-11-28 23:59:59",
        "type": "json"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "dateStart",
            "description": "<p>tanggal awal summary yang diinginkan dengan format YYYY-MM-DD HH:MM:SS</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "dateEnd",
            "description": "<p>tanggal akhir summary yang diinginkan dengan format YYYY-MM-DD HH:MM:SS</p>"
          }
        ]
      }
    },
    "filename": "./appware.js",
    "groupTitle": "Summary"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./doc/main.js",
    "group": "_home_alpha_Documents_AppWare_api_doc_doc_main_js",
    "groupTitle": "_home_alpha_Documents_AppWare_api_doc_doc_main_js",
    "name": ""
  }
] });
