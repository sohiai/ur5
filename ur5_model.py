"""Predefined robot models."""
import numpy as np  # type: ignore


def kuka_lbr_iiwa_7() -> np.ndarray:  # pragma: no cover
    """Get KUKA LBR iiwa 7 MDH model."""
    return np.array(
        [
            [0, 0, 0, 340],
            [-np.pi / 2, 0, 0, 0],
            [np.pi / 2, 0, 0, 400],
            [np.pi / 2, 0, 0, 0],
            [-np.pi / 2, 0, 0, 400],
            [-np.pi / 2, 0, 0, 0],
            [np.pi / 2, 0, 0, 126],
        ]
    )


def mecademic_meca500() -> np.ndarray:  # pragma: no cover
    """Get Meca500 MDH model."""
    return np.array(
        [
            [0, 0, 0, 135],
            [-np.pi / 2, 0, -np.pi / 2, 0],
            [0, 135, 0, 0],
            [-np.pi / 2, 38, 0, 120],
            [np.pi / 2, 0, 0, 0],
            [-np.pi / 2, 0, np.pi, 72],
        ]
    )


def puma560() -> np.ndarray:  # pragma: no cover
    """Get PUMA560 MDH model."""
    return np.array(
        [
            [0, 0, 0, 0],
            [-np.pi / 2, 0, 0, 0],
            [0, 612.7, 0, 0],
            [0, 571.6, 0, 163.9],
            [-np.pi / 2, 0, 0, 115.7],
            [np.pi / 2, 0, np.pi, 92.2],
        ]
    )


def ur10_copy() -> np.ndarray:  # pragma: no cover
    """Get UR10 MDH model."""
    return np.array(
        [
            [0, 0, 0, 118],
            [np.pi / 2, 0, np.pi, 0],
            [0, 612.7, 0, 0],
            [0, 571.6, 0, 163.9],
            [-np.pi / 2, 0, 0, 115.7],
            [np.pi / 2, 0, np.pi, 92.2],
        ]
    )


def ur10_site() -> np.ndarray:  # pragma: no cover
    """Get UR10 MDH model."""
    return np.array(
        [
            [0, 0, 0, 180.7],
            [np.pi / 2, 0, np.pi, 0],
            [0, 612.7, 0, 0],
            [0, 571.6, 0, 174.2],
            [-np.pi / 2, 0, 0, 119.9],
            [np.pi / 2, 0, np.pi, 116.6],
        ]
    )


def ur5_site() -> np.ndarray:  # pragma: no cover
    """Get UR10 MDH model."""
    return np.array(
        [
            [0, 0, 0, 162.5],
            [np.pi / 2, 0, np.pi, 0],
            [0, 425, 0, 0],
            [0, 392.2, 0, 133.3],
            [-np.pi / 2, 0, 0, 99.7],
            [np.pi / 2, 0, np.pi, 99.6],
        ]
    )