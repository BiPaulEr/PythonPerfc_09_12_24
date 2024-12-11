import asyncio
import time

class ContextManagerShowMeAsynchrone:
    async def __aenter__(self):
        print("Je prépare le contexte")
        return "Object disponible dans le contexte"

    async def __aexit__(self, type_exc, exc, tb):
        print("Je nettoie le contexte")
        if (type_exc is None):
            print("Pas d'exception")
        else:
            print(f"Exception {type_exc} {exc}")
        return True


async def main():  
    async with ContextManagerShowMeAsynchrone() as object:
        print(object)
        print("Je suis dans le contxete")
        raise Exception("Erreur ?")

asyncio.run(main())