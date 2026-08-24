from metadrive import MetaDriveEnv
from metadrive.manager.traffic_manager import TrafficMode


class MetaDriveSimulator:

    def __init__(self, render=True, manual=False):

        self.manual_mode = bool(manual)

        self.env = MetaDriveEnv(
            {
                "num_scenarios": 1,
                "use_render": render,

                # Enable keyboard input system
                "manual_control": True,

                "traffic_density": 0.2,
                "traffic_mode": TrafficMode.Trigger,
            }
        )

    def reset(self):
        obs, info = self.env.reset()

        # Respect the requested starting mode.
        self.env.current_track_agent.expert_takeover = not self.manual_mode

        return obs, info

    def step(self, action=None):

        # T key is handled by MetaDrive's manual controller.
        # We explicitly check whether takeover has changed.

        agent = self.env.current_track_agent

        # When expert_takeover=True -> automatic controller
        # When expert_takeover=False -> keyboard/manual control
        if agent.expert_takeover:
            mode = "AUTO"
        else:
            mode = "MANUAL"

        # In manual mode MetaDrive reads W/A/S/D itself.
        # In auto mode [0, 0] lets the expert policy control the car.
        if action is None:
            action = [0.0, 0.0]

        result = self.env.step(action)

        # Show current mode on the MetaDrive interface
        self.env.render(
            text={
                "Control Mode (T)": mode,
                "Manual": "W A S D",
                "Automatic": "Expert / IDM",
            }
        )

        return result

    def close(self):
        self.env.close()