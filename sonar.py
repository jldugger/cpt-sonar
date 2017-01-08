#!/usr/bin/python

from collections import deque


class Chart:

    def __init__(self, width=10, height=10):
        self.grid = [[0 for x in range(width)] for y in range(height)]
        self.grid[0] = ['.', '.', '.', 'X', '.', '.', '.', '.', '.', '.']
        self.grid[1] = ['.', '.', '.', '.', '.', '.', '.', 'X', '.', '.']
        self.grid[2] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.grid[3] = ['.', '.', 'X', '.', '.', '.', '.', 'X', '.', '.']
        self.grid[4] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.grid[5] = ['.', '.', '.', '.', 'X', '.', '.', '.', '.', '.']
        self.grid[6] = ['.', '.', '.', '.', '.', '.', 'X', '.', '.', '.']
        self.grid[7] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.grid[8] = ['.', '.', '.', 'X', '.', '.', '.', 'X', '.', '.']
        self.grid[9] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.width = width
        self.height = height

    def square(self, pos):
        x, y = pos
        return self.grid[y][x]

    def print_grid(self):
        for i in xrange(len(self.grid)):
            print self.grid[i]

    def move(self, (x, y), dir):
        if dir == 'N':
            y -= 1
        elif dir == 'S':
            y += 1
        elif dir == 'E':
            x += 1
        elif dir == 'W':
            x -= 1
        return (x, y)

    def empty_space(self, pos):
        return self.square(pos) != 'X'

    def oob(self, (x, y)):
        return x < 0 or x >= self.height or y < 0 or y >= self.height

    def is_intersecting_path(self, path):
        (x, y) = (0, 0)
        subpath = []
        for dir in path:
            subpath.append((x, y))
            (x, y) = self.move((x, y), dir)
            if (x, y) in subpath:
                return True
        return False

    def valid_path(self, path, pos):
        if path is None or not self.empty_space(pos) or self.is_intersecting_path(path):
            return False
        for i in path:
            pos = self.move(pos, i)
            if self.oob(pos) or not self.empty_space(pos):
                return False
        return True

    def find_valid_start_position(self, path):
        for x in range(self.width):
            for y in range(self.height):
                if self.valid_path(path, (x, y)):
                    return (x, y)

    def valid_starts(self, path):
        starts = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.valid_path(path, (x, y)):
                    starts += 1
        return starts

    def bfs_target_path(self):
        queue = deque([['N'], ['S'], ['E'], ['W']])
        result = []
        while queue:
            path = queue.popleft()
            valid_positions = self.valid_starts(path)
            if valid_positions == 0:
                continue
            elif valid_positions == 1:
                result.append(path)
            else:
                if not result:
                    for dir in set(['N', 'S', 'E', 'W']) - set(path[-1]):
                        next = list(path)
                        next.append(dir)
                        queue.append(next)
        return result

c = Chart()

c.print_grid()

shortest_paths = c.bfs_target_path()

for p in shortest_paths:
    print p
    print c.find_valid_start_position(p)
