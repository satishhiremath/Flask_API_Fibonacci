import io
import pstats
import cProfile


class ServiceProfiler:
    def __init__():
        pass

    def profile(funct):
        """Decorator that uses cProfile to profile a function"""
        def fun(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            ret_value = funct(*args, **kwargs)
            pr.disable()

            str_io = io.StringIO()
            sort_by = 'cumulative'
            ps = pstats.Stats(pr, stream=str_io).sort_stats(sort_by)
            ps.print_stats()
            print(str_io.getvalue())
            return ret_value

        return fun
