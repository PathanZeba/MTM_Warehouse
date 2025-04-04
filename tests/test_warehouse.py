import pytest
from app.models.warehouse_info import WarehouseInfo
from app.services.warehouse_service import WarehouseService

@pytest.fixture
def warehouse_service():
    """Service instance for testing."""
    return WarehouseService()


@pytest.mark.parametrize("total_capacity, space_available, expected_percentage", [
    (1000, 800, 20),
    (15000, 6000, 60),
    (30000, 27000, 10)
])
def test_check_percentage(warehouse_service, total_capacity, space_available, expected_percentage):
    warehouse_info = WarehouseInfo(
        w_total_capacity=total_capacity,
        w_space_available=space_available,
        w_percent_full=expected_percentage
    )

    percent_full = warehouse_service.w_percentage(warehouse_info)

    assert percent_full == expected_percentage


@pytest.mark.parametrize("total_capacity, space_available", [
    (1000, 800),
    (15000, 10000),
    (25000, 5000)
])
def test_check_space_available(warehouse_service, total_capacity, space_available):
    warehouse_info = WarehouseInfo(
        w_total_capacity=total_capacity,
        w_space_available=space_available
    )

    space_available_result = warehouse_service.w_space_available(warehouse_info)

    assert space_available_result == space_available
