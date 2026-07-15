from fastapi import FastAPI, HTTPException
import httpx
from datetime import datetime

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="Weather API",
    description="API que consulta el clima actual usando Open-Meteo",
    version="1.0.0"
)

# Diccionario simple con coordenadas de algunas ciudades de Argentina
CITIES = {
    "mar-del-plata": {"lat": -38.0004, "lon": -57.5562},
    "buenos-aires": {"lat": -34.6131, "lon": -58.3772},
    "cordoba": {"lat": -31.4135, "lon": -64.1810},
}

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la Weather API",
        "status": "Online",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/weather/{city}")
async def get_weather(city: str):
    # Validamos que la ciudad esté en nuestro diccionario
    city_lower = city.lower()
    if city_lower not in CITIES:
        raise HTTPException(
            status_code=404, 
            detail=f"Ciudad no encontrada. Probá con: {', '.join(CITIES.keys())}"
        )

    coords = CITIES[city_lower]
    
    # Consultamos la API pública y gratuita de Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status() # Verifica si hubo errores de conexión
            data = response.json()
            
            # Extraemos y devolvemos solo la información que nos interesa
            current_weather = data.get("current_weather", {})
            return {
                "city": city,
                "temperature": current_weather.get("temperature"),
                "windspeed": current_weather.get("windspeed"),
                "weathercode": current_weather.get("weathercode")
            }
        except httpx.HTTPError:
            raise HTTPException(status_code=503, detail="Servicio meteorológico no disponible")
