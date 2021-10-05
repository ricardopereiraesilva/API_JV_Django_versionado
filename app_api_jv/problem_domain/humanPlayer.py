from app_api_jv.problem_domain import player
from app_api_jv.problem_domain import move

class HumanPlayer(player.Player):
	def __init__(self):
		super().__init__()

	def enable(self, aState):
		self.turn = True
		return move.Move(0, 0)