from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

counter_value = 0

@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>App-1</title>
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
            <style>
                body,h1 {font-family: "Raleway", sans-serif}
                body, html {height: 100%}
                .bgimg {
                  background-image: url('https://storage.googleapis.com/a-dream/br2.jpg');
                  min-height: 100%;
                  background-position: center;
                  background-size: cover;
                }

                .w3-display-middle {
                  background-image: url('https://storage.googleapis.com/a-dream/1hot.png');
                  background-size: cover;
                  padding: 200px; /* Add padding to make it look better */
                  border-radius: 25px; /* Optional: adds rounded corners */
                  text-align: center; /* Center-align the text */
                }

                .transparent-background {
                  background-color: rgba(17, 17, 17, 0.5); /* Adjust the rgba values for desired transparency */
                  padding-top: 1px; /* Set the top padding */
                  padding-bottom: 1px; /* Set the bottom padding */
                  padding-left: 2px; /* Set the left padding */
                  padding-right: 2px; /* Set the right padding */
                  border-radius: 5px; /* Optional: adds rounded corners */
                  display: inline-block; /* Inline-block to wrap around content */
                }
                .w3-display-middle h1 {
                  font-size: 4em; /* Increase the font size of the heading */
                }

                .w3-display-middle p {
                  font-size: 1.5em; /* Increase the font size of the paragraph */
                }

                .counter-container {
                  margin-top: 20px;
                }

                button { 
                  font-size: 2em; 
                  padding: 10px 20px; 
                  background: transparent;
                  color: white;
                  border: 2px solid white;
                  cursor: pointer;
                }

                button:hover {
                  background: rgba(255, 255, 255, 0.2);
                }
            </style>
        </head>
        <body>

        <div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
          <div class="w3-display-topleft w3-padding-large w3-xlarge">
            <h1 class="w3-jumbo w3-animate-top">APPLICATION-A</h1>
          </div>
          <div class="w3-display-middle">
            <h1>Counter Value: <span id="counter">{{ counter }}</span></h1>
            <div class="counter-container">
              <button onclick="incrementCounter()">Push me</button>
            </div>
          </div>
        </div>

        <script>
            function incrementCounter() {
                fetch('/increment', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('counter').innerText = data.counter;
                    });
            }
        </script>

        </body>
        </html>
    ''', counter=counter_value)

@app.route('/increment', methods=['POST'])
def increment():
    global counter_value
    counter_value += 1
    return jsonify(counter=counter_value)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)