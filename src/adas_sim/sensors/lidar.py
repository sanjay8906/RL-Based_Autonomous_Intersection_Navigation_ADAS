class LidarSensor:

    def __init__(self):
        print("LiDAR Initialized")

    def process(self, observation):

        print("Observation Length:", len(observation))

        return observation