from gr_node import GameNode
from gr_hashmap import Hashmap


# A legend, so-to-speak, of each titles tag/genre values

genre_sample = {"Action": None, "Adventure": None, "Alt-Sports": None, "Anime - Comic": None, "Arcade": None, "Battle": None, "Building": None, "Card Game": None, "Casual": None, "Cinematic": None, "Comedy": None, "Cute": None, "Fantasy": None, "Fighting": None, "First-Person Perspective": None, "Freeform": None, "Gambling": None, "Hidden Object": None, "Historical": None, "Horror": None , "Indie": None, "Management": None,  "Metroidvania": None, "Mystery": None, "Party": None, "Platformer": None, "Point-and-Click": None, "Puzzle": None, "Racing": None, "Retro": None, "Rhythm": None, "Roguelike": None, "Role-Playing Game": None, "Sandbox": None, "Sci-fi": None, "Sexual - Nudity": None, "Shooter": None, "Sidescroller": None, "Simulation": None, "Sports": None, "Stealth": None, "Story": None, "Strategy": None, "Survival": None, "Top-Down Perspective": None, "Third-Person Perspective": None, "Visual Novel": None, "Mobile": None, "Multiplayer": None, "Portable": None, "Singleplayer": None, "Splitscreen": None, "Coop": None, "VR": None}

special_sample = {"Copies Sold": None, "ESRB": [None,[None]], "Rating": None, "Developer": None, "Publisher": None, "Release Date": None, "Difficulty": None, "Size": None, "Platform": [None], "Lowest Cost": [None]}


# GAME & GENRE DICTIONARY

