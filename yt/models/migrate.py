from telemetry.models.shema import Gateways, Wristbands
import random
import names
from telemetry.models import profiling


def all():
    cities = ['Warszawa', 'Białystok', 'Gdańsk', 'London']
    addresses = ['ul. Woronicza', 'ul. Sienkiewicza', 'ul. Sienkiewicza', 'ul. Szarych Szeregów']

    for g in range(1, 88):
        gateway = {
            "names": "GTW_" + str(g),
            "id": f"{g:0>15}",
            "internaltemp": random.randint(1, 25) + 0.25,
            "lat": random.randint(1, 50) + 0.65,
            "lon": random.randint(1, 50) + 0.32,
            "rssi": g + g + 21,
            "address": f"{random.choice(cities)} {random.choice(addresses)} {g}",
        }

        Gateways().insert(gateway)

        Wristbands().insert([{
            "id": f"BB8039:{g:0>2}:{w:0>2}",
            "nt_child": w,
            "battery": 0,
            "charge": 0,
            "gateway_id": gateway['id'],
            "voltage": g + g + 21,
            "name": f"{names.get_full_name()} ({g:0>2}:{w:0>2})"
        } for w in range(1, 5)])


if __name__ == "__main__":
    with profiling.code():
        all()
