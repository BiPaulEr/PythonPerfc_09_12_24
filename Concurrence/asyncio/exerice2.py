import asyncio
import random

async def fetch_weather(city):
    await asyncio.sleep(1)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}

async def main():
    liste_city = ["City1", "City2", "City3"]
    result = await asyncio.gather(*[fetch_weather(city) for city in liste_city])
    print(result)
    
    somme = sum(map(lambda dictionnaire : dictionnaire["température"], result))
    print(f"Moyenne {somme / len(result)}")


asyncio.run(main())