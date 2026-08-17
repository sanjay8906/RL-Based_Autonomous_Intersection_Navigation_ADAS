from adas_sim.metadrive.adapter import MetaDriveSimulator


def main():

    simulator = MetaDriveSimulator(
        render=True,
        manual=False
    )

    observation, info = simulator.reset()

    while True:

        action = [0.0, 0.5]

        observation, reward, terminated, truncated, info = simulator.step(action)

        if terminated or truncated:
            observation, info = simulator.reset()
            from adas_sim.sensors.lidar import LidarSensor
            lidar = LidarSensor()
        lidar.process(observation)



if __name__ == "__main__":
    main()