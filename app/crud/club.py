from uuid import uuid4, UUID

from loguru import logger
from psycopg.rows import class_row

from app.database.connection import pool
from app.error.error import ClubNotFoundError, ClubNameExistError, CoachInClubAlreadyExistError, \
    CoachInClubNotFoundError, ClubUpdateError, ClubDeleteError
from app.event import event_pb2
from app.models.club import ClubInfo, Club


async def club_name_exists(
        club_name: str
) -> ClubNameExistError | None:
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT name
                FROM "club"
                WHERE name = '{club_name}' AND is_deleted = FALSE;
                            """)
            club = await cur.fetchone()
            if club is None:
                return None
            return ClubNameExistError()


async def create_club(
        create_club_data: event_pb2.CreateClubRequest,
) -> UUID | None:
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    WITH club_data AS (
                        INSERT INTO "club" (id, name, about, updated_at, created_at, is_deleted)
                        VALUES ('{uuid4()}',
                                '{create_club_data.name}',
                                '{create_club_data.about}',
                                now()::timestamp,
                                now()::timestamp,
                                FALSE
                        )
                        RETURNING id
                    )
                    INSERT INTO "club_coach" (id, coach_id, club_id)
                    VALUES ('{uuid4()}',
                            '{create_club_data.coach_id}',
                            (SELECT id FROM club_data)
                    )
                    RETURNING (SELECT id FROM club_data);
                                """)
                club_id = await cur.fetchone()
                await conn.commit()
                return club_id[0] if club_id else None
    except Exception as e:
        logger.error(e)
        await conn.rollback()

async def get_club_id_by_name(
        club_name: str
) -> (str | None, ClubNotFoundError | None):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT id
                FROM "club"
                WHERE name = '{club_name}' AND is_deleted = FALSE;
                            """)
            name = await cur.fetchone()
            if name is None:
                return name, ClubNotFoundError()
            return name[0], None

async def club_exists(
        club_id: UUID
) -> (str | None, ClubNotFoundError | None):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                   SELECT id
                   FROM "club"
                   WHERE id = '{club_id}' AND is_deleted = FALSE;
                               """)
            id = await cur.fetchone()
            if id is None:
                return id, ClubNotFoundError()
            return id[0], None

async def get_clubs(
        data = event_pb2.GetClubsRequest
) -> list[ClubInfo] | None:
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(ClubInfo)) as cur:
            sql = """
                SELECT id, name
                FROM "club"
                WHERE is_deleted = False"""

            sql += f" LIMIT {data.page_size} OFFSET {(data.page - 1) * data.page_size}"

            await cur.execute(sql)
            data = await cur.fetchall()
            return data


async def add_coach_to_club(
        data = event_pb2.AddCoachToClubRequest
) -> UUID | None:
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                       INSERT INTO "club_coach" (id, coach_id, club_id)
                       VALUES ('{uuid4()}',
                               '{data.coach_id}', 
                               '{data.club_id}'
                       )
                       RETURNING id;
                                   """)
                club_coach_id = await cur.fetchone()
                await conn.commit()
                return club_coach_id[0] if club_coach_id else None
    except Exception as e:
        logger.error(e)
        await conn.rollback()


async def check_coach_in_club(
        club_id: UUID,
        coach_id: UUID
) -> (UUID | None, CoachInClubAlreadyExistError | None):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT id
                FROM "club_coach"
                WHERE coach_id = '{coach_id}' AND club_id = '{club_id}';
                            """)
            club_coach_id = await cur.fetchone()
            if club_coach_id is not None:
                return club_coach_id[0], CoachInClubAlreadyExistError()
            return club_coach_id, None


async def remove_coach_to_club(
        club_id: UUID,
        coach_id: UUID
) -> (UUID | None, None | CoachInClubNotFoundError):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    DELETE FROM "club_coach"
                    WHERE coach_id='{coach_id}' AND club_id='{club_id}'
                    RETURNING id;
                                """)
                club_coach_id = await cur.fetchone()
                if club_coach_id is None:
                    return club_coach_id, CoachInClubNotFoundError()
                return club_coach_id[0], None
    except Exception as e:
        logger.error(e)
        await conn.rollback()


async def update_club(
        data: event_pb2.UpdateClubRequest
) -> (str | None, ClubUpdateError | None, Exception | None):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                logger.info(data)
                await cur.execute(f"""
                    UPDATE "club"
                    SET name = COALESCE(
                        {f"'{data.name}'" if data.name != '' else 'NULL'},
                        name
                    ),
                    about = COALESCE(
                        {f"'{data.about}'" if data.about != '' else 'NULL'},
                        about
                    ),
                    updated_at = now()::timestamp
                    WHERE id = '{data.club_id}' AND is_deleted = FALSE
                    RETURNING name;
                                """)
            await conn.commit()
            name = await cur.fetchone()
            if name is None:
                return name, ClubUpdateError(), None
            return name[0], None, None
    except Exception as e:
        logger.error(e)
        await conn.rollback()
        return None, ClubUpdateError(), e


async def delete_club(
    club_id: UUID
) -> (str | None, ClubDeleteError | None, Exception | None):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    UPDATE "club"
                    SET is_deleted = TRUE,
                    updated_at = now()::timestamp
                    WHERE id = '{club_id}' AND is_deleted = False
                    RETURNING name;
                                """)
                await conn.commit()
                name = await cur.fetchone()
                if name is None:
                    return name, ClubDeleteError(), None
                return name[0], None, None

    except Exception as e:
        logger.error(e)
        await conn.rollback()
        return None, ClubDeleteError(), e

async def get_club_by_name(
       club_name: str
) ->(Club | None, ClubNotFoundError | None):
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(Club)) as cur:
            await cur.execute(f"""
                SELECT id, name, about
                FROM "club"
                WHERE name = '{club_name}' AND is_deleted = FALSE;
                            """)
            data = await cur.fetchone()
            if data is None:
                return None, ClubNotFoundError()
            return data, None


async def get_club_by_id(
       club_id: str
) ->(Club | None, ClubNotFoundError | None):
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(Club)) as cur:
            await cur.execute(f"""
                SELECT id, name, about
                FROM "club"
                WHERE id = '{club_id}' AND is_deleted = FALSE;
                            """)
            data = await cur.fetchone()
            if data is None:
                return None, ClubNotFoundError()
            return data, None


async def get_club_coaches_by_id(
        club_id: str
) -> list[UUID] | None:
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT coach_id
                FROM "club_coach"
                WHERE club_id = '{club_id}';
                            """)
            data = await cur.fetchall()
            return data
