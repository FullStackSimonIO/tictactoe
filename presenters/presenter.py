from presenters.pvp import PlayerVsPlayerPresenter
from presenters.pvc import PlayerVsComputerPresenter


class Presenter(PlayerVsPlayerPresenter, PlayerVsComputerPresenter):

    def __init__(self):
        super().__init__()

    def play(self):
        while True:
            menu_input = self.view.print_menu()

            if menu_input == 1:
                self.play_pvp_game()

            elif menu_input == 2:
                self.play_pvc_game()
            elif menu_input == 3:
                self.play_pvp_game()
                self.game.load_from_json("game.json")

            elif menu_input == 4:
                self.play_pvc_game()
