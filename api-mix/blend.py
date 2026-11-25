"""The original volume-weighted API approximation, shared by CLI and GUI."""
import math


def calculate_blend(tanks):
    if not 2 <= len(tanks) <= 4:
        raise ValueError('Select 2 to 4 tanks.')
    if any(not math.isfinite(volume) or volume < 0 or not math.isfinite(api)
           for volume, api in tanks):
        raise ValueError('Volumes must be finite and nonnegative; API must be finite.')
    try:
        total = math.fsum(volume for volume, _ in tanks)
        if total <= 0:
            raise ValueError('Combined volume must be greater than zero.')
        average = math.fsum((volume / total) * api for volume, api in tanks)
    except OverflowError as error:
        raise ValueError('Values are too large to calculate.') from error
    if not math.isfinite(average):
        raise ValueError('Values are too large to calculate.')
    return total, average
