import uuid
from datetime import datetime

import ormar
from conf import settings


class BaseModelQueryset(ormar.queryset.QuerySet):
    pass


class BaseModelMeta(ormar.Model.Meta):
    abstract = True
    database = settings.db
    metadata = settings.db_meta
    queryset_class = BaseModelQueryset
    orders_by = ["created_at", "id"]


class BaseModel(ormar.Model):
    uuid: int = ormar.UUID(default=uuid.uuid4)
    id: int = ormar.Integer(primary_key=True, unique=True, autoincrement=True)
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now, nullable=True)

    class Meta(BaseModelMeta):
        pass
