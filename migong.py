def dfs(maze, start, end, path=[], required_points=[]):
    if start == end:
        if len(required_points) == 0:
            return path + [start]
        else:
            return None

    if start[0] < 0 or start[0] >= len(maze) or start[1] < 0 or start[1] >= len(maze[0]) or maze[start[0]][start[1]] == '#':
        return None

    if start in required_points:
        required_points.remove(start)

    maze[start[0]][start[1]] = '#'

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        next_position = (start[0] + direction[0], start[1] + direction[1])
        next_path = dfs(maze, next_position, end, path + [start], required_points)
        if next_path:
            return next_path

    return None

maze = [
    ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' '],
    ['#',' ','#',' ','#',' ',' ',' ','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#'],
    ['#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#'],
    ['#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#'],
    ['#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#'],
    ['#','#','#',' ','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#'],
    ['#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#'],
    ['#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#'],
    ['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
    ['#',' ','#','#','#','#','#',' ','#','#','#','#','#',' ','#','#','#','#','#',' ','#'],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#'],
    ['#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#',' ','#'],
    ['#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#'],
    ['#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#'],
    ['#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#'],
    ['#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#'],
    ['#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#'],
    ['#','#','#',' ','#',' ','#','#','#',' ','#',' ','#',' ',' ',' ','#',' ','#',' ','#'],
    [' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
    ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
]

start = (19, 0)
end = (1, 20)
path_points = [(15, 5), (17,17)]

path = dfs(maze, start, end, required_points=path_points)
print(path)

output = []
coordinates = [(19, 0), (19, 1), (19, 2), (19, 3), (18, 3), (17, 3), (17, 2), (17, 1), (16, 1), (15, 1), (15, 2), (15, 3), (14, 3), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (14, 7), (15, 7), (15, 8), (15, 9), (15, 10)]
output = []

# 初始运行方向为正向直行
current_direction = 'forward'

for i in range(1, len(path)):
    x_diff = path[i][0] - path[i-1][0]
    y_diff = path[i][1] - path[i-1][1]

    if current_direction == 'forward':
        if x_diff == 0 and y_diff == 1:  # 直行
            output.append(1)
        elif x_diff == -1 and y_diff == 0:  # 左转
            output.append(2)
            current_direction = 'left'
        elif x_diff == 1 and y_diff == 0:  # 右转
            output.append(3)
            current_direction = 'right'
        elif x_diff == 0 and y_diff == -1:  # 后退
            output.append(4)
            current_direction = 'backward'

    elif current_direction == 'left':
        if x_diff == -1 and y_diff == 0:  # 直行
            output.append(1)
        elif x_diff == 0 and y_diff == -1:  # 左转
            output.append(2)
            current_direction = 'backward'
        elif x_diff == 0 and y_diff == 1:  # 右转
            output.append(3)
            current_direction = 'forward'
        elif x_diff == 1 and y_diff == 0:  # 后退
            output.append(4)
            current_direction = 'right'

    elif current_direction == 'right':
        if x_diff == 1 and y_diff == 0:  # 直行
            output.append(1)
        elif x_diff == 0 and y_diff == 1:  # 左转
            output.append(2)
            current_direction = 'forward'
        elif x_diff == 0 and y_diff == -1:  # 右转
            output.append(3)
            current_direction = 'backward'
        elif x_diff == -1 and y_diff == 0:  # 后退
            output.append(4)
            current_direction = 'left'

    elif current_direction == 'backward':
        if x_diff == 0 and y_diff == -1:  # 直行
            output.append(1)
        elif x_diff == 1 and y_diff == 0:  # 左转
            output.append(2)
            current_direction = 'right'
        elif x_diff == -1 and y_diff == 0:  # 右转
            output.append(3)
            current_direction = 'left'
        elif x_diff == 0 and y_diff == 1:  # 后退
            output.append(4)
            current_direction = 'forward'


print(output)

