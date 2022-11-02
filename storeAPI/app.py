from flask import Flask,request

app=Flask(__name__)

stores=[{'name':'gasabo','items':[{'name':'chair','price':17.9}]}]

@app.get('/store')
def allStores():
    return stores


@app.get('/store/<string:name>')
def storeByName(name):
    for store in stores:
        if store.get('name')==name:
            return store
    return {'message':'store not found!'},404


@app.get('/store/<string:name>/item')
def storeItemByName(name):
    for store in stores:
        if store.get('name')==name:
            return store.get('items')
    return {'message':'store not found!'},404


@app.post('/store')
def createStore():
    storedata=request.get_json()
    new_store={'name':storedata.get('name'),'items':[]}
    stores.append(new_store)
    return new_store,201


@app.post('/store/<string:name>')
def addStoreItem(name):
    storeitem=request.get_json()
    for store in stores:
        if store.get('name')==name:
            store['items'].append(storeitem)
            return storeitem,201
    return {'message':'store cant be found!'},404

