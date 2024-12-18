from bottle import Bottle, route, run, request, response
from xml.etree.ElementTree import Element, tostring

app = Bottle()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/currency")
def get_currency():
    today = request.query.get("today")
    if today is not None:
        return "USD - 41.5"
    else:
        return "Будь ласка, вкажіть параметр ''сьогодні''."

@app.route("/content_type")
def handle_request():
    content_type = request.get_header("Content-Type")

    if content_type == "application/json":
        return {"message": "Відповідь у форматі JSON."}
    elif content_type == "application/xml":
        root = Element("response")
        message = Element("message")
        message.text = "This is an XML response."
        root.append(message)
        response.content_type = "application/xml"
        return tostring(root).decode()
    else:
        return "Відповідь у вигляді звичайного тексту."

if __name__ == '__main__':
    run(app, host='localhost', port=8000)