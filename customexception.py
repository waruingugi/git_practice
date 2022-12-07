# Creating a custom exception

class LocationTooFarError(Exception):
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return 'Location is not within 10km: ' + str(self.distance)


def schedule_delivery(distance_from_store):
    if distance_from_store > 10:
        raise LocationTooFarError(distance_from_store)
    else:
        print('Scheduling the delivery....')


schedule_delivery(10)