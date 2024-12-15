from flask import Flask, jsonify,request

#Put amd Delete 
# Working with APIs

app = Flask(__name__)

## Creating some initial data
items = [
    {"id":1,"name":"Item 1","description":"This is item 1"},
    {"id":2,"name":"Item 2","description":"This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the Sample To-Do List applitcation"

#GEt : Retrive all the items
@app.route('/items',methods = ['GET'])
def get_items():
    return jsonify(items)

#GET : retrive item by id
@app.route('/items/<int:item_id>',methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id),None)
    if item == None:
        return jsonify({"Error":"Item not found"})
    return jsonify(item)

#POST : creating a new task - API
@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"Error":"Improper Format"})
    else:
        new_item = {
            "id" : items[-1]["id"]+1 if items else 1,
            "name" : request.json["name"],
            "description" : request.json["description"]
        }
        items.append(new_item)
        return jsonify(items)
    
#Put : Update an existing item
@app.route('/items/<int:item_id>',methods = ["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id),None)
    if item == None:
        return jsonify({"Eror":"Item is not found"})
    item["name"] = request.json.get("name",item["name"])
    item["description"] = request.json.get("description",item["description"])
    return jsonify(item)
    '''Start
        |
        v
Receive PUT request with item_id and JSON data
            |
            v
Is there an item with the given item_id?
    |                           \
    |                           \
    Yes                         No
    |                           \
    v                           v
Extract "name" and          Return error:
"description" from          {"Error": "Item not found"}
request JSON using get():       |
    - For "name":               v
        If provided,             End
        update item["name"]
        Else, keep the current 
        value of item["name"]
    - For "description": 
        If provided, 
        update item["description"]
        Else, keep the current 
        value of item["description"]
    |
    v
Return updated item as JSON
    |
    v
    End
'''

#Delete a item
@app.route('/items/<int:item_id>',methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"deleted" : "Item is deleted successfully"})
if __name__ == '__main__':
    app.run(debug=True)