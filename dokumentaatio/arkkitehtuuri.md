```mermaid
classDiagram
class Game{
 +list rooms
 +tuple position
 +start()
 }
 class Rooms{
 +int pysty
 +int vaaka
 +str name
 +str description
 +str item
 +room_decoder()
 }
class Commands{
 +command_handler()
 +move()
 +move_checker()
 +get_room()
 }
Game --> Rooms
Game --> Commands
