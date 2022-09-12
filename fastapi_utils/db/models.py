import uuid
from datetime import datetime

import ormar
from conf import settings


class BaseModelQueryset(ormar.queryset.QuerySet):
    async def update_or_create(self, defaults: dict | None = None, **kwargs):
        if defaults is None:
            defaults = {}
        if (instance := await self.get_or_none(**kwargs)) is None:
            # если объект существует, то обновляем
            return await self.create(**kwargs, **defaults), True
        return await self.filter(pk=instance.pk).update(**kwargs, **defaults), False

    async def get_or_create(self, defaults: dict | None = None, **kwargs):
        if defaults is None:
            defaults = {}
        if (instance := await self.get_or_none(**kwargs)) is None:
            # если объект существует, то обновляем
            return await self.create(**kwargs, **defaults), True
        return instance, False


class BaseModelMeta(ormar.ModelMeta):
    database = settings.db
    metadata = settings.db_meta
    queryset_class = BaseModelQueryset
    orders_by = ["created_at", "id"]


class BaseModel(ormar.Model):
    uuid: int = ormar.UUID(default=uuid.uuid4)
    id: int = ormar.Integer(primary_key=True, unique=True, autoincrement=True)
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now, nullable=True)

    class Meta(BaseModelMeta):
        abstract = True
