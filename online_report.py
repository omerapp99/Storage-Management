from operator import itemgetter

from flask import Flask, session, jsonify


# The flask function for the website server and api
def flasks(self):
    app = Flask("Omer API Server", static_url_path='')
    app.secret_key = "asdasdasdas3123asdasdasdasda"

    # Set the routing for the function in the HTML
    @app.route('/api/get_number', methods=["GET"])
    # Get the number of the Items and the totat of items in the storage.
    def get_number():
        total = 0
        session["quan"] = int(len(self.item_list))
        session["tquan"] = list(map(itemgetter('quantity'), self.item_list))
        for ele in range(0, len(session["tquan"])):
            total = total + int(session["tquan"][ele])
        session["tquan"] = total
        return jsonify({"tquan": session["tquan"], "quan": session["quan"]})

    debug = False
    app.run(host='0.0.0.0', port=80, debug=debug)
