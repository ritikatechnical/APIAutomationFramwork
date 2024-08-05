import requests
import allure
import pytest


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Create Booking status and verify that Booking Id should not be null")

    def test_create_booking_positive(self):
        pass

