import pathlib
from logging import Logger, getLogger, StreamHandler, Formatter, DEBUG
import typing
import numpy as xp
import scipy
_default_logger = getLogger(__name__)
log_handler = StreamHandler()
log_handler.setLevel(DEBUG)
log_formatter = Formatter("%(created)f\t%(message)s")
log_handler.setFormatter(log_formatter)
_default_logger.addHandler(log_handler)

_default_logger.setLevel(DEBUG)
_default_logger.propagate = False


def path2numpy(
    bgm_path: pathlib.Path,
    talk_path: pathlib.Path,
    logger: typing.Optional[Logger]
):
    bgm_rate = bgm_numpy


def resampling_wavs(
    rate_list: tuple(int),
    wavdata_list: tuple(typing.Any),
    resampling_rate: int = None,
    logger: typing.Optional[Logger],
):
    """
    TODO: set wavdata type
    """
    logger.debug('length of rate_list:{} monoral_list:{}'.format(len(rate_list), len(wavdata_list)))
    assert len(rate_list) == len(wavdata_list), 'length of rate_list & monoral_list must be the same.'

    if resampling_rate is None:
        resampling_rate = min(rate_list)
    else:
        resampling_rate = rate_list.index(min(rate_list))

    resampled_monoral = list()
    for rate, monoral in zip(rate_list, wavdata_list):
        resampled_monoral.append(
            monoral if rate == resampling_rate else scipy.signal.resample(monoral, resampling_rate)
        )

    return minimum_rate, resampled_monoral_list
