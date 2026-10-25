def rps(p1, p2):
    dict = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if dict[p1] == p2:
        return "Player 1 won!"
    elif dict[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
        