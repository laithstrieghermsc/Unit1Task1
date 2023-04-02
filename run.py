#########################################################################
#                                                                       #
#                        Mindarie Senior College                        #
#                            Laith Striegher                            #
#                            Task 1 - Unit 1                            #
#                               'Shuffle'                               #
#                     Program startup file -- run.py                    #
#                                                                       #
#########################################################################


import main

size = 3
win_size = 1000
title = "Shuffle Game"
shuffle_rule = pow(size, 6)
default_color = "#f0f0f0"
complete_color = "#00ff00"
exit_on_completion = False
overrideredirect = False,
spot_detection = False
highlight_thickness = 1
applicible_photos = (  # Array of photos
    ["demo\\0.png", "demo\\1.png", "demo\\2.png", "demo\\3.png", "demo\\4.png", "demo\\5.png",
     "demo\\6.png",
     "demo\\7.png", "demo\\8.png", "demo\\9.png", "demo\\a.png", "demo\\b.png", "demo\\c.png",
     "demo\\d.png",
     "demo\\e.png", "demo\\f.png", "demo\\10.png", "demo\\11.png", "demo\\12.png", "demo\\13.png",
     "demo\\14.png",
     "demo\\15.png", "demo\\16.png", "demo\\17.png", "demo\\18.png", "demo\\19.png", "demo\\1a.png",
     "demo\\1b.png",
     "demo\\1c.png", "demo\\1d.png", "demo\\1e.png", "demo\\1f.png", "demo\\20.png", "demo\\21.png",
     "demo\\22.png",
     "demo\\23.png", "demo\\24.png", "demo\\25.png", "demo\\26.png", "demo\\27.png", "demo\\28.png",
     "demo\\29.png",
     "demo\\2a.png", "demo\\2b.png", "demo\\2c.png", "demo\\2d.png", "demo\\2e.png", "demo\\2f.png",
     "demo\\30.png"])

game = main.shuffle(size=size, win_size=win_size, title=title, shuffle_rule=shuffle_rule, default_color=default_color,
                    complete_color=complete_color, exit_on_completion=exit_on_completion,
                    overrideredirect=overrideredirect, spot_detection=spot_detection,
                    highlight_thickness=highlight_thickness, applicable_photos=applicible_photos)
while True:
    game.start()
    game.reset(size=size, win_size=win_size, title=title, shuffle_rule=shuffle_rule, default_color=default_color,
               complete_color=complete_color, exit_on_completion=exit_on_completion,
               overrideredirect=overrideredirect, spot_detection=spot_detection,
               highlight_thickness=highlight_thickness, applicable_photos=applicible_photos)

# if game.game.is_complete():
#     exit()
