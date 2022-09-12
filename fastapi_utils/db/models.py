from datetime import datetime

import ormar
from conf import settings


class BaseModelQueryset(ormar.queryset.QuerySet):
    pass


class BaseModel(ormar.Model):
    id: int = ormar.Integer(primary_key=True, unique=True, autoincrement=True)
    created_at: datetime = ormar.DateTime(timezone=settings.TIMEZONE, default=datetime.now, nullable=True)

    class Meta(ormar.Model.Meta):
        abstract = True
        database = settings.db
        metadata = settings.db_meta
        queryset_class = BaseModelQueryset
        orders_by = ["created_at", "id"]
