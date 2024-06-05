from elasticsearch import Elasticsearch
from ..config import settings

es = Elasticsearch(settings.ELASTIC_URL)
