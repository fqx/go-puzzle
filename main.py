# This is a Python script that can generate go puzzles.
# Get sgf-render here. https://github.com/julianandrews/sgf-render/releases

import os, random, glob
style = 'minimalist'
input_folder = 'sgf'
output_folder = 'output'
n_min = 10
n_max = 50
num_moves = 10
num_samples = 20


def sgf2png(sgf_file, output_file, n=0, num_moves=0):
    '''
    Generate png file of go board
    :param sgf_file: str, location of sgf file
    :param output_file: str, location of output_file
    :param n: node to render, 0 for last
    :param num_moves: number of last moves to numbered, if 0, all moves are numbered
    :return:
    '''
    options = '-o {} --style {} --no-board-labels --move-numbers'.format(output_file, style)

    if n:
        options += ' -n {}'.format(n)
        if num_moves:
            options += ' --first-move-number {}'.format(n - num_moves + 1)
    else:
        options += ' -n last'

    # print(options)

    retcode = os.system('./sgf-render {} {}'.format(sgf_file, options))
    return retcode


def generate_qna(sgf_file, i):
    '''
    generate q and a picture pairs
    :param sgf_file: str, location of sgf file
    :param i: int, index
    :return:
    '''
    # make sure black first
    steps = round((n_max - n_min) / 2)
    node = n_min + random.randint(0, steps) *2
    # Q
    output_file = output_folder + '/' + '{:03d}'.format(i) + '_x.png'
    sgf2png(sgf_file, output_file, node)

    # A
    output_file = output_folder + '/' + '{:03d}'.format(i) + '_y.png'
    sgf2png(sgf_file, output_file, node+num_moves, num_moves)


if __name__ == '__main__':
    i = 0
    for sgf_file in random.sample(glob.glob('{}/*/*/*.sgf'.format(input_folder)), num_samples):
        print('generate {}.png'.format(i))
        generate_qna(sgf_file, i)
        i += 1