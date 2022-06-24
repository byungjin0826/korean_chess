import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# paths = route + destination


class Board:  # Factory & Observer
    def __init__(self, settings=('MSMS', 'MSMS')):
        self.players = [Player(setting) for setting in settings]
        self.stones = [King]
        self.positions = []

    def get_positions(self):
        pass
    pass


class Player:  # 두 명, 필요 한가?
    def __init__(self, setting='MSMS'):
        self.setting = setting
        pass
    pass


class Stone:  #
    def __init__(self, survival=1, position=None, score=None):
        self.survival = survival
        self.position = np.array(position)
        self.score = score
        self.possible_moves = []
        self.selected = 0  # todo: 아직은 필요 없는 듯.
    pass


class King(Stone):

    def get_all_moves(self):
        # 9개 칸에 대해서 모두
        originated_position = self.position - np.array([4, 1])
        print(originated_position)
        if np.array_equal(originated_position, np.array([0, 0])):  # 1. 가운데
            moves = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        elif np.array_equal(originated_position, [-1, 1]):  # 2. 좌상단
            moves = [[1, 0], [0, -1], [1, -1]]
        elif np.array_equal(originated_position, [0, 1]):  # 3. 상단
            moves = [[-1, 0], [1, 0], [0, -1]]
        elif np.array_equal(originated_position, [1, 1]):  # 4. 우상단
            moves = [[-1, 0], [-1, -1], [0, -1]]
        elif np.array_equal(originated_position, [-1, 0]):  # 5. 좌측
            moves = [[0, 1], [1, 0], [0, -1]]
        elif np.array_equal(originated_position, [1, 0]):  # 6. 우측
            moves = [[0, 1], [-1, 0], [0, -1]]
        elif np.array_equal(originated_position, [-1, -1]):  # 7. 좌하단
            moves = [[0, 1], [1, 1], [1, 0]]
        elif np.array_equal(originated_position, [0, -1]):  # 8. 하단
            moves = [[-1, 0], [0, 1], [1, 0]]
        else:  # 9. 우하단
            moves = [[-1, 1], [0, 1], [-1, 0]]
        return np.array(moves)

    def check_possible_move(self, board):
        pass

    pass


class Cha(Stone):
    def get_all_moves(self):
        total = np.array([[[x, y] for x in range(9)] for y in range(10)]).reshape(-1, 2)
        total_df = pd.DataFrame(total, columns=['X', 'Y'])
        moves = total_df.loc[((total_df.X == self.position[0]) | (total_df.Y == self.position[1])) &
                             ~((total_df.X == self.position[0]) & (total_df.Y == self.position[1]))]
        moves = moves.values - self.position
        return moves
    pass


class Sa(Stone):
    def get_all_moves(self):
        pass
    pass


class Ma(Stone):
    pass


class Sang(Stone):
    pass


def plot_moves(start_position, moves):
    # todo: 장기 판처럼 꾸미기, 배경 및 궁성 표현 필요
    plt.xlim(0, 8)
    plt.ylim(0, 9)

    # 눈금 간격 1로 변경(x, y축 모두)
    plt.xticks(range(9))
    plt.yticks(range(10))

    plt.grid()
    plt.scatter(*start_position)

    for move in moves:
        plt.quiver(*start_position, *move, angles='xy', scale_units='xy', scale=1)  # todo: 라인을 다른 색으로 하면 좋을 듯
    # todo: 움직임 벡터로 표시
    plt.show()


if __name__ == "__main__":
    cha = Cha(1, [4, 1], 13)
    plot_moves(cha.position, cha.get_all_moves())
    pass
