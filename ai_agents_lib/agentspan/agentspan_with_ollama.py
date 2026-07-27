import os
from conductor.ai.agents import Agent, AgentRuntime, tool

os.environ.setdefault("CONDUCTOR_MP_START_METHOD", "fork")

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return f"72°F and sunny in {city}"


@tool
def get_attractions(city: str) -> str:
    """Get popular local attractions for a city."""
    return f"Top attractions in {city}: Red Fort, Qutub Minar, India Gate"


def main():
    """Configures and runs the weather agent and tour agent with a local Ollama model."""
    weather_agent = Agent(
        name="weatherbot",
        model="ollama/ornith-1.0-9b-Q4",
        base_url="http://localhost:11434",
        instructions=(
            "You are a helpful assistant. When asked about a city, look up the weather and answer."
        ),
        tools=[get_weather],
    )

    tour_agent = Agent(
        name="tourbot",
        model="ollama/ornith-1.0-9b-Q4",
        base_url="http://localhost:11434",
        instructions=(
            "You are a local tour guide assistant. When asked about a city, look up its top local "
            "attractions and return 2-3 must-visit spots."
        ),
        tools=[get_attractions],
    )

    with AgentRuntime() as runtime:
        print("Running weather agent with Ollama model...")
        weather_result = runtime.run(weather_agent, "What should I do today in Delhi?")
        weather_result.print_result()

        print("\nRunning tour agent with Ollama model...")
        tour_result = runtime.run(tour_agent, "What are the top attractions to visit in Delhi?")
        tour_result.print_result()


if __name__ == "__main__":
    main()
