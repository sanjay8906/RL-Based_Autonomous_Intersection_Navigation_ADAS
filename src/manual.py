from adas_sim.metadrive.adapter import MetaDriveSimulator


def main():

    simulator = MetaDriveSimulator(
        render=True,
        manual=True
    )

    simulator.reset()

    print("=" * 60)
    print("Manual Driving")
    print("Use MetaDrive controls:")
    print("W -> Accelerate")
    print("S -> Brake")
    print("A -> Left")
    print("D -> Right")
    print("=" * 60)

    while True:

        simulator.step(None)


if __name__ == "__main__":
    main()