# Animarathon XVI: Operation Ohio Interlude 3
# 
# Copyright (C) 2018  Anime In Northwest Ohio
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author :      Maxwell Paul Brickner
# Maintainer :  Maxwell Paul Brickner

label interlude_3:

    play music eurobeat fadeout 1

    show bg rave with vpunch

    call pachinko_create

    show text "{size=50}SMASH THE BUTTON AND WIN THE MONEY!{/size}" at truecenter with dissolve

    system "Are you a real pachinko baller? Let's go!"

    hide text

    show guest funky
    with easeinright

    guest_funky "Let's get funky! {b}GROOVY DISCOBALL PACHINKO{/b}!" with vpunch

    hide guest
    with easeoutright

    menu:

        ann_thoughts "I can't loose here! I need to gain the advantage!"

        "(Anime Yelling)" if energy >= 50:

            ann_thoughts "If I just show my winning spirit, I have to win!"

            show ann genki
            with easeinleft

            a "YAAAAAAAAAA!"

            python:
                energy -= 50
                pachinko_balls += 5000

        "Chuunibyou Pose":

            ann_thoughts "If I just trick them into thinking I'm powerful, I have to win!"

            show ann genki
            with easeinleft

            a "Don't make me reveal the power of my magic arm!"

            python:
                pachinko_balls += 500

        "Zettai Ryouiki Zone":

            ann_thoughts "As long as I have the higher score, I have to win!"

            show ann genki
            with easeinleft

            a "I won't let you score {b}ANY{/b} points!"

            python:
                pachinko_balls += 500

        "Ball Bukkake":

            ann_thoughts "If I unleash all my balls at once, I have to win!"

            show ann genki
            with easeinleft

            a "Eat this!"

            python:
                pachinko_balls += 500

        "Magical Girl JUSTICE" if magical_girl:

            show ann genki
            with easeinleft

            a "Magical Girl Justice!"

            python:
                pachinko_balls += 500
                magical_girl_earnings += 500
                money += 500

    hide ann
    with easeoutleft

    call pachinko_cleanup

    hide bg rave with vpunch

    return
