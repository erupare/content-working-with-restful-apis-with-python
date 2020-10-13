from flask import Flask, json, jsonify, make_response, request

app = Flask(__name__)

class Contact:
    def __init__(self, contact_id, name, address, favorite_food):
        self.contact_id = contact_id
        self.name = name
        self.address = address
        self.favorite_food = favorite_food
    
    def serialize(self):
        return self.__dict__


contacts = {
    "1": Contact("1", "Bugs Bunny", "1 Carrot Lane, Toontown", "carots"),
    "2": Contact("2", "Sylvester", "5 Alleyway, Toontown", "Tweety"),
    "3": Contact("3", "Scooby Doo", "32 Dog Lake, Toontowm", "Scooby Snacks")
}

def update_full_contact(contact_id, data):
    contacts['contact_id']['name'] = data.get('name', contacts['contact_id']['name'])
    contacts['contact_id']['address'] = data.get('address', contacts['contact_id']['address'])
    contacts['contact_id']['favorite_food'] = data.get('favorite_food', contacts['contact_id']['favorite_food'])

def update_partial_contact(contact_id, data):
    if 'name' in dict.keys():
        contacts['contact_id']['name'] = data.get('name')
    if 'address' in dict.keys():
        contacts['contact_id']['address'] = data.get('address')
    if 'favorite_food' in dict.keys():
        contacts['contact_id']['favorite_food'] = data.get('favorite_food')

def remove_contact(contact_id):
    del contacts['contact_id']

@app.route('/api/contacts/all', methods=['GET'])
def get_contacts():
    return jsonify(data=[contacts[id].serialize() for id in contacts])


@app.route('/api/contacts/<contact_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def contact(contact_id):
    
    if request.method == 'GET':
        return contacts[contact_id].serialize()
    elif request.method == 'PUT':
        update_full_contact(contact_id, request.get_json())
        return contacts[contact_id].serialize()
    elif request.method == 'PATCH':
        update_partial_contact(contact_id, request.get_json())
        return contacts[contact_id].serialize()
    elif request.method == 'DELETE':
        remove_contact(contact_id)
        return None

@app.route('/api/contacts/new', methods=['POST'])
def create_contact():
    data = request.get_json()
    data["contact_id"] = str(int(sorted(contacts.keys())[-1]) + 1)
    new_contact = Contact(**data)
    contacts[data['contact_id']] = new_contact

    return new_contact.serialize()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
