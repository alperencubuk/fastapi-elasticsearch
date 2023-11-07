from elasticsearch import Elasticsearch

from source.core.settings import settings

# TODO Could be AsyncElasticsearch
es = Elasticsearch(settings.ELASTICSEARCH_URI)


async def elasticsearch_health() -> bool:
    try:
        # TODO Health could not be green
        es.cat.health()
        return True
    except Exception:
        return False
