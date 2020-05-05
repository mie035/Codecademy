
######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []
  def add_child(self,node):
    self.choices.append(node)
  def traverse(self):
    story_node = self
    while story_node.choices != []:
      choice = input("Enter 1 or 2 to continue the story: ")
      if not choice in ["1","2"] :
        print("do not enter number except of 1 and 2")
      chosen_index = int(choice) - 1
      chosen_child = story_node.choices[chosen_index]
      print("you chose:{0} \n {1}".format(chosen_index,chosen_child.story_piece))
      story_node = chosen_child


######
# VARIABLES FOR TREE
######
user_nm = input("What is your name?")
print("Hi,there {0}!!".format(user_nm))
print("Once upon a time…")
story_root = TreeNode(
"""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

#start a familly
choice_a = TreeNode(
"""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
    )

choice_a_1 = TreeNode(
"""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
)
choice_a_2 = TreeNode(
"""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")
#end 1 familly
choice_b = TreeNode(
"""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
)

choice_b_1 = TreeNode(
"""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")
choice_b_2 = TreeNode(
"""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
)
######
# TESTING AREA
######
print(story_root.story_piece)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse()
