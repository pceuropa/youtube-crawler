from cProfile import Profile
from io import StringIO
import pstats
import contextlib

sort_mode = ['cumulative', 'time']
max_rows = 10


@contextlib.contextmanager
def code():
    profile = Profile()
    profile.enable()
    yield
    profile.disable()

    sio = StringIO()
    ps = pstats.Stats(profile, stream=sio).sort_stats(sort_mode[1])
    ps.print_stats(max_rows)
    print(sio.getvalue())
