import robot_race_functions as rr
from collections import deque, Counter, namedtuple
from time import time, sleep

maze_file_name = 'maze_data_1.csv'
seconds_between_turns = 0.3
max_turns = 35

# Initialize the robot race
maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)

# Populate a deque of all robot commands for the provided maze
robot_moves = deque()
num_of_turns = 0
while not rr.is_race_over(bots) and num_of_turns < max_turns:
  # For every bot in the list of bots, if the bot has not reached the end, add a new move to the robot_moves deque
  # Add your code below!
  for bot in bots:
    if bot.has_finished == False:
      robot_moves.append(rr.compute_robot_logic(walls, goal, bot))
  num_of_turns += 1
print(robot_moves)
# Count the number of moves based on the robot names
# Add your code below!
num_moves = Counter(vals[0] for vals in robot_moves)
# Count the number of collisions by robot name
# Add your code below!
num_collisions = Counter(vals[0] for vals in robot_moves if vals[2] is True)
# Create a namedtuple to keep track of our robots' points
# Add your code below!
Robot = namedtuple('BotScoreData', ['name', 'num_moves', 'num_collisions', 'score'])
# Calculate the scores (moves + collisions) for each robot and append it to bot_scores 
bot_scores = []
# Add your code below!
for bot in bots:
  bot_scores.append(Robot(bot.name, num_moves[bot.name], num_collisions[bot.name], num_moves[bot.name] + num_collisions[bot.name]))

# Populate a dict to keep track of the robot movements
bot_data = {}
# Add your code below!
for bot in bots:
  bot_data[bot.name] = bot

# Move the robots and update the map based on the moves deque
while len(robot_moves) > 0:
  # Make sure to pop moves from the front of the deque
  # Add your code below!
  bot_data[robot_moves[0][0]].process_move(robot_moves.popleft()[1])

  # Update the maze characters based on the robot positions and print it to the console
  rr.update_maze_characters(maze_data, bots)
  rr.print_maze(maze_data)
  sleep(seconds_between_turns - time() % seconds_between_turns)

# Print out the results!
rr.print_results(bot_scores)
