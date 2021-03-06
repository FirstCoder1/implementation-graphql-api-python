""" Methods for fetching film related data from database """

import asyncio

import sqlalchemy
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from movierental.database.models import Actor, Film, FilmActor

from .db import db, session


async def get_film_by_id(film_ids):
    query = session.query(Film).options(joinedload(Film.language))

    if film_ids:
        query = query.filter(Film.film_id.in_(film_ids))

    return query


async def get_films(release_years=None, limit=10):
    query = session.query(Film).options(joinedload(Film.language))

    if release_years:
        query = query.filter(Film.release_year.in_(release_years))

    query = query.limit(limit)

    return query


def get_actors_for_a_film(film_id):
    query = session.query(FilmActor).filter(FilmActor.film_id == film_id)

    actor_ids = []
    for actor in query:
        actor_ids.append(actor.actor_id)

    return actor_ids


if __name__ == "__main__":
    asyncio.run(get_films())
