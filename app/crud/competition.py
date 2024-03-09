from uuid import UUID, uuid4

from loguru import logger

from app.database.connection import pool
from app.error.error import CompetitionNameExistError
from app.event import event_pb2


async def create_competition(
        create_competition_data: event_pb2.CreateCompetitionRequest,
) -> UUID | None:
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                        INSERT INTO "competition" (id, name, about, price, date, prize_pool, limit_boxers, country, 
                                                    region, city, organizer_id, updated_at, created_at, is_deleted)
                        VALUES ('{uuid4()}',
                                '{create_competition_data.name}',
                                '{create_competition_data.about}',
                                '{create_competition_data.price}',
                                '{create_competition_data.date}',
                                '{create_competition_data.prize_pool}',
                                '{create_competition_data.limit_boxers}',
                                '{create_competition_data.country}',
                                '{create_competition_data.region}',
                                '{create_competition_data.city}',
                                '{create_competition_data.organizer_id}',
                                now()::timestamp,
                                now()::timestamp,
                                FALSE
                        )
                        RETURNING id;
                                """)
                competition_id = await cur.fetchone()
                await conn.commit()
                return competition_id[0] if competition_id else None
    except Exception as e:
        logger.error(e)
        await conn.rollback()

async def competition_name_exists(
        competition_name: str
) -> CompetitionNameExistError | None:
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT name
                FROM "competition"
                WHERE name = '{competition_name}' AND is_deleted = FALSE;
                            """)
            club = await cur.fetchone()
            if club is None:
                return None
            return CompetitionNameExistError()