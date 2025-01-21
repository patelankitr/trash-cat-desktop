import time

from alttester import By, AltKeyCode
from pages.base_method_page import click_on_the_element


class MyTests:
    # XPaths of the elements to be used
    start_button_element = "/UICamera/Loadout/StartButton"

    def __init__(self, driver):
        self.alt_driver = driver

    def trash_launch_game(self):

        # You might want to load the scene here
        self.alt_driver.load_scene("Main", True)
        click_on_the_element(self.alt_driver, "PATH", self.start_button_element, 2, 'Test')

    @property
    def pause_button(self):
        return self.alt_driver.wait_for_object(By.NAME, 'pauseButton', timeout=5)

    @property
    def character(self):
        return self.alt_driver.wait_for_object(By.NAME, 'PlayerPivot', timeout=5)

    @property
    def obstacles(self):
        return self.alt_driver.find_objects_which_contain(By.NAME, 'Obstacle')

    def is_displayed(self):
        return self.pause_button and self.character

    def press_pause(self):
        self.pause_button.tap()

    def get_current_life(self):
        return int(self.character.get_component_property('CharacterInputController', 'currentLife', 'Assembly-CSharp'))

    def jump(self):
        self.character.call_component_method('CharacterInputController', 'Jump', 'Assembly-CSharp')
        # self.alt_driver.press_key(AltKeyCode.UpArrow, power=1, duration=0.5, wait=False)

    def move_right(self):
        # self.character.call_component_method('CharacterInputController', 'ChangeLane', 'Assembly-CSharp',
        #                                     parameters=['1'])
        self.alt_driver.press_key(AltKeyCode.RightArrow, power=5, duration=0.8, wait=False)

    def move_left(self):
        self.character.call_component_method('CharacterInputController', 'ChangeLane', 'Assembly-CSharp',
                                             parameters=['-1'])

        # self.alt_driver.press_key(AltKeyCode.RightArrow, power=1, duration=0.5, wait=False)

    def slide(self):
        self.character.call_component_method('CharacterInputController', 'Slide', 'Assembly-CSharp')
        # self.alt_driver.press_key(AltKeyCode.DownArrow, power=1, duration=0.5, wait=False)


    def avoid_obstacles_and_play(self, number_of_obstacles=15):
        time.sleep(4)
        character = self.character
        moved_left = False
        moved_right = False
        for _ in range(number_of_obstacles):
            # Retrieve all obstacles and sort them by their worldZ value
            all_obstacles = self.alt_driver.find_objects_which_contain(By.NAME, "Obstacle")
            all_obstacles = sorted(all_obstacles, key=lambda obs: obs.worldZ)
            all_obstacles = [obs for obs in all_obstacles if obs.worldZ >= character.worldZ]

            if not all_obstacles:
                print("No obstacles ahead.")
                break

            obstacle = all_obstacles[0]
            next_obstacle = all_obstacles[1]

            # Wait until the obstacle is within an actionable range
            while obstacle.worldZ - character.worldZ > 10.50:
                obstacle = self.alt_driver.find_object(By.ID, str(obstacle.id))
                character = self.alt_driver.find_object(By.NAME, "PlayerPivot")

            print(f"OBSTACLE: {obstacle.name}, z: {obstacle.worldZ}, x: {obstacle.worldX}")
            print(f"NEXT: {next_obstacle.name}, z: {next_obstacle.worldZ}, x: {next_obstacle.worldX}")
            if "ObstacleHighBarrier(Clone)" in obstacle.name: # ObstacleHighBarrier
                self.slide()
                print(f"Player slide at z: {obstacle.worldZ}")
            elif "ObstacleLowBarrier(Clone)" in obstacle.name or "ObstacleRat(Clone)" in obstacle.name or "RoadWorksBarrierLow" in obstacle.name: # ObstacleLowBarrier # Rat
                self.jump()
                print(f"Player jump at z: {obstacle.worldZ}")

            else:
                if len(all_obstacles) > 1 and obstacle.worldZ == all_obstacles[1].worldZ:
                    if obstacle.worldX == character.worldX:
                        if all_obstacles[1].worldX == -1.5:
                            self.move_right()
                            moved_right = True
                        else:
                            self.move_left()
                            moved_left = True
                    elif all_obstacles[1].worldX == character.worldX:
                        if obstacle.worldX == -1.5:
                            self.move_right()
                            moved_right = True
                        else:
                            self.move_left()
                            moved_left = True
                elif obstacle.worldX == character.worldX:
                    self.move_right()
                    moved_right = True

            while character.worldZ < obstacle.worldZ and character.worldX < 99:
                obstacle = self.alt_driver.find_object(By.ID, obstacle.id)
                character = self.character

            # Move back to the center lane if any side move was made
            if moved_left:
                self.move_right()
                moved_left = False

            if moved_right:
                self.move_left()
                moved_right = False

