import unittest
from commands import Commands
class TestCommands(unittest.TestCase):
	def setUp(self):
		pass

	def test_move(self):
		self.assertEqual(Commands.move("west"), "This is where you would move west!")

	def test_command_handler_move(self):
		self.assertEqual(Commands.command_handler("move west"), "This is where you would move west!")
