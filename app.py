from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
    <title>Get GPS Location</title>
</head>
<body>
    <h2>Get Current GPS Location</h2>
    <button onclick="getLocation()">Get Location</button>
    <p id="result"></p>

    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition, showError);
            } else {
                document.getElementById("result").innerHTML = "Geolocation is not supported by this browser.";
            }
        }

        function showPosition(position) {
            fetch('/location', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude
                })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("result").innerHTML = 
                    `Latitude: ${data.latitude}, Longitude: ${data.longitude}`;
            });
        }

        function showError(error) {
            switch (error.code) {
                case error.PERMISSION_DENIED:
                    alert("User denied the request for Geolocation.");
                    break;
                case error.POSITION_UNAVAILABLE:
                    alert("Location information is unavailable.");
                    break;
                case error.TIMEOUT:
                    alert("The request to get user location timed out.");
                    break;
                case error.UNKNOWN_ERROR:
                    alert("An unknown error occurred.");
                    break;
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    return jsonify({'latitude': lat, 'longitude': lon})

if __name__ == '__main__':
    app.run(debug=True)
