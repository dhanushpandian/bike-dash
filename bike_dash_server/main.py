from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>

<head>
    <title>Bike Dashboard</title>

    <style>
        body {
            background: black;
            color: white;
            font-family: Arial;
            text-align: center;
            margin-top: 100px;
        }

        .speed {
            font-size: 100px;
            font-weight: bold;
        }
    </style>
</head>

<body>

    <h1>BIKE DASH</h1>

    <div class="speed" id="speed">0</div>
    <div>km/h</div>

    <script>
        function updateSpeed(speed) {
            if (speed === null) {
                document.getElementById('speed').innerText = "0";
                return;
            }

            const kmh = (speed * 3.6).toFixed(0);

            document.getElementById('speed').innerText = kmh;
        }

        navigator.geolocation.watchPosition(
            (position) => {
                const speed = position.coords.speed;

                console.log("Speed:", speed);

                updateSpeed(speed);
            },

            (error) => {
                console.log(error);
            },

            {
                enableHighAccuracy: true,
                maximumAge: 0,
                timeout: 5000
            }
        );
    </script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return html