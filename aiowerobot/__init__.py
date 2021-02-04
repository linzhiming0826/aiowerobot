__all__ = ["AioWeRoBot"]

try:
    from aiowerobot.robot import AioWeRoBot
except ImportError:  # pragma: no cover
    pass  # pragma: no cover
