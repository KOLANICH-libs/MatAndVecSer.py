from pathlib import Path

import numpy as np

__all__ = ("MatAndVecFiles", "MatAndVec")

# pylint:disable=too-few-public-methods


class MatAndVec:
	__slots__ = ("vec", "mat")

	def __init__(self, *, vec: np.ndarray, mat: np.ndarray) -> None:
		self.vec = vec
		self.mat = mat

	def save(self, paramsFiles: "MatAndVecFiles") -> None:
		# pylint:disable=protected-access
		self.__class__._saveComponent(paramsFiles.mat, self.mat)
		self.__class__._saveComponent(paramsFiles.vec, self.vec)

	@classmethod
	def load(cls, paramsFiles: "MatAndVecFiles") -> "MatAndVec":
		"""Initializes the stuff in a bit weird way to allow subclasses to rename the ctor arguments"""
		res = cls(vec=None, mat=None)
		res.vec = cls._loadComponent(paramsFiles.vec)
		res.mat = cls._loadComponent(paramsFiles.mat)
		return res

	@classmethod
	def _saveComponent(cls, path: Path, comp: np.ndarray) -> None:
		path.parent.mkdir(parents=True, exist_ok=True)
		np.save(path, comp, allow_pickle=False)

	@classmethod
	def _loadComponent(cls, path: Path) -> np.ndarray:
		return np.load(path, allow_pickle=False)


class MatAndVecFiles:
	__slots__ = ("vec", "mat")

	MAT_FILE_NAME = "mat"
	VEC_FILE_NAME = "vec"

	MAT_AND_VEC_CTOR = MatAndVec

	def __init__(self, *, vec: Path = None, mat: Path = None, directory: Path = None) -> None:
		if directory is not None:
			vec = directory / (self.__class__.VEC_FILE_NAME + ".npy")
			mat = directory / (self.__class__.MAT_FILE_NAME + ".npy")

		self.vec = vec
		self.mat = mat

	def load(self) -> "MatAndVec":
		return self.__class__.MAT_AND_VEC_CTOR.load(self)
