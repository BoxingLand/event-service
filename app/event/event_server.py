from datetime import datetime
from uuid import UUID

import grpc
from loguru import logger

from app.crud.competition import competition_name_exists, create_competition
from app.error.error import CoachInClubNotFoundError
from app.event import event_pb2_grpc, event_pb2
from app.crud.club import club_name_exists, create_club, get_club_id_by_name, get_clubs, check_coach_in_club, \
    add_coach_to_club, remove_coach_to_club, club_exists, update_club, delete_club, get_club_by_name, get_club_by_id, \
    get_club_coaches_by_id


class Event(event_pb2_grpc.EventServicer):

    async def CreateClub(
            self,
            request: event_pb2.CreateClubRequest,
            context: grpc.aio.ServicerContext,
    ) -> event_pb2.CreateClubResponse:
        club_name_exist = await club_name_exists(club_name=request.name)
        if club_name_exist is not None:
            await club_name_exist.raise_error(context=context)

        club_id = await create_club(create_club_data=request)
        if club_id is not None:
            return event_pb2.CreateClubResponse(id=str(club_id))

    async def GetClubIDByName(
            self,
            request: event_pb2.GetClubIDByNameRequest,
            context: grpc.aio.ServicerContext,
    ) -> event_pb2.GetClubIDByNameResponse:
        club_id, error = await get_club_id_by_name(club_name=request.name)
        if error is not None:
            await error.raise_error(context=context)
        return event_pb2.GetClubIDByNameResponse(club_id=str(club_id))

    async def GetClubs(
            self,
            request: event_pb2.GetClubsRequest,
            context: grpc.aio.ServicerContext,
    ) -> event_pb2.GetClubsResponse:
        clubs = await get_clubs(data=request)
        for club in clubs:
            yield event_pb2.GetClubsResponse(**club.to_dict())

    async def AddCoachToClub(
            self,
            request: event_pb2.AddCoachToClubRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.AddCoachToClubResponse:
        _, error = await club_exists(club_id=UUID(request.club_id))
        if error is not None:
            await error.raise_error(context=context)

        _, error = await check_coach_in_club(
            club_id=UUID(request.club_id),
            coach_id=UUID(request.coach_id)
        )
        if error is not None:
            await error.raise_error(context=context)

        club_coach_id = await add_coach_to_club(data=request)
        if club_coach_id is not None:
            return event_pb2.AddCoachToClubResponse(message=str(club_coach_id))

    async def RemoveCoachToClub(
            self,
            request: event_pb2.RemoveCoachToClubRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.RemoveCoachToClubResponse:
        club_coach_id, error = await remove_coach_to_club(
            club_id=UUID(request.club_id),
            coach_id=UUID(request.coach_id)
        )
        if error is not None:
            await error.raise_error(context=context)

        if club_coach_id is not None:
            return event_pb2.RemoveCoachToClubResponse(message=str(club_coach_id))

    async def UpdateClub(
            self,
            request: event_pb2.UpdateClubRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.UpdateClubResponse:
        _, error = await club_exists(club_id=UUID(request.club_id))
        if error is not None:
            await error.raise_error(context=context)

        name, error, details = await update_club(data=request)
        if error is not None:
            await error.raise_error(context=context, details=details)
        return event_pb2.UpdateClubResponse(message=f"Club {name} successfully updated")

    async def DeleteClub(
            self,
            request: event_pb2.DeleteClubRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.DeleteClubResponse:
        _, error = await club_exists(club_id=UUID(request.club_id))
        if error is not None:
            await error.raise_error(context=context)

        coach_id, _ = await check_coach_in_club(
            club_id=UUID(request.club_id),
            coach_id=UUID(request.coach_id)
        )
        if coach_id is None:
            await CoachInClubNotFoundError().raise_error(context=context)
        name, error, details = await delete_club(club_id=UUID(request.club_id))
        if error is not None:
            await error.raise_error(context=context, details=details)
        return event_pb2.DeleteClubResponse(message=f"Club {name} successfully deleted")

    async def GetClubByName(
            self,
            request: event_pb2.GetClubByNameRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetClubResponse:
        club, error = await get_club_by_name(club_name=request.name)
        if error is not None:
            await error.raise_error(context=context)
        return event_pb2.GetClubResponse(**club.to_dict())

    async def GetClubByID(
            self,
            request: event_pb2.GetClubByIDRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetClubResponse:
        club, error = await get_club_by_id(club_id=request.club_id)
        if error is not None:
            await error.raise_error(context=context)
        return event_pb2.GetClubResponse(**club.to_dict())

    async def GetClubCoachesID(
            self,
            request: event_pb2.GetClubCoachesIDRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetClubCoachesIDResponse:
        _, error = await club_exists(club_id=UUID(request.club_id))
        if error is not None:
            await error.raise_error(context=context)
        coaches_id = await get_club_coaches_by_id(club_id=request.club_id)
        logger.info(coaches_id)
        for coach_id in coaches_id:
            yield event_pb2.GetClubCoachesIDResponse(coach_id=str(coach_id[0]))

    async def CreateCompetition(
            self,
            request: event_pb2.CreateCompetitionRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.CreateCompetitionResponse:
        # if request.date <= datetime.now().date():
        #     await
        logger.info(datetime.now().date())
        competition_name_exist = await competition_name_exists(competition_name=request.name)
        if competition_name_exist is not None:
            await competition_name_exist.raise_error(context=context)

        club_id = await create_competition(create_competition_data=request)
        if club_id is not None:
            return event_pb2.CreateCompetitionResponse(id=str(club_id))

    async def AddBoxerToCompetition(
            self,
            request: event_pb2.AddBoxerToCompetitionRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.AddBoxerToCompetitionResponse:
        ...

    async def RemoveBoxerToCompetition(
            self,
            request: event_pb2.RemoveBoxerToCompetitionRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.RemoveBoxerToCompetitionResponse:
        ...

    async def UpdateCompetition(
            self,
            request: event_pb2.UpdateCompetitionRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.UpdateCompetitionResponse:
        ...

    async def DeleteCompetition(
            self,
            request: event_pb2.DeleteCompetitionRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.DeleteCompetitionResponse:
        ...

    async def GetCompetitions(
            self,
            request: event_pb2.GetCompetitionsRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetCompetitionsResponse:
        ...

    async def GetCompetitionByName(
            self,
            request: event_pb2.GetCompetitionByNameRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetCompetitionResponse:
        ...

    async def GetCompetitionByID(
            self,
            request: event_pb2.GetCompetitionByIDRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetCompetitionResponse:
        ...

    async def CreateFight(
            self,
            request: event_pb2.CreateFightRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.CreateFightResponse:
        ...

    async def SetWinner(
            self,
            request: event_pb2.SetWinnerRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.SetWinnerResponse:
        ...

    async def GetFightsCompetition(
            self,
            request: event_pb2.GetFightsCompetitionRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetFightResponse:
        ...

    async def GetFightsBoxer(
            self,
            request: event_pb2.GetFightsBoxerRequest,
            context: grpc.aio.ServicerContext
    ) -> event_pb2.GetFightResponse:
        ...
