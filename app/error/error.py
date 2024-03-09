import grpc
from grpc import StatusCode
from loguru import logger
import abc

from app.error.error_details import CLUB_NOT_FOUND, CLUB_NAME_EXIST, COACH_IN_CLUB_ALREADY_EXIST, \
    COACH_IN_CLUB_NOT_FOUND, COMPETITION_NAME_EXIST


class BaseError(abc.ABC):

    @abc.abstractmethod
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        """ """

class Error(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        ...


class ClubNotFoundError(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        logger.error(f"Status: {StatusCode.NOT_FOUND}, Details: {CLUB_NOT_FOUND}")
        await context.abort(code=grpc.StatusCode.NOT_FOUND, details=CLUB_NOT_FOUND)


class ClubNameExistError(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        logger.error(f"Status: {StatusCode.ALREADY_EXISTS}, Details: {CLUB_NAME_EXIST}")
        await context.abort(code=grpc.StatusCode.ALREADY_EXISTS, details=CLUB_NAME_EXIST)


class CoachInClubAlreadyExistError(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        logger.error(f"Status: {StatusCode.ALREADY_EXISTS}, Details: {COACH_IN_CLUB_ALREADY_EXIST}")
        await context.abort(code=grpc.StatusCode.ALREADY_EXISTS, details=COACH_IN_CLUB_ALREADY_EXIST)


class CoachInClubNotFoundError(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        logger.error(f"Status: {StatusCode.NOT_FOUND}, Details: {COACH_IN_CLUB_NOT_FOUND}")
        await context.abort(code=grpc.StatusCode.NOT_FOUND, details=COACH_IN_CLUB_NOT_FOUND)


class ClubUpdateError(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        logger.error(f"Status: {StatusCode.UNKNOWN}, Details: {details}")
        await context.abort(code=grpc.StatusCode.UNKNOWN, details=str(details))


class ClubDeleteError(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        logger.error(f"Status: {StatusCode.UNKNOWN}, Details: {details}")
        await context.abort(code=grpc.StatusCode.UNKNOWN, details=str(details))


class CompetitionNameExistError(BaseError):
    async def raise_error(self, context: grpc.aio.ServicerContext, details: Exception | None = None):
        logger.error(f"Status: {StatusCode.ALREADY_EXISTS}, Details: {COMPETITION_NAME_EXIST}")
        await context.abort(code=grpc.StatusCode.ALREADY_EXISTS, details=COMPETITION_NAME_EXIST)
