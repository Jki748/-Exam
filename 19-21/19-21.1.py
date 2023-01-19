"""
+1
*4
"""

def f(start, second, win_step, curr_step):
    if start + second >= 61:
        return win_step % 2 == curr_step % 2
    if win_step == curr_step:
        return 0
    next_step = [f(start + 1, second, win_step, curr_step + 1),
                 f(start * 4, second, win_step, curr_step + 1),
                 f(start, second + 1, win_step, curr_step + 1),
                 f(start, second * 4, win_step, curr_step + 1)]
    return any(next_step) if (curr_step + 1) % 2 == win_step % 2 else all(next_step)

for s in range(1,58):
    for step in range(1, 6):
        if f(s, 3, step, 0):
            print(s, step)


