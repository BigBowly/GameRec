Game Recommendation Exercise - Readme
- Nate Tufts - bigbowlofnate@gmail.com


Summary: The program asks a few questions, gathers genre preferences and supposedly uses these preferences to create a list of game recommendations. Algorithms and data structures seem sound, my methodology for correctly deciphering human preference might not be.


Directions: Python 3 program. Drop all these files in the same folder and use either gr_main_bfs.py or gr_main_dfs.py to run the program. It has a clear screen function built to run with Windows, Mac, or Linux, supposedly - but it hasn't been at all thoroughly tested. The program has been tested, but if your goal is to break it, you probably can. One final note - I might revisit this at a later date as I learn more. Some of the debugging lines are commented out, but not deleted. Hopefully it doesn't make it too difficult to read.


Files:

gr_main_bfs.py, gr_main_dfs.py - Starting files. The only difference is which algorithm is called.   

gr_userdata.py - Asks questions and turns answers into user preferences.  

game_database_sep.py - 30 game dictionary database - handmade specifically for this program. 

gr_node.py - GameNode class 

gr_hashmap.py - Hashmap class - for genre values mainly 

gr_genregraph.py - GenreGraph class - holds lists of GameNodes 

gr_graphhashmap.py - GraphHashmap class - dedicated to GenreGraphs

gr_maxheap.py - Maxheap class - half the programs sorting uses heaps

gr_quicksort.py - Quicksort class - used for the rest of sorting. 

gr_creategraphs.py - Creates and maintains GenreGraphs within GraphHashmap 

gr_graphsearch.py - Two algorithms - depends on which gr_main file is used. 

gr_miscfunctions.py - Holds random functions - clear screen function. 
