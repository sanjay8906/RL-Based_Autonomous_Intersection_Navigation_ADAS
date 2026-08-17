from metadrive import MetaDriveEnv
from metadrive.manager.traffic_manager import TrafficMode


class MetaDriveSimulator:

    def __init__(self, render=True, manual=False):

        self.manual = manual

        self.env = MetaDriveEnv(
            {
                "num_scenarios": 1,
                "use_render": render,

                "manual_control": manual,

                "traffic_density": 0.2,
                "traffic_mode": TrafficMode.Trigger,
            }
        )

    def reset(self):
        return self.env.reset()

    def step(self, action):
        return self.env.step(action)

    def close(self):
        self.env.close()