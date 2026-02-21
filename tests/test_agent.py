from agent.agent import SimpleAgent

def test_addition():
    agent = SimpleAgent()
    response = agent.run("Add 5 and 7")
    assert response == "12"
