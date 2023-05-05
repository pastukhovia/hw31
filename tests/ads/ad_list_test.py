import pytest

from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads = AdFactory.create_batch(5)

    response = client.get('/ad/')

    assert response.status_code == 200
    assert response.data['results'] == AdListSerializer(ads, many=True).data
