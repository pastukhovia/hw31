import pytest

from ads.serializers import AdRetrieveSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_retrieve(client, login):
    access_token, _ = login
    ad = AdFactory.create()
    response = client.get(f'/ad/{ad.pk}/', HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 200
    assert response.data == AdRetrieveSerializer(ad).data
