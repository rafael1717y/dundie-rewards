"""Core module of dundie"""
from csv import reader

from dundie.database import add_person, commit, connect
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database.
    >>> len(load('assets/people.csv'))
    2
    >>> load('assets/people.csv')[0][0]
    'J'
    """
    try:
        csv_data = reader(open(filepath))
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    db = connect()
    people = []

    # Leitura do csv com a biblioteca reader.
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop("email")  # remove o email pq será pk.
        person, created = add_person(db, pk, person_data)

        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk  # inclui novamento o email
        people.append(return_data)  # acumula

    commit(db)
    return people


# query recebe um email ou dept
def read(**query):
    """Read data from db and filers using query.
    red(email="joe@doe.com")
    """
    db = connect()
    return_data = []
    for pk, data in db["people"].items():

        # a partir do python 3.8
        dept = query.get("dept")
        if dept and dept != data["dept"]:
            continue

        # Walrus / assignment expression - a partir do python 3.8
        if (email := query.get("email")) and email != pk:
            continue

        return_data.append(
            {
                "email": pk,
                "balance": db["balance"][pk],
                "last_movement": db["movement"][pk][-1]["date"],
                **data,
            }
        )
    return return_data


def add(value, **query):
    """Add value to each record on query."""