# each titles values - dictionaries within a dictionary
genre_dict = {\

  "Horizon Zero Dawn": {"Action": 90, "Adventure": 100, "Alt-Sports": 20, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 80, "Fighting": 70, "First-Person Perspective": 10, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 20, "Mystery": 20, "Party": 0, "Platformer": 30, "Point-and-Click": 0, "Puzzle": 10, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 80, "Sandbox": 40, "Sci-fi": 100, "Sexual - Nudity": 0, "Shooter": 80, "Sidescroller": 0, "Simulation": 10, "Sports": 0, "Stealth": 60, "Story": 100, "Strategy": 0, "Survival": 20, "Top-Down Perspective": 0, "Third-Person Perspective": 100, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Doom (2016)": {"Action": 100, "Adventure": 100, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 20, "Fighting": 70, "First-Person Perspective": 100, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 50, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 30, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 10, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 50, "Sandbox": 0, "Sci-fi": 100, "Sexual - Nudity": 0, "Shooter": 100, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 50, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 20, "Portable": 0, "Singleplayer": 80, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "NBA 2K21": {"Action": 50, "Adventure": 0, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 0, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 20, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 80, "Sports": 100, "Stealth": 0, "Story": 0, "Strategy": 15, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 100, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 50, "Portable": 80, "Singleplayer": 50, "Splitscreen": 100, "Coop": 0, "VR": 0},
               
  "Noctropolis": {"Action": 0, "Adventure": 90, "Alt-Sports": 0, "Anime - Comic": 50, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 60, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 10, "Indie": 20, "Management": 0, "Metroidvania": 0, "Mystery": 20, "Party": 0, "Platformer": 0, "Point-and-Click": 100, "Puzzle": 70, "Racing": 0, "Retro": 100, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 30, "Sexual - Nudity": 10, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 100, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},
                  
  "Super Mario Brothers 2": {"Action": 70, "Adventure": 50, "Alt-Sports": 0, "Anime - Comic": 60, "Arcade": 80, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 20, "Cinematic": 0, "Comedy": 30, "Cute": 80, "Fantasy": 80, "Fighting": 20, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 100, "Point-and-Click": 0, "Puzzle": 10, "Racing": 0, "Retro": 100, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 100, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 20, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 100, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},
                             
  "Burnout: Paradise City": {"Action": 50, "Adventure": 30, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 20, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 10, "Cinematic": 0, "Comedy": 10, "Cute": 0, "Fantasy": 0, "Fighting": 15, "First-Person Perspective": 50, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 100, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 100, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 60, "Sports": 0, "Stealth": 0, "Story": 0, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 50, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 30, "Portable": 0, "Singleplayer": 70, "Splitscreen": 0, "Coop": 20, "VR": 0},
                             
  "Filament": {"Action": 0, "Adventure": 50, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 20, "Cinematic": 0, "Comedy": 0, "Cute": 30, "Fantasy": 20, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 10, "Historical": 0, "Horror": 10, "Indie": 100, "Management": 0, "Metroidvania": 0, "Mystery": 60, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 100, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 50, "Sci-fi": 100, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 90, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 80, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},
               
  "Heroes of Hammerwatch": {"Action": 100, "Adventure": 70, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 50, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 10, "Cinematic": 0, "Comedy": 0, "Cute": 40, "Fantasy": 100, "Fighting": 80, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 100, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 70, "Rhythm": 0, "Roguelike": 100, "Role-Playing Game": 30, "Sandbox": 20, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 30, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 10, "Story": 10, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 100, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 60, "Portable": 0, "Singleplayer": 40, "Splitscreen": 0, "Coop": 100, "VR": 0},

  "Kingdom Come: Deliverance": {"Action": 85, "Adventure": 100, "Alt-Sports": 10, "Anime - Comic": 0, "Arcade": 50, "Battle": 20, "Building": 0, "Card Game": 20, "Casual": 0, "Cinematic": 80, "Comedy": 0, "Cute": 0, "Fantasy": 100, "Fighting": 75, "First-Person Perspective": 95, "Freeform": 0, "Gambling": 20, "Hidden Object": 0, "Historical": 80, "Horror": 0, "Indie": 80, "Management": 0, "Metroidvania": 10, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 20, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 100, "Sandbox": 100, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 10, "Sidescroller": 0, "Simulation": 20, "Sports": 0, "Stealth": 60, "Story": 100, "Strategy": 10, "Survival": 40, "Top-Down Perspective": 0, "Third-Person Perspective": 10, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "River City Ransom: Underground": {"Action": 100, "Adventure": 50, "Alt-Sports": 0, "Anime - Comic": 50, "Arcade": 100, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 20, "Comedy": 20, "Cute": 30, "Fantasy": 0, "Fighting": 100, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 100, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 30, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 80, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 70, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 100, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 40, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 10, "Mobile": 0, "Multiplayer": 30, "Portable": 0, "Singleplayer": 70, "Splitscreen": 100, "Coop": 100, "VR": 0},

  "The Hunter: Call of the Wild": {"Action": 40, "Adventure": 60, "Alt-Sports": 100, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 20, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 15, "Fighting": 0, "First-Person Perspective": 100, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 80, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 30, "Sandbox": 100, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 100, "Sidescroller": 0, "Simulation": 100, "Sports": 0, "Stealth": 80, "Story": 0, "Strategy": 0, "Survival": 30, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 80, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 80, "VR": 0},

  "Apex Legends": {"Action": 100, "Adventure": 50, "Alt-Sports": 60, "Anime - Comic": 15, "Arcade": 20, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 50, "Fighting": 40, "First-Person Perspective": 100, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 30, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 30, "Sandbox": 70, "Sci-fi": 100, "Sexual - Nudity": 0, "Shooter": 100, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 0, "Strategy": 20, "Survival": 20, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 100, "Multiplayer": 100, "Portable": 100, "Singleplayer": 0, "Splitscreen": 0, "Coop": 50, "VR": 0},

  "Rockband": {"Action": 20, "Adventure": 50, "Alt-Sports": 0, "Anime - Comic": 15, "Arcade": 20, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 40, "Cinematic": 30, "Comedy": 30, "Cute": 50, "Fantasy": 50, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 100, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 100, "Roguelike": 0, "Role-Playing Game": 20, "Sandbox": 0, "Sci-fi": 20, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 70, "Sports": 0, "Stealth": 0, "Story": 15, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 60, "Portable": 0, "Singleplayer": 40, "Splitscreen": 100, "Coop": 100, "VR": 0},

  "Rocket League": {"Action": 80, "Adventure": 0, "Alt-Sports": 100, "Anime - Comic": 0, "Arcade": 20, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 10, "Fighting": 10, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 80, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 40, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 50, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 70, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 30, "Stealth": 0, "Story": 0, "Strategy": 20, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 100, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 80, "Portable": 0, "Singleplayer": 20, "Splitscreen": 100, "Coop": 50, "VR": 0},

  "Leisure Suit Larry: Love For Sail": {"Action": 0, "Adventure": 100, "Alt-Sports": 0, "Anime - Comic": 100, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 30, "Cinematic": 30, "Comedy": 100, "Cute": 30, "Fantasy": 0, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 15, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 100, "Puzzle": 40, "Racing": 0, "Retro": 100, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 100, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 100, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 10, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Layers of Fear": {"Action": 0, "Adventure": 100, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 15, "Cinematic": 70, "Comedy": 0, "Cute": 0, "Fantasy": 50, "Fighting": 0, "First-Person Perspective": 100, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 15, "Horror": 100, "Indie": 100, "Management": 0, "Metroidvania": 0, "Mystery": 50, "Party": 0, "Platformer": 0, "Point-and-Click": 100, "Puzzle": 70, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 100, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 20, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 100},

  "Cuphead": {"Action": 100, "Adventure": 30, "Alt-Sports": 0, "Anime - Comic": 100, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 10, "Comedy": 60, "Cute": 50, "Fantasy": 70, "Fighting": 60, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 10, "Horror": 0, "Indie": 70, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 100, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 50, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 100, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 60, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 20, "Portable": 100, "Singleplayer": 80, "Splitscreen": 100, "Coop": 100, "VR": 0},

  "Slay the Spire": {"Action": 20, "Adventure": 80, "Alt-Sports": 0, "Anime - Comic": 60, "Arcade": 0, "Battle": 100, "Building": 0, "Card Game": 100, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 100, "Fighting": 20, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 100, "Management": 20, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 100, "Role-Playing Game": 50, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 10, "Strategy": 50, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 100, "Singleplayer": 100, "Splitscreen": 0, "Coop": 10, "VR": 0},

  "Heavy Rain": {"Action": 10, "Adventure": 80, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 10, "Cinematic": 100, "Comedy": 0, "Cute": 0, "Fantasy": 0, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 40, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 100, "Party": 0, "Platformer": 0, "Point-and-Click": 50, "Puzzle": 30, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 30, "Sci-fi": 20, "Sexual - Nudity": 10, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 100, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 100, "Visual Novel": 20, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Metroid": {"Action": 100, "Adventure": 70, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 50, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 0, "Fighting": 60, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 10, "Indie": 0, "Management": 0, "Metroidvania": 100, "Mystery": 0, "Party": 0, "Platformer": 100, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 100, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 20, "Sci-fi": 100, "Sexual - Nudity": 0, "Shooter": 50, "Sidescroller": 100, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 10, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "NHL 99": {"Action": 70, "Adventure": 0, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 30, "Battle": 0, "Building": 20, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 0, "Fighting": 20, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 10, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 70, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 80, "Sports": 100, "Stealth": 0, "Story": 10, "Strategy": 15, "Survival": 0, "Top-Down Perspective": 100, "Third-Person Perspective": 100, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 40, "Portable": 0, "Singleplayer": 60, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Rise of the Triad": {"Action": 100, "Adventure": 20, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 15, "Cute": 0, "Fantasy": 0, "Fighting": 10, "First-Person Perspective": 100, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 20, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 100, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 50, "Sexual - Nudity": 0, "Shooter": 100, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 30, "Strategy": 0, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 30, "Portable": 0, "Singleplayer": 70, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Dungeon Defenders: Awakened": {"Action": 100, "Adventure": 20, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 20, "Building": 70, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 40, "Fantasy": 100, "Fighting": 50, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 70, "Management": 50, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 50, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 60, "Sandbox": 0, "Sci-fi": 15, "Sexual - Nudity": 0, "Shooter": 50, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 0, "Strategy": 100, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 100, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 60, "Portable": 100, "Singleplayer": 40, "Splitscreen": 0, "Coop": 100, "VR": 0},

  "Jupiter Hell": {"Action": 100, "Adventure": 20, "Alt-Sports": 0, "Anime - Comic": 30, "Arcade": 10, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 0, "Fighting": 40, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 70, "Indie": 100, "Management": 20, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 30, "Rhythm": 0, "Roguelike": 100, "Role-Playing Game": 60, "Sandbox": 0, "Sci-fi": 100, "Sexual - Nudity": 0, "Shooter": 100, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 30, "Strategy": 60, "Survival": 0, "Top-Down Perspective": 100, "Third-Person Perspective": 50, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Haven Park": {"Action": 0, "Adventure": 100, "Alt-Sports": 0, "Anime - Comic": 10, "Arcade": 0, "Battle": 0, "Building": 100, "Card Game": 0, "Casual": 100, "Cinematic": 0, "Comedy": 0, "Cute": 100, "Fantasy": 0, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 100, "Management": 100, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 50, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 50, "Strategy": 40, "Survival": 40, "Top-Down Perspective": 100, "Third-Person Perspective": 50, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Big Farm Story": {"Action": 0, "Adventure": 30, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 100, "Card Game": 0, "Casual": 90, "Cinematic": 0, "Comedy": 0, "Cute": 80, "Fantasy": 15, "Fighting": 0, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 100, "Management": 100, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 40, "Sandbox": 50, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 70, "Sports": 0, "Stealth": 0, "Story": 100, "Strategy": 40, "Survival": 40, "Top-Down Perspective": 100, "Third-Person Perspective": 50, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 20, "Portable": 0, "Singleplayer": 80, "Splitscreen": 0, "Coop": 10, "VR": 0},

  "Super Hot VR": {"Action": 100, "Adventure": 15, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 0, "Fighting": 50, "First-Person Perspective": 100, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 80, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 70, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 70, "Sexual - Nudity": 0, "Shooter": 100, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 0, "Strategy": 60, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 100},

  "Rust": {"Action": 40, "Adventure": 70, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 100, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 30, "Fighting": 50, "First-Person Perspective": 100, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 70, "Management": 30, "Metroidvania": 0, "Mystery": 0, "Party": 0, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 100, "Sci-fi": 30, "Sexual - Nudity": 20, "Shooter": 30, "Sidescroller": 0, "Simulation": 60, "Sports": 0, "Stealth": 30, "Story": 0, "Strategy": 20, "Survival": 100, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 80, "Portable": 0, "Singleplayer": 20, "Splitscreen": 0, "Coop": 100, "VR": 0},

  "Street Fighter V": {"Action": 100, "Adventure": 0, "Alt-Sports": 10, "Anime - Comic": 30, "Arcade": 30, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 15, "Fighting": 100, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 0, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 0, "Mystery": 0, "Party": 15, "Platformer": 0, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 0, "Sandbox": 0, "Sci-fi": 0, "Sexual - Nudity": 10, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 0, "Story": 0, "Strategy": 10, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 0, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 95, "Portable": 0, "Singleplayer": 5, "Splitscreen": 0, "Coop": 0, "VR": 0},

  "Sekiro: Shadows Die Twice": {"Action": 100, "Adventure":100, "Alt-Sports": 0, "Anime - Comic": 0, "Arcade": 0, "Battle": 0, "Building": 0, "Card Game": 0, "Casual": 0, "Cinematic": 0, "Comedy": 0, "Cute": 0, "Fantasy": 100, "Fighting": 100, "First-Person Perspective": 0, "Freeform": 0, "Gambling": 0, "Hidden Object": 0, "Historical": 10, "Horror": 0, "Indie": 0, "Management": 0, "Metroidvania": 50, "Mystery": 0, "Party": 0, "Platformer": 60, "Point-and-Click": 0, "Puzzle": 0, "Racing": 0, "Retro": 0, "Rhythm": 0, "Roguelike": 0, "Role-Playing Game": 80, "Sandbox": 50, "Sci-fi": 0, "Sexual - Nudity": 0, "Shooter": 0, "Sidescroller": 0, "Simulation": 0, "Sports": 0, "Stealth": 70, "Story": 100, "Strategy": 10, "Survival": 0, "Top-Down Perspective": 0, "Third-Person Perspective": 100, "Visual Novel": 0, "Mobile": 0, "Multiplayer": 0, "Portable": 0, "Singleplayer": 100, "Splitscreen": 0, "Coop": 0, "VR": 0}


}


# SPECIAL SORT DICTIONARY

special_dict = {\

  "Horizon Zero Dawn": {"Copies Sold": 1000000, "ESRB": ["13-T", ["Blood", "Drug Reference", "Language", "Mild Sexual Themes", "Violence"]], "Rating": 4.5, "Developer": "Guerrilla", "Publisher": "Playstation Mobile, Inc.", "Release Date": 2020, "Difficulty": 7, "Size": 100000, "Platform": ["Playstation 4", "PC"], "Lowest Cost": [50]},

  "Doom (2016)": {"Copies Sold": 1000000, "ESRB": ["18-M", ["Blood", "Gore", "Violence"]], "Rating": 4.5, "Developer": "id Software", "Publisher": "Bethesda Softworks", "Release Date": 2016, "Difficulty": 7, "Size": 55000, "Platform": ["Playstation 4", "PC"], "Lowest Cost": [20]},

  "NBA 2K21": {"Copies Sold": 1000000, "ESRB": ["03-E", None], "Rating": 4, "Developer": "Visual Concepts", "Publisher": "2K", "Release Date": 2016, "Difficulty": 7, "Size": 55000, "Platform": ["Playstation 4", "PC"], "Lowest Cost": [60]},

  "Noctropolis": {"Copies Sold": 50000, "ESRB": ["-1-NA", None], "Rating": 2.5, "Developer": "Flashpoint Studios", "Publisher": "Nightdive Studios", "Release Date": 1994, "Difficulty": 8, "Size": 800, "Platform": ["PC"], "Lowest Cost": [10]},
                  
  "Super Mario Brothers 2": {"Copies Sold": 1000000, "ESRB": ["03-E", None], "Rating": 4, "Developer": "Nintendo", "Publisher": "Nintendo", "Release Date": 1988, "Difficulty": 6, "Size": 0, "Platform": ["NES"], "Lowest Cost": [26, "Subscription"]},
                             
  "Burnout: Paradise City": {"Copies Sold": 1000000, "ESRB": ["03-E", None], "Rating": 4.6, "Developer": "Criterion Games", "Publisher": "Electronic Arts", "Release Date": 2018, "Difficulty": 6, "Size": 8000, "Platform": ["Playstation 3", "PC", "XBox 360"], "Lowest Cost": [7]},
                             
  "Filament": {"Copies Sold": 40000, "ESRB": ["03-E", None], "Rating": 4, "Developer": "Kasedo Games", "Publisher": "Kasedo Games", "Release Date": 2020, "Difficulty": 9, "Size": 1000, "Platform": ["PC"], "Lowest Cost": [7.60]},
               
  "Heroes of Hammerwatch": {"Copies Sold": 40000, "ESRB": ["13-T", None], "Rating": 4.3, "Developer": "Crackshell", "Publisher": "Crackshell", "Release Date": 2018, "Difficulty": 7, "Size": 500, "Platform": ["PC"], "Lowest Cost": [12]},

  "Kingdom Come: Deliverance": {"Copies Sold": 400000, "ESRB": ["18-M", None], "Rating": 4.1, "Developer": "Warhorse Studios", "Publisher": "Warhorse Studios", "Release Date": 2018, "Difficulty": 8, "Size": 80000, "Platform": ["PC"], "Lowest Cost": [30]},

  "River City Ransom: Underground": {"Copies Sold": 95000, "ESRB": ["13-T", None], "Rating": 4, "Developer": "Conatus Creative Inc.", "Publisher": "Conatus Creative Inc.", "Release Date": 2017, "Difficulty": 6.5, "Size": 128, "Platform": ["PC", "Mac", "Linux"], "Lowest Cost": [20]},

  "The Hunter: Call of the Wild": {"Copies Sold": 95000, "ESRB": ["13-T", None], "Rating": 4.5, "Developer": "Expansive Worlds", "Publisher": "Expansive Worlds", "Release Date": 2017, "Difficulty": 5, "Size": 60000, "Platform": ["PC", "PS4", "XBox One"], "Lowest Cost": [20]},

  "Apex Legends": {"Copies Sold": 4000000, "ESRB": ["13-T", None], "Rating": 4.5, "Developer": "Respawn Entertainment", "Publisher": "Electronic Arts", "Release Date": 2020, "Difficulty": 6, "Size": 56000, "Platform": ["PC", "PS4", "XBox One", "Android", "iOS", "Nintendo Switch"], "Lowest Cost": [0, "Free"]},

  "Rockband": {"Copies Sold": 5000000, "ESRB": ["03-E", None], "Rating": 4.2, "Developer": "Harmonix", "Publisher": "MTV Games", "Release Date": 2007, "Difficulty": 6, "Size": 10000, "Platform": ["PS3", "XBox 360", "Nintendo Wii"], "Lowest Cost": [160]},

  "Rocket League": {"Copies Sold": 600000, "ESRB": ["03-E", None], "Rating": 4.2, "Developer": "Harmonix", "Publisher": "MTV Games", "Release Date": 2007, "Difficulty": 6, "Size": 10000, "Platform": ["PS3", "XBox 360", "Nintendo Wii"], "Lowest Cost": [0, "Free"]},

  "Leisure Suit Larry: Love For Sail": {"Copies Sold": 2000000, "ESRB": ["18-M", None], "Rating": 4.5, "Developer": "Sierra", "Publisher": "Sierra", "Release Date": 1996, "Difficulty": 6, "Size": 600, "Platform": ["PC"], "Lowest Cost": [7]},

  "Layers of Fear": {"Copies Sold": 400000, "ESRB": ["18-M", None], "Rating": 3.8, "Developer": "Bloober Team SA", "Publisher": "Aspyr", "Release Date": 2016, "Difficulty": 5, "Size": 5000, "Platform": ["PC"], "Lowest Cost": [20]},

  "Cuphead": {"Copies Sold": 400000, "ESRB": ["03-E", None], "Rating": 4.5, "Developer": "Studio MDHR Entertainment Inc.", "Publisher": "Studio MDHR Entertainment Inc.", "Release Date": 2017, "Difficulty": 10, "Size": 4000, "Platform": ["PC", "PS4", "XBox One", "Nintendo Switch", "Mac"], "Lowest Cost": [20]},

  "Slay the Spire": {"Copies Sold": 600000, "ESRB": ["03-E", None], "Rating": 4.6, "Developer": "Mega Crit Games", "Publisher": "Mega Crit Games", "Release Date": 2019, "Difficulty": 8, "Size": 441, "Platform": ["PC", "PS4", "XBox One", "Nintendo Switch", "Mac", "Linux", "Android", "iOS"], "Lowest Cost": [12.50]},

  "Heavy Rain": {"Copies Sold": 2000000, "ESRB": ["18-M", None], "Rating": 4.4, "Developer": "Quantic Dream", "Publisher": "Quantic Dream", "Release Date": 2010, "Difficulty": 6, "Size": 35000, "Platform": ["PC", "PS4", "PS3"], "Lowest Cost": [2]},

  "Metroid": {"Copies Sold": 10000000, "ESRB": ["03-E", None], "Rating": 3.8, "Developer": "Nintendo", "Publisher": "Nintendo", "Release Date": 1987, "Difficulty": 7, "Size": 0, "Platform": ["NES"], "Lowest Cost": [19, "Subscription"]},

  "NHL 99": {"Copies Sold": 3000000, "ESRB": ["03-E", None], "Rating": 4.2, "Developer": "EA Sports", "Publisher": "EA Sports", "Release Date": 1998, "Difficulty": 6, "Size": 0, "Platform": ["Playstation", "PC", "Nintendo 64"], "Lowest Cost": [3]},

  "Rise of the Triad": {"Copies Sold": 1000000, "ESRB": ["18-M", None], "Rating": 3.8, "Developer": "Apogee Software", "Publisher": "Apogee Software", "Release Date": 1994, "Difficulty": 7, "Size": 500, "Platform": ["PC"], "Lowest Cost": [15]},

  "Dungeon Defenders: Awakened": {"Copies Sold": 100000, "ESRB": ["13-T", None], "Rating": 3, "Developer": "Chromatic Games", "Publisher": "Chromatic Games", "Release Date": 2020, "Difficulty": 6.5, "Size": 30000, "Platform": ["PC"], "Lowest Cost": [30]},

  "Jupiter Hell": {"Copies Sold": 70000, "ESRB": ["18-M", None], "Rating": 4.1, "Developer": "ChaosForge", "Publisher": "Hyperstrange", "Release Date": 2021, "Difficulty": 8, "Size": 2000, "Platform": ["PC"], "Lowest Cost": [25]},

  "Haven Park": {"Copies Sold": 20000, "ESRB": ["03-E", None], "Rating": 3.6, "Developer": "Fabien Weibel", "Publisher": "Mooneye Studios", "Release Date": 2021, "Difficulty": 3, "Size": 300, "Platform": ["PC"], "Lowest Cost": [7.60]},

  "Big Farm Story": {"Copies Sold": 50000, "ESRB": ["03-E", None], "Rating": 3.7, "Developer": "Goodgame Studios", "Publisher": "Goodgame Studios", "Release Date": 2021, "Difficulty": 4.5, "Size": 1000, "Platform": ["PC"], "Lowest Cost": [18]},

  "Super Hot VR": {"Copies Sold": 1000000, "ESRB": ["18-M", None], "Rating": 3.8, "Developer": "SUPERHOT Team", "Publisher": "SUPERHOT Team", "Release Date": 2017, "Difficulty": 7, "Size": 4000, "Platform": ["PC"], "Lowest Cost": [25]},

  "Rust": {"Copies Sold": 600000, "ESRB": ["18-M", None], "Rating": 4.1, "Developer": "Facepunch Studios", "Publisher": "Facepunch Studios", "Release Date": 2018, "Difficulty": 8, "Size": 20000, "Platform": ["PC"], "Lowest Cost": [40]},

  "Street Fighter V": {"Copies Sold": 3000000, "ESRB": ["13-T", None], "Rating": 3.8, "Developer": "Capcom", "Publisher": "Capcom", "Release Date": 2016, "Difficulty": 7, "Size": 5000, "Platform": ["PC", "Linux", "Arcade", "PS4"], "Lowest Cost": [20]},

  "Sekiro: Shadows Die Twice": {"Copies Sold": 3000000, "ESRB": ["18-M", None], "Rating": 4.4, "Developer": "FromSoftware", "Publisher": "Activision", "Release Date": 2019, "Difficulty": 9, "Size": 25000, "Platform": ["PC", "Xbox One", "PS4"], "Lowest Cost": [20]}



}



# GAME NODES

# the genre dictionary is turned into game nodes
# each node has a genre hashmap and special-sort hashmap
game_nodes = Hashmap("Game Nodes", 100)

# creates and adds GameNode to game_nodes
for title in genre_dict:
  # game_nodes.append(GameNode(game_dict[game_dict.keys()[i]]))

  game_nodes.set_value(title, GameNode(title)) 

  # takes the edge and weight values(percentages) and addes them to the GameNodes edge hashmap
  for genre in genre_dict[title]:
    
    game_nodes.get_value(title).genre_edges.set_value(genre, genre_dict[title][genre])
  
  for special in special_dict[title]:

    game_nodes.get_value(title).special_edges.set_value(special, special_dict[title][special])




# Independent Count Code

#game_count = 0

#for key in special_dict.keys():
#  game_count += 1

#print(f"# games ---> {game_count}")



# Code to test correctness of genre and special tags compared to the samples

#titles_with_genre_errors = {}

#for title in genre_dict.keys():

#  genre_errors = []

#  for genre in genre_dict[title]:
#    if genre not in list(genre_sample.keys()):
#      genre_errors.append(genre)
    
#  titles_with_genre_errors[title] = genre_errors


#titles_with_special_errors = {}

#for title in special_dict.keys():

#  special_errors = []

#  for special in special_dict[title]:
#    if special not in list(special_sample.keys()):
#      special_errors.append(special)
    
#  titles_with_special_errors[title] = special_errors




#print(f"\ngenre_errors --- {titles_with_genre_errors}\n")
#print(f"\nspecial_errors --- {titles_with_special_errors}\n")

